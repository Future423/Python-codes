def game():
    a = input("Do want to play a Mind Game? (yes/no): ")
    if a.lower() == 'no':
        exit()
      
    print("Nice! Sure, the game goes like this: you have to think of a number, and I will try to guess that number. Now, what you need to do next is simply calculate it in your mind, and when you've done the calculation, you can just respond with (okay, yes, hmm) to let me know.")
    input()
    print("Well then, let's get started. Think of any number between 0 and 20, so that it's easy for you to perform the calculation. After all, I am intelligent, aren't I? 😅 ")
    input()
    print("Now, imagine that one of your friends has given you the same number, and your total number has doubled from the one you had originally thought of.")
    input()
    print("Great! now, add 10 to that total number from my side.")
    input()
    print("Okey! now, donate 50% of that total number.")
    input()
    print("Now, your friend is asking for the number they gave you earlier, so please return them that number.")
    input()
    print("Alright, this is the last step. Now, subtract 2 from the remaining number you have.")
    input()
    print("😄So, your number is 3.")
    
    b = input("Do you want to play again? (yes/no): ")
    if b.lower() == 'no':
        print("Okay, goodbye!")
        exit()
    else: game()
    
print("Hey there!")
game()
