maxnum=None
secmaxnum=None
leastnum=None
secleastnum=None
while True:
    num1=int(input("please enter an age between 10 and 90:"))
    if num1==-1:
        break
    if 10<=num1<=90:
        if maxnum==None or num1>maxnum:
            secmaxnum=maxnum 
            maxnum=num1
            
        elif secmaxnum==None or num1>secmaxnum:
            secmaxnum=num1
            
        if leastnum==None or num1<leastnum:
            secleastnum=leastnum
            leastnum=num1   
            
        elif secleastnum==None or secleastnum>num1:
            secleastnum=num1  
                
    else:
        print("invalid number!")               
if maxnum is None:
    print("No valid age was entered.")
else:
    print("Max age:", maxnum, "second Max age:" , secmaxnum, "your least age:", leastnum, "your second least age is:", secleastnum)
    
        
    