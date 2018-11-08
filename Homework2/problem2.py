import random
num = random.randint(1, 100)

guess = int(input("Guess the number:"))


while guess != exit:
  while guess != num:    
    if guess > num:
      print("too high")
    else: 
      print("too low")
    guess = int(input("Guess the number:"))
  if guess == num:  
    print("exactly right")
    break

if guess == exit:
   quit()



