class Tank:
    def __init__(self, name, ammo):
        # self ตัวใส่ข้อมูล รถถัง และคืนค่าออกไปให้คนสั่งซื้อรถถัง
        self.name = name
        self.ammo = ammo

    def add_ammo(self, ammo):
        # ข้อดีในการเรียกใช้คือสามารถ จำกัดอะไรหรือจะเขียนอะไรก็ได้ ทุกคนที่เรียกใช้ ammo จะได้กฏเดียวกัน
        if self.ammo + ammo <= 10:
            self.ammo + ammo
    
    def fire(self): # รถ ยิงได้ ทีละนัด ยิงได้เรื่อย ๆ จนกว่า กระสุนจะหมด
        if self.ammo >0:
            self.ammo -=1
    