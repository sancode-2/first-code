run=0
ball=0
wicket=0
overs=int(input("How many overs match: "))
over=0
i=0
while i<=60:
    enter=int(input("enter 0 for dot ball \nenter 1 for single\nenter 2 for two run \nenter 3 for three run \nenter 4 for four run \nenter 5 for wicket \nenter 6 for six run \nenter 7 for other run "))
    
    if enter==0:
        ball+=1
        print("************************************************")
        print("run=",run)
        print("wicket down: ",wicket)
        print(over+1,"over is running")
        print("************************************************")
        
    elif enter==1:
        run+=1
        ball+=1
        print("************************************************")
        print("run=",run)
        print("wicket down: ",wicket)
        print(over+1,"over is running")
        print("************************************************")
        
    elif enter==2:
        run+=2
        ball+=1
        print("************************************************")
        print("run=",run)
        print("wicket down: ",wicket)
        print(over+1,"over is running")
        print("************************************************")
        
    elif enter==3:
        run+=3
        ball+=1
        print("************************************************")
        print("run=",run)
        print("wicket down: ",wicket)
        print(over+1,"over is running")
        print("************************************************")
        
    elif enter==4:
        run+=4
        ball+=1
        print("************************************************")
        print("run=",run)
        print("wicket down: ",wicket)
        print(over+1,"over is running")
        print("OH! four run")
        print("************************************************")
        
    elif enter==5:
        wicket+=1
        ball+=1
        print("************************************************")
        print("run=",run)
        print("wicket down: ",wicket)
        print(over+1,"over is running")
        print("************************************************")
        
    elif enter==6:
        run+=6
        ball+=1
        print("************************************************")
        print("run=",run)
        print("wicket down: ",wicket)
        print(over+1,"over is running")
        print("wow!! its six")
        print("************************************************")
    elif enter==7:
        oth_run=int(input("enter extra run"))
        run+=oth_run
        print("************************************************")
        print("run=",run)
        print("wicket down: ",wicket)
        print(over+1,"over is running")
        print("************************************************")
        
    if ball%6==0:
        print("OVER END")
        print("************************************************")
        over+=1
    if over==overs:
        break
i+=1

print("************************************************")
print("      SCORECARD after end of the innings")
print("      run:   ",  run)
print("wicket down: ",wicket)
print("                 INNINGS END")
print("************************************************")