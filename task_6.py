words = ["сетевое программирование\n", "сокет\n", "декоратор\n"]
file_src = "test_file.txt"

with open(file_src, "w") as file:
    for word in words:
        file.write(word)

f_n = open(file_src)

if(f_n.encoding != "UTF-8"):
    print("Кодировка" + f_n.encoding)
    f_n.close()
    with open(file_src, encoding="utf-8") as file1:
        for line in file1:
            print(line)
else:
    print("Кодировка UTF-8")
    for line in f_n:
        print(line)
f_n.close()
