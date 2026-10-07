import os
from utils.file_manager import (load_employees, load_assignments,load_customers,load_invoices,load_jobs,load_payments)

def system_management_menu():
    while True:
        print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                    SYSTEM MANAGEMENT                         ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║   [1] View System Information                                ║
║   [2] Manage Directories                                     ║
║   [3] View Logs                                              ║
║   [4] System Configuration                                   ║
║   [5] Create Backup                                          ║
║   [6] Restore Backup                                         ║
║                                                              ║
║   [0] Back to Main Menu                                      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
""")
        choice = input("Enter your choice: ")
        if choice == "1":
            system_information()
        elif choice == "2":
            directory_management()

        elif choice == "3":
            view_logs()

        elif choice == "4":
            system_configuration()

        elif choice == "5":
            create_backup()

        elif choice == "6":
            restore_backup()

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")


def system_information():
    employees = load_employees()
    customers = load_customers()
    jobs = load_jobs()
    assignments = load_assignments()
    invoices = load_invoices()
    payments = load_payments()
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                   SYSTEM INFORMATION                         ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
""")
    print("    System name       : OPSCORE")
    if os.path.exists("data"):
        print("  \n    Data Directory    : Available")
    else:
        print("    Data Directory    : Missing")

    if os.path.exists("logs"):
        print("    Logs Directory    : Available")
    else:
        print("    Logs Directory    : Missing")

    if os.path.exists("backups"):
        print("    Backup Directory  : Available")
    else:
        print("    Backup Directory  : Missing")

    print(f"\n    EMPLOYEES         : {len(employees)} ")
    print(f"    CUSTOMERS         : {len(customers)}")
    print(f"    JOBS              : {len(jobs)}")
    print(f"    ASSIGNMENTS       : {len(assignments)}")
    print(f"    INVOICES          : {len(invoices)}")
    print(f"    PAYMENTS          : {len(payments)}")

    print("""
╚══════════════════════════════════════════════════════════════╝
""")

    input("Press Enter to return to System Management...")