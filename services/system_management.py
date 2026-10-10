import os
import shutil
from datetime import datetime
from utils.file_manager import (load_employees, load_assignments,load_customers,load_invoices,load_jobs,load_payments)
import json

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


def directory_management():
    while True:
        print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║                    MANAGE DIRECTORIES                        ║
    ║                                                              ║
    ╠══════════════════════════════════════════════════════════════╣
    ║                                                              ║
    ║   [1] View Directory Contents                                ║
    ║   [2] Check Directory Status                                 ║
    ║   [3] Create Directory                                       ║
    ║   [4] Remove Directory                                       ║
    ║                                                              ║
    ║   [0] Back to System Management                              ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
        choice = input("Enter your choice: ")
        if choice == "1":
            view_directory()
        elif choice == "2":
            view_status()
        elif choice == "3":
            create_directory()
        elif choice == "4":
            remove_directory()
        elif choice == "0":
             break
        
        else:
            print("Invalid choice. Please try again.")

def view_directory():
    while True:    
        print("""
    Select Directory

    [1] data
    [2] logs
    [3] backups
    [0] Back

    """)
        choice = input("Enter your choice: ")
        if choice == "1":
            files = os.listdir("data")
            for file in files:
                print(file)
        elif choice == "2":
            files = os.listdir("logs")
            for file in files:
                print(file)
        elif choice == "3":
            files = os.listdir("backups")
            for file in files:
                print(file)
        elif choice == "0":
            break
        else:
            print("Invalid option. please try again")

def view_status():
    while True:
        print("""
Select Directory

    [1] data
    [2] logs
    [3] backups
    [0] Back

""")

        choice = input("Enter your choice: ")

        if choice == "1":
            directory = "data"

        elif choice == "2":
            directory = "logs"

        elif choice == "3":
            directory = "backups"

        elif choice == "0":
            break

        else:
            print("Invalid option. Please try again.")
            continue

        print("\nDIRECTORY STATUS:")
        print(f"\nDirectory name: {directory}")

        if os.path.exists(directory):
            print("Exists        : Yes")

            if os.path.isdir(directory):
                print("Type          : Directory")
                print(f"Items         : {len(os.listdir(directory))}")
            else:
                print("Type          : Not a Directory")
                print("Items         : 0")

        else:
            print("Exists        : No")
            print("Type          : Not Found")
            print("Items         : 0")

        input("\nPress Enter to continue...")


def create_directory():
    ask_name = input("Enter name to create directory: ")

    exists = os.path.exists(ask_name)

    if exists:
        print("directoty already exist.")
        input("\nPress Enter to continue...")

    elif not exists:
        os.makedirs(ask_name)
        log_event(f"Directory {ask_name} created")
        print(f"directory {ask_name} created successfully.")
        input("\nPress Enter to continue...")


def remove_directory():
    ask_name = input("Enter directory name to remove: ")

    protected_directories = ["data", "logs", "backup"]
    if ask_name.lower() in protected_directories:
        print("This is a protected OPSCORE directory and cannot be removed.")
        input("\nPress Enter to continue...")
        return
    exists = os.path.exists(ask_name)

    if exists:
        confirmation = input("do you really want to remove directory? (yes/no): ")
        if confirmation == "yes":
            os.rmdir(ask_name)
            log_event(f"Directory {ask_name} removed")
            print(f"Directory {ask_name} deleted succesfully.")
            input("\nPress Enter to continue...")
        elif confirmation == "no":
            print("removal canceled.")
            input("\nPress Enter to continue...")
        else:
            print("Invalid option selected. please try again.")

    else:
        print("Directory does not exists.")
        input("\nPress Enter to continue...")


def view_logs():
    while True:
        print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║                         VIEW LOGS                            ║
    ║                                                              ║
    ╠══════════════════════════════════════════════════════════════╣
    ║                                                              ║
    ║   [1] View All Logs                                          ║
    ║   [2] View Latest Log Entries                                ║
    ║   [0] Back to System Management                              ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
        choice = input("Enter your choice: ")
        if choice == "1":
            view_all_logs()
        elif choice == "2":
            latest_log()
        elif choice == "0":
            break
        else:
            print("Invalid option selected. please try again.")


def view_all_logs():
    exists = os.path.exists("logs/opscore.log")

    if exists:
        with open("logs/opscore.log", "r") as file:
            logs = file.read()
            print("\n========== OPSCORE LOGS ==========\n")
            print(logs)

        input("\nPress Enter to continue...")

    else:
        print("log file does not exists.")
        print("No logs available.")
        input("\nPress Enter to continue...")


def latest_log():
    exists = os.path.exists("logs/opscore.log")

    if exists:
        with open("logs/opscore.log", "r") as file:
            logs = file.readlines()
            logs = logs[-10:]
            print("========== LATEST LOG ENTRIES ==========")
            for log in logs:
                print(log, end="")
        input("\nPress Enter to continue...")

    else:
        print("log file does not exists.")
        print("No logs available.")
        input("\nPress Enter to continue...")


def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%M")

    with open("logs/opscore.log", "a") as file:
        file.write(f"{timestamp} - {message}\n")

def system_configuration():
    while True:
        print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                    SYSTEM CONFIGURATION                      ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║   [1] View Current Configuration                             ║
║   [2] Update Configuration                                   ║
║                                                              ║
║   [0] Back to System Management                              ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
""")

        choice = input("Enter option number: ")

        if choice == "1":
            view_configuration()
        elif choice == "2":
            update_configuration()
        elif choice == "0":
            break
        else:
            print("Invalid option.")

def view_configuration():
    with open("data/system_config.json", "r") as file:
        config = json.load(file)

        for key, value in config.items():
            print(f"{key}: {value}")

def update_configuration():
    with open("data/system_config.json", "r") as file:
        config = json.load(file)

        print("\n========== UPDATE CONFIGURATION ==========\n")

        for key, value in config.items():
            print(f"{key}: {value}")

        setting = input("Enter the setting name to update: ")

        if setting not in config:
            print("Invalid setting Name.")
            input("Press Enter to continue...")
            return

        new_value = input("Enter new value: ").strip()

        if setting == "low_stock_threshold":
            try:
                new_value = int(new_value)
                if new_value < 0:
                    print("Threshold cannot be negative.")
                    input("\nPress Enter to continue...")
                    return
            except ValueError:
                print("Threshold must be a whole number.")
                input("\nPress Enter to continue...")
                return
        config[setting] = new_value

        with open("data/system_config.json", "w") as file:
            json.dump(config, file, indent=4)

        print("Configuration updated successfully.")
        log_event(f"Configuration setting '{setting}' updated")

        input("\nPress Enter to continue...")

def create_backup():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_name = f"backup_{timestamp}"
    backup_path = f"backups/{backup_name}"
    try:
        shutil.copytree("data", backup_path)
        print(f"backup created {backup_path}")
        log_event(f"backup created at {backup_path}")
    except OSError as e:
        print(f"Backup failed {e}")





    
