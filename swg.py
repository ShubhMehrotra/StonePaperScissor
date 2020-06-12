import random
lst=['S','P','SC']
Max_Chance=5
Hit=0
Computer=0
User=0



print("Enter Your Choice\n1:S for Stone \n2:P for Paper\n3:SC for Scissor")
while Hit<Max_Chance:
      input_=input("Lets Play")
      random_=random.choice(lst)
      if random_==input_:
         a=f"{input_}={random_}"
         print(a,"Match Tied Sorry No Point for that")
      elif input_=='S' and random_=='P':
         User=User+1
         print(f"You Win because you enter {input_} and Computer`s move was{random_}")
         print(f"User`s Score={User}\nComputer`s Score={Computer}")
      elif input_=='P'and random_=='SC':
         Computer=Computer+1
         print(f"You Loose because you enter {input_} and Computer`s move was{random_}")
         print(f"User`s Score={User}\nComputer`s Score={Computer}")
      elif input_=='SC' and random_=='S':
         Computer=Computer+1
         print(f"You Loose because you enter {input_} and Computer`s move was{random_}")
         print(f"User`s Score={User}\nComputer`s Score={Computer}")
      elif input_=='SC' and random_=='P':
         User=User+1
         print(f"You Win because you enter {input_} and Computer`s move was{random_}")
         print(f"User`s Score={User}\nComputer`s Score={Computer}")
      elif input_=='P'and random_=='SC':
         Computer=Computer+1
         print(f"You Loose because you enter {input_} and Computer`s move was{random_}")
         print(f"User`s Score={User}\nComputer`s Score={Computer}")
      elif input_=='S' and random_=='SC':
         User=User+1
         print(f"You win because you enter {input_} and Computer`s move was{random_}")
         print(f"User`s Score={User}\nComputer`s Score={Computer}")
      else:
          print("You entered Wrong Choice Try Again")
      Hit=Hit+1
      print(f"{Max_Chance-Hit}is left out of {Max_Chance}")
if Computer>User:
   print("Computer Wins")
elif User>Computer:
     print("You Wins")
else:
    print("Game Over")
print(f"your point is {User} and computer point is {Computer}")


         
         
