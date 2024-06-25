from flask import Flask, jsonify 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    salary = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Employee {self.name}, {self.salary}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'salary': self.salary
        }

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/employees')
def get_employees():
    employees = Employee.query.all()
    return { "employees": [str(emp) for emp in employees] }

@app.route('/employee/<int:id>')
def get_employee(id):
    employee = Employee.query.get(id)  # Query employee by ID
    if employee:
        return jsonify(employee.serialize())  # Return serialized employee
    else:
        return jsonify({"error": "Employee not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
