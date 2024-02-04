import random
def allname() -> list:
    names_list = []
    with open("names (1).txt",encoding="utf-8") as file:
        for line in file:
            names_list.append(line[:3])  
    return names_list


names_list = allname()
print("========取名系統========")
while(True):
    first_name = input("請輸入你的姓氏:")
    count = eval(input("請輸入您要的名字數量:"))
    random_list = random.choices(names_list,k = count)
    for name in random_list :
        print(first_name+name[-2:])

    again = input("是否要繼續(y/n):")
    if again.lower() == "n":
        break

print("系統結束")