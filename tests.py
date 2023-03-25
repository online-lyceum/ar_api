import requests, json

users = [
        {"name": "John A.", "coordinates": "0.11112", "job_title": "Middle backend"},
        {"name": "John B.", "coordinates": "0.5332", "job_title": "Middle frontend"},
        {"name": 'John Bron',
         "job_title": 'Team Leader'},
        {"name": 'Abragham Joasdf',
         "job_title": 'Junior'},
        {"name": 'John Hawling',
         "job_title": 'Junior Developer'}
]
for u in users:
    u['coordinates'] = '1.0 1.0'
print(users)
user_after = {"name": "John A.", "coordinates": "0.33312", "job_title": "Middle backend"}
#api_url = "https://ufo.lyceumland.ru/api/user"
api_url = "http://127.0.0.1:8080/api/user"
user_filter = {"name_filter": 'John', "job_title_filter": ''}


def create_user(user_data):
    res = requests.put(api_url, data=json.dumps(user_data))
    assert res.status_code == 201


def get_users(user_filter_data):
    res = requests.get(api_url, params=user_filter_data)
    return json.loads(res.text)


for user in users:
    create_user(user)
print(*[u['name'] for u in get_users(user_filter)['users']], sep='\t')
print(*get_users({})['users'])
#for _ in range(5):
#    users = get_users(user_filter)['users']
#    print(users)
#    user = users[0]
#    user['coordinates'] = str(float(user['coordinates']) + 2.02)
#    create_user(user)
#    print(get_users(user_filter))
