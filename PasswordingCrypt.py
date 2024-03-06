import random
import string
done=False
lc=list(string.ascii_lowercase)
uc=list(string.ascii_uppercase)
on=("1","3","5","7","9")
en=("2","4","6","8")
bincd=0
stop=0
nomore=0
val=0
ram=0
code=""
bincd2=[]
digit1=""
digit2=""
digit3=""
digit4=""
digit5=""
print("Welcome to password creator.")
print("At this program your text messages will be turned into a password.")
print("The password would not translate anything except letters even you would add.")
print("Enter a text to generate a password.")
print ("Just say e to end the program.")
while True:
    code=""
    text=input(str("Enter your password :"))
    if text=="e":
        break
    for digit in text:
        done=False
        bincd2=""
        for ucd in uc:
            if digit==ucd:
                done=True
                bincd=bin(uc.index(ucd)+1)
                break
        if done==False:
            for lcd in lc:
                if digit==lcd:
                    done=True
                    bincd=bin(lc.index(lcd)+1)
                    break
        bincd2=[]
        if done==True:
            stop=0
            for g in bincd:
                if stop>1:
                    bincd2.append(g)
                stop+=1
            val=5-len(bincd2)
            if val>0:
                for n in range(val):
                    bincd2.insert(0,"0")
            nomore=0
            digit1=int(bincd2[0])
            digit2=int(bincd2[1])
            digit3=int(bincd2[2])
            digit4=int(bincd2[3])
            digit5=int(bincd2[4])
            while nomore<5:
                ram=random.randint(1,10)
                if ram==10:
                    code=code+'0'
                    nomore-=1
                else:
                    if nomore==0:
                        if digit1%2==0:
                            ram=random.randint(0,3)
                            code=code+en[ram]
                        else:
                            ram=random.randint(0,4)
                            code=code+on[ram]
                    if nomore==1:
                        if digit2%2==0:
                            ram=random.randint(0,3)
                            code=code+en[ram]
                        else:
                            ram=random.randint(0,4)
                            code=code+on[ram]
                    if nomore==2:
                        if digit3%2==0:
                            ram=random.randint(0,3)
                            code=code+en[ram]
                        else:
                            ram=random.randint(0,4)
                            code=code+on[ram]
                    if nomore==3:
                        if digit4%2==0:
                            ram=random.randint(0,3)
                            code=code+en[ram]
                        else:
                            ram=random.randint(0,4)
                            code=code+on[ram]
                    if nomore==4:
                        if digit5%2==0:
                            ram=random.randint(0,3)
                            code=code+en[ram]
                        else:
                            ram=random.randint(0,4)
                            code=code+on[ram]
                nomore+=1
    if done==True:
        print(code)