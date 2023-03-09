import tkinter as tk

def set_message():
    text = text_input.get() # get message in text_input var
    title_label.configure(text=text) # เซ็ตข้อความใน title label
window = tk.Tk()
window.title("basic python")
window.minsize(width=200, height=200) # ต้องใส่ค่า default ไว้ไม่งั้นมันจะ เล็กมาก

# ui ข้อความ 
title_label = tk.Label(master=window, text="calculator") #บอกว่า lebel นี้จะถูกใส่ไว้ที่ไหน ในตัวอย่างนี้คือ window
title_label.pack()# เอา label แปะ ลงไป

# text input
text_input = tk.Entry(master=window)
text_input.pack()

#  button
ok_buuton = tk.Button(master=window,text="ok", command=set_message) # 4 ใส่ชื่อ function สังเกตุว่าจะไม่ใส่ วงเล็บ เพราะว่าไม่ต้องการให้ function ทำงานก่อนจะกด
ok_buuton.pack()

# 1 เมื่อกรอกข้อความอะไรเข้าไป ให้แสดงข้อความที่กรอกเข้าไป
# 2 บอก ปุ่มว่า ถ้ากด ให้ไปเรียกใช้งาน function
# 3 create function
# เมื่อปุ่มถูกกด ฟังก์ จะทำงาน ลองรัน


window.mainloop()



