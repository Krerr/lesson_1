words = ["разработка", "администрирование", "protocol", "standart"]

for word in words:
    word_byte = word.encode(encoding="utf-8")
    print(word_byte)
    word_str = word_byte.decode(encoding="utf-8")
    print(word_str)
