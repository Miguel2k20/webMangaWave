# Usa a imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependências
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código do backend
COPY . .

# Expõe a porta que o backend vai rodar (ex: 5000)
EXPOSE 5000

# Comando para rodar a aplicação Python
CMD ["python", "index.py"]