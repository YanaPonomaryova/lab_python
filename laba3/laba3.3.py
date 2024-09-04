sentence = input("Введіть речення: ")

words = sentence.split()

# Фільтруємо слова, які закінчуються на «ий»
words_ending_with_iy = [word for word in words if word.endswith("ий")]

if words_ending_with_iy:
    print("Слова, які закінчуються на 'ий':", ", ".join(words_ending_with_iy))
else:
    print("Немає слів, які закінчуються на 'ий'.")
