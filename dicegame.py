min = 1 
max = 6 


x = 0
y = 0

print
player_name = input ("Enter your name please: ")
Cap = player_name.upper()

roll_again = "yes"

while roll_again == "yes": 
   if roll_again == "no":
      exit(0)
   print
   print ("Your Turn")
   print
   time.sleep(1)
   print ("Rolling the die...")
      
   time.sleep (2)

   x = random.randint(min, max)
   y = random.randint(min, max)
 
   def dice (m):
     if m == 1:
      print (""" 
          _________
         |         |
         |         |  
         |    *    | 
         |         | 
         |_________|  """)
         
     elif m == 2:
      print  ("""
          _________
         |         |
         |     *   |
         |         | 
         |   *     | 
         |_________|  """)
      
     elif m == 3:
      print ("""
          _________
         |         |
         |      *  |  
         |    *    | 
         |  *      | 
         |_________|  """) 
    
     elif m == 4:
      print ("""
          _________
         |         |
         |  *   *  |  
         |         | 
         |  *   *  | 
         |_________|  """) 
    
    
     elif m == 5:
      print (""" 
          _________
         |         |
         |  *   *  |  
         |    *    | 
         |  *   *  | 
         |_________|  """)
    
    
     elif m == 6:
      print ("""   
          _________
         |         |
         |  *   *  |  
         |  *   *  | 
         |  *   *  | 
         |_________|  """) 
   

   dice (x)
   
   print
   time.sleep(1)
   print
   print ("Computer's Turn")
   time.sleep(1)
   print
   print ("Rolling the die")
   time.sleep(2)
    
   dice(y)
   
   time.sleep(1)
   
   
   # We set the condition of win, loss 
   # and here.
   
   if x == y:
      print
      print ("Ah! It's a draw.")
      time.sleep(1)
      print
      print ("Input 'yes' to play again or 'no' to stop playing.")
      print
      
   elif x > y:
      print
      print ("Congrats! You Won"), Cap
      time.sleep(1)
      print 
      print ("To play again, input 'yes'. To stop playing, input 'no'.")
      print
      
   elif x < y:
      print
      print ("Sorry! You Lost. Try again"), Cap
      time.sleep(1)
      print  
      print ("To roll again, input 'yes'. To stop playing input 'no'.")
      print
     
   roll_again = input("Roll the die again?")
   