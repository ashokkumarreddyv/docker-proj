from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    try:
        db = mysql.connector.connect(
            host="mysql",
            user="root",
            password="root",
            database="testdb"
        )
        cursor = db.cursor()
        cursor.execute("SELECT 'Hello from Yodhan & Hithwik 🚀'")
        result = cursor.fetchone()
        return result[0]
    except Exception as e:
        return str(e)

app.run(host='0.0.0.0', port=5000)