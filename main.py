# # https://pynative.com/python-basic-exercise-for-beginners/

# # x, y, next_checkpoint_x, next_checkpoint_y = [int(i) for i in input() ]
# #
# #
# # print(x)


# # x = int(input())
# # print(x+x)

# # def remove_chars(word, n):
# #     print('Original string:', word)
# #     x = word[n:]
# #     return x
# #
# # print("Removing characters from a string")
# # n = int(input('how much character you want to remove from the string: '))
# # strin = input('Enter String: ')
# #
# # print(remove_chars(strin, n))
# # print(remove_chars(strin, n))


# # Exercise 6: Display numbers divisible by 5 from a list
# # Iterate the given list of numbers and print only those numbers which are divisible by 5
# #
# # Expected Output:
# #
# # Given list is  [10, 20, 33, 46, 55]
# # Divisible by 5
# # 10
# # 20
# # 55


# # q = input().split()
# # list = [int(i) for i in q]
# # for i in list:
# #     if i%5 == 0:
# #         print(list)

# # for num in range(10):
# #     for i in range(num):
# #         print (num, " ") #print number
# #     # new line after each row to display pattern correctly
# #
# #     print("\n")


# # concept of "end" parameter of print() function or method
# # num = 1
# # for i in range(2):
# #     print(num, end = " ")


# '''

# Exercise 9: Check Palindrome Number
# Write a program to check if the given number is a palindrome number.

# A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers

# Expected Output:

# original number 121
# Yes. given number is palindrome number

# original number 125
# No. given number is not palindrome number

# '''

# # num = input("Enter Any Number: ")
# # reverse_num = num[::-1]
# # if num == reverse_num:
# #     print('Palindrome number')
# #     print("number is: ",int(num))
# # else:
# #     print('Not a Palindrome number.')


# '''
# Concatinating two lists

# '''
# # list1 = [1,2,3]
# # list2 = [4,5,6]
# # list_merge = list1 + list2
# # print(list_merge)

# # number = 1
# # print("Given number", number)
# # while number > 0:                                #  number 1234 123 12 1
# #     # get the last digit
# #     digit = number % 10                        #  % digit  4 3 2 0
# #     # remove the last digit and repeat the loop
# #     number = number // 10                       #  // number  123 12 1 0
# #     print(digit, end=" ")                      #   print  digit  4 3 2 0


# '''#selection of Food'''

# # from random import Random
# # from time import sleep
# # import os
# # while True:
# #
# #     a = Random()
# #     food = [i for i in input("Enter Food Choices with Space and Press Enter when You finish: ").split()]
# #     select = a.randint(0, len(food)-1)
# #     print(food[select])
# #     sleep(1)
# #     os.system('clear')

# ''''''''''''''''''''''''''


# # # Python program to demonstrate
# # # passing dictionary as argument
# #
# #
# # # A function that tak//es dictionary
# # # as an argument
# # def func(d):
# #     for key in d:
# #         print("key:", key, "Value:", d[key])
# #
# #
# # # Driver's code
# # D = {'a': 1, 'b': 2, 'c': 3}
# # func(D)


# #
# # def print_key1():
# #     return "This is Gfg's value"
# #
# #
# # # initializing dictionary
# # # check for function name as key
# # test_dict = {"Gfg": print_key1, "is": 5, "best": 9}
# #
# # # printing original dictionary
# # print("The original dictionary is : " + str(test_dict))
# #
# # # calling function using brackets
# # res = test_dict['is']
# #
# # # printing result
# # print("The required call result : " + str(res))
# #


# # def bic():
# #     dic =5
# #     dic2 = 6
# #     return dic
# #
# #
# # def home():
# #
# # home()

# # def accept_num():
# #     num = [int(i) for i in input('Enter two numbers: ').split()]
# #
# #     print(sum(num))
# # accept_num()

# # numbers = []

# # 5 is the list size
# # run loop 5 times


# #
# # a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# # for i in range(len(a)):
# #     for j in range(len(a[i])):
# #         print(a[i][j], end=' ')
# #     print()
# #
# # import flet
# # from flet import Page, Text,ElevatedButton,Container,Column,Image
# #
# #
# # def show_order():
# #     return ord('a')
# #
# #
# # def main(page: Page):
# #     q = Container(bgcolor='purple',height=500,width=500,content=Column(horizontal_alignment='center',controls=[Text("hi",),Text("hi",text_align = 'center')]))
# #     a = Text('enter')
# #     b = ElevatedButton(on_click=show_order())
# #     page.add(q)
# # flet.app(target=main,)
# #


