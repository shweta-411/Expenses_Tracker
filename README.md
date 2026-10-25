# Expense Tracker Web Application

## Project Overview

The Expense Tracker is a web application developed using Python and Flask to record, manage, and track daily expenses. It stores expense details in an SQLite database and helps users review spending over different time periods.

## Features

- **Add Expenses:** Record an expense with its description, category, amount, and date.
- **Delete Expenses:** Remove expense records.
- **View All Expenses:** Display saved expenses and calculate the total amount.
- **Daily Expense Filter:** View expenses for the current day.
- **Monthly Expense Filter:** Review expenses for the current month.
- **Yearly Expense Filter:** Review expenses for the current year.
- **Quarterly Expense Filter:** Filter expenses by the current quarter.
- **Custom Date Range:** View expenses between selected dates.
- **Category-wise Chart Data:** Summarize expense amounts by category for visualization.

## Technologies Used

- **Python** — Application logic
- **Flask** — Web application framework
- **SQLite** — Database for storing expense records
- **HTML, CSS, JavaScript** — Frontend technologies, if used in the templates

## Database Structure

The application uses an `expenses` table with the following fields:

| Column | Description |
|---|---|
| `id` | Unique expense ID |
| `description` | Expense description |
| `category` | Expense category |
| `amount` | Expense amount |
| `date` | Expense date |

## Project Structure

```text
Expenses_Tracker/
├── app.py
├── expenses.db
├── static/
├── templates/
└── README.md
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/shweta-411/Expenses_Tracker.git
```

### 2. Open the project folder

```bash
cd Expenses_Tracker
```

### 3. Install Flask

```bash
pip install flask
```

### 4. Run the application

```bash
python app.py
```

### 5. Open the application

Open the local URL displayed in the terminal, usually:

```text
http://127.0.0.1:5000/
```

## Learning Outcomes

- Building a web application using Flask
- Connecting Python with an SQLite database
- Performing database operations using SQL
- Implementing date-based filtering
- Calculating total and category-wise expenses
- Working with routes, forms, and templates

## Conclusion

This project demonstrates how Python, Flask, and SQLite can be used together to build an expense tracking application. It provides practical experience in web development, database management, and expense organization.

## Author

Shweta Patil

GitHub: [Expenses_Tracker](https://github.com/shweta-411/Expenses_Tracker)
