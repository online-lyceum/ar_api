import requests, json

user = {"name": "John A.", "coordinates": "0.11112 5.333", "job_title": "Middle backend"}
user2 = {"name": "John A.", "coordinates": "0.5332 7.833", "job_title": "Middle frontend"}
user_after = {"name": "John A.", "coordinates": "0.33312 5.333", "job_title": "Middle backend"}
api_url = "http://127.0.0.1:8080/api/user"
user_filter = {"name_filter": '', "job_title_filter": ''}


def create_user(user_data):
    res = requests.put(api_url, data=json.dumps(user_data))
    return res


def get_users(user_filter_data):
    res = requests.get(api_url, data=json.dumps(user_filter_data))
    return res.text


print(create_user(user))
print(create_user(user2))
print(get_users(user_filter))
print(create_user(user_after))
print(get_users(user_filter))
