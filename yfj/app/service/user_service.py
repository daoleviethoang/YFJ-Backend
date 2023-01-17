from ..models import User
from cryptography.fernet import Fernet
import numpy as np
from numpy.linalg import norm
from ..models import UserCategoryEnum

class UserService:
    key = b'pT8ZDjwCvnWkfPEYBm12q2p9srNkM-nWC6Ss9aAcMEw='
    fernet = Fernet(key)

    def convert_to_score_array(self, user):
        arr = []
        arr.append(user.math)
        arr.append(user.physics)
        arr.append(user.chemistry)
        arr.append(user.biology)
        arr.append(user.literature)
        arr.append(user.history)
        arr.append(user.geography)
        arr.append(user.phylosophy)
        arr.append(user.art)
        arr.append(user.foreign_language)
        return arr

    def convert_arr_uses_to_matrix(self, users):
        matrix = []
        for u in users:
            row = []
            row.append(u.math)
            row.append(u.physics)
            row.append(u.chemistry)
            row.append(u.biology)
            row.append(u.literature)
            row.append(u.history)
            row.append(u.geography)
            row.append(u.phylosophy)
            row.append(u.art)
            row.append(u.foreign_language)
            matrix.append(row)
        return matrix

    def calculate_similarity(self, user):
        user_score_arr_np = np.array(self.convert_to_score_array(user))
        users = self.get_all_by_role(UserCategoryEnum.Volunteer)
        users_score_matrix = self.convert_arr_uses_to_matrix(users)
        users_score_matrix.append(user_score_arr_np)

        user_matrix_np = np.array(users_score_matrix)
        
        #Normalize the data matrix: 
        #Score course of each user - average score of 1 course (total course score of the users / number of users)
        avg_col_user_maxtrix_np = np.array(user_matrix_np.mean(axis=0))
        normalize_matrix = user_matrix_np - avg_col_user_maxtrix_np

        #Get the user need to calculate the similarity
        user_score_roots = normalize_matrix[len(normalize_matrix) - 1]

        #Remove user need to calculate from normalize_matrix
        normalize_matrix = np.delete(normalize_matrix, len(normalize_matrix) - 1, 0)

        #Use the cosine similarity function to calculate the similarity between users
        cosine_similarities = np.dot(normalize_matrix,user_score_roots)/(norm(normalize_matrix, axis=1)*norm(user_score_roots))

        #Get users with similarity greater than 0
        users_highest_similarity = []
        for index, cs in enumerate(cosine_similarities):
            if cs > 0:
                users_highest_similarity.append(users[index])

        return users_highest_similarity

    def get_advices(self, user):
        users_highest_similarity = self.calculate_similarity(user)
        jobs_suggest = []
        for uhs in users_highest_similarity:
            for job in uhs.jobs:
                jobs_suggest.append(job)
                if(len(jobs_suggest) == 3):
                    break

        user.jobs = jobs_suggest
        return user

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
        if user: 
            user = self.get_advices(user)
            return user.to_json()
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