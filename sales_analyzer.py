from pathlib import Path
import csv
from collections import defaultdict

total_revenue = 0
product_quantity = defaultdict(int)
product_revenue = defaultdict(float)

data_file = Path(__file__).parent / "sales_data.csv"

with data_file.open(newline="", encoding="utf-8") as file:
    rows = csv.DictReader(file)

    for row in rows:
        product = row["Product"]
        quantity = int(row["Quantity"])
        price = float(row["Price"])

        revenue = quantity * price

        total_revenue += revenue
        product_quantity[product] += quantity
        product_revenue[product] += revenue

best_selling_product = max(product_quantity, key=product_quantity.get)
highest_revenue_product = max(product_revenue, key=product_revenue.get)

print("Sales Analysis Report")
print("-" * 25)
print(f"Total revenue: {total_revenue:,.2f}")
print(f"Best-selling product: {best_selling_product}")
print(f"Units sold: {product_quantity[best_selling_product]}")
print(f"Highest-revenue product: {highest_revenue_product}")
print(f"Revenue from it: {product_revenue[highest_revenue_product]:,.2f}")


summary_rows = [
    {"Metric": "Total revenue", "Value": f"{total_revenue:,.2f}"},
    {"Metric": "Best-selling product", "Value": best_selling_product},
    {"Metric": "Units sold", "Value": product_quantity[best_selling_product]},
    {"Metric": "Highest-revenue product", "Value": highest_revenue_product},
    {
        "Metric": "Highest product revenue",
        "Value": f"{product_revenue[highest_revenue_product]:,.2f}"
    }
]

with open("sales_summary.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Metric", "Value"])
    writer.writeheader()
    writer.writerows(summary_rows)

print("\nSummary saved to sales_summary.csv")
