# 1 create class
# 2 create object
#  อธิบายว่า self เป็น ไม่ต้องส่งเข้าไป 
# 3 ลอง print



class Tank:
    def __init__(self, name, ammo):
        # self ตัวใส่ข้อมูล รถถัง และคืนค่าออกไปให้คนสั่งซื้อรถถัง
        self.name = name
        self.ammo = ammo

    def add_ammo(self, ammo):
        # ข้อดีในการเรียกใช้คือสามารถ จำกัดอะไรหรือจะเขียนอะไรก็ได้ ทุกคนที่เรียกใช้ ammo จะได้กฏเดียวกัน
        if self.ammo + ammo <= 10:
            self.ammo + ammo
    
tank_1 = Tank("zero", 3)

# print(tank_1.ammo)

tank_1.ammo += 5
# print(tank_1.ammo)

tank_2 = Tank("first", 10)  # แม้ว่าจะเรียก tank เหมือนกัน แต่ว่า สิ่งที่ได้จะแตกต่างกันขึ้นอยู่กับว่า เราสั่งอะไรไป
# print(tank_2.ammo)

# บรรจุกระสุน และก็ ยิง
# method
tank_1.add_ammo(5)
print(tank_1.ammo)
tank_2.add_ammo(5) # จะเห็นว่า เพิ่มไม่ได้แล้ว เพราะว่าติด limit
print(tank_2.ammo)
