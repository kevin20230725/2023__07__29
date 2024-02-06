import random
def get_score() -> list:
    score = []
    for i in range(5):
        score.append(random.randint(50,100))
    return score

#取得30個姓名
def get_names(num:int) -> list: 
    with open("names (1).txt",encoding="utf-8") as file:
        names_str = file.read()
        all_names_list = names_str.split("\n")      #將字串中的'\n'作為分割，形成一個list
        names_list = random.choices(all_names_list,k=num)
    return names_list


nums_list = int(input("請輸入學生數量:"))
#取得nums_list個名字
names_list = get_names(nums_list)



student = []
for i in range(nums_list):
    score = get_score()
    new_list = [names_list[i]] + score
    student.append(new_list)
print(student)
