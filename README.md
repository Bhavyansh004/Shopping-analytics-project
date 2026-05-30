# 🛍️ Shopping Analytics Project

> Uncovering retail insights through Python, SQL, and Power BI

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat&logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791?style=flat&logo=postgresql)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=flat&logo=powerbi)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat)

---

## 📌 Overview

This end-to-end data analytics project analyzes the shopping behavior of **3,900 customers** across product categories, demographics, and purchase patterns. The goal was to extract actionable business insights using a full analytics pipeline — from raw data to an interactive dashboard and presentation.

**Key questions answered:**
- Which customer segments generate the most revenue?
- Do subscribed customers spend more than non-subscribers?
- Which products have the highest ratings and discount rates?
- How does age group and gender influence purchasing behavior?

---

## 📂 Dataset

| Property | Details |
|----------|---------|
| **Source** | Customer Shopping Behavior Dataset (CSV) |
| **Records** | 3,900 rows × 18 columns |
| **Key Features** | Age, Gender, Category, Purchase Amount, Review Rating, Subscription Status, Shipping Type, Payment Method |
| **Missing Values** | 37 nulls in `Review Rating` — imputed using category-level median |

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| **Python** (pandas, matplotlib) | Data loading, EDA, cleaning, feature engineering |
| **Jupyter Notebook** | Interactive analysis environment |
| **PostgreSQL** | SQL-based business intelligence queries |
| **SQLAlchemy** | Python-to-PostgreSQL data pipeline |
| **Power BI** | Interactive dashboard & data visualization |
| **Gamma** | AI-powered project presentation (PPT) |
| **MS Word** | Detailed project report |

---

## 🔄 Project Workflow

```
Raw CSV  →  Python (EDA & Cleaning)  →  PostgreSQL (SQL Analysis)  →  Power BI (Dashboard)  →  Report + PPT
```

### Step 1 — Data Loading & Exploration
- Loaded CSV using `pandas`
- Inspected shape, data types, null counts with `df.info()`, `df.describe()`, `df.isnull().sum()`

### Step 2 — Data Cleaning
- Imputed 37 missing `Review Rating` values using category-level median
- Standardized column names to `snake_case`
- Dropped `promo_code_used` (duplicate of `discount_applied`)

### Step 3 — Feature Engineering
- Created `age_group` column using `pd.qcut()` → Young Adult / Adult / Middle-Aged / Senior
- Created `purchase_frequency_days` by mapping text frequencies to numeric values

### Step 4 — SQL Analysis (PostgreSQL)
- Loaded cleaned DataFrame into PostgreSQL via `SQLAlchemy`
- Wrote **10 business queries** covering:
  - Revenue by gender and age group
  - Subscriber vs non-subscriber spend
  - Top products by rating and discount rate
  - Customer segmentation (New / Returning / Loyal)
  - Top 3 products per category using window functions (`ROW_NUMBER()`)

### Step 5 — Power BI Dashboard
- Built interactive dashboard with KPI cards, bar charts, donut charts, and slicers
- Slicers: Subscription Status, Gender, Category, Shipping Type

### Step 6 — Report & Presentation
- Detailed project report created in MS Word (with all figures, SQL outputs, and insights)
- Presentation built using **Gamma AI**

---

## 📊 Dashboard Preview

> Built in Power BI with dynamic slicers for Gender, Category, Subscription Status, and Shipping Type.

**KPIs at a Glance:**

| Metric | Value |
|--------|-------|
| Total Customers | 3,900 |
| Average Purchase Amount | $59.76 |
| Average Review Rating | 3.75 / 5 |
| Subscription Rate | 27% |

**Visuals included:**
- % of Customers by Subscription Status (Donut Chart)
- Revenue by Category (Bar Chart)
- Sales by Category (Bar Chart)
- Revenue by Age Group (Horizontal Bar)
- Sales by Age Group (Horizontal Bar)

---

## 📈 Key Results & Insights

| # | Insight |
|---|---------|
| 1 | **Clothing** is the top revenue category (~$104K), followed by Accessories |
| 2 | **Male customers** generate 68% of total revenue ($157,890 vs $75,191) |
| 3 | **Subscribed customers** have a higher average spend than non-subscribers |
| 4 | **Young Adults** are the highest revenue-contributing age group |
| 5 | **73% of customers are unsubscribed** — a major growth opportunity |
| 6 | Many **repeat buyers (>5 purchases) are not subscribed** — a loyalty-conversion gap |
| 7 | **Free Shipping** is the most preferred shipping method |
| 8 | **PayPal** leads payment preferences across all segments |

---

## 🗂️ Repository Structure

```
📦 retail-behavior-insights
 ┣ 📄 customer_shopping_behavior.csv       # Raw dataset
 ┣ 📓 EDA_and_Cleaning.ipynb               # Jupyter Notebook (Python)
 ┣ 📄 SQL_queries.sql                      # All 10 PostgreSQL queries
 ┣ 📊 Customer_Behavior_Dashboard.pbix     # Power BI dashboard file
 ┣ 📝 Customer_Shopping_Behavior_Report.docx  # Full project report
 ┣ 📑 Presentation.pdf                     # Gamma AI presentation (exported)
 ┗ 📄 README.md                            # Project documentation
```

---

## ▶️ How to Run

### Python (EDA & Cleaning)
```bash
# Clone the repository
git clone https://github.com/Bhavyansh004/retail-behavior-insights.git
cd retail-behavior-insights

# Install dependencies
pip install pandas matplotlib sqlalchemy psycopg2-binary

# Run the notebook
jupyter notebook EDA_and_Cleaning.ipynb
```

### PostgreSQL (SQL Queries)
```bash
# 1. Create a database in pgAdmin or psql
CREATE DATABASE customer_behavior;

# 2. Run the notebook to load data into PostgreSQL
#    (SQLAlchemy connection is configured in the notebook)

# 3. Open SQL_queries.sql in pgAdmin or any SQL client and execute
```

### Power BI Dashboard
```
1. Open Customer_Behavior_Dashboard.pbix in Power BI Desktop
2. Update the data source path if needed
3. Refresh the dataset
```

---

## 📋 SQL Queries Included

| # | Query | Technique |
|---|-------|-----------|
| Q1 | Total revenue by gender | `GROUP BY`, `SUM` |
| Q2 | Discount users spending above average | Subquery, `WHERE` |
| Q3 | Top 5 products by avg review rating | `ORDER BY`, `LIMIT` |
| Q4 | Standard vs Express shipping avg spend | Conditional `WHERE` |
| Q5 | Subscriber vs non-subscriber spend | `GROUP BY`, aggregations |
| Q6 | Top 5 products by discount rate | `CASE WHEN`, `ROUND` |
| Q7 | Customer segmentation (New/Returning/Loyal) | `CTE`, `CASE WHEN` |
| Q8 | Top 3 products per category | `CTE`, `ROW_NUMBER()` window function |
| Q9 | Repeat buyers vs subscription status | `WHERE`, `COUNT` |
| Q10 | Revenue by age group | `GROUP BY`, `ORDER BY` |

---

## 👤 Author

**Bhavyansh Nandwana**  
📧 [nandwanabhavyansh1234@gmail.com](mailto:nandwanabhavyansh1234@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/bhavyansh-n-617627258/)  
🐙 [GitHub](https://github.com/Bhavyansh004)

---

*If you found this project helpful, please consider giving it a ⭐ on GitHub!*