# #
# # import flet
# # from flet import ListView, Page, Text
# #
# # def main(page: Page):
# #     lv = ListView(expand=True, spacing=10)
# #     for i in range(5000):
# #         lv.controls.append(Text(f"Line {i}"))
# #     page.add(lv)
# #
# # flet.app(target=main, view=flet.WEB_BROWSER)
# # import flet
# # from flet import AppBar, ElevatedButton, Page, Text, View, colors,Container
# #
# #
# # def main(page: Page):
# #     page.title = "Routes Example"
# #
# #     print("Initial route:", page.route)
# #
# #     def route_change(route):
# #         print("Route change:", route)
# #         page.views.clear()
# #         page.views.append(
# #             View(
# #                 "/",
# #                 [
# #                     AppBar(title=Text("Flet app")),
# #                     ElevatedButton("Go to settings", on_click=open_settings),
# #                 ],
# #             )
# #         )
# #         if page.route == "/settings" or page.route == "/settings/mail":
# #             page.views.append(
# #                 View(
# #                     "/settings",
# #                     [
# #                         AppBar(title=Text("Settings"), bgcolor=colors.SURFACE_VARIANT),
# #                         Text("Settings!", style="bodyMedium"),
# #                         ElevatedButton(
# #                             "Go to mail settings", on_click=open_mail_settings
# #                         ),
# #                     ],
# #                 )
# #             )
# #         if page.route == "/settings/mail":
# #             page.views.append(
# #                 View(
# #                     "/settings/mail",
# #                     [
# #                         AppBar(
# #                             title=Text("Mail Settings"), bgcolor=colors.SURFACE_VARIANT
# #                         ),
# #                         Text("Mail settings!"),
# #                     ],
# #                 )
# #             )
# #         page.update()
# #
# #     def view_pop(view):
# #         print("View pop:", view)
# #         page.views.pop()
# #         top_view = page.views[-1]
# #         page.go(top_view.route)
# #
# #     page.on_route_change = route_change
# #     page.on_view_pop = view_pop
# #
# #     def open_mail_settings(e):
# #         page.go("/settings/mail")
# #
# #     def open_settings(e):
# #         page.go("/settings")
# #
# #     page.go(page.route)
# #
# #
# # flet.app(target=main, )

# #
# # import flet
# # from flet import Container, Page, Stack, colors, Column
# #
# # def main(page: Page):
# #
# #     page.horizontal_alignment = "center"
# #     page.vertical_alignment = "center"
# #
# #     page.add(
# #         Container(
# #             Stack( [
# #                     Container(width=20, height=20, bgcolor=colors.RED, border_radius=5),
# #                     Container(
# #                         width=20,
# #                         height=20,
# #                         bgcolor=colors.YELLOW,
# #                         border_radius=5,
# #                         right=0,
# #                     ),
# #                     Container(
# #                         width=20,
# #                         height=20,
# #                         bgcolor=colors.BLUE,
# #                         border_radius=5,
# #                         right=0,
# #                         bottom=0,
# #                     ),
# #                     Container(
# #                         width=20,
# #                         height=20,
# #                         bgcolor=colors.GREEN,
# #                         border_radius=5,
# #                         left=0,
# #                         bottom=0,
# #                     ),
# #                     Column(
# #                         [
# #                             Container(
# #                                 width=20,
# #                                 height=20,
# #                                 bgcolor=colors.PURPLE,
# #                                 border_radius=5,
# #                             )
# #                         ],
# #                         left=35,
# #                         top=35,
# #                     ),
# #                 ]
# #             ),
# #             border_radius=8,
# #             padding=5,
# #             width=100,
# #             height=100,
# #             bgcolor=colors.BLACK,
# #         )
# #     )
# #
# # flet.app(target=main)


# #
# # import flet
# # from flet import IconButton, Page, Row, TextField, icons,Text,AppBar,ListView
# # import pandas as pd
# # import pyautogui as p
# # import time
# #
# # def main(page: Page):
# #
# #     time.sleep(4)
# #     for i in range(15):
# #        aq = p.typewrite("hi ")
# #        wq = p.press("Enter")
# #     a = pd.read_csv('/Users/muhammadadeel/Downloads/Uber Drives 2016.csv')
# #     ab = TextField(value='juice mango soda')
# #     abc = str(ab.value)
# #     c = abc.split()
# #
# #     d = random.randint(0,len(c)-1)
# #     w = c[d]
# #     page.title = "Flet counter example"
# #     page.appbar = AppBar(title=Text(f'hi'),color='red',bgcolor='purple')
# #     page.controls = [ab,Text(f'value is {aq}'),]
# #     page.update()
# #
# # flet.app(target=main)

