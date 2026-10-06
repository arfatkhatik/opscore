from utils.file_manager import (load_employees,save_employee,load_jobs,save_jobs,load_assignments,save_assignments,load_customers,save_customer,load_invoices,save_invoices,load_payments,save_payments)
def reports_menu():
    while True:
        print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                    REPORTS & ANALYTICS                       ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║   [1] Operations Summary                                     ║
║   [2] Job Performance Report                                 ║
║   [3] Employee Performance Report                            ║
║   [4] Financial Report                                       ║
║   [0] Back to Main Menu                                      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
""")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            operations_summary()
        elif choice == "2":
            job_performance_report()
        elif choice == "3":
            employee_performance_report()
        elif choice == "4":
            financial_report()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")


def operations_summary():
    employees = load_employees()
    customers = load_customers()
    jobs = load_jobs()
    assignments = load_assignments()
    invoices = load_invoices()
    while True:
        print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                       REPORTS DIRECTORY                      ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
    """)
        print("                       EMPLOYEES REPORT")
        print(f"\n      • TOTAL EMPLOYEES: {len(employees)}")
        active_emp = 0
        inactive_emp = 0
        for employee in employees:
            if employee['status'].lower() == "active":
                active_emp += 1
            else:
                inactive_emp += 1
        print(f"      • ACTIVE EMPLOYEES: {active_emp}")
        print(f"      • INACTIVE EMPLOYEES: {inactive_emp}")
        print("\n────────────────────────────────────────────────────────────────")
        print("\n                      CUSTOMERS REPORT")
        print(f"\n      • TOTAL CUSTOMERS: {len(customers)}")
        active_cus = 0
        inactive_cus = 0
        for customer in customers:
            if customer['status'].lower() == "active":
                active_cus += 1
            else:
                inactive_cus += 1
        print(f"      • ACTIVE CUSTOMERS: {active_cus}")
        print(f"      • INACTIVE CUSTOMERS: {inactive_cus}")
        print("\n────────────────────────────────────────────────────────────────")
        print("\n                       JOBS REPORT")
        print(f"\n      • TOTAL JOBS: {len(jobs)}")
        pending_jobs = 0
        assigned_jobs = 0
        completed_jobs = 0

        for job in jobs:
            status = job['status'].lower()

            if status == "pending":
                pending_jobs += 1
            elif status == "assigned":
                assigned_jobs += 1
            elif status == "completed":
                completed_jobs += 1
        print(f"      • PENDING JOBS: {pending_jobs}")
        print(f"      • ASSIGNED JOBS: {assigned_jobs}")
        print(f"      • COMPLETED JOBS: {completed_jobs}")
        print("\n────────────────────────────────────────────────────────────────")
        print("\n                      ASSIGNMENTS REPORT")
        print(f"\n      • TOTAL ASSIGNMENTS: {len(assignments)}")
        print("\n────────────────────────────────────────────────────────────────")
        print("\n                      FINANCIAL REPORT")
        total_invoice = 0
        paid_invoice = 0
        unpaid_invoice = 0

        for invoice in invoices:
            status = invoice['status'].lower()
            amount = invoice['amount']
            total_invoice += amount
            if status == "paid":
                paid_invoice += amount
            else:
                unpaid_invoice += amount
        print(f"\n      • TOTAL INVOICES: ₹{total_invoice}")
        print(f"      • PAID INVOICES: {paid_invoice}")
        print(f"      • UNPAID INVOICES: {unpaid_invoice}")

        print("\n╚══════════════════════════════════════════════════════════════╝")
        input("\nPress Enter to return to Main Menu...")
        break


def job_performance_report():
    jobs = load_jobs()
    if not jobs:
        print("No jobs found")
        return

    print("\n                       JOBS PERFORMANCE REPORT")
    total_jobs = len(jobs)
    print(f"\n      • TOTAL JOBS: {total_jobs}")
    
    pending_jobs = 0
    assigned_jobs = 0
    completed_jobs = 0
    
    for job in jobs:
        status = job['status'].lower()
    
        if status == "pending":
                    pending_jobs += 1
        elif status == "assigned":
            assigned_jobs += 1
        elif status == "completed":
            completed_jobs += 1
    if total_jobs == 0:
        completion_rate = 0
    else:
        completion_rate = completed_jobs / total_jobs * 100
    print(f"      • PENDING JOBS: {pending_jobs}")
    print(f"      • ASSIGNED JOBS: {assigned_jobs}")
    print(f"      • COMPLETED JOBS: {completed_jobs}")
    print(f"      • COMPLETION RATE: {completion_rate:.2f}%")
    
    print("\n────────────────────────────────────────────────────────────────")
    input("\nPress Enter to return to Reports Menu...")


def employee_performance_report():
    employees = load_employees()
    assignments = load_assignments()
    jobs = load_jobs()
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                 EMPLOYEE PERFORMANCE REPORT                  ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
""")
    
    for employee in employees:
        employee_assignments = 0
        completed_jobs = 0
        active_jobs = 0
        print(f"\n    Employee ID:     {employee['employee_id']}")
        print(f"    Employee Name:   {employee['name']}")
        for assignment in assignments:
            if assignment['employee_id'].lower() == employee['employee_id'].lower():
                employee_assignments += 1
                for job in jobs:
                    if job['job_id'].lower() == assignment['job_id'].lower():
                        if job['status'] == "completed":
                            completed_jobs += 1
                        elif job['status'].lower() == "assigned":
                            active_jobs += 1
        print(f"    Total assignments: {employee_assignments}")
        print(f"    Completed jobs:    {completed_jobs}")
        print(f"    Active jobs:       {active_jobs}")
        print("\n────────────────────────────────────────────────────────────────")
    print("\n╚══════════════════════════════════════════════════════════════╝")
    input("\nPress Enter to return to Reports Menu...")


def financial_report():
    invoices = load_invoices()
    payments = load_payments()

    if not invoices:
        print("No invoices found.")
        return

    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                     FINANCIAL REPORT                         ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
""")

    
    total_invoices = len(invoices)

    paid_count = 0
    unpaid_count = 0
    overdue_count = 0

    total_invoiced = 0
    total_collected = 0

    for invoice in invoices:
        status = invoice['status'].lower()
        amount = invoice['amount']

        total_invoiced += amount

        if status == "paid":
            paid_count += 1
            total_collected += amount

        elif status == "unpaid":
            unpaid_count += 1

        elif status == "overdue":
            overdue_count += 1

    total_outstanding = total_invoiced - total_collected

    if total_invoiced == 0:
        collection_rate = 0
    else:
        collection_rate = (total_collected / total_invoiced) * 100

    print("INVOICE OVERVIEW")
    print(f"\n    Total Invoices:         {total_invoices}")
    print(f"    Paid Invoices:          {paid_count}")
    print(f"    Unpaid Invoices:        {unpaid_count}")
    print(f"    Overdue Invoices:       {overdue_count}")

    print("\nCOLLECTION ANALYSIS")
    print(f"\n    Total Invoiced:         ₹{total_invoiced}")
    print(f"    Total Collected:        ₹{total_collected}")
    print(f"    Total Outstanding:      ₹{total_outstanding}")
    print(f"    Collection Rate:        {collection_rate:.2f}%")

    print("\nPAYMENT OVERVIEW")
    total_payments = len(payments)
    print(f"\n    Payments Recorded:      {total_payments}")

    print("\n────────────────────────────────────────────────────────────────")
    input("\nPress Enter to return to Reports Menu...")