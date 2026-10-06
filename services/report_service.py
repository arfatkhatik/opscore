from utils.file_manager import (load_employees,save_employee,load_jobs,save_jobs,load_assignments,save_assignments,load_customers,save_customer,load_invoices,save_invoices,load_payments,save_payments)

def operations_summary():
    employees = load_employees()
    customers = load_customers()
    jobs = load_jobs()
    assignments = load_assignments()
    invoices = load_invoices()
    payments = load_payments()
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