#coding:utf8
import sys
# print("谢富燕是大坏蛋")
# name = 'My nameis Mik'
# print(name[0])
# print(name[-4])
# print(name[11:14])
#
# word = 'friends'
#
# find_the_evil_in_your_friends = \
# print(word[0]+word[2:4]+word[-3:-1])
# print(find_the_evil_in_your_friends)
#
# s= car.door.open()
# search = '168'
# num_a = '1386-168-0006'
# num_b = '1681-222-0006'
# print(search + ' is at '+ str(num_a.find(search)) + ' to '  + str(num_a.find(search) + len(search)) + ' of num_a')
# print(search + ' is at '+ str(num_b.find(search)) + ' to  ' + str(num_b.find(search) + len(search)) + ' of num_b')
#
# city = input("write down the name of city")
# url = "http://api.map.baidu.com/telematics/v3/weather?citypiny={}.format(city)"


#咒语:define a funcction named 'function' which has two arguments:arg1 and arg2，returns the result - 'something'

# def  function (arg1,arg2):
#     return  somthing

# def trapeaoid_area(base_up,base_down,height=3):
#     return 1/2 * (base_up + base_down) * height
# a = trapeaoid_area(1,2,height=15)
# print(a)

# file = open('C://Users/hashlinux/Desktop/text.txt','w')
# file.write('hello world')
# def text_create(name,msg):
#     desktop_path = 'C://Users/hashlinux/Desktop/'
#     full_path = desktop_path + name + '.txt'
#     file = open(full_path,'w')
#     file.write(msg)
#     file.close()
#     print('Done')
# text_create('hello','hello world') #调用函数




import sys
sys.setrecursionlimit(1000000) #调用次数

password_list = ['*#*#','12345']
def account_login():
    password = input('Password')
    password_corrent = password == password_list[-1]
    password_reset = password == password_list[0]
    if password_corrent:
        print('Login sucess !')
    elif password_reset:
        new_password = input('Enter a new password:')
        password_list.append(new_password)
        print('Your password has changed sucessfulLy')
        account_login()
    else:
        print('Wrong password  or invalid  input')
        account_login()
account_login()

