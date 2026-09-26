def register_user(path='users.txt'):
    username = input('Create username: ')
    password = input('Create password: ')
    with open(path, 'a', encoding='utf-8') as f:
        f.write(f"{username},{password}\n")
    print('Registered')

def login_user(path='users.txt'):
    username = input('Username: ')
    password = input('Password: ')
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                u, p = line.strip().split(',')
                if u == username and p == password:
                    print('Login successful')
                    return
        print('Invalid credentials')
    except FileNotFoundError:
        print('No users registered')

if __name__ == '__main__':
    choice = input('1:Register 2:Login > ')
    if choice == '1':
        register_user()
    else:
        login_user()
