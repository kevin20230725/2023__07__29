#自訂function，此種寫法較好修改
import random
def play_game():
  count = 0
  min = 1
  max = 10
  target = random.randrange(1,11)
  print(target)
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

while True:
  play_game()   #呼叫function
  play_again = input("請問是否繼續遊戲(y/n):")
  if play_again == "n":
    break
  else:
    print("繼續遊戲------")
    continue
print("遊戲結束")