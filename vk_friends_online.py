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
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    users_online = api.friends.getOnline()
    return api.users.get(user_ids=users_online)


def output_friends_to_console(friends_online):
    print('List of my friends online:')
    print('--------------------------')
    for count_user, user in enumerate(friends_online):
        print('{}. {} {}'.format(count_user+1, user['first_name'], user['last_name']))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
