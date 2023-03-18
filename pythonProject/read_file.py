path = r'C:\Users\Kazuomi\Documents\GitHub\jirawan-chuapradit\BasicPython\pythonProject\group_score.txt'

file = open(path)

# print(file.read())

# for score in file:
#     print(score)

pass_counter = 0
for  group_score in file:
    group_score_list = group_score.split(" ")
    for score in group_score_list:
        if int(score) > 50:
            pass_counter +=1

print(pass_counter)

file.close()