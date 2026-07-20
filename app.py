import streamlit as st
from datetime import datetime
from database import (
    save_salary,
    get_latest_salary,
    save_expense,
    get_total_expenses,
    get_category_expenses,
    get_all_expenses,
)
st.set_page_config(
    page_title="Personal Expense & Savings Tracker",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Personal Expense & Savings Tracker")

# Salary
st.header("💼 Monthly Salary")

current_month = datetime.now().strftime("%B")

salary = st.number_input(
    "Enter Monthly Salary (₹)",
    min_value=0,
    step=100
)

if st.button("Save Salary"):
    save_salary(current_month, salary)
    st.success("Salary Saved Successfully!")

# Dashboard
latest_salary = get_latest_salary()
total_expenses = get_total_expenses()

remaining_balance = latest_salary - total_expenses
savings = remaining_balance if remaining_balance > 0 else 0

st.divider()
st.header("📊 Dashboard")

col1, col2 = st.columns(2)

with col1:
    st.metric("💰 Monthly Salary", f"₹{latest_salary:,.0f}")

with col2:
    st.metric("💸 Total Expenses", f"₹{total_expenses:,.0f}")

col3, col4 = st.columns(2)

with col3:
    st.metric("💵 Remaining Balance", f"₹{remaining_balance:,.0f}")

with col4:
    st.metric("🏦 Monthly Savings", f"₹{savings:,.0f}")

st.divider()

if total_expenses <= latest_salary:
    st.success("🟢 You are within your budget.")
else:
    st.error("🔴 Budget Exceeded!")
st.divider()

st.subheader("📊 Expense Category Analysis")

category_data = get_category_expenses()

if category_data:

    chart_data = {}

    for category, amount in category_data:
        chart_data[category] = amount

    st.bar_chart(chart_data)

else:
    st.info("No expense data available yet.")

# Add Expense
st.header("➕ Add Expense")

expense_date = st.date_input("Date")

category = st.selectbox(
    "Category",
    [
        "Food",
        "Travel",
        "Shopping",
        "Bills",
        "Medical",
        "Education",
        "Entertainment",
        "Other"
    ]
)

amount = st.number_input(
    "Expense Amount (₹)",
    min_value=0,
    step=100
)

description = st.text_input("Description")

if st.button("Save Expense"):
    st.write(category)
    save_expense(
        str(expense_date),
        category,
        amount,
        description
    )
    st.success("Expense Saved Successfully!")