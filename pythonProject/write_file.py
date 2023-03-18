path = r'C:\Users\Kazuomi\Documents\GitHub\jirawan-chuapradit\BasicPython\pythonProject\test_text.txt'

file = open(path, "w",encoding="utf8")

file.write("สวัสดี ฉัน เป็น คนไทย นะจ๊ะ\n")
file.write("hello world")

file.close()
