# Welcome

Nice to meet you! We use this test at CubiCasa to evaluate all Python developer applicants before interviews. We hope you'll have fun with this assignment.

## Introduction

**Your Future Job** (YFJ) is a nonprofit service that helps high school students to choose a profession to follow.
The users of the system may be of 2 categories:
- Students: come to the system to get advice on the best matched jobs that they can follow after school
- Volunteers who come to help students by providing their data

**Stats service** is public service which investigates the labour market and can provide data regarding jobs and earnings. YFJ uses the data from stats for its computation but it doesn't own these data. The endpoint YFJ will consume from stats is _/job_earnings_ which provides a list of jobs together with average earning for each jobs

## Assignment

Your mission is to help YFJ build a RESTful Web Service that can be consumed by various frontend clients: web, mobile apps.

For that you should implement the endpoints for students and volunteers in YFJ site

1. Student can input his school performance as average scores for school subjects: Math, Physics, Chemistry, Biology, Literature, History, Geography, Phylosophy, Art and Foreign Language and get back 3 most apropriate jobs in recommendation. When student input data, the system stores his/her data for the future computation. Students can also update or delete their data at any time if they have concern regarding privacy.
The URL for student is `/{PeopleID}/advices`

2. Volunteers are people who have already landed on good jobs. They come back and use the URL `/{PeopleID}/jobs` to tell about their current job(s), so that the system can use those data to make a better recommendation to students.
Volunteer can come to system many times if he/she has changed job in various periods of life. But the prerequisite is that volunteer should input his/her school performance at least once before input data about job
The format of data to be input is like {jobs: [job1, job2, ...]}, e.g: a list of job name, nothing else.

3. Student and volunteer can come back to site at any moment and update or delete his/her data at will

**Note:**
- To maintain user's privacy, the PeopleID should not be stored as unencrypted text in the database 
- The most appropriate jobs are recommended based on student performance as well as the data about job earning from stats service.
- There is no unique solution in computing the recommended jobs, feel free to suggest one.
- You should not care about authentication or authorization, YFJ is open to wide public

## How to complete and what is expected

### Software needed to install
- https://docs.docker.com/ docker and docker-compose for working with container
- PostgresSQL client tools (such as https://www.pgadmin.org/) for manipulating database, our db service use PostgresSQL.

### How to run
Follow the steps below:
    1. Run all services with docker: docker-compose up -d
    2. cd yfj -> flask db migrate -> flask db upgrade 
    3. [If YFJ fail with docker] Run FYJ service: export FLASK_APP=app && flask run --port 9000
        - If error run: pip install requests or pip3 install requests before run export FLASK_APP=app && flask run --port 9000
    4. Click to this link when run success: http://127.0.0.1:9000/
       (This API helps to load all the master data needed in the project)

To see output of Stats Service, browse to: `localhost:8000/job_earnings`

To see YFJ site, browse to:  `localhost:9000`

### APIs
You can import the postman_collection file into postman so you can test all the APIs. 
Attachments in folder yfj
1. Get and create master data (job data):
This API get all job from stats service and save it to yfi database
- GET localhost:9000/
2. Get most appropriate jobs in recommendation with username:
- GET localhost:9000/<username>/advices
3. Create user information:
- Student: POST localhost:9000/advices

Body: 
```
{
    "username": "",
    "role": "Student",
    "math": 0,
    "physics": 0,
    "chemistry": 0,
    "biology": 0,
    "literature": 0,
    "history": 0,
    "geography": 0,
    "phylosophy": 0,
    "art": 0,
    "foreign_language": 0
}
```
- Volunteer: POST localhost:9000/jobs

Body: jobs name get from API: GET localhost:9000/
```
{
    "username": "",
    "role": "Volunteer",
    "math": 0,
    "physics": 0,
    "chemistry": 0,
    "biology": 0,
    "literature": 0,
    "history": 0,
    "geography": 0,
    "phylosophy": 0,
    "art": 0,
    "foreign_language": 0,
    "jobs": [
        "Software engineer",
        "Games developer",
        "Lecturer, higher education"
    ]
}
```
4. update user information:

- Student: PATCH localhost:9000/{username}/advices

Body: 
```
{
    "role": "Student",
    "math": 0,
    "physics": 0,
    "chemistry": 0,
    "biology": 0,
    "literature": 0,
    "history": 0,
    "geography": 0,
    "phylosophy": 0,
    "art": 0,
    "foreign_language": 0
}
```
- Volunteer: PATCH localhost:9000/{username}/jobs

Body: jobs name get from API: GET localhost:9000/
```
{
    "username": "",
    "role": "Volunteer",
    "math": 0,
    "physics": 0,
    "chemistry": 0,
    "biology": 0,
    "literature": 0,
    "history": 0,
    "geography": 0,
    "phylosophy": 0,
    "art": 0,
    "foreign_language": 0,
    "jobs": [
        "Software engineer",
        "Games developer",
        "Lecturer, higher education"
    ]
}
```
5. Delete user:
- DELETE localhost:9000/{username}/user
6. Get 
jobs with username:
- GET localhost:9000/{username}/user
###Solution in computing the recommended jobs


