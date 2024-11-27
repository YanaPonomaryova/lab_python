import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

# Завантаження стоп-слів
nltk.download('stopwords')
nltk.download('punkt')

# Зчитування тексту з файлу
file_path = 'carroll-alice.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Розділення тексту на слова
words = word_tokenize(text)

# Визначення кількості слів у тексті
word_count = len(words)
print(f"Кількість слів у тексті: {word_count}")

# Визначення 10 найбільш вживаних слів та побудова діаграми
fdist = FreqDist(words)
top_words = fdist.most_common(10)
print("10 найбільш вживаних слів у тексті:", top_words)

# Побудова стовпчастої діаграми
plt.bar(*zip(*top_words))
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.title('10 найбільш вживаних слів у тексті')
plt.show()

# Видалення стоп-слів та пунктуації
stop_words = set(stopwords.words('english'))
filtered_words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]

# Визначення 10 найбільш вживаних слів після фільтрації та побудова діаграми
fdist_filtered = FreqDist(filtered_words)
top_words_filtered = fdist_filtered.most_common(10)
print("10 найбільш вживаних слів у тексті після фільтрації:", top_words_filtered)

# Побудова стовпчастої діаграми після фільтрації
plt.bar(*zip(*top_words_filtered))
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.title('10 найбільш вживаних слів у тексті після фільтрації')
plt.show()

