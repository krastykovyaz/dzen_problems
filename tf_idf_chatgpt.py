import math

# Функция для вычисления TF (Term Frequency)
def calculate_tf(term, document):
    # Разбиваем документ на слова
    words = document.split()
    # Считаем, сколько раз термин встречается в документе
    term_count = words.count(term)
    # Вычисляем TF
    tf = term_count / len(words)
    return tf

# Функция для вычисления IDF (Inverse Document Frequency)
def calculate_idf(term, document_collection):
    # Считаем, сколько документов в коллекции содержат заданный термин
    document_count = sum(1 for doc in document_collection if term in doc)
    # Вычисляем IDF
    idf = math.log(len(document_collection) / (document_count + 1))
    return idf

# Функция для вычисления TF-IDF
def calculate_tf_idf(term, document, document_collection):
    tf = calculate_tf(term, document)
    print(tf)
    idf = calculate_idf(term, document_collection)
    print(idf)
    tf_idf = tf * idf
    return tf_idf

# Пример использования функций
document_collection = ["Это пример текста", "Это другой пример текста", "TF-IDF это важный термин"]

document = "TF-IDF это мера важности термина в тексте. Это пример его использования."

term = "TF-IDF"
tf_idf = calculate_tf_idf(term, document, document_collection)
print(f"TF-IDF для термина '{term}' в данном документе: {tf_idf}")
