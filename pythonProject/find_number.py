
numbers = [12, 75, 150, 180, 145, 525, 50]

# วน ทุก ๆ ตำแหน่งภายใน list
for item in numbers:
    if item > 500: # ถ้า item มากกว่า 500 ให้หยุด
        break
    elif item > 150: # ถ้า item มากกว่า 150 ให้ ข้าม
        continue
    # เช็ค item หาร 5 ลงตัว ให้ print
    elif item % 5 == 0:
        print(item)