# MLOps Pipeline Notebook
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from sklearn.metrics import accuracy_score

# Carregar os dados
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Avaliar o modelo
y_pred = clf.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Acurácia no teste: {acc:.4f}")

# Exportar artefatos
joblib.dump(clf, 'model.joblib')
print("Modelo salvo como `model.joblib`")
