import random
computer = random.choice([-1, 0, 1])

youstr=(input("enter your choice : "))
yourdect={"rock":-1,"paper":0,"sessior":1}
reversedect={-1:"rock",0:"paper",1:"sessior"}
you=yourdect[youstr]

print(f"your choice {reversedect[you]}\ncomputer choice {reversedect[computer]}")

if(computer==you):
    print("match draw")
else:
    if(computer==-1 and you==0 ):
        print("you win")
    elif(computer==-1 and you==1 ):
        print("you lose")
    
    elif(computer==0 and you==-1 ):
        print("you lose")
    elif(computer==0 and you==1 ):
        print("you win")
    elif(computer==1 and you==-1 ):
        print("you win")
    elif(computer==1 and you==0 ):
        print("you lose")
    else:
        print("something went wrong")
