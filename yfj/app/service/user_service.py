import base64
from ..models import User
from cryptography.fernet import Fernet

class UserService:
    key = b'pT8ZDjwCvnWkfPEYBm12q2p9srNkM-nWC6Ss9aAcMEw='
    fernet = Fernet(key)

    def get_all_by_role(self, role):
        users = User.query.all()
        users = [user for user in users if user.role==role]
        return users

    def check_username_exists(self, username):
        users = User.query.all()
        for user in users:
            username_decrypt = self.fernet.decrypt(user.username).decode()
            if username == username_decrypt:
                return user

    def get_by_username(self, username):
        user = self.check_username_exists(username)
        if user: return user.to_json()
        raise Exception('User not found')  

    def add(self, data):
        user = User(
            data.get('username'), 
            data.get('role'), 
            data.get('math'), 
            data.get('physics'),
            data.get('chemistry'),
            data.get('biology'),
            data.get('literature'),
            data.get('history'),
            data.get('geography'),
            data.get('phylosophy'),
            data.get('art'),
            data.get('foreign_language')
        )

        if self.check_username_exists(user.username):
            raise Exception('User exists')
        user.username = self.fernet.encrypt(bytes(user.username, 'utf-8')).decode()
        return user
    
    def update(self, data, username):
        user = self.check_username_exists(username)
        if not user:
            raise Exception('User does not exists')
        else:
            user.role = data.get('role')
            user.math = data.get('math'), 
            user.physics = data.get('physics'),
            user.chemistry = data.get('chemistry'),
            user.biology = data.get('biology'),
            user.literature = data.get('literature'),
            user.history = data.get('history'),
            user.geography = data.get('geography'),
            user.phylosophy = data.get('phylosophy'),
            user.art = data.get('art'),
            user.foreign_language = data.get('foreign_language')
            return user

    def delete(self, username):
        user = self.check_username_exists(username)
        if not user:
            raise Exception('User does not exists')
        else:
            user.delete()
            return "Delete user success."