import os

path = r'C:\Users\Kazuomi\Documents\GitHub\jirawan-chuapradit\BasicPython\pythonProject\score.txt'

file = open(path)

# print(file.read()) # อ่านมาทีเดียว
# readline จะอ่าน ทีละ บรรทัด

for score in file:
    print(score)

file.close()