
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
        print("║      [8]   Find Available Employees                          ║")
        print("║      [9]   Recommend Employees                               ║")
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
            check_employee_availability()
            input("Press Enter to go back to menu: ")

        elif choice == "7":
            job_schedule()
            input("Press Enter to go back to menu: ")
        elif choice == "8":
            find_available_employees()
            input("Press Enter to go back to menu: ")
        elif choice == "9":
            recommend_employees()
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
            if employee['status'].lower() != "active":
                print("Employee is not active and cannot be assigned to a job.")
                return
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


def check_employee_availability():
    employees = load_employees()
    assignments = load_assignments()
    jobs = load_jobs()

    ask_employee = input("Enter Employee ID: ").lower().strip() 
    ask_date = input("Enter Date (YYYY-MM-DD): ").strip()       

    for employee in employees:
        if employee['employee_id'].lower() == ask_employee:
            break
    else:
        print("No employee found with that ID.")  
        return  

    try:
        requested_date = datetime.strptime(ask_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. please use YYYY-MM-DD format.")
        return

    has_conflict = False
    for assignment in assignments:
        if assignment['employee_id'].lower() != employee['employee_id'].lower():
            continue

        for job in jobs:
            if job['job_id'].lower() == assignment['job_id'].lower():
                job_date = datetime.strptime(job['schedule_date'], "%Y-%m-%d").date()
                if job_date == requested_date:
                    has_conflict = True
                    
                    print(f"\nEmployee: {employee['name']}")
                    print(f"Employee ID: {employee['employee_id']}")
                    print(f"Existing Job: {job['job_title']}")
                    print(f"Job ID: {job['job_id']}")
                    print(f"Scheduled Date: {job['schedule_date']}")
                    print("\nAvailability: NOT AVAILABLE")

                return
                
    if not has_conflict:
        print(f"\nEmployee: {employee['name']}")
        print(f"Employee ID: {employee['employee_id']}")
        print(f"Requested Date: {ask_date}")
        print("\nAvailability: AVAILABLE")


def find_available_employees():
    jobs = load_jobs()
    assignments = load_assignments()
    employees = load_employees()

    ask_job_id = input("Enter job ID to find available employees: ").lower().strip()
    found_job = False

    for job in jobs:
        if job['job_id'].lower() == ask_job_id:
            found_job = True
            requested_job = job
            break

    if not found_job:
        print("No job found with that ID.")
        return

    job_date = datetime.strptime(requested_job['schedule_date'], "%Y-%m-%d").date()

    print("\n────────────────────────────────────────────────────────────────")
    print("JOB DETAILS:")
    print(f"\n      Job ID        :          {requested_job['job_id']}")
    print(f"      Customer ID   :          {requested_job['customer_id']}")
    print(f"      Job Title     :          {requested_job['job_title']}")
    print(f"      Schedule Date :          {job_date}")
    print(f"      Priority      :          {requested_job['priority']}")
    print(f"      Status        :          {requested_job['status']}")
    print("\n────────────────────────────────────────────────────────────────")

    available_found = False
    for employee in employees:
        if employee['status'].lower() != "active":
            continue

        has_conflict = False
        for assignment in assignments:
            if assignment['employee_id'].lower() != employee['employee_id'].lower():
                continue

            for assigned_job in jobs:
                if assigned_job['job_id'].lower() == assignment['job_id'].lower():
                    assigned_job_date = datetime.strptime(assigned_job['schedule_date'], "%Y-%m-%d").date()

                    if assigned_job_date == job_date:
                        has_conflict = True
                        break
            if has_conflict:
                break

        if not has_conflict:
            available_found = True
            print("\n────────────────────────────────────────────────────────────────")
            print("AVAILABLE EMPLOYEE DETAILS:")
            print(f"\n      Employee ID   :          {employee['employee_id']}")
            print(f"      Employee Name :          {employee['name']}")
            print(f"      Department    :          {employee['department']}")
            print(f"      Role          :          {employee['role']}")
            print(f"      Availability  :          AVAILABLE")
            print("\n────────────────────────────────────────────────────────────────")

    if not available_found:
        print("No available employees found for the specified job date.")


def recommend_employees():
    jobs = load_jobs()
    assignments = load_assignments()
    employees = load_employees()

    ask_job_id = input("Enter job ID to find recommended employees: ").lower().strip()

    active_employees = list(filter(lambda employee: employee['status'].lower() == "active", employees))
    found = False
    for job in jobs:
        if job['job_id'].lower() == ask_job_id:
            found = True
            requested_job = job
            break
    if not found:
        print("No job found with that ID.")
        return
    
    job_date = datetime.strptime(requested_job['schedule_date'], "%Y-%m-%d").date()

    for employee in active_employees:
        has_conflict = False
        for assignment in assignments:
            if assignment['employee_id'].lower() != employee['employee_id'].lower():
                continue
            for assigned_job in jobs:
                if assigned_job['job_id'].lower() == assignment['job_id'].lower():
                    assigned_job_date = datetime.strptime(assigned_job['schedule_date'], "%Y-%m-%d").date()
                    if assigned_job_date == job_date:
                        has_conflict = True
                        break
            if has_conflict:
                break

        if not has_conflict:
            print("\n────────────────────────────────────────────────────────────────")
            print("RECOMMENDED EMPLOYEE DETAILS:")
            print(f"\n      Employee ID   :          {employee['employee_id']}")
            print(f"      Employee Name :          {employee['name']}")
            print(f"      Department    :          {employee['department']}")
            print(f"      Role          :          {employee['role']}")
            print(f"      Availability  :          AVAILABLE")
            print("\n────────────────────────────────────────────────────────────────")
