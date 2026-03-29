a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))

print("=== TỔNG & TÍCH ===")
tong = a + b + c
tich = a * b * c
print("Tổng:", tong)
print("Tích:", tich)

print("=== HIỆU 2 SỐ BẤT KỲ ===")
print("Hiệu a - b:", a - b)
print("Hiệu b - c:", b - c)
print("Hiệu a - c:", a - c)

print("=== PHÉP CHIA ===")
if b != 0:
    print("Chia nguyên a // b:", a // b)
    print("Phần dư a % b:", a % b)
    print("Chia chính xác a / b:", a / b)
else:
    print("Không thể chia cho 0")