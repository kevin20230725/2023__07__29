#student module
#提供變數，module提供的常數
#提供class
#提供function



class Student:
    def __init__(self,name:str,chinese:int,english:int,math:int) -> None:   #第一個參數self可省略
        #實體的attribute
        self.name = name
        self.chinese = chinese
        self.english = english
        self.math = math

    #實體的方法(method)
    def total(self)->int:
        return self.chinese + self.english + self.math
    
    #建立property -> 類似method,沒有參數,一定傳出一個值
    #呼叫方法類似attribute      self.average
    @property
    def average(self)->float:
        return self.total() / 3.0

    #定義print輸出顯示的資料
    def __repr__(self) -> str:
        return f"這是Student的實體，我的name是:{self.name}"
    
import random

def get_student(n:str)->Student:
    ch = random.randint(50,100)
    en = random.randint(50,100)
    ma = random.randint(50,100)
    return Student(name=n,chinese=ch,english=en,math=ma)

