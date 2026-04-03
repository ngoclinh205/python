def tong_2_so(a, b):
    return a + b

def tong_nhieu_so(*args):
    return sum(args)

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def so_nguyen_to_trong_doan(a, b):
    for i in range(a, b + 1):
        if la_so_nguyen_to(i):
            print(i, end=" ")
    print()

def la_so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n

def so_hoan_hao_trong_doan(a, b):
    for i in range(a, b + 1):
        if la_so_hoan_hao(i):
            print(i, end=" ")
    print()

def tong_2_so(a, b):
    return a + b

def tong_nhieu_so(*args):
    return sum(args)

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def so_nguyen_to_trong_doan(a, b):
    for i in range(a, b + 1):
        if la_so_nguyen_to(i):
            print(i, end=" ")
    print()

def la_so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n

def so_hoan_hao_trong_doan(a, b):
    for i in range(a, b + 1):
        if la_so_hoan_hao(i):
            print(i, end=" ")
    print()

# ===== MENU =====
while True:
    print("\n===== MENU =====")
    print("1. Tổng 2 số")
    print("2. Tổng nhiều số")
    print("3. Kiểm tra số nguyên tố")
    print("4. Tìm số nguyên tố trong đoạn")
    print("5. Kiểm tra số hoàn hảo")
    print("6. Tìm số hoàn hảo trong đoạn")
    print("0. Thoát")

    chon = int(input("Chọn chức năng: "))

    if chon == 1:
        a = int(input("Nhập a: "))
        b = int(input("Nhập b: "))
        print("Tổng =", tong_2_so(a, b))

    elif chon == 2:
        ds = list(map(int, input("Nhập các số (cách nhau bởi dấu cách): ").split()))
        print("Tổng =", tong_nhieu_so(*ds))

    elif chon == 3:
        n = int(input("Nhập n: "))
        if la_so_nguyen_to(n):
            print("Là số nguyên tố")
        else:
            print("Không phải số nguyên tố")

    elif chon == 4:
        a = int(input("Nhập a: "))
        b = int(input("Nhập b: "))
        so_nguyen_to_trong_doan(a, b)

    elif chon == 5:
        n = int(input("Nhập n: "))
        if la_so_hoan_hao(n):
            print("Là số hoàn hảo")
        else:
            print("Không phải số hoàn hảo")

    elif chon == 6:
        a = int(input("Nhập a: "))
        b = int(input("Nhập b: "))
        so_hoan_hao_trong_doan(a, b)

    elif chon == 0:
        print("Thoát chương trình!")
        break

    else:
        print("Chọn sai!")