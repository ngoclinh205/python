_so = int(input("So nguyen duong: "))
if _so % 2 == 0:
    if _so % 3 == 0:
        print("chia het ca 2 va 3")
    else:
        print("chi chia het cho 2")
elif _so % 3 == 0:
    print("chi chia het cho 3")