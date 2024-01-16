# Define a imagem base para o estágio de construção como Debian 11 Slim
FROM debian:11-slim AS build

# Atualiza o índice de pacotes do sistema
RUN apt-get update && \
    # Instala dependências necessárias para criar um ambiente virtual Python
    apt-get install --no-install-suggests --no-install-recommends --yes python3-venv gcc libpython3-dev && \
    # Cria um ambiente virtual Python em /venv
    python3 -m venv /venv && \
    # Atualiza o pip e as ferramentas de empacotamento dentro do ambiente virtual
    /venv/bin/pip install --upgrade pip setuptools wheel

# Define um novo estágio de construção para instalar as dependências da aplicação
FROM build AS build-venv

# Copia o arquivo requirements.txt para o container
COPY /src/requirements.txt /requirements.txt

# Instala as dependências listadas em requirements.txt dentro do ambiente virtual
RUN /venv/bin/pip install --disable-pip-version-check -r /requirements.txt

# Define a imagem base final como gcr.io/distroless/python3-debian11 (mais leve e segura)
FROM gcr.io/distroless/python3-debian11

# Copia o ambiente virtual do estágio anterior para a imagem final
COPY --from=build-venv /venv /venv

# Copia todos os arquivos e diretórios do contexto de construção para /app
COPY . /app

# Define o diretório de trabalho para /app
WORKDIR /app

# Define o ponto de entrada da imagem como o interpretador Python no ambiente virtual e o script "src"
ENTRYPOINT ["/venv/bin/python3", "src"]