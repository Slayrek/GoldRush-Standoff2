import os
import time as t
import random as r

print("!!!ВЕДЕТЬСЯ ПОШУК ПРОГРАМИ ЧІТА, БУДЬ ЛАСКА НЕ ВИМИКАЙТЕ ПРОГРАМУ ДО ВИВОДУ ПОВІДОМЛЕННЯ ПРО ЗАКІНЧЕННЯ ЇЇ РОБОТИ!!!")

t.sleep(14)
print("Hotfix(s):                 20 Hotfix(s) Installed. [01]: KB5027122 [02]: KB4534170 [03]: KB4537759[04]: KB4545706 [05]: KB4562830[06]: KB4598481 [07]: KB5003791 [08]: KB5012170[09]: KB5015684 [10]: KB5027215[11]: KB5014671[12]: KB5015895 [13]: KB5016705")
print("[14]: KB5018506")
print("[15]: KB5020372")
print("[16]: KB5022924")
print("[17]: KB5023794")
print("[18]: KB5025315")
var = r.randint(2, 15)
t.sleep(var)
print("[19]: KB5026879")
print("[20]: KB5003742")
var = r.randint(4, 15)
t.sleep(var)
print("[20]: KB5003742")
var = r.randint(1, 7)
t.sleep(var)
print("[01]: Intl4 Family 6 Model 140 Stepping 1 GenuineIntel ~2419 MhzBIS Ver: 13.03.2023")
  
def search_file(filename, search_path):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

filename = "чіта"
search_path = os.getcwd() 

result = search_file(filename, search_path)

if result:
    print(f"Файл {filename} знайдено за шляхом: {result}")
else:
    print(f"Файл {filename} не знайдено.")
