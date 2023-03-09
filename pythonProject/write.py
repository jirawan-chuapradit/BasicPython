# path = r'C:\Users\Kazuomi\Documents\GitHub\jirawan-chuapradit\BasicPython\pythonProject\test.txt' # ชื่อ ไฟล์ ไม่จำเป็นต้องมีไฟล์นั้นอยู่ก่อน

# file = open(path, "w",encoding='utf8')

# # wrte something in file
# file.write("hello world\n")
# file.write("my name is jugjig\n")
# file.write("ฉันเป็นคนไทย\n")
# file.close()




















# โจทย์ group score
# คำนวน คะแนนเฉลี่ยของแต่ละห้อง
# เขียนคะแนน เฉลี่ย แต่ละห้องลงในไฟล์

path_gruop_score = r'C:\Users\Kazuomi\Documents\GitHub\jirawan-chuapradit\BasicPython\pythonProject\group_score.txt' 
path_test = r'C:\Users\Kazuomi\Documents\GitHub\jirawan-chuapradit\BasicPython\pythonProject\test.txt' 

file_r = open(path_gruop_score)
file_w = open(path_test,"w")

for group_score in file_r:
    total_score = 0
    group_score_list = group_score.split(" ")
    for score in group_score_list:
        score_n = int(score)
        total_score += score_n
    avg = total_score / len(group_score_list)
    file_w.write(str("avg = "+ str(avg)+ "\n"))
    
file_r.close()
file_w.close()