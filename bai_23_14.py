import time
import random
class Vehicle:
    def __init__(self, id):
        self.id = id
        self.pos = [10.776, 106.690] # Tọa độ gốc
        self.status = "Rảnh"
    def move_to(self, target):
        self.status = "Đang giao hàng"
        # Mô phỏng di chuyển đơn giản (tịnh tiến tọa độ)
        for _ in range(5):
            self.pos[0] += (target[0] - self.pos[0]) * 0.2
            self.pos[1] += (target[1] - self.pos[1]) * 0.2
            print(f"Xe {self.id} đang ở: {self.pos[0]:.4f}, {self.pos[1]:.4f}")
            time.sleep(0.5)
        self.status = "Hoàn thành"
        print(f"--- Xe {self.id} đã giao xong! ---")
v1 = Vehicle("SHP-001")
print(f"Trạng thái ban đầu: {v1.status}")
order_pos = [10.785, 106.710]
v1.move_to(order_pos)