# # a = 'juice fries tomato soda'
# # b = str('juice fries tomato soda')
# # c = b.split()
# # print(c)

# '''
# simple application to open whatapp web
# '''
# # import pywhatkit
# # import flet
# # from flet import Slider, Text,ElevatedButton
# #
# #
# # def main(page):
# #
# #     def button_clicked(e):
# #         # pywhatkit.open_web()
# #         # or
# #         # a = pywhatkit.open_web()
# #         # does same work
# #         pywhatkit.open_web()
# #         page.update()
# #
# #     def button_clicked2(e):
# #         # pywhatkit.open_web()
# #         # or
# #         # a = pywhatkit.open_web()
# #         # does same work
# #         pywhatkit.sendwhatmsg('+923144540046','hi',22,55)
# #         page.update()
# #
# #     button1 = ElevatedButton("Button with 'click' event", on_click=button_clicked)
# #     button2 = ElevatedButton("Button with 'click' event", on_click=button_clicked2)
# #
# #     page.add(button1,button2)
# #
# #
# # flet.app(target=main,port=52573)


# '''Gives exchange rate'''

# # import pywhatkit
# # import flet
# # from flet import Slider, Text,ElevatedButton,TextField
# #
# #
# # def main(page):
# #     t = Text()
# #     t3 = Text()
# #     t4 = Text()
# #
# #     def chnage_event_for_budget(e):
# #         t3.value = e.control.value
# #         page.update()
# #     def change_exchange_rate(e):
# #         t4.value = e.control.value
# #         page.update()
# #     budget = TextField(data=0,on_change=chnage_event_for_budget)
# #     exchange_rate = TextField(data=0,on_change=change_exchange_rate)
# #
# #     def exchange_money(e):
# #         """
# #
# #         :param budget1: float - amount of money you are planning to exchange.
# #         :param exchange_rate1: float - unit value of the foreign currency.
# #         :return: float - exchanged value of the foreign currency you can receive.
# #         """
# #
# #         a = budget.value
# #         b = exchange_rate.value
# #
# #
# #         exchanged_money = int(a)/int(b)
# #         t.value = exchanged_money
# #         page.update()
# #     def button_clicked(e):
# #         # pywhatkit.open_web()
# #         # or
# #         # a = pywhatkit.open_web()
# #         # does same work
# #         pywhatkit.open_web()
# #         page.update()
# #
# #     def button_clicked2(e):
# #         # pywhatkit.open_web()
# #         # or
# #         # a = pywhatkit.open_web()
# #         # does same work
# #         pywhatkit.sendwhatmsg('+923144540046','hi',22,55)
# #         page.update()
# #
# #     button1 = ElevatedButton("Click Here To Open Whatsapp Web", on_click=button_clicked)
# #     button2 = ElevatedButton("Button2 with 'click' event", on_click=button_clicked2)
# #     button3 = ElevatedButton("Click Here For Division", on_click=exchange_money)
# #     t2 = Text(f'Your Value is: ')
# #     page.add(Text('Enter First Value'),budget,Text('Enter Second Value'),exchange_rate,button1,button3,t)
# #
# #
# # flet.app(target=main,port=52573)


# # import pywhatkit as wkit
# # import flet
# # from flet import Slider, Text,ElevatedButton,TextField,Page


# # def main(page:Page):

# #     def send_msg_to_whatsapp():
# #         wkit.sendwhatmsg_to_group_instantly('BjO4ZFeNtjLI2kUO1S7imv','hi',4)


# #     def button_clicked():
# #         # pywhatkit.open_web()
# #         # or
# #         # a = pywhatkit.open_web()
# #         # does same work
# #         pywhatkit.open_web()
# #         page.update()

# #     def button_clicked2(e):
# #         # pywhatkit.open_web()
# #         # or
# #         # a = pywhatkit.open_web()
# #         # does same work
# #         pywhatkit.sendwhatmsg('+923144540046','hi',22,55)
# #         page.update()

# #     button1 = ElevatedButton("Button1 with 'click' event", on_click=button_clicked)
# #     button2 = ElevatedButton("Button2 with 'click' event", on_click=button_clicked2)
# #     button3 = ElevatedButton("Button3 with 'click' event", on_click=exchange_money)
# #     t2 = Text(f'Your Value is: ')
# #     page.add(budget,exchange_rate,button1,button2,button3,t)


