FROM python:3.9

# Atualize e instale o cliente do MariaDB
RUN apt-get update && \
    apt-get install -y mariadb-client

# Defina o diretório de trabalho
WORKDIR /app/taskmanager/

# Copie os arquivos de requisitos e instale dependências
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copie o restante dos arquivos da aplicação
COPY . /app/

# Copie o script de espera para o container
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

# Comando para iniciar o servidor
CMD ["/app/wait-for-it.sh", "db", "--", "gunicorn", "taskmanager.wsgi:application", "--bind", "0.0.0.0:8000"]