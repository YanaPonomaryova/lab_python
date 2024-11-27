import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string

nltk.download('wordnet')

# ������ ����� � �����
with open('data.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# ���������� �� ������
tokens = word_tokenize(text)

# ������������ �� �������
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
lemmatized = [lemmatizer.lemmatize(token) for token in tokens]
stemmed = [stemmer.stem(token) for token in lemmatized]

# ��������� ����-���
stop_words = set(stopwords.words('english'))
filtered = [word for word in stemmed if not word in stop_words]

# ��������� ����������
processed = [word for word in filtered if word.isalnum()]

# �������� ���������� ����� � ����� ����
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(' '.join(processed))

