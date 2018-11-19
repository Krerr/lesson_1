words = ["attribute", "класс", "функция", "type"]

for word in words:
    try:
        word_ascii = word.encode("ascii")
    except Exception:
        print("Слово " + word + " невозможно записать в битовом виде")




