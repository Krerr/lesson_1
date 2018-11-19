words = ["разработка", "сокет", "декоратор"]

for word in words:
    print(type(word))
    print(word)

unicode_words = [
    "\u0440\u0430\u0437\u0440\u0430\u0431\u043E\u0442\u043A\u0430",
    "\u0441\u043E\u043A\u0435\u0442",
    "\u0434\u0435\u043A\u043E\u0440\u0430\u0442\u043E\u0440"
]

for unicode_word in unicode_words:
    print(type(unicode_word))
    print(unicode_word)