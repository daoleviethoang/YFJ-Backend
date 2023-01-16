from ..models import Job
import requests

class JobService:
    def get_all(self):
        return Job.query.all()

    def check_jobs_exists(self, data):
        jobs = Job.query.all()
        jobs_data = []
        for job in jobs:
            if job.name in data:
                jobs_data.append(job)
        if len(jobs_data) != len(data):
            raise Exception("Job does not exists.")
        else: 
            return jobs_data

    def create(self) -> bool:
        jobs = Job.query.all()
        jobs_name = [job.name for job in jobs]
        response = requests.get(f"{'http://localhost:8000/job_earnings'}")
        if response.status_code == 200:
            for item in response.json():
                if item[0] not in jobs_name:
                    job = Job(item[0], item[1])
                    job.create()
            return True
        else:
            return False

