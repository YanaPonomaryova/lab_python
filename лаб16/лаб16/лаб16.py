import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

# ������������ ����-���
nltk.download('stopwords')
nltk.download('punkt')

# ���������� ������ � �����
file_path = 'carroll-alice.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# ��������� ������ �� �����
words = word_tokenize(text)

# ���������� ������� ��� � �����
word_count = len(words)
print(f"ʳ������ ��� � �����: {word_count}")

# ���������� 10 ������� �������� ��� �� �������� �������
fdist = FreqDist(words)
top_words = fdist.most_common(10)
print("10 ������� �������� ��� � �����:", top_words)

# �������� ���������� �������
plt.bar(*zip(*top_words))
plt.xlabel('�����')
plt.ylabel('�������')
plt.title('10 ������� �������� ��� � �����')
plt.show()

# ��������� ����-��� �� ����������
stop_words = set(stopwords.words('english'))
filtered_words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]

# ���������� 10 ������� �������� ��� ���� ���������� �� �������� �������
fdist_filtered = FreqDist(filtered_words)
top_words_filtered = fdist_filtered.most_common(10)
print("10 ������� �������� ��� � ����� ���� ����������:", top_words_filtered)

# �������� ���������� ������� ���� ����������
plt.bar(*zip(*top_words_filtered))
plt.xlabel('�����')
plt.ylabel('�������')
plt.title('10 ������� �������� ��� � ����� ���� ����������')
plt.show()

