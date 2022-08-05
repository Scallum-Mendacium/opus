import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("src/serviceAccountKey.json")
app = firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "https://opus-db287-default-rtdb.asia-southeast1.firebasedatabase.app/"
    },
)

teams = db.reference("Teams")
users = db.reference("Users")


# FORMAT TO ADD TASKS
# teams.set(
#     {
#         "team_name": {
#             "tasks": {
#                 "task_name": {
#                     "description": "Cool description",
#                     "assignees": ["praneeth"],
#                     "creator": "utkarsh",
#                     "created_on": "Some date_time object",
#                     "due_date": "Some date_time object",
#                     "notes": ["note1", "note2"],
#                 }
#             }
#         }
#     }
# )

# users.set(
#     {
#         "username": {
#             "tasks": {
#                 "task_name": {
#                     "description": "Cool description",
#                     "created_on": "Some date_time object",
#                     "due_date": "Some date_time object",
#                     "notes": ["note1", "note2"],
#                 }
#             }
#         }
#     }
# )
