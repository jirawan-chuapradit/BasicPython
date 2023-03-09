#exerise
# ได้เวลาเอาความรู้ที่เรียนมาสร้าง app สูตรคูณ
# เช่นใส่เลข 5 กด ได้แก่ จะได้สูตรคูณแม่ 5 ออกมา 
# ถ้าเปลี่ยนใส่ แม่ 12 ก็จะได้สูตรคูณแม่ 12

# 1 import tkinter
import tkinter as tk

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
go_btn = tk.Button(master=window,text="ได้แก่")
go_btn.pack()

# 7 create result area
output_label = tk.Label(master=window) #ยังไม่แสดงข้อความไว้แสดงตอน กด
output_label.pack()

# 8 run


window.mainloop()

