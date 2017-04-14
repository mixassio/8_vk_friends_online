import vk
import getpass

APP_ID = '5969195'  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    login = input('Please, enter login:')
    return login


def get_user_password():
    password = getpass.getpass()
    return password


def get_online_friends(login, password):
    my_dict = {}
    list_user_online = []
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    list_users = api.friends.getOnline(online_mobile=1)
    users_online = list(api.users.get(user_ids=list_users['online']))
    users_online_mobile = api.users.get(user_ids=list_users['online_mobile'])
    return users_online, users_online_mobile


def output_friends_to_console(friends_online, friends_online_mobile):
    print('----------------------------------------')
    print('List of my friends into computer-online:')
    print('----------------------------------------')
    for count_user, user in enumerate(friends_online):
        print('{}. {} {}'.format(count_user+1, user['first_name'], user['last_name']))
    print('----------------------------------------')
    print('List of my friends into mobile-online:')
    print('----------------------------------------')
    for count_user, user in enumerate(friends_online_mobile):
        print('{}. {} {}'.format(count_user+1, user['first_name'], user['last_name']))

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online, friends_online_mobile = get_online_friends(login, password)
    output_friends_to_console(friends_online, friends_online_mobile)
