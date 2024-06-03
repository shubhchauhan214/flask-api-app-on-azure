from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


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
    # Query all employees from the Employee table
    employees = Employee.query.all()

    # Convert the result to a list of dictionaries
    employee_list = [{"ID": emp.ID, "FirstName": emp.FirstName, "LastName": emp.LastName} for emp in employees]

    # Return the list as JSON
    return jsonify(employee_list)

if __name__ == "__main__":
    app.run()