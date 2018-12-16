password_list = ['###','12345']
def account_login():
    tries = 3
    while tries > 0:
        password = input('Password  :')
        password_corrent = password == password_list[-1]
        password_reset = password == password_list[0]
        if password_corrent:
            print('Login sucess !')
        elif password_reset:
            new_password = input('Enter a new_password  :')
            password_list.append(new_password)
            print('Your new_password has changed sucessfully!')
            account_login()
        else:
            print('Wrong password  or invalid input')
            tries = tries - 1
            print(tries,'times left ')
    else:
        print('Your account  has been subspended !')
account_login()

