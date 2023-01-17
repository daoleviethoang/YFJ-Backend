from .user_service import UserService

class StudentService:
    user_service = UserService()

    def add(self, data):
        user = self.user_service.add(data)
        user.create()
        user = self.user_service.get_advices(user)
        return user.to_json()
    
    def update(self, data, username):
        user = self.user_service.update(data, username)
        user.update()
        user = self.user_service.get_advices(user)
        return user.to_json()