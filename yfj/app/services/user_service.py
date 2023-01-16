import base64
from ..models import User
from cryptography.fernet import Fernet

class UserService:
    key = b'pT8ZDjwCvnWkfPEYBm12q2p9srNkM-nWC6Ss9aAcMEw='
    fernet = Fernet(key)

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
        user.create()
        return user.to_json()