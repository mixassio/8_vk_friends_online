import vk, getpass

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
    for user in api.friends.get(fields=('last_name')):
        if user['online']:
            my_dict['first_name'] = user['first_name']
            my_dict['last_name'] = user['last_name']
            list_user_online.append(my_dict.copy())
    return list_user_online


def output_friends_to_console(friends_online):
    print('List of my friends into online:')
    print('-------------------------------')
    i = 1
    for user in friends_online:
        print('{}. {} {}'.format(i, user['first_name'], user['last_name']))
        i += 1

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
