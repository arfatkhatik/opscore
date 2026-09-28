class Job:
    def __init__(self, job_id, customer_id, job_title, description, priority, schedule_date, status="pending"):
        self.job_id = job_id
        self.customer_id = customer_id
        self.job_title = job_title
        self.description = description
        self.priority = priority
        self.status = status
        self.schedule_date = schedule_date

    def display_info(self):
        print(f"Job ID          :              {self.job_id}")
        print(f"Customer ID     :              {self.customer_id}")
        print(f"Job Title       :              {self.job_title}")
        print(f"Description     :              {self.description}")
        print(f"Priority        :              {self.priority}")
        print(f"Status          :              {self.status}")
        print(f"Schedule Date   :              {self.schedule_date}")