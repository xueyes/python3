password_list = ['******','123456']
def account_login():
    password = input('Password')
    password_corrent = password == password_list[-1]
    password_reset = password == password_list[0]
    if password_corrent:
        print('Login sucess!')
    elif password_reset:
        new_password = input('Enter a new password:')
        password_list.append(new_password)
        print('Your password has changed sucessfully')
    else:
        print('Wrong passwd or invalid input!')
        account_login()
account_login()