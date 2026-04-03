filePath = "test.txt"
text = input("Nhập nội dung: ")

file = open(filePath, "w", encoding="utf-8")
file.write(text)
file.close()

file = open(filePath, "r", encoding="utf-8")
print("Nội dung file:")
print(file.read())
file.close()