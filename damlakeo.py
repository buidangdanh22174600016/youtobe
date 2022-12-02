from random import randint  

print("nhập đấm ,lá ,kéo")

player = input()
computer = randint(0,2)

if computer == 0:
    computer="đấm"
if computer == 1:
    computer="lá"
if computer == 2:
    computer="kéo" 

print("---")
print("you choose:" + player)
print("computer chooses:" + computer)
print("---")

if player == computer:
    print("hòa")
else:    
 if player == "kéo":
    if computer == "đấm":
        print("bạn thua")
    else:
        print("bạn thắng")

 elif player == "đấm":
    if computer == "lá":
        print("bạn thua")
    if computer == "kéo":
        print("bạn thắng")

 elif player == "lá":
    if computer == "kéo":
        print("bạn thua")
    else:
        print("bạn thắng")                     
 else:
  print("nhập sai  !")        