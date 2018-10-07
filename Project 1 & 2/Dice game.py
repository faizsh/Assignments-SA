#DICE rolling game where user has to guess the sum of two dices


import random
import time
count=0

min=1
max=6
player_name=input('Enter your name please: ')
cap=player_name.upper()
while True:
   player_guess=int(input('Enter you guess of the sum of two dice: '))
   count=count+1
   if player_guess>12 or player_guess<2:
      print('The entered guess is out of range please select the guess between 1 to 12')
   else:
      print('lets proceed further')
   x=random.randint(min,max)
   y=random.randint(min,max)
   print('The dices are rolling')
   time.sleep(2)
   print('The First dice started rolling')
   time.sleep(2)
   if x == 1:
      print (""" 
          _________
         |         |
         |         |  
         |    *    | 
         |         | 
         |_________|  """)
         
   elif x == 2:
      print  ("""
          _________
         |         |
         |     *   |
         |         | 
         |   *     | 
         |_________|  """)
      
   elif x == 3:
      print ("""
          _________
         |         |
         |      *  |  
         |    *    | 
         |  *      | 
         |_________|  """)
   elif x == 4:
      print ("""
          _________
         |         |
         |  *   *  |  
         |         | 
         |  *   *  | 
         |_________|  """) 
    
    
   elif x == 5:
      print (""" 
          _________
         |         |
         |  *   *  |  
         |    *    | 
         |  *   *  | 
         |_________|  """)
    
    
   elif x == 6:
      print ("""   
          _________
         |         |
         |  *   *  |  
         |  *   *  | 
         |  *   *  | 
         |_________|  """)
   print('The second dice started rolling')
   time.sleep(2)
   if y == 1:
      print (""" 
          _________
         |         |
         |         |  
         |    *    | 
         |         | 
         |_________|  """)
         
   elif y == 2:
      print  ("""
          _________
         |         |
         |     *   |
         |         | 
         |   *     | 
         |_________|  """)
      
   elif y == 3:
      print ("""
          _________
         |         |
         |      *  |  
         |    *    | 
         |  *      | 
         |_________|  """)
   elif y == 4:
      print ("""
          _________
         |         |
         |  *   *  |  
         |         | 
         |  *   *  | 
         |_________|  """) 
    
    
   elif y == 5:
      print (""" 
          _________
         |         |
         |  *   *  |  
         |    *    | 
         |  *   *  | 
         |_________|  """)
    
    
   elif y == 6:
      print ("""   
          _________
         |         |
         |  *   *  |  
         |  *   *  | 
         |  *   *  | 
         |_________|  """)

   print('The value for the first dice after rolling is',x)
   print('The value for the second dice after rolling is',y)
   a=print('The sum of dice after rolling is',x+y)
   if player_guess==a:
      print('You have won')
   else:
      print('You have lost')
   print('Do you want to play again?')
   ans=input()
   ans1=ans.lower()
   while ans1!='yes' and ans1!='no':
      ans=input('Enter a valid option')
      ans1=ans.lower()
   if ans1=='no':
      break
   if count==4:
      print('Your guessing chance limit has exceeded')
      break
print('\n Game Over\n Thanks for playing')
