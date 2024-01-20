import random
count = 0
min = 1
max = 10
target = random.randrange(1,11)
print("--------猜數字遊戲-------\n\n")
while True:
  guess = eval(input(f"請輸入{min}-{max}之間的數字:"))
  count += 1
  if guess <= max and guess >= min:
    if target == guess :
      print(f"答對了!!，答案是{target}，總共猜了{count}次")
      break
    elif guess > target:
      print("猜錯了再小一點")
    else:
      print("猜錯了再大一點")
  else: 
    print("超出範圍")
print("遊戲結束")