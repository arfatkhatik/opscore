from utils.file_manager import (load_jobs, load_employees, load_assignments, save_assignments , save_jobs)
from datetime import datetime
from models.assignment import Assignment


def assignment_menu():

    while True:
        print("\n")
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                                                              ║")
        print("║                 ASSIGNMENT & SCHEDULING                      ║")
        print("║                                                              ║")
        print("╠══════════════════════════════════════════════════════════════╣")
        print("║                                                              ║")
        print("║      [1]   Assign Employee to Job                            ║")
        print("║      [2]   View Assignments                                  ║")
        print("║      [3]   Search Assignment                                 ║")
        print("║      [4]   Update Assignment                                 ║")
        print("║      [5]   Remove Assignment                                 ║")
        print("║                                                              ║")
        print("║      [6]   Employee Availability                             ║")
        print("║      [7]   Job Schedule                                      ║")
        print("║                                                              ║")
        print("║      [0]   Back to Main Menu                                 ║")
        print("║                                                              ║")
        print("╚══════════════════════════════════════════════════════════════╝")

        choice = input("Enter your choice: ")

        if choice == "1":
            assign_employee()
            input("Press Enter to go back to menu: ")

        elif choice == "2":
            view_assignments()
            input("Press Enter to go back to menu: ")

        elif choice == "3":
            print("Search Assignment selected.")
            input("Press Enter to go back to menu: ")

        elif choice == "4":
            print("Update Assignment selected.")
            input("Press Enter to go back to menu: ")

        elif choice == "5":
            print("Remove Assignment selected.")
            input("Press Enter to go back to menu: ")

        elif choice == "6":
            print("Employee Availability selected.")
            input("Press Enter to go back to menu: ")

        elif choice == "7":
            print("Job Schedule selected.")
            input("Press Enter to go back to menu: ")

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")


def assign_employee():
    jobs = load_jobs()
    employees = load_employees()

    if not jobs:
        print("No Jobs Found.")
        return

    ask_job = input("Enter job ID: ").lower().strip()

    for job in jobs:
        if job['job_id'].lower() == ask_job:
            print(f"\n    Job ID        :          {job['job_id']}")
            print(f"    Customer ID   :          {job['customer_id']}")
            print(f"    Job Title     :          {job['job_title']}")
            print(f"    Description   :          {job['description']}")
            print(f"    Priority      :          {job['priority']}")
            print(f"    Status        :          {job['status']}")
            print(f"    Schedule Date :          {job['schedule_date']}")
            break
    else:
        print("No job Found with that ID")
        return

    ask_employee = input("Enter employee ID: ").lower().strip()

    for employee in employees:
        if employee['employee_id'].lower() == ask_employee:
            print(f"    employee Id:           {employee['employee_id']}")
            print(f"    Name:                  {employee['name']}")
            print(f"    Department  :          {employee['department']}")
            print(f"    Role        :          {employee['role']}")
            print(f"    Salary      :          ₹{employee['salary']}")
            print(f"    Status      :          {employee['status']}")
            break
    else:
        print("No employee found with that ID")
        return

    assignments = load_assignments()
    assignment_number = len(assignments) +1
    assignment_id = f"A{assignment_number:03d}"

    assigned_date = datetime.now().strftime("%Y-%m-%d")

    assignment = Assignment(
        assignment_id,
        job["job_id"],
        employee["employee_id"],
        assigned_date
    )

    assignment_data = {
        "assignment_id": assignment.assignment_id,
        "job_id": assignment.job_id,
        "employee_id": assignment.employee_id,
        "assigned_date": assignment.assignment_date,
        "status": assignment.status
    }
    assignments.append(assignment_data)
    save_assignments(assignments)

    job['status'] = "assigned"
    save_jobs(jobs)

    print("\nEmployee assigned to job successfully.")
    print(f"Assignment ID : {assignment.assignment_id}")


def view_assignments():
    assignments = load_assignments()
        
    if not assignments:
        print("No assignment found.")
        return

    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                    ASSIGNMENT DIRECTORY                      ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
            """)

    for assignment in assignments:
        print(f"    Assignment ID :          {assignment['assignment_id']}")
        print(f"    Job ID        :          {assignment['job_id']}")
        print(f"    Employee ID   :          {assignment['employee_id']}")
        print(f"    Assigned Date :          {assignment['assigned_date']}")
        print(f"    Status        :          {assignment['status']}")
        print("\n────────────────────────────────────────────────────────────────")


    print("""
╚══════════════════════════════════════════════════════════════╝
            """)