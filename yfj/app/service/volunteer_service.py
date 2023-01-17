from cryptography.fernet import Fernet
from .job_service import JobService
from .user_service import UserService

class VolunteerService:
    job_service = JobService()
    user_service = UserService()

    def add(self, data):
        user = self.user_service.add(data)
        jobs = self.job_service.check_jobs_exists(data.get("jobs"))
        user.jobs = jobs
        user.create()
        return user.to_json()

    def update(self, data, username):
        user = self.user_service.update(data, username)
        jobs = self.job_service.check_jobs_exists(data.get("jobs"))
        user.jobs = jobs
        user.update()
        return user.to_json()
