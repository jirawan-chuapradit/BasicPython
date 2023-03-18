path = r'C:\Users\Kazuomi\Documents\GitHub\jirawan-chuapradit\BasicPython\pythonProject\group_score.txt'
file = open(path)


w_path = r'C:\Users\Kazuomi\Documents\GitHub\jirawan-chuapradit\BasicPython\pythonProject\test_text.txt'
w_file = open(w_path, "w",encoding="utf8")

for  group_score in file:
    total_score = 0
    group_score_list = group_score.split(" ")
    for score in group_score_list:
        total_score += int(score)
    avg = total_score / len(group_score_list)

    w_file.write(str("avg: "+str(avg)+ "\n"))


file.close()
w_file.close()