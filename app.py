# app.py
from flask import Flask, jsonify
from tasks import count_birthdays_by_month, read_employees

app = Flask(__name__)

@app.route("/birthdays")
def get_birthdays():
    try:
        employees = read_employees("employees.csv")
        result = count_birthdays_by_month(employees)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
