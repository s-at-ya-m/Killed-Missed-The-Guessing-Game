# Import required module 
import random 
import sys

# Returns list of digits 
# of a number 
def getDigits(num): 
	return [int(i) for i in str(num)] 
	

# Returns True if number has 
# no duplicate digits 
# otherwise False	 
def noDuplicates(num): 
	num_li = getDigits(num) 
	if len(num_li) == len(set(num_li)): 
		return True
	else: 
		return False


# Generates a 4 digit number 
# with no repeated digits	 
def generateNum(level): 
    while True:
        if level == 1:
            num = random.randint(1000, 9999) 
        elif level == 2:
            num = random.randint(10000, 99999)
        elif level == 3:
            num = random.randint(100000, 999999)
        
        if noDuplicates(num): 
            return num 


# Returns common digits with exact 
# matches (bulls) and the common 
# digits in wrong position (cows) 
def numOfKillMiss(num,guess): 
	Kill_Miss = [0,0] 
	num_li = getDigits(num) 
	guess_li = getDigits(guess) 
	
	for i,j in zip(num_li,guess_li): 
		
		# common digit present 
		if j in num_li: 
		
			# common digit exact match 
			if j == i: 
				Kill_Miss[0] += 1
			
			# common digit match but in wrong position 
			else: 
				Kill_Miss[1] += 1
				
	return Kill_Miss 
	
	
# Secret Code 

print("\t\t\t\tWELCOME TO THE GUESSING GAME")
print("\t\t**********************************************************")
print("Rules:-")
print("1. It is a 4/5/6 digits number with no digit repeated.")
print("2. Choose your level:   A. Easy - 4 digits number\n\t\t\tB. Medium - 5 digits number\n\t\t\tC. Hard - 6 digits number.")
print("3. Choose number of tries in which you can guess it right.")
print("4. After every Guess, You will get number of KILLED and number of MISSED.")
print("5. KILLED: Right digit at right place")
print("6. MISSED: Right digit at wrong place")
print("Challenge your friend and let's see who can guess it first")
print("\t\t\t\t---All the best---")
print("\t\t**********************************************************")


level=int(input('Levels \n 1. Easy\n 2. Medium\n 3. Hard\nChoose your level: '))
if level != 1 and level !=2 and level != 3:
	print('Invalid Choice')
	exit()
	

tries =int(input('Enter number of tries: ')) 
num = generateNum(level) 



# Play game until correct guess 
# or till no tries left 
while tries > 0: 
	guess = int(input("Enter your guess: ")) 
	
	if not noDuplicates(guess): 
		print("Number should not have repeated digits. Try again.") 
		continue
	if level==1:
		if guess < 1000 or guess > 9999: 
			print("Enter 4 digit number only. Try again.") 
			continue
	elif level==2:
		if guess < 10000 or guess > 99999: 
			print("Enter 5 digit number only. Try again.") 
			continue
	elif level==3:
		if guess < 100000 or guess > 999999: 
			print("Enter 6 digit number only. Try again.") 
			continue	

	
	Kill_Miss = numOfKillMiss(num,guess) 
	print(f"{Kill_Miss[0]} KILLED, {Kill_Miss[1]} MISSED") 
	tries -=1
	
	if Kill_Miss[0] == level+3: 
		print("You guessed right!") 
		break
else: 
	print(f"You ran out of tries. Number was {num}")
