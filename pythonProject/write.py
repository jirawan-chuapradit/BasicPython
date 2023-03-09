path = r'C:\Users\Kazuomi\Documents\GitHub\jirawan-chuapradit\BasicPython\pythonProject\test.txt' # ชื่อ ไฟล์ ไม่จำเป็นต้องมีไฟล์นั้นอยู่ก่อน

file = open(path, "w",encoding='utf8')

# wrte something in file
file.write("hello world")
file.write("my name is jugjig")
file.write("ฉันเป็นคนไทย")
file.close()
