from employee import Employee

def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            age = input("Enter age: ")
            gender = input("Enter gender: ")
            department = input("Enter department: ")
            salary = input("Enter salary: ")
            employee = Employee(name=name, age=age, gender=gender, department=department, salary=salary)
            Employee.create_employee(employee)
            print("Employee added successfully!")
        
        elif choice == '2':
            employees = Employee.read_employees()
            print("\nEmployee List:")
            for emp in employees:
                print(emp)

        elif choice == '3':
            emp_id = int(input("Enter Employee ID to update: "))
            name = input("Enter new name: ")
            age = input("Enter new age: ")
            gender = input("Enter new gender: ")
            department = input("Enter new department: ")
            salary = input("Enter new salary: ")
            employee = Employee(emp_id=emp_id, name=name, age=age, gender=gender, department=department, salary=salary)
            Employee.update_employee(employee)
            print("Employee updated successfully!")

        elif choice == '4':
            emp_id = int(input("Enter Employee ID to delete: "))
            Employee.delete_employee(emp_id)
            print("Employee deleted successfully!")

        elif choice == '5':
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
