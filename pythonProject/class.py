# 1 create class
# 2 create object
#  อธิบายว่า self เป็น ไม่ต้องส่งเข้าไป 
# 3 ลอง print



class Tank:
    def __init__(self, name, ammo):
        # self ตัวใส่ข้อมูล รถถัง และคืนค่าออกไปให้คนสั่งซื้อรถถัง
        self.name = name
        self.ammo = ammo
    
tank_1 = Tank("zero", 3)

print(tank_1.ammo)

tank_1.ammo += 5
print(tank_1.ammo)
