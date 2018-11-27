def ArmN(x):
    sum=0
    t=x
    while(t>0): #starts while loop
      d=t%10    #extracts last digit
      sum+=d**3 #cube of extracted digit
      t=t//10   #gives quotent of input
    if sum==x:
        return "Armstrong No."
    else:
         return "Not Armstrong No."
x=int(input())
print(ArmN(x))
