# Use a imagem base do Python
FROM python:3.11-alpine

# Define o diretório de trabalho no container
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do projeto
RUN pip install -r requirements.txt

# Copie o restante do código-fonte para o diretório de trabalho
COPY . .

# Configure as variáveis de ambiente, se necessário
# ENV DEBUG=True

# Exponha a porta em que o aplicativo Django vai rodar
EXPOSE 8000

# Executar as migrações do Django
RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations
RUN python manage.py migrate