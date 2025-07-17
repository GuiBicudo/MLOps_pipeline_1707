import joblib
import numpy as np
from sklearn.datasets import load_iris

def test_model_exists():
    """
    Verifica se o arquivo model.joblib existe e pode ser carregado.
    """
    model = joblib.load('model.joblib')
    assert model is not None

def test_model_predicts():
    """
    Faz uma previsão com o modelo e verifica se as saídas têm o formato esperado.
    """
    iris = load_iris()
    X = iris.data[:5]  # primeiras 5 amostras
    model = joblib.load('model.joblib')
    preds = model.predict(X)

    assert preds.shape == (5,)
    assert np.all(preds >= 0)

if __name__ == "__main__":
    test_model_exists()
    test_model_predicts()
    print("✅ Todos os testes passaram.")
