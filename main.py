from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import logging
from logging.handlers import RotatingFileHandler


app = Flask(__name__)

# Configure logging
if not app.debug:
    handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.ERROR)
    app.logger.addHandler(handler)

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://admin123:#WRwinInferno2@flasktestdbserver.database.windows.net/testdb?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Define a model for the Employee table
class Employee(db.Model):
    __tablename__ = 'Employee'
    ID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50))
    LastName = db.Column(db.String(50))

@app.route("/")
def home():
    return "This is home from api."

@app.route("/getdetails/<username>")
def get_user(username):
    return "Hi " + username + " . We are getting this from our api."

@app.route("/employees", methods=['GET'])
def get_employees():
    try:
        employees = Employee.query.all()
        return jsonify([{"ID": emp.ID, "FirstName": emp.FirstName, "LastName": emp.LastName} for emp in employees])
    except Exception as e:
        app.logger.error('Error fetching employees: %s', e)
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run()