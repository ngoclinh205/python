filePath = "demo_file1.txt"
file = open(filePath, "w", encoding="utf-8")
file.write("Thuc\nhanh\nvoi\nfile\nIO")
file.close()

# in 1 dòng
filePath = "demo_file1.txt"
file = open(filePath, "r", encoding="utf-8")
content = file.read().replace("\n", " ")
print(content)
file.close()

# in từng dòng
filePath = "demo_file1.txt"
file = open(filePath, "r", encoding="utf-8")
for line in file:
    print(line.strip())
file.close()