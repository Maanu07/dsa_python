# GUESS THE NUMBER

from random import randint

def userGuess(n):
  randomNumber=randint(1,n)
  guess=0
  while (guess!=randomNumber):
    guess=int(input(f'Guess a number between 0 and {n} '))
    if guess > randomNumber:
      print("Too High")
    elif guess < randomNumber:
      print('Too Low')

  print(f'Congrats! you guessed it correct, the number was {randomNumber}') 

# userGuess(10)
      
     

def computerGuess(n):
  low=1
  high=n
  feedback=None
  print(f'Imagine a number for me to guess between 1 to {high} !!')
  input('Type yes, if you imagined a number! => ')
  while(feedback!='c'):
    guessed=randint(low,high)
    feedback=input(f'I guessed {guessed}, is am too low(L), too high(H) or correct(C) :').lower()
    if feedback == 'l':
      low=guessed+1
    elif feedback=='h':
      high=guessed-1

  print(f'Congrats to me i guessed your number, it is {guessed}.')

computerGuess(10)





#Usb keyboard problem
""" budget=int(input("Enter the budget "))
n1=int(input('Enter number of keyboard prices '))
n2=int(input('Enter number of usb prices '))

keyboardPrices=[]
for i in range(0,n1):
    keyboardPrices.append(int(input('Enter price for keyboard')))
usbPrices=[]
for i in range(0,n2):
    usbPrices.append(int(input('Enter price for usb')))
    
sum=0
for i in keyboardPrices:
    for j in usbPrices:
        if i+j <= budget:
            if i+j > sum:
                sum=i+j

print(sum) """



""" #Hurdles and potion
n=int(input('Enter number of hurdles'))
h=int(input("max height"))
potion=0
hurdles=[]
for i in range(0,n):
  hurdles.append(int(input('hurdle height')))

for i in hurdles:
  if i > h:
    diff=i-h
    h+=diff
    potion+=diff
    
print(potion) """