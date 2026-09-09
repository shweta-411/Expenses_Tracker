

from flask import Flask,render_template,redirect,url_for,request,jsonify

import sqlite3

import datetime

app = Flask(__name__)

# Creating file based databsae and table
def init_db():
    conn = sqlite3.connect("expenses.db")
    cur=conn.cursor()
    cur.execute("""
        create table if not exists expenses(
            id integer primary key autoincrement,
            description text not null ,
            category text not null ,
            amount real not null ,
            date text not null 
        )
    """)
    conn.commit()
    conn.close()


# Show all records from table
@app.route("/")
def index():
    conn = sqlite3.connect("expenses.db")
    cur= conn.cursor()
    cur.execute("select * from expenses order by id asc")
    expenses = cur.fetchall()
    total = sum([row[3] for row in expenses])
    conn.close()
    return render_template("index.html",expenses=expenses,total=total,title="All Expenses")


# To Add Expenses into table
# Flask whenever sombody sends a post request to / add excute add()
@app.route("/add",methods=["POST"])
def add():
    description = request.form.get("description")
    category = request.form.get("category")
    amount = request.form.get("amount")
    date = request.form.get("date") or datetime.now().strftime("%Y-%m-%d")

    if description and category and amount :
        conn = sqlite3.connect("expenses.db")
        cur = conn.cursor()
        cur.execute(" INSERT INTO expenses(description,category,amount,date) values(?,?,?,?)",
                    (description,category,float(amount),date))
        conn.commit()
        conn.close()
    return redirect(url_for("index"))


# Delete records from table by expense id
@app.route("/delete/<int:expense_id>")
def delete(expense_id):
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM expenses WHERE id = ?",(expense_id))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


# Filter data by month by year by quarter by custom range
@app.route("/filter",methods=["GET","POST"])
def filter_expenses():
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()

    filter_type = request.args.get("type")

    title = ""

    if filter_type == "day" :
        today = datetime.now().strftime("%Y-%m-%d")
        cur.execute("SELECT * FROM expenses WHERE date = ?",(today))
        title = f"Expenses for Today - {today}"

    elif filter_type == "month":
        month = datetime.now().strftime("%Y-%m")
        cur.execute("SELECT * FROM expenses WHERE strftime('%Y-%m',date)= ?",(month))
        title = f"Expenses for This Month - {month}"

    elif filter_type == "year":
        year = datetime.now().strftime("%Y")
        cur.execute("SELECT * FROM expenses WHERE strftime('%Y',date)=?",(year))
        title = f"Expenses for This Year - {year}"

    elif filter_type == "quarter":
        month = datetime.now().month
        year = datetime.now().strftime("%Y")

        if month in [1,2,3] :
            start , end = 1,3
            q = "Q1"

        elif month in [4,5,6]:
            start , end = 4,6
            q = "Q2"

        elif month in [7,8,9]:
            start , end = 7,9
            q = "Q3"

        else:
            start , end = 10,12
            q = "Q4"

        cur.execute("""SELECT * FROM expenses 
                        WHERE strftime('%Y',date) = ?
                        AND CAST(strftime('%m',date) as INTEGER) BETWEEN ? AND ? """,
                        (year,start,end))
        title = f"Expenses for this Quarter - {q} and year {year}"


# customized date range (from_date , to_date)
    elif request.method == "POST":
        from_date = request.form.get("from_date")
        to_date = request.form.get("to_date")

        if from_date and to_date :
            cur.execute("SELECT * FROM expenses WHERE date BETWEEN ? AND ? ORDER BY date DESC",
                        (from_date,to_date))
            title = f"Expenses from {from_date} to {to_date}"
        else:
            cur.execute("SELECT * FROM expenses ORDER BY id DESC")
            title = "All Expenses"

    else:
        cur.execute("SELECT * FROM expenses ORDER BY id ASC")
        title = "All Expenses"

    expenses = cur.fetchall()
    total = sum([row[3] for row in expenses])
    conn.close()

    return render_template("index.html",expenses=expenses,total=total,title=title)

        
        
    # Group By Category caculated total of amount
# using chart 
@app.route('/chart-date')
def chart_date():
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()
    cur.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    category_data = cur.fetchall()
    conn.close()

    labels = [row[0] for row in category_data]
    values = [row[1] for row in category_data]
    return jsonify({"labels":labels,"values":values})


# ---- Run App------
if __name__ == "__main__":
    init_db() # calls your database function
    app.run(debug=True) # starts your flask server outcome is like this : running to url 





