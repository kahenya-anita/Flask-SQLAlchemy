from app import app, db, Employee  # Import app, db, and Employee model from app

# Function to seed initial data into the database
def seed_data():
    with app.app_context():  # Ensure operations are within the Flask app context
        db.create_all()  # Create all tables
        # Create sample employee data
        employee1 = Employee(name='Alice', salary=50000)
        employee2 = Employee(name='Bob', salary=60000)
        db.session.add(employee1)  # Add employee1 to the session
        db.session.add(employee2)  # Add employee2 to the session
        db.session.commit()  # Commit the session to save changes

# Run the seed function if this script is executed directly
if __name__ == '__main__':
    seed_data()
