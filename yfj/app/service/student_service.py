import base64
from ..models import User
from cryptography.fernet import Fernet
from .user_service import UserService

class StudentService:
    user_service = UserService()

    def add(self, data):
        user = self.user_service.add(data)
        user.create()
        return user.to_json()
    
    def update(self, data, username):
        user = self.user_service.update(data, username)
        user.update()
        return user.to_json()