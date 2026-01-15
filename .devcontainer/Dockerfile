FROM mcr.microsoft.com/devcontainers/python:3.12

# Pyxelが動作するために必要なシステムパッケージをインストール
RUN apt-get update && apt-get install -y \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    && rm -rf /var/lib/apt/lists/*

# Pyxelをインストール
RUN pip install pyxel