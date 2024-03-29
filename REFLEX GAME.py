# REFLEX GAME

import time
import random
import sys
import os

x = True
while x == True:
   print("play\npress on the number you see on the screen and enter")
   print("1 --> easy\n2 --> mid\n3 --> difficult\n4 --> exit")
   difficulty = int(input())
   start = input("enter to start!")
   os.system("clear")
   print("3!")
   time.sleep(1)
   os.system("clear")
   print("2!!")
   time.sleep(1)
   os.system("clear")
   print("1!!!")
   time.sleep(1)
   os.system("clear")
   print("GO")
   time.sleep(0.3)
   os.system("clear")
   if difficulty == 1:
      time_start = time.time()
      number = random.randint(0,9)
      print(number)
      user_answer = int(input(""))
      time_finish = time.time()
      if user_answer == number:
         print("WELL DONE")
         time.sleep(1)
         os.system("clear")
         print("Q:{} A:{}".format(number,user_answer))
         print("YOUR TIME --> {} seconds".format(time_finish-time_start))
         time.sleep(3)
         os.system("clear")
      else:
         print("hahah loser")
         time.sleep(1)
         os.system("clear")
         print("Q:{} A:{}".format(number,user_answer))
         print("YOUR TIME --> {} seconds".format(time_finish-time_start))
   
   elif difficulty == 2:
      time_start = time.time()
      number = random.randint(10,99)
      print(number)
      user_answer = int(input(""))
      time_finish = time.time()
      if user_answer == number:
         print("WELL DONE")
         time.sleep(1)
         os.system("clear")
         print("Q:{} A:{}".format(number,user_answer))
         print("YOUR TIME --> {} seconds".format(time_finish-time_start))
         time.sleep(3)
         os.system("clear")
      else:
         print("hahah loser")
         time.sleep(1)
         os.system("clear")
         print("Q:{} A:{}".format(number,user_answer))
         print("YOUR TIME --> {} seconds".format(time_finish-time_start))

   elif difficulty == 3:
      time_start = time.time()
      number = random.randint(100,999)
      print(number)
      user_answer = int(input(""))
      time_finish = time.time()
      if user_answer == number:
         print("WELL DONE")
         time.sleep(3)
         os.system("clear")
         print("Q:{} A:{}".format(number,user_answer))
         print("YOUR TIME --> {} seconds".format(time_finish-time_start))
         time.sleep(6)
         os.system("clear")
      else:
         print("hahah loser")
         time.sleep(1)
         os.system("clear")
         print("Q:{} A:{}".format(number,user_answer))
         print("YOUR TIME --> {} seconds".format(time_finish-time_start))

   elif difficulty == 4:
      print("adios :(")
      time.sleep(3)
      break

         

   
