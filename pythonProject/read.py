import os

path = r'C:\Users\Kazuomi\Documents\GitHub\jirawan-chuapradit\BasicPython\pythonProject\score.txt'

file = open(path)

# print(file.read()) # อ่านมาทีเดียว
# readline จะอ่าน ทีละ บรรทัด

# ตรวจสอบหานักเรียนที่สอบผ่านว่ามีกี่คน
# socre ที่ได้มายังไม่ใช้ตัวเลข

pass_count = 0
for score in file:
    score_int = int(score)
    if score_int > 50:
        pass_count+=1
print("Student passed = "+ str(pass_count))

file.close()