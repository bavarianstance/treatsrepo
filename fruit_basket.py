def fruit_basket():
 fruit_basket = ["Apple", "Banana", "Watermelon", "Tomato", "Pear"]
 Guess_Correct = False
 User_Guess =5
 while (User_Guess != 0):
   response_User = raw_input("Please guess the fruit\n")
   if response_User in fruit_basket:
     print("You are correct")
     Guess_Correct = True
     break
   else:
     print("You are wrong")
     User_Guess = User_Guess -1
 print("Thanks for playing")