# # flet.app(target=main,port=52573)


# '''Whatsapp Automator (also for resume)'''
# # import time
# # import pandas as pd
# # import flet
# # import pywhatkit as pwt
# # # import pyautogui as pag
# # from flet import Page, Text,ElevatedButton,Row,TextField
# #
# #
# # def main(page: Page):
# #     csv_file = pd.read_csv('Uber Drives 2016.csv')
# #     a3 = csv_file.values
# #     input1 = TextField()
# #     print(len(a3))
# #     def pywkit(e):
# #         # a = ['BjO4ZFeNtjLI2kUO1S7imv','BjO4ZFeNtjLI2kUO1S7imv','BjO4ZFeNtjLI2kUO1S7imv','BjO4ZFeNtjLI2kUO1S7imv','BjO4ZFeNtjLI2kUO1S7imv']
# #         # a2 = ['+923144540046']
# #         for i in range(0,len(a3)+1):
# #             pwt.sendwhatmsg_instantly(a3[i],input1.value,10,True)
# #             # pag.press('enter')
# #             # pwt.sendwhatmsg_to_group_instantly(a[i],input1.value,7,True)
# #         # for i in range(8):
# #         #     pag.typewrite('I am Usama ')
# #         #     pag.press('enter')
# #     page.add(Text("Enter Your Link Below"),input1,Text("Click The Following Button and wait sometime"),ElevatedButton(text='Click Here',on_click=pywkit))
# #
# # flet.app(target=main, host=flet.w)


# 'loop code'
# # import time
# # import flet
# # import pywhatkit as pwt
# # import pyautogui as pag
# # from flet import Page, Text,ElevatedButton,Row,TextField
# #
# #
# # def main(page: Page):
# #     input1 = TextField()
# #
# #     def pywkit(e):
# #         # a = ['BjO4ZFeNtjLI2kUO1S7imv','BjO4ZFeNtjLI2kUO1S7imv','BjO4ZFeNtjLI2kUO1S7imv','BjO4ZFeNtjLI2kUO1S7imv','BjO4ZFeNtjLI2kUO1S7imv']
# #         a2 = ['+923144540046']
# #         # for i in range(0,1):
# #         pwt.sendwhatmsg_instantly(a2[0], input1.value, 10)
# #         # pag.press('enter')
# #         # pwt.sendwhatmsg_to_group_instantly(a[i],input1.value,7,True)
# #         for i in range(20):
# #             pag.typewrite(input1.value)
# #             pag.press('enter')
# #
# #     page.add(Text("Enter Your Link Below"),input1,Text("Click The Following Button and wait sometime"),ElevatedButton(text='Click Here',on_click=pywkit))
# #
# # flet.app(target=main)




# '''check internet speed,# Python program to test
# # internet speed'''
# # import speedtest
# #
# #
# # st = speedtest.Speedtest()
# #
# # option = int(input('''What speed do you want to test:
# #
# # 1) Download Speed
# #
# # 2) Upload Speed
# #
# # 3) Ping
# #
# # Your Choice: '''))
# #
# #
# # if option == 1:
# #
# # 	print(st.download())
# #
# # elif option == 2:
# #
# # 	print(st.upload())
# #
# # elif option == 3:
# #
# # 	servernames =[]
# #
# # 	st.get_servers(servernames)
# #
# # 	print(st.results.ping)
# #
# # else:
# #
# # 	print("Please enter the correct choice !")

# '''API integration'''
# # import requests
# #
# # def get_data(api):
# #     response = requests.get(f"{api}")
# #     if response.status_code == 200:
# #         print("sucessfully fetched the data")
# #         formatted_print = response.json()
# #         return formatted_print
# #     else:
# #         print(f"Hello person, there's a {response.status_code} error with your request")
# #
# # get_data('https://jsonplaceholder.typicode.com/photos')

# '''Hand Writings to Text'''
# import os, io
# from google.cloud import vision_v1
# from google.cloud.vision_v1 import types
# import pandas as pd

# os. environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'
# client = vision_v1.ImageAnnotatorClient()

# FOLDER_PATH = r'/Users/muhammadadeel/Downloads/'
# IMAGE_FILE = "img.png"
# FILE_PATH = os.path.join(FOLDER_PATH, IMAGE_FILE)

# with io.open(FILE_PATH, 'rb') as image_file:
#     content = image_file.read()

# image = vision_v1.types.Image(content=content)
# response = client.document_text_detection(image=image)
# docText = response.full_text_annotation.text
# print (docText)