from flask import Flask, render_template
import os
import mysql.connector

app = Flask(__name__)
db_host = "db"  # MySQL host
db_user = "root"  # MySQL username
db_password = "1234"  # MySQL password
db_name = "develop"  # MySQL database name

# Function to execute the init.sql file
def execute_init_script():
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cursor = conn.cursor()
    print("connected")
# Function to increment the visit count
def increment_visit_count():
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cursor = conn.cursor()
    cursor.execute("UPDATE visits SET count = count + 1")
    conn.commit()
    conn.close()

# Function to retrieve the current visit count
def get_visit_count():
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cursor = conn.cursor()
    cursor.execute("SELECT count FROM visits")
    count = cursor.fetchone()
    conn.close()
    return count[0] if count else 0

@app.route("/")
def hello_world():
    increment_visit_count()
    count = get_visit_count()
    return render_template("index.html", count=count)


if __name__ == "__main__":
    execute_init_script()  # Execute the init.sql file
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
