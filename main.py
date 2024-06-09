from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# change made in Feature_1 branch

# Read database credentials from environment variables
DB_SERVER = os.environ.get('DB_SERVER')
DB_NAME = os.environ.get('DB_NAME')
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql+pyodbc://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server'
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
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run()


# comment made by shubham