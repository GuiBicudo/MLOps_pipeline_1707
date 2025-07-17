# MLOps Pipeline Demo

Este projeto demonstra a migração de um notebook para produção usando GitHub Actions para implementar um pipeline básico de MLOps com testes automatizados.

This project demonstrates migrating a notebook to production using GitHub Actions to implement a basic MLOps pipeline with automated tests.

---

## Descrição / Description

Este repositório contém:
- Um notebook (`notebook_mlops_pipeline.ipynb`) que treina um modelo simples com o dataset Iris e salva o artefato (`model.joblib`).
- Um arquivo `requirements.txt` com as dependências.
- Um script de testes automatizados (`test_model.py`) que valida se o modelo salvo está funcionando corretamente.
- Um workflow do GitHub Actions que:
  - Instala o ambiente Python.
  - Executa os testes automatizados usando `pytest`.

This repository contains:
- A notebook (`notebook_mlops_pipeline.ipynb`) that trains a simple model using the Iris dataset and saves the artifact (`model.joblib`).
- A `requirements.txt` file with dependencies.
- An automated test script (`test_model.py`) that validates the saved model works as expected.
- A GitHub Actions workflow that:
  - Sets up the Python environment.
  - Runs automated tests using `pytest`.

---

## Como executar localmente / How to run locally

Passos
1. Clone o repositório:
```bash
git clone https://github.com/SEU_USUARIO/mlops-pipeline-demo.git
cd mlops-pipeline-demo
```

2. Crie um ambiente virtual e instale as dependências:
```bash
python -m venv .venv
source .venv/bin/activate   # ou .venv\Scripts\activate no Windows
pip install -r requirements.txt
```

3. Execute o notebook para gerar model.joblib:
```bash
jupyter notebook notebook_mlops_pipeline.ipynb
```

4. Rode os testes automatizados:
```bash
pytest test_model.py
```

Steps
1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/mlops-pipeline-demo.git
cd mlops-pipeline-demo
```

2. Create a virtual environment and install the dependencies:
```bash
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

3. Run the notebook to generate model.joblib:
```bash
jupyter notebook notebook_mlops_pipeline.ipynb
```

4. Run the automated tests:
```bash
pytest test_model.py
```

