# show case 

import tkinter as tk

def calculate():
    num = int(text_input.get())
    if num == 0:
        result_area.configure(text="ผิดที่ไว้ใจ :-(")
        return
    
    output = ""
    for i in range (1,13,1):
        output += str(num) + " x " + str(i) + " = " + str(num * i) 
        output += "\n"
    result_area.configure(text=output)
        

window = tk.Tk()
window.title("basic multy table")
window.minsize(width=400,height=400)


title_label = tk.Label(master=window, text="สูตรคูณแม่")
title_label.pack(pady=20)


text_input = tk.Entry(master=window)
text_input.pack()


ok_btn = tk.Button(master=window, text="ได้แก่", command=calculate,width=17,height=1)
ok_btn.pack(pady=20)



result_area = tk.Label(master=window,text="")
result_area.pack()


window.mainloop()

