import sqlite3
from flask import Flask, render_template_string, request

app = Flask(_name_)
DATABASE = "users.db"


def init_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
    )
    cursor.execute(
        "INSERT OR IGNORE INTO users (id, username, password) VALUES (1, 'admin', 'admin123')"
    )
    conn.commit()
    conn.close()


init_database()


@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # INTENTIONALLY VULNERABLE CODE (لأغراض التعليم والاختبار)
        query = f"""
        SELECT * FROM users
        WHERE username = '{username}'
        AND password = '{password}'
        """

        print("\n[DEBUG] SQL Query:")
        print(query)

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        try:
            cursor.execute(query)
            user = cursor.fetchone()
            if user:
                message = f"SUCCESS: Welcome {user[1]}!"
            else:
                message = "FAILED: Invalid credentials."
        except Exception as e:
            message = f"ERROR: {e}"
        finally:
            conn.close()

    return render_template_string(
        """
        <!DOCTYPE html>
        <html>
        <head><title>SQL Injection Lab</title></head>
        <body style="font-family: Arial, sans-serif; margin: 40px;">
            <h2>SQL Injection Demo Login</h2>
            <form method="POST">
                <label>Username:</label><br>
                <input type="text" name="username" style="width: 300px;"><br><br>
                <label>Password:</label><br>
                <input type="password" name="password" style="width: 300px;"><br><br>
                <input type="submit" value="Login">
            </form>
            <h3>{{ message }}</h3>
        </body>
        </html>
    """,
        message=message,
    )


if _name_ == "_main_":
    app.run(debug=True, port=5000)