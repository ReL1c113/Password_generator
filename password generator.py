#RANDOM PASSWORD GENERATOR
import random
print("WELCOME TO RANDOM PASSWORD GENERATOR YOUR PASSWORD WILL BE A COMBINATION OF ALPHABETS SYMBOLS AND NUMBERS\nYOU CAN ENTER HOW MANY ALPHABETS NUMBERS OR SYMBOLS YOU WOULD LIKE AND WE WILL GENERATE YOUR PASSWORD ")
print("\nHOW MANY ALPHABETS WOULD YOU LIKE TO HAVE.")
i=int(input())
print("HOW MANY SYMBOLS WOULD YOU LIKE TO HAVE.")
j=int(input())
print("HOW MANY NUMBERS WOULD YOU LIKE TO HAVE")
k=int(input())
var1="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
var2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
var3="@#$%^&*"
while(True):
       x=random.choice(var2)
       print(x,end="")
       for a in range(0,i-1):
         y=random.choice(var1)
         print(y,end="")
       for a in range(0,j):
         z=random.choice(var3)
         print(z,end="")
       for a in range(0,k):
         w=random.randint(0,9)
         print(w,end="")
       print("\n\nWOULD YOU LIKE A NEW PASSWORD\n YES    NO")
       q=input()
       if q=="YES" or q=="yes":
           continue
       else:
           break