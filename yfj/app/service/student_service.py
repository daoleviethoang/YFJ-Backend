from .user_service import UserService
from ..models import UserCategoryEnum
import numpy as np
from numpy.linalg import norm

class StudentService:
    user_service = UserService()

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
        users = self.user_service.get_all_by_role(UserCategoryEnum.Volunteer)
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

    def add(self, data):
        user = self.user_service.add(data)
        user.create()
        user = self.get_advices(user)
        return user.to_json()
    
    def update(self, data, username):
        user = self.user_service.update(data, username)
        user.update()
        user = self.get_advices(user)
        return user.to_json()