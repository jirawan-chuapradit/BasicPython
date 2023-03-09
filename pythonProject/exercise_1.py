#exerise
# ได้เวลาเอาความรู้ที่เรียนมาสร้าง app สูตรคูณ
# เช่นใส่เลข 5 กด ได้แก่ จะได้สูตรคูณแม่ 5 ออกมา 
# ถ้าเปลี่ยนใส่ แม่ 12 ก็จะได้สูตรคูณแม่ 12

# 1 import tkinter
import tkinter as tk


def show_output():
    num = int(number_input.get()) # คำสั่ง get() will return string
    
    if num == 0:
        output_label.configure(text="ผิดที่ไว้ใจ :-(")
        return
    
    output = "" # ตอนแรกจะยังไม่มีข้อความอะไร
    # เอา 1 ไป คูณ 12
    for i in range (1, 13):
        output += str(num) + " x " + str(i)# ต้องการให้มันต่อท้ายข้อความไปเรื่อย ๆ เช่น 1 x 1 = 1
        output += " = " + str(num * i) + "\n"
    output_label.configure(text=output)


# 2 create window
window = tk.Tk()
window.title("basic python")
# 3 set window size
window.minsize(width=400,height=400)

# 4 set label
title_label = tk.Label(master=window,text="สูตรคูณแม่")
title_label.pack()

# 5 create input
number_input = tk.Entry(master=window)
number_input.pack()

# 6 create btn
go_btn = tk.Button(
    master=window,text="ได้แก่",
    command=show_output
    )
go_btn.pack()

# 7 create result area
output_label = tk.Label(master=window) #ยังไม่แสดงข้อความไว้แสดงตอน กด
output_label.pack()

# 8 run

# 9 create function for button
# 10 ให้แสดงผลลัพธ์
# 11 run


# 12 ไม่ต้องการให้คำนวน แม่ 0 เนื่องจาก 0 คูณ อะไรก็ได้ 0 ถ้าใส่ 0 ให้ จบการทำงาน


window.mainloop()

