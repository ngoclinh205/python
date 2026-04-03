filePath = "demo_file2.txt"
file = open(filePath, "w", encoding="utf-8")
file.write("Dem so luong tu xuat hien abc abc abc 12 12 it it eaut")
file.close()

filePath = "demo_file2.txt"
file = open(filePath, "r", encoding="utf-8")
text = file.read().lower()
file.close()
words = text.split()
count = {}
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(count)