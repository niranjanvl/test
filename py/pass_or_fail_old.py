def Min(x,y):  #x and y are inputs. It returns the minimum of the two.
 if(x<=y):
  return x
 else:
  return y
        
def Evaluate(math, phys, chem) : #Evaluare Pass/Fail given the MPC marks.
 min = Min(math, phys)
 min = Min(min, chem)
    
 if(min >= 35):
  print("Pass")
 else:
  if(min < 25):
   print("Fail")
  else:
   count_50_or_above = 0
   if( math >= 50):
    count_50_or_above += 1
   if( phys >= 50):
    count_50_or_above += 1
   if( chem >= 50):
    count_50_or_above += 1
   if(count_50_or_above >= 2):
    print("Pass")
   else:
    print("Fail")
                
Evaluate(25,50,50)
