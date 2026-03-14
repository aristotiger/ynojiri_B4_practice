FROM debian:stable-slim

RUN apt-get update && \
    apt-get install -y \
    texlive-latex-base \
    texlive-latex-recommended \
    texlive-latex-extra \
    latexmk \
    && apt-get clean

WORKDIR /workspace