filePath = "setInfo.txt"

name = input("Tên: ")
age = input("Tuổi: ")
email = input("Email: ")
skype = input("Skype: ")
address = input("Địa chỉ: ")
work = input("Nơi làm việc: ")

file = open(filePath, "w", encoding="utf-8")
file.write("Tên: " + name + "\n")
file.write("Tuổi: " + age + "\n")
file.write("Email: " + email + "\n")
file.write("Skype: " + skype + "\n")
file.write("Địa chỉ: " + address + "\n")
file.write("Nơi làm việc: " + work + "\n")
file.close()

filePath = "setInfo.txt"
file = open(filePath, "r", encoding="utf-8")
print("Thông tin đã lưu:")
print(file.read())
file.close()