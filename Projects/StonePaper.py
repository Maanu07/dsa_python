import random 

def play():
  #take a entry from user
  userEntry=input('What do you want? "r" for rock,"p" for paper or "s" for scissor\n').lower()
  #let computer randomly select from any three
  computerEntry=random.choice(['r','p','s'])

  #checking conditions
  if userEntry == computerEntry:
    return('It\'s a tie!')
   # r>s , s>p , p>r
  if (userEntry=='s' and computerEntry=='p') or (userEntry=='r' and computerEntry=='s') or (userEntry=='p' and computerEntry=='r'):
    return('You win!')
   
  return ('You loss!')


print(play())