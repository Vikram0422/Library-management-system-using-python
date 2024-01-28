import random
rnum = random.randint(0, 100)
print(rnum)
count = 1
num = None
while(rnum != num):
    num = int(input("Enter a number to be guessed: "))
    if(num>rnum):
        print("You entered higher number!")
        count +=1
    elif(num<rnum):
        print("You entered lower number!")
        count +=1
    else:
        print(f"Hooray! You entered the correct number in {count}th guess")

with open("hiscore.txt","r") as f:
    highscore = int(f.read())

    if(count<highscore):
        print("Congragulation you just broke the highscore!")
        with open("hiscore.txt","w") as f:
            f.write(str(count))

