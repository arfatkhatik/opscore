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
            view_employee()
            input("press Enter to go back menu: ")

        elif choice == "3":
            search_employee()
            input("Press Enter to go back to menu: ")
        elif choice == "4":
            update_employee()
            input("Press Enter to go back to menu: ")

        elif choice == "5":
            remove_employee()
            input("Press Enter to go back to menu: ")

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
        print(f"    employee Id:           {employee['employee_id']}")
        print(f"    Name:                  {employee['name']}")
        print(f"    Department  :          {employee['department']}")
        print(f"    Role        :          {employee['role']}")
        print(f"    Salary      :          ₹{employee['salary']}")
        print(f"    Status      :          {employee['status']}")
        print("\n────────────────────────────────────────────────────────────────")


    print("╚══════════════════════════════════════════════════════════════╝")


def search_employee():
    employees = load_employees()

    if not employees:
        print("No employees found.")
        return

    search_id = input("Enter Employee ID: ")

    for employee in employees:
         if employee['employee_id'].lower() == search_id.lower():
            print("Employee found.")
            print("────────────────────────────────────────")
            print(f"    employee Id:           {employee['employee_id']}")
            print(f"    Name:                  {employee['name']}")
            print(f"    Department  :          {employee['department']}")
            print(f"    Role        :          {employee['role']}")
            print(f"    Salary      :          ₹{employee['salary']}")
            print(f"    Status      :          {employee['status']}")
            print("────────────────────────────────────────")

            return

    print("Employee not found")


def update_employee():
    employees = load_employees()

    if not employees:
        print("No employees found.")
        return

    search_id = input("Enter id to update: ")

    for employee in employees:
        if employee['employee_id'].lower() == search_id.lower():
            print("Employee found.")
            print("────────────────────────────────────────────────────────────────")
            print(f"employee Id:           {employee['employee_id']}")
            print(f"Name:                  {employee['name']}")
            print(f"Department  :          {employee['department']}")
            print(f"Role        :          {employee['role']}")
            print(f"Salary      :          ₹{employee['salary']}")
            print(f"Status      :          {employee['status']}")
            print("────────────────────────────────────────────────────────────────")

            print("""
                What do you want to update?

                    [1] Name
                    [2] Email
                    [3] Phone
                    [4] Department
                    [5] Role
                    [6] Salary
                    [7] Status
                    [0] Cancel

                 """)
            choice = input("Enter option number: ")
            if choice == "1":
                 employee['name'] = input("Enter new name: ")
            elif choice == "2":
                employee['email'] = input("Enter new email: ")
            elif choice == "3":
                employee['phone'] = input("Enter new phone number: ")
            elif choice == "4":
                employee['department'] = input("Enter new department: ")
            elif choice == "5":
                 employee['role'] = input("Enter new role: ")
            elif choice == "6":
                 employee['salary'] = input("Enter new salary: ")
            elif choice == "7":
                employee['status'] = input("Enter new status: ")
            elif choice == "0":
                print("Update cancelled.")
                return
            else:
                print("Invalid option.")
                return

            save_employee(employees)

            print("Employee details updated successfully.")
            return


def remove_employee():
    employees = load_employees()

    if not employees:
        print("NO Employees found.")
        return

    employee_id = input("Enter id to remove Employee: ")

    for employee in employees:
        if employee['employee_id'].lower() == employee_id.lower():
            print("Employee found.")
            print("────────────────────────────────────────────────────────────────")
            print(f"employee Id:           {employee['employee_id']}")
            print(f"Name:                  {employee['name']}")
            print(f"Department  :          {employee['department']}")
            print(f"Role        :          {employee['role']}")
            print(f"Salary      :          ₹{employee['salary']}")
            print(f"Status      :          {employee['status']}")
            print("────────────────────────────────────────────────────────────────")

            confirmation = input("Do you really want to remove this Employee (yes/no): ").lower().strip()
            if confirmation == "yes":
                employees.remove(employee)
                save_employee(employees)
                print(f"Employee named {employee['name']} removed successfully.")
                return
            elif confirmation == "no":
                print("Employee removal canceled.")
                return
            else:
                print("Invalid option.")
                return
    print("Employee not found.")
    
     