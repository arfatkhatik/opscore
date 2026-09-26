from models.employee import Employee
from utils.file_manager import save_employee, load_employees
def employee_menu():

    while True:
        print("\n")
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                                                              ║")
        print("║                    EMPLOYEE MANAGEMENT                       ║")
        print("║                                                              ║")
        print("╠══════════════════════════════════════════════════════════════╣")
        print("║                                                              ║")
        print("║      [1]   Add Employee                                      ║")
        print("║      [2]   View Employees                                    ║")
        print("║      [3]   Search Employee                                   ║")
        print("║      [4]   Update Employee                                   ║")
        print("║      [5]   Remove Employee                                   ║")
        print("║                                                              ║")
        print("║      [0]   Back to Main Menu                                 ║")
        print("║                                                              ║")
        print("╚══════════════════════════════════════════════════════════════╝")

        choice = input("\nEnter your choice:  ")

        if choice == "1":
             add_employee()
             input("press Enter to go back menu: ")

        elif choice == "2":
            print("\nView Employees selected.")
            view_employee()
            input("press Enter to go back menu: ")

        elif choice == "3":
            print("\nSearch Employee selected.")

        elif choice == "4":
            print("\nUpdate Employee selected.")

        elif choice == "5":
            print("\nRemove Employee selected.")

        elif choice == "0":
            break

        else:
            print("\nInvalid choice. Please try again.")

def add_employee():
                employee_id = input("Enter Employee ID: ")
                name = input("Enter name: ")
                email = input("Enter email: ")
                phone = input("Enter phone No: ")
                department = input("Enter Department: ")
                role = input("Enter Role: ")
                salary = input("Enter Salary: ")

                employee = Employee(employee_id, name, email, phone, department, role, salary)
                employee_data = {
                    "employee_id": employee.employee_id,
                    "name": employee.name,
                    "email": employee.email,
                    "phone": employee.phone,
                    "department": employee.department,
                    "role": employee.role,
                    "salary": employee.salary,
                    "status": employee.status
                }

                employees = load_employees()
                employees.append(employee_data)
                save_employee(employees)
                print("Employee added successfully")


def view_employee():
    employees = load_employees()
    if not employees:
        print("No employee found.")
        return
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                    EMPLOYEE DIRECTORY                        ║")
    print("╠══════════════════════════════════════════════════════════════╣")
    for employee in employees:
        print(f"    employee Id:           {employee["employee_id"]}")
        print(f"    Name:                  {employee["name"]}")
        print(f"    Department  :          {employee['department']}")
        print(f"    Role        :          {employee['role']}")
        print(f"    Salary      :          ₹{employee['salary']}")
        print(f"    Status      :          {employee['status']}")
        print("\n────────────────────────────────────────────────────────────────")


    print("╚══════════════════════════════════════════════════════════════╝")