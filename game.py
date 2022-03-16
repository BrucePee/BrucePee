import math
from platform import java_ver
import random
import time

password = random.randint(1,10)
isCorrect = False
guesses = 0
guessesLimit = 5
print("[+]Game Made By CamBath ")
print("""
      o__ __o                                   o__ __o                  o       o         
     /v     v\                                 <|     v\                <|>     <|>        
    />       <\                                / \     <\               < >     / >        
  o/                o__ __o/  \o__ __o__ __o   \o/     o/     o__ __o/   |      \o__ __o   
 <|                /v     |    |     |     |>   |__  _<|     /v     |    o__/_   |     v\  
  \\              />     / \  / \   / \   / \   |       \   />     / \   |      / \     <\ 
    \         /   \      \o/  \o/   \o/   \o/  <o>      /   \      \o/   |      \o/     o/ 
     o       o     o      |    |     |     |    |      o     o      |    o       |     <|  
     <\__ __/>     <\__  / \  / \   / \   / \  / \  __/>     <\__  / \   <\__   / \    / \ 
                                                                                           
                                                                                           
                                                                                           
""")
first = input("[+]Do You Agree To Join The Game ? ")

if first == "yes":
    print("[+]Good The Game Will Start In ...")
    print("1")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("[+]Start")
    second = input("[+]Choose Number From 1-10 ")
    while second != password:
        second = input("[+]Try Again ")
        guesses = guesses + 1
        if guesses == password:
            print("[+]You Won Hurray !!!")
            break
        elif guesses == 4:
            print("[+]One More Chance")
        elif guesses == guessesLimit:
            print("[+]You Lost :(  And The Word Was", password)
            break
elif first == "no":
    print("[+]Ok Get Out...")


