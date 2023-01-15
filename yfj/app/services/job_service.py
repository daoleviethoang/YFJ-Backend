from ..models import Job
import requests
import json


class JobService:
    def create(self) -> str:
        jobs = Job.query.all()
        jobs_name = [job.name for job in jobs]
        response = requests.get(f"{'http://localhost:8000/job_earnings'}")
        if response.status_code == 200:
            for item in response.json():
                if item[0] not in jobs_name:
                    job = Job(item[0], item[1])
                    job.create()
            return "Sucessfully fetched and insert the data.\n"
        else:
            return "Failed to fetch data.\n"

