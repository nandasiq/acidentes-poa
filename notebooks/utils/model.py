"""
Funções auxiliares para modelagem e avaliação de modelos.
"""

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE
import seaborn as sns
import matplotlib.pyplot as plt

def balancear(X, y):
    """Balanceia classes com SMOTE."""
    return SMOTE(random_state=42).fit_resample(X, y)

def split_train_test(X, y, test_size=0.2, random_state=42):
    """Divide dataset em treino e teste com estratificação."""
    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)

def avaliar_modelo(modelo, X_test, y_test):
    """Imprime métricas de avaliação e retorna matriz de confusão."""
    y_pred = modelo.predict(X_test)
    print(classification_report(y_test, y_pred))
    return confusion_matrix(y_test, y_pred)

def plotar_matriz_confusao(cm, labels):
    """Plota matriz de confusão."""
    plt.figure(figsize=(6,5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=labels, yticklabels=labels)
    plt.ylabel("Real")
    plt.xlabel("Previsto")
    plt.show()
