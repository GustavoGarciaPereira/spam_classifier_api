# Classificador de Spam com FastAPI - Projeto de Demonstração

![Logo](https://img.icons8.com/color/96/000000/spam.png)

## 📄 Descrição

Este projeto de **Classificador de Spam** é uma demonstração prática do uso do algoritmo **Naive Bayes** em Python, integrado a uma **API** desenvolvida com **FastAPI**. A API permite que usuários enviem textos ou frases e recebam a probabilidade de serem classificados como *spam* ou *ham* (não spam), além de uma classificação final.

**Nota**: Este projeto é destinado apenas para fins de demonstração e aprendizado. Não é recomendado para uso em ambientes de produção sem as devidas adaptações e otimizações.

## 🚀 Funcionalidades

- **Classificação de Texto**: Determine se uma mensagem é *spam* ou *ham*.
- **Probabilidades Logarítmicas**: Receba as probabilidades logarítmicas de uma mensagem pertencer a cada classe.
- **API Restful**: Interface amigável para integração com outras aplicações.
- **Interface Interativa**: Utilize a interface Swagger UI fornecida pelo FastAPI para testar os endpoints.

## 📦 Estrutura do Projeto

```
spam_classifier_api/
├── classifier.py        # Lógica do classificador Naive Bayes
├── main.py              # Definição da API com FastAPI
├── requirements.txt     # Lista de dependências do projeto
├── spam.csv             # Dataset de mensagens para treinamento
└── README.md            # Documentação do projeto
```

## 🛠️ Instalação

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/spam_classifier_api.git
cd spam_classifier_api
```

### 2. Configurar o Ambiente Virtual

É recomendado utilizar um ambiente virtual para gerenciar as dependências do projeto.

```bash
# Criar um ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# No Windows:
venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate
```

### 3. Instalar as Dependências

As dependências estão listadas no arquivo `requirements.txt`. Instale-as utilizando o `pip`:

```bash
pip install -r requirements.txt
```

### 4. Baixar Recursos do NLTK

O projeto utiliza recursos do NLTK que precisam ser baixados. Isso já está implementado no código, mas você pode executar manualmente se preferir.

```python
import nltk
nltk.download('stopwords')
```

## 🏃‍♂️ Como Executar

### 1. Iniciar a API

Com o ambiente virtual ativado e as dependências instaladas, inicie a API utilizando o **Uvicorn**:

```bash
uvicorn main:app --reload
```

- **`main:app`**: Indica que o objeto `app` está no arquivo `main.py`.
- **`--reload`**: Ativa o modo de recarregamento automático durante o desenvolvimento.

Você verá uma saída semelhante a esta:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28712] using statreload
INFO:     Started server process [28714]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### 2. Acessar a Interface Interativa

Abra seu navegador e vá para [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) para acessar a interface **Swagger UI**. Aqui, você pode interagir com os endpoints da API de forma intuitiva.

## 🛤️ Endpoints da API

### 1. Rota Raiz

- **URL**: `/`
- **Método**: `GET`
- **Descrição**: Retorna uma mensagem de boas-vindas.
- **Resposta**:
  ```json
  {
    "message": "Bem-vindo à API de Classificação de Spam!"
  }
  ```

### 2. Predict Probabilities

- **URL**: `/predict`
- **Método**: `POST`
- **Descrição**: Recebe um texto e retorna as probabilidades logarítmicas de ser *spam* ou *ham*.
- **Corpo da Requisição**:
  ```json
  {
    "text": "seu texto aqui"
  }
  ```
- **Resposta**:
  ```json
  {
    "spam": -20.842408988403072,
    "ham": -15.29606179837844
  }
  ```

### 3. Classify Text

- **URL**: `/classify`
- **Método**: `POST`
- **Descrição**: Recebe um texto e retorna a classificação final como *spam* ou *ham*.
- **Corpo da Requisição**:
  ```json
  {
    "text": "seu texto aqui"
  }
  ```
- **Resposta**:
  ```json
  {
    "classification": "ham"
  }
  ```

## 📝 Exemplos de Uso

### 1. Utilizando a Interface Swagger UI

1. Acesse [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
2. Selecione o endpoint desejado (`/predict` ou `/classify`).
3. Clique em **"Try it out"**.
4. Insira o texto no campo `text`.
5. Clique em **"Execute"** para ver a resposta.

### 2. Utilizando `curl`

#### Predict Probabilities

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d "{\"text\": \"where are you?\"}"
```

**Resposta:**
```json
{
  "spam": -20.842408988403072,
  "ham": -15.29606179837844
}
```

#### Classify Text

```bash
curl -X POST "http://127.0.0.1:8000/classify" \
     -H "Content-Type: application/json" \
     -d "{\"text\": \"where are you?\"}"
```

**Resposta:**
```json
{
  "classification": "ham"
}
```

### 3. Utilizando Postman ou Insomnia

1. Crie uma nova requisição `POST`.
2. Defina a URL como `http://127.0.0.1:8000/predict` ou `http://127.0.0.1:8000/classify`.
3. No corpo da requisição, selecione o formato **JSON** e insira:
   ```json
   {
     "text": "seu texto aqui"
   }
   ```
4. Envie a requisição e visualize a resposta.

## 📚 Tecnologias Utilizadas

- **Python 3.7+**
- **FastAPI**: Framework web rápido e moderno para construir APIs com Python.
- **Uvicorn**: Servidor ASGI rápido para aplicações Python.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **NLTK**: Toolkit para processamento de linguagem natural.
- **NumPy**: Biblioteca para computação científica.
- **scikit-learn** (opcional): Para possíveis melhorias e experimentações futuras.

## 📦 Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`. As principais são:

- **fastapi**
- **uvicorn**
- **pandas**
- **nltk**
- **numpy**

Para instalar todas as dependências, execute:

```bash
pip install -r requirements.txt
```

## 🛠️ Melhorias Futuras

- **Autenticação**: Adicionar mecanismos de autenticação para proteger a API.
- **Rate Limiting**: Implementar limites de requisições para evitar abusos.
- **Persistência de Modelo**: Salvar o modelo treinado para evitar recálculos em cada inicialização.
- **Interface Web**: Desenvolver uma interface web amigável para interagir com a API.
- **Suporte a Outros Idiomas**: Expandir o classificador para suportar múltiplos idiomas.

**Nota**: Essas melhorias não foram implementadas neste projeto de demonstração, mas podem ser adicionadas conforme necessário.

<!-- ## 🤝 Contribuições

Contribuições são bem-vindas! Este projeto de demonstração está aberto para aprimoramentos e ajustes que possam enriquecer sua funcionalidade e aprendizado.

1. **Fork** o projeto
2. **Crie** sua feature branch (`git checkout -b feature/nova-feature`)
3. **Commit** suas alterações (`git commit -m 'Adiciona nova feature'`)
4. **Push** para a branch (`git push origin feature/nova-feature`)
5. **Abra** um **Pull Request**

## 📄 Licença

Este projeto está licenciado sob a **MIT License**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🎓 Agradecimentos

- **NLTK**: Por fornecer ferramentas essenciais para processamento de linguagem natural.
- **FastAPI**: Por tornar a criação de APIs rápida e eficiente.
- **Comunidade Python**: Pelo constante suporte e desenvolvimento de bibliotecas incríveis.

---

**Nota**: Este documento foi ajustado para enfatizar que o projeto é uma demonstração. Sinta-se à vontade para personalizar ainda mais conforme as necessidades específicas do seu projeto ou público-alvo. -->

Imgens do projeto rodando:

![imagem](/img/Screenshot%20from%202024-09-24%2017-37-33.png)
![imagem](/img/Screenshot%20from%202024-09-24%2017-38-23.png)
![imagem](/img/Screenshot%20from%202024-09-24%2017-38-48.png)
![imagem](/img/Screenshot%20from%202024-09-24%2017-39-03.png)