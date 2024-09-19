run=0
ball=0
wicket=0
over=0
i=0

overs=int(input("How many overs match: "))
while i<=300:
    enter=int(input("enter 0 for dot ball \nenter 1 for single\nenter 2 for two run \nenter 3 for three run \nenter 4 for four run \nenter 5 for wicket \nenter 6 for six run \nenter 7 for other run "))
    
    if enter==0:
        ball+=1
        print("************************************************")
        print("          DOT ball!")
    elif enter==1:
        run+=1
        ball+=1
        print("************************************************")
        print("          batsman play for a sigle")
    elif enter==2:
        run+=2
        ball+=1 
        print("************************************************")
        print("          here! copuple of runs") 
    elif enter==3:
        run+=3
        ball+=1
        print("************************************************") 
        print("          nice! running between the wicket 3 run")   
    elif enter==4:
        run+=4
        ball+=1
        print("************************************************")       
        print("          nice! shot its FOUR run")
    elif enter==5:
        wicket+=1
        ball+=1
        print("************************************************")
        print("          OH!! wickets down")
    elif enter==6:
        run+=6
        ball+=1
        print("************************************************")
        print("          over the boundry its SIX run")
    elif enter==7:
        oth_run=int(input("enter extra run"))
        print("************************************************")
        print("          here batsman found extra run")
        run+=oth_run 
    if ball%6==0:
        print("OVER END")
        print("************************************************")
        over+=1
    if over==overs:
        break
    print("************************************************")
    print("run=",run)
    print("wicket down: ",wicket)
    print(over+1,"over is running")
    print("************************************************")
    i+=1

print("************************************************")
print("      SCORECARD after end of the innings")
print("      run:   ",  run)
print("wicket down: ",wicket)
print("       over: ",over)
print("                 INNINGS END")
print("************************************************")