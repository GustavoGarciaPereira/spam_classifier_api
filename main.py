from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from classifier import NaiveClassifier
import os

app = FastAPI(title="Spam Classifier API", version="1.0")

# Definir o caminho para o arquivo de dados
DATA_FILEPATH = "./spam.csv"

# Verificar se o arquivo de dados existe
if not os.path.exists(DATA_FILEPATH):
    raise FileNotFoundError(f"O arquivo {DATA_FILEPATH} não foi encontrado.")

# Inicializar o classificador
classifier = NaiveClassifier(filepath=DATA_FILEPATH)

# Definir modelos Pydantic para as requisições e respostas

class TextInput(BaseModel):
    text: str

class ProbabilitiesOutput(BaseModel):
    spam: float
    ham: float

class ClassificationOutput(BaseModel):
    classification: str

@app.post("/predict", response_model=ProbabilitiesOutput)
def predict_probabilities(input: TextInput):
    """
    Retorna as probabilidades logarítmicas de uma frase ser spam ou ham.
    """
    if not input.text:
        raise HTTPException(status_code=400, detail="Texto vazio fornecido.")
    
    tokens = classifier._preprocess_text(input.text, stem=True)
    probabilities = classifier.predict_log_probabilities(tokens)
    return ProbabilitiesOutput(spam=probabilities["spam"], ham=probabilities["ham"])

@app.post("/classify", response_model=ClassificationOutput)
def classify_text(input: TextInput):
    """
    Retorna a classificação da frase como spam ou ham.
    """
    if not input.text:
        raise HTTPException(status_code=400, detail="Texto vazio fornecido.")
    
    tokens = classifier._preprocess_text(input.text, stem=True)
    classification = classifier.classify(tokens)
    return ClassificationOutput(classification=classification)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Classificação de Spam!"}
