from models.jobs import Job
from utils.file_manager import save_jobs, load_jobs

def job_menu():

    while True:
        print("\n")
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                                                              ║")
        print("║                       JOB MANAGEMENT                         ║")
        print("║                                                              ║")
        print("╠══════════════════════════════════════════════════════════════╣")
        print("║                                                              ║")
        print("║      [1]   Add Job                                           ║")
        print("║      [2]   View Jobs                                         ║")
        print("║      [3]   Search Job                                        ║")
        print("║      [4]   Update Job                                        ║")
        print("║      [5]   Remove Job                                        ║")
        print("║                                                              ║")
        print("║      [0]   Back to Main Menu                                 ║")
        print("║                                                              ║")
        print("╚══════════════════════════════════════════════════════════════╝")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_job()
            input("press Enter to go back menu: ")
        elif choice == "2":
            print("View Jobs selected.")

        elif choice == "3":
            print("Search Job selected.")

        elif choice == "4":
            print("Update Job selected.")

        elif choice == "5":
            print("Remove Job selected.")

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")


def add_job():
    job_id = input("Enter job ID: ")
    customer_id = input("Enter customer ID: ")
    job_title = input("Enter Job Title: ")
    description = input("Enter Description: ")
    priority = input("Enter priority: ")
    schedule_date = input("Enter schedule date: ")

    job = Job(job_id, customer_id, job_title, description, priority, schedule_date)

    job_data = {
        "job_id": job.job_id,
        "customer_id": job.customer_id,
        "job_title": job.job_title,
        "description": job.description,
        "priority": job.priority,
        "schedule_date": job.schedule_date,
        "status": job.status
    }

    jobs = load_jobs()
    jobs.append(job_data)
    save_jobs(jobs)
    print("Job added successfully")