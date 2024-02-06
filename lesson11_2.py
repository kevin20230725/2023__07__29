import random
def get_score() -> list:
    score = []
    for i in range(5):
        score.append(random.randint(50,100))
    return score

nums_list = int(input("請輸入學生數量:"))
#取得30個姓名
with open("names (1).txt",encoding="utf-8") as file:
    names_str = file.read()
    all_names_list = names_str.split("\n")      #將字串中的'\n'作為分割，形成一個list
    random_names = random.choices(all_names_list,k=nums_list)
print(random_names)

student = []
for i in range(nums_list):
    score = get_score()
    student.append([random_names[i]]+score)
print(student)
