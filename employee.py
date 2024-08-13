from db_config import get_db_connection

class Employee:
    def __init__(self, emp_id=None, name = None, age = None, gender= None, department = None, salary = None):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.gender = gender
        self.department = department
        self.salary = salary

    @staticmethod
    def create_employee(employee):
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "INSERT INTO employees (name, age, gender, department, salary) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (employee.name, employee.age, employee.gender, employee.department, employee.salary))
        connection.commit()
        cursor.close()
        connection.close()
        
    @staticmethod
    def read_employees():
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM employees"
        cursor.execute(query)
        employees = cursor.fetchall()
        cursor.close()
        connection.close()
        return employees
    
    @staticmethod
    def update_employee(employee):
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "UPDATE employees SET name=%s, age=%s, gender=%s, department=%s, salary=%s WHERE emp_id=%s"
        cursor.execute(query, (employee.name, employee.age, employee.gender, employee.department, employee.salary, employee.emp_id))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def delete_employee(emp_id):
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "DELETE FROM employees WHERE emp_id=%s"
        cursor.execute(query, (emp_id,))
        connection.commit()
        cursor.close()
        connection.close()

