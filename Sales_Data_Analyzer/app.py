from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route('/')
def home():

    # Create static folder automatically
    os.makedirs('static', exist_ok=True)

    # Load CSV
    var = pd.read_csv('Sales_Data_Analyzer/Walmart_Sales.csv')

    # Data Cleaning
    var = var.dropna()
    var = var.drop_duplicates()

    # Total Sales by CPI
    var["Total_Sales"] = var.groupby("CPI")["Weekly_Sales"].transform("sum")

    # Fuel Cost
    var["Fuel_cost"] = var["Fuel_Price"].sum()

    # Insights
    total_revenue = round(var["Weekly_Sales"].sum(), 2)
    avg_sales = round(var["Weekly_Sales"].mean(), 2)
    max_sales = round(var["Weekly_Sales"].max(), 2)
    min_sales = round(var["Weekly_Sales"].min(), 2)

    # Charts
    plt.figure(figsize=(12,8))

    plt.subplot(2,2,1)
    plt.hist(var["Total_Sales"], bins=20)
    plt.title("Total Sales")

    plt.subplot(2,2,2)
    plt.scatter(var["Weekly_Sales"], var["Temperature"])
    plt.title("Weekly Sales vs Temperature")

    plt.subplot(2,2,3)
    plt.hist(var["Unemployment"], bins=20)
    plt.title("Unemployment")

    plt.subplot(2,2,4)
    plt.scatter(var["Fuel_Price"], var["Fuel_cost"])
    plt.title("Fuel Price vs Fuel Cost")

    plt.tight_layout()

    chart_path = os.path.join(app.root_path, 'static', 'sales_charts.png')
    plt.savefig(chart_path)
    plt.close()

    return render_template(
        'index.html',
        total_revenue=total_revenue,
        avg_sales=avg_sales,
        max_sales=max_sales,
        min_sales=min_sales
    )

if __name__ == '__main__':
    app.run(debug=True)