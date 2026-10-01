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
            search_assignment()
            input("Press Enter to go back to menu: ")

        elif choice == "4":
            update_assignment()
            input("Press Enter to go back to menu: ")

        elif choice == "5":
            remove_assignment()
            input("Press Enter to go back to menu: ")

        elif choice == "6":
            employee_assignment()
            input("Press Enter to go back to menu: ")

        elif choice == "7":
            job_schedule()
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
            print("\n────────────────────────────────────────────────────────────────")
            print(f"\n    Job ID        :          {job['job_id']}")
            print(f"    Customer ID   :          {job['customer_id']}")
            print(f"    Job Title     :          {job['job_title']}")
            print(f"    Description   :          {job['description']}")
            print(f"    Priority      :          {job['priority']}")
            print(f"    Status        :          {job['status']}")
            print(f"    Schedule Date :          {job['schedule_date']}")
            print("\n────────────────────────────────────────────────────────────────")
            break
    else:
        print("No job Found with that ID")
        return

    ask_employee = input("Enter employee ID: ").lower().strip()

    for employee in employees:
        if employee['employee_id'].lower() == ask_employee:
            print("\n────────────────────────────────────────────────────────────────")
            print(f"    employee Id:           {employee['employee_id']}")
            print(f"    Name:                  {employee['name']}")
            print(f"    Department  :          {employee['department']}")
            print(f"    Role        :          {employee['role']}")
            print(f"    Salary      :          ₹{employee['salary']}")
            print(f"    Status      :          {employee['status']}")
            print("\n────────────────────────────────────────────────────────────────")
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


def search_assignment():
    assignments = load_assignments()

    if not assignments:
        print("No assignment Found.")
        return

    user_id = input("Enter assignment ID to search: ").lower()

    for assignment in assignments:
        if assignment['assignment_id'].lower() == user_id:
            print("\n────────────────────────────────────────────────────────────────")
            print(f"    Assignment ID :          {assignment['assignment_id']}")
            print(f"    Job ID        :          {assignment['job_id']}")
            print(f"    Employee ID   :          {assignment['employee_id']}")
            print(f"    Assigned Date :          {assignment['assigned_date']}")
            print(f"    Status        :          {assignment['status']}")
            print("\n────────────────────────────────────────────────────────────────")
            return
    print("No assignment Found.")


def update_assignment():
    assignments = load_assignments()
    employees = load_employees()
    jobs = load_jobs()

    if not assignments:
        print("No assignment found.")
        return

    user_id = input("Enter assigned ID to update: ").lower().strip()

    for assignment in assignments:
        if assignment['assignment_id'].lower() == user_id:
            print("\n────────────────────────────────────────────────────────────────")
            print(f"    Assignment ID :          {assignment['assignment_id']}")
            print(f"    Job ID        :          {assignment['job_id']}")
            print(f"    Employee ID   :          {assignment['employee_id']}")
            print(f"    Assigned Date :          {assignment['assigned_date']}")
            print(f"    Status        :          {assignment['status']}")
            print("\n────────────────────────────────────────────────────────────────")

            print("""
            [1] Update Employee ID
            [2] Update Job ID
            [3] Update Assigned Date
            [4] Update Status
            [0] Cancel
            """)

            choice = input("Enter your Choice: ").lower().strip()

            if choice in ("1", "employee id", "update employee id"):
                new_employee_id = input("Enter new employee ID: ").strip()
                for employee in employees:

                    if employee['employee_id'].lower() == new_employee_id.lower():

                        assignment['employee_id'] = employee['employee_id']

                        save_assignments(assignments)

                        print(
                            f"Employee ID changed to "
                            f"{employee['employee_id']}."
                        )

                        return
                print("Employee not found.")
                return
            elif choice in ("2","job id", "update job id"):
                new_job_id = input("Enter new job id: ").strip()
                for job in jobs:

                    if job['job_id'].lower() == new_job_id.lower():

                        assignment['job_id'] = job['job_id']

                        save_assignments(assignments)

                        print(
                            f"Job ID changed to "
                            f"{job['job_id']}."
                        )

                        return
                print("NO job found.")
                return
            elif choice in ("3", "assigned date", "update assigned date"):
                new_assigned_date = input("Enter new assigned date: ").strip()

                assignment['assigned_date'] = new_assigned_date

                save_assignments(assignments)

                print(
                    f"Assigned date changed to "
                    f"{new_assigned_date}."
                )

                return
            elif choice in ("4", "status", "update status"):
                new_status = input("Enter new status")
                assignment['status'] = new_status
                save_assignments(assignments)
                print(f"status changed to {new_status}.")
            elif choice in ("0", "cancel"):
                return
            else:
                print("Invalid option.")

            

    print("Assignment not found.")


def remove_assignment():
    assignments = load_assignments()

    if not assignments:
        print("No assignment found.")
        return

    user_id = input("Enter assignment ID to remove: ").lower().strip()
    for assignment in assignments:
        if assignment['assignment_id'].lower() == user_id:
            print("\n────────────────────────────────────────────────────────────────")
            print(f"    Assignment ID :          {assignment['assignment_id']}")
            print(f"    Job ID        :          {assignment['job_id']}")
            print(f"    Employee ID   :          {assignment['employee_id']}")
            print(f"    Assigned Date :          {assignment['assigned_date']}")
            print(f"    Status        :          {assignment['status']}")
            print("\n────────────────────────────────────────────────────────────────")

            print("Do you really want to cancel this assignment ?")
            confirmation = input("[1] Yes [2] No \nEnter option: ")
            if confirmation in ("1", "yes"):
                assignments.remove(assignment)
                save_assignments(assignments)
                print("assignment removed successfully.")
                return
            elif confirmation in ("2", "no"):
                print("assignment removal canceled.")
                return
            else:
                print("Invalid option selected.")
                return
    print("No assignment found.")
    return


def employee_assignment():
    employees = load_employees()
    assignments = load_assignments()

    ask_id = input("Enter Employee ID to check avaiblity: ").lower().strip()

    for employee in employees:
        if employee['employee_id'].lower() == ask_id:
            print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                    EMPLOYEE AVAILABILITY                     ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
""")
            print(f"    employee Id:           {employee['employee_id']}")
            print(f"    Name:                  {employee['name']}")
            print(f"    Department  :          {employee['department']}")
            print(f"    Role        :          {employee['role']}")
            print(f"    Salary      :          ₹{employee['salary']}")
            print(f"    Status      :          {employee['status']}")
            print("\n────────────────────────────────────────────────────────────────")

            has_assignment = False
            for assignment in assignments:
                if assignment['employee_id'].lower() == employee['employee_id'].lower():
                    has_assignment = True
                    print(f"    Assignment ID   :       {assignment['assignment_id']}")
                    print(f"    Job ID          :       {assignment['job_id']}")
                    print(f"    Status          :       {assignment['status']}")
                    print("\n────────────────────────────────────────────────────────────────")
            if has_assignment:
                print("            Employee currently has an assignment.")
                print("                Availability: NOT AVAILABLE")
            elif not has_assignment:
                print("                Availability: AVAILABLE")
                        
            print("\n╚══════════════════════════════════════════════════════════════╝")




def job_schedule():
    jobs = load_jobs()
    assignments = load_assignments()
    employees = load_employees()

    ask_job = input("Enter job ID to check schedule: ").lower().strip()

    for job in jobs:
        if job['job_id'].lower() == ask_job:
            print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                       JOB SCHEDULE                           ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
                    """)
            print("\n────────────────────────────────────────────────────────────────")
            print("JOB DETAILS:")
            print(f"\n      Job ID        :          {job['job_id']}")
            print(f"      Customer ID   :          {job['customer_id']}")
            print(f"      Job Title     :          {job['job_title']}")
            print(f"      Schedule Date :          {job['schedule_date']}")
            print(f"      Status        :          {job['status']}")
            print("\n────────────────────────────────────────────────────────────────")
            assignment_found = False
            for assignment in assignments:
                if assignment['job_id'].lower() == job['job_id'].lower():
                    assignment_found = True
                    for employee in employees:
                        if employee['employee_id'].lower() == assignment['employee_id'].lower():
                            print("ASSIGNED EMPLOYEE DETAILS:")
                            print(f"\n      Assignment ID :          {assignment['assignment_id']}")
                            print(f"      Employee ID   :          {assignment['employee_id']}")
                            print(f"      Assigned Date :          {assignment['assigned_date']}")
                            print(f"      Status        :          {assignment['status']}")
                            print("\n────────────────────────────────────────────────────────────────")
                    if not assignment_found:
                        print("No Employee Assigned to this Job.")
            print("\n╚══════════════════════════════════════════════════════════════╝")
            return
            