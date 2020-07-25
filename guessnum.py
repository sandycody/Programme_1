"""Design a programme where user have to guess the original number which is given by the programmer. If the number 
    entered by the user is greater or smaller than the original number, then print "the number is greater or smaller"
    and also print number of guesses left. Once the number of guesses reaches to 0,then print "Game Over" and 
    if the guess is correct then specify how many guesses he took to finish?(Total no of guesses are 10 and
    original number is 20)"""


 #  SOLUTION 
orig_num=20    
no_of_guesses=10
print("Total number of guesses: ",no_of_guesses)
while(True):
    num=int(input("Guess the number: "))
    if (num > orig_num):
        print("Your number is greater, Try again!")
        no_of_guesses = no_of_guesses-1
        print("No of guesses left: ", no_of_guesses)
        if(no_of_guesses==0):
            print("Game Over")  
            break          
    elif (num < orig_num):
        print("Your number is smaller, Try again!")
        no_of_guesses= no_of_guesses-1
        print("No of guesses left: ", no_of_guesses)
        if(no_of_guesses==0):
            print("Game Over")     
            break
    else:
        print("Congratulations!You have guessed original number")
        print("No of guesses you took to finish :",10-no_of_guesses)
        break