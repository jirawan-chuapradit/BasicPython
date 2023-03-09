import tkinter as tk

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
ok_buuton = tk.Button(master=window,text="ok")
ok_buuton.pack()
window.mainloop()



