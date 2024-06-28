text = '''TF (Term Frequency) - это отношение количества раз, которое слово (термин) встречается в конкретном документе (например, тексте), к общему числу слов в этом документе. Формула для TF может быть записана как:

TF(t, d) = (количество раз, когда термин t встречается в документе d) / (общее количество слов в документе d)

IDF (Inverse Document Frequency) - это логарифм обратной частоты документа. Это оценка того, насколько слово редко встречается в коллекции документов. Формула для IDF может быть записана как:

IDF(t, D) = log((общее количество документов в коллекции D) / (количество документов, в которых термин t встречается хотя бы раз))

Когда вы перемножаете TF и IDF, вы получаете TF-IDF для данного термина в данном документе. Это значение показывает, насколько важен данный термин в контексте этого документа и коллекции документов.

TF-IDF используется для оценки важности слов в текстовых документах и широко применяется в информационном поиске, анализе текстов и машинном обучении.'''
import math


def tf(term, doc):
    count_doc = len(doc.split())
    return doc.count(term) / count_doc


def idf(term, docs_collect):
    count = 0
    for doc in docs_collect:
        if term in doc:
            count+=1
    return math.log( len(docs_collect) / (count) + 1)

def calculate_tf_idf(term, document, docs_collect):
    tf_ = tf(term, document)
    print(tf_)
    idf_ = idf(term, docs_collect)
    print(idf_)
    return tf_ * idf_

if __name__=='__main__':
    document_collection = ["Это пример текста", "Это другой пример текста", "TF-IDF это важный термин"]

    document = "TF-IDF это мера важности термина в тексте. Это пример его использования."

    term = "TF-IDF"
    print(calculate_tf_idf(term, document, document_collection))
