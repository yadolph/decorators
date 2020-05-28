from mydecorator import logger_decorator
import requests


TOKEN = '72ef1d6372ef1d6372ef1d630f729fe3e9772ef72ef1d632c7d5e58ea3c5c25b48aafe9'

class User:

    def __init__(self,screen_name):
        if isinstance(screen_name, int):
            self.user_id = screen_name
        else:
            try:
                params = {
                    'user_ids': screen_name,
                    'access_token': TOKEN,
                    'v': '5.89',
                    'lang': 'ru',
                    'fields': 'id'
                }
                response = requests.get('https://api.vk.com/method/users.get', params=params)
                self.user_id = response.json()['response'][0]['id']
            except KeyError:
                exit('Проверьте правильность написания индентификаторов')

    def __str__(self):
        return f'https://vk.com/id{self.user_id}'

    def friend_list(self):
        params = {
            'user_id': self.user_id,
            'access_token': TOKEN,
            'v': '5.89',
            'lang': 'ru'
        }
        response = requests.get('https://api.vk.com/method/friends.get', params=params)
        return response.json()['response']['items']

    def __and__(self, another):

        fl1 = self.friend_list()
        fl2 = another.friend_list()

        common_friends = set(fl1).intersection(set(fl2))
        common_friends = list(common_friends)
        common_friends_cl = []

        for friend in common_friends:
            common_friends_cl.append(User(friend))

        return common_friends_cl


@logger_decorator('log.txt')
def print_friend_list(flist):
    if flist:
        print('Общие друзья указанных пользователей: ')
        for friend in flist:
            print(friend)
    else:
        print('Похоже, у этих пользователей нет общих друзей')


wanted_ids = input('Введите идентификаторы пользователей, разделенные пробелом: ')
wanted_ids = wanted_ids.split(' ')

id1 = User(wanted_ids[0])
id2 = User(wanted_ids[1])

common_friend_list = id1 & id2

print_friend_list(common_friend_list)