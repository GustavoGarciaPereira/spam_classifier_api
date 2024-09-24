import nltk
import pandas as pd
from collections import defaultdict
import numpy

nltk.download('stopwords')

df = pd.read_csv("./spam.csv", encoding='windows-1252')
# df.info()
df = df.rename(columns={"v1": "classe", "v2": "mensagem", "Unnamed: 2": "dicionario_tolken"})
# print(df)


classe = df['classe'].value_counts(normalize=True) * 100

print(classe)


class NaiveClassifier2Classes(object):

    # Criamos o objeto com a probabilidade prior da classe 1 e a lista de probabilidades
    def __init__(self, p_spam, probabilities):
        self.p_spam = p_spam
        self.p_ham = 1 - p_spam
        self.probabilities = probabilities

    # Aqui criamos a função da classe que vai devolver o fit no modelo em escala log.
    def fit(self, array_tokens) -> float:
        p = {"spam": 0, "ham": 0}
        for k1, l1 in self.probabilities.items():
            for w in array_tokens:
                p[k1] = p[k1] + self.probabilities[k1][w]

        return {"spam": p["spam"] + numpy.log(self.p_spam), "ham": p["ham"] + numpy.log(self.p_ham)}




from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')

from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english", ignore_stopwords=True)

def word_prep(phrase, stemm=True):
    tokenized = tokenizer.tokenize(phrase.lower())
    stem = []
    for token in tokenized:
        stem.append(stemmer.stem(token))
    if stemm == True:
        return stem
    return tokenized


def return_value():
    def return_value2():
        return 1
    return defaultdict(return_value2)

contagem = defaultdict(return_value)
for index, row in df.iterrows():
    for word in tokenizer.tokenize(row['mensagem']):
        contagem[row['classe']][word.lower()] += 1


total = {"spam": 0, "ham": 0}
for k1, i1 in contagem.items():
    for k2, i2 in i1.items():
        total[k1] += i2


def return_value():
    def return_value2():
        return 0
    return defaultdict(return_value2)

probabilidade = defaultdict(return_value)

for k1, i1 in contagem.items():
    for k2, i2 in i1.items():
        probabilidade[k1][k2] += i2 * 1. / total[k1]

prob_ln = defaultdict(return_value)

for k1, i1 in probabilidade.items():
    for k2, i2 in i1.items():
        prob_ln[k1][k2] += numpy.log(i2)

nc = NaiveClassifier2Classes(0.135, prob_ln)

phrese = "where are you?"
# phrese = "enlarge your penis?"
#result = nc.fit(word_prep(phrese,stemm=False))
result = nc.fit(word_prep(phrese,stemm=True))
print(f">>>> {result}")