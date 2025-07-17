# MLOps Pipeline Demo

Este projeto demonstra a migração de um notebook para produção usando GitHub Actions para implementar um pipeline básico de MLOps.

This project demonstrates migrating a notebook to production using GitHub Actions to implement a basic MLOps pipeline.

---

## Descrição / Description

🇧🇷  
Este repositório contém:

- Um notebook (`notebook_mlops_pipeline.ipynb`) que treina um modelo simples com o dataset Iris e salva o artefato (`model.joblib`).
- Um arquivo `requirements.txt` com as dependências.
- Um workflow do GitHub Actions que:
  - Instala o ambiente Python.
  - Executa o notebook automaticamente.
  - Verifica se o modelo foi salvo com sucesso.

🇺🇸  
This repository contains:

- A notebook (`notebook_mlops_pipeline.ipynb`) that trains a simple model using the Iris dataset and saves the artifact (`model.joblib`).
- A `requirements.txt` file with dependencies.
- A GitHub Actions workflow that:
  - Sets up the Python environment.
  - Automatically executes the notebook.
  - Checks if the model file was successfully saved.

---

## Como executar localmente / How to run locally

### 🇧🇷 Passos

1️⃣ Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/mlops-pipeline-demo.git
cd mlops-pipeline-demo
```
