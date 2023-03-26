import requests, json
from random import randint

apiurl = 'https://ufo.lyceumland.ru/api/user'


def create_user(user: 'User'):
    res = requests.put(apiurl, data=json.dumps(user.get_data()))
    assert res.status_code == 201


def get_users():
    res = requests.get(apiurl)
    return res.json()['users']


def find_path(user, end_x, end_y):
    params = {'start_x': float(user.coords[0]), 'start_y': float(user.coords[1]), 'end_x': float(end_x), 'end_y': float(end_y)}
    res = requests.get('https://ufo.lyceumland.ru/api/path', params=params)
    print(res)
    return res.json()


class User:
    def __init__(self, name, job_title, coordinates):
        self.name = name
        self.job = job_title
        self.coords = coordinates

    def get_data(self):
        return {'name': self.name, 'job_title': self.job, 
                'coordinates': ' '.join(map(str, self.coords))} 

    def __repr__(self):
        return f'{self.name} {self.coords}'


def parse_users(users):
    ret = []
    for u in users:
        u = User(u['name'], u['job_title'], tuple(map(lambda i: int(float(i)), u['coordinates'].split())))
        if len(u.coords) > 2:
            u.coords = u.coords[:2]
        ret.append(u)
    return ret


#u = User('John', 'Middle', (randint(10, 50), randint(1, 20)))
#u2 = User('Adam', "Senior", (randint(10, 50), randint(1, 20)))
#create_user(u)
#create_user(u2)
while True:
    users = parse_users(get_users())
    #for y in range(-30, 30):
    #    for x in range(-50, 50):
    #        print(('@' if (x, y) in [user.coords for user in users] else '.'), end='')
    #    print()

    print(users)
    path = [tuple(point.values()) for point in find_path(users[0], *users[1].coords)['points']]
    print(path)
    for y in range(-30, 30):
        for x in range(-50, 50):
            if (float(x), float(y)) in path:
                print('+', end='')
            else:
                print(('@' if (x, y) in [user.coords for user in users] else '.'), end='')
        print()
