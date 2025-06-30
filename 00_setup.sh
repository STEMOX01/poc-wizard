#!/usr/bin/env bash
set -euo pipefail

echo "Uppdaterar APT och installerar systempaket..."
apt update
apt install -y build-essential cmake git wget unzip

echo "Installerar Miniconda om den saknas..."
if ! command -v conda &> /dev/null; then
  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
  bash miniconda.sh -b -p $HOME/miniconda
  rm miniconda.sh
  eval "$($HOME/miniconda/bin/conda shell.bash hook)"
  conda init
fi

echo "Skapar Python-miljö 'poc-env'..."
conda create -y -n poc-env python=3.10
conda activate poc-env

echo "Installerar Python-beroenden..."
pip install --upgrade pip
pip install pymupdf faiss-cpu streamlit transformers jq
conda install -c conda-forge llama-cpp-python

echo "Setup färdig! Aktivera miljön med 'conda activate poc-env'."
