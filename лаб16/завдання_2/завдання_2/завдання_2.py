import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string

nltk.download('wordnet')

# Читаємо текст з файлу
with open('data.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Токенізація по словам
tokens = word_tokenize(text)

# Лемматизація та стеммінг
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
lemmatized = [lemmatizer.lemmatize(token) for token in tokens]
stemmed = [stemmer.stem(token) for token in lemmatized]

# Видалення стоп-слів
stop_words = set(stopwords.words('english'))
filtered = [word for word in stemmed if not word in stop_words]

# Видалення пунктуації
processed = [word for word in filtered if word.isalnum()]

# Записуємо оброблений текст у інший файл
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(' '.join(processed))

