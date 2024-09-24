import pandas as pd
import numpy as np
from collections import defaultdict
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer
import nltk

# Baixar recursos do NLTK
nltk.download('stopwords')

class NaiveClassifier:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.tokenizer = RegexpTokenizer(r'\w+')
        self.stemmer = SnowballStemmer("english", ignore_stopwords=True)
        self.probabilidade_log = defaultdict(lambda: defaultdict(float))
        self.prior_spam = 0.0
        self.prior_ham = 0.0
        self._prepare_classifier()

    def _load_data(self) -> pd.DataFrame:
        df = pd.read_csv(self.filepath, encoding='windows-1252')
        df = df.rename(columns={
            "v1": "classe",
            "v2": "mensagem",
            "Unnamed: 2": "dicionario_tolken"
        })
        return df

    def _preprocess_text(self, text: str, stem: bool = True) -> list:
        tokens = self.tokenizer.tokenize(text.lower())
        if stem:
            return [self.stemmer.stem(token) for token in tokens]
        return tokens

    def _prepare_classifier(self):
        df = self._load_data()

        # Distribuição das classes
        class_distribution = df['classe'].value_counts(normalize=True) * 100
        self.prior_spam = class_distribution.get('spam', 0.0) / 100  # Converter para probabilidade
        self.prior_ham = 1 - self.prior_spam

        # Contagem de palavras por classe
        contagem = defaultdict(lambda: defaultdict(int))
        for _, row in df.iterrows():
            classe = row['classe']
            tokens = self._preprocess_text(row['mensagem'], stem=True)
            for token in tokens:
                contagem[classe][token] += 1

        # Total de palavras por classe
        total_palavras = {classe: sum(tokens.values()) for classe, tokens in contagem.items()}

        # Cálculo das probabilidades
        probabilidade = defaultdict(lambda: defaultdict(float))
        for classe, tokens in contagem.items():
            for token, count in tokens.items():
                probabilidade[classe][token] = count / total_palavras[classe]

        # Cálculo do log das probabilidades
        self.probabilidade_log = defaultdict(lambda: defaultdict(float))
        for classe, tokens in probabilidade.items():
            for token, prob in tokens.items():
                self.probabilidade_log[classe][token] = np.log(prob)

    def predict_log_probabilities(self, tokens: list) -> dict:
        log_prob = {"spam": 0.0, "ham": 0.0}
        for classe in self.probabilidade_log:
            for token in tokens:
                log_prob[classe] += self.probabilidade_log[classe].get(token, 0)
            if classe == "spam":
                log_prob[classe] += np.log(self.prior_spam) if self.prior_spam > 0 else -np.inf
            else:
                log_prob[classe] += np.log(self.prior_ham) if self.prior_ham > 0 else -np.inf
        return log_prob

    def classify(self, tokens: list) -> str:
        log_prob = self.predict_log_probabilities(tokens)
        return "spam" if log_prob["spam"] > log_prob["ham"] else "ham"
