# ===============================================================
# ANÁLISE EXPLORATÓRIA E CLASSIFICAÇÃO DO DATASET IRIS
# ===============================================================

# Importação das bibliotecas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# ===============================================================
# 1. Carregamento e Visualização dos Dados
# ===============================================================

# Carrega o dataset Iris diretamente do sklearn
iris = load_iris()

# Cria um DataFrame pandas com as features
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
df['species'] = df['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Exibe as 5 primeiras linhas
print("=== Primeiras 5 linhas do dataset ===")
print(df.head())

# Exibe as estatísticas básicas
print("\n=== Estatísticas descritivas ===")
print(df.describe())

# ===============================================================
# 2. Análise Exploratória
# ===============================================================

sns.set(style="whitegrid", palette="pastel")

# --- Scatter plots pairwise ---
sns.pairplot(df, hue="species", diag_kind="hist")
plt.suptitle("Relações entre as variáveis do Iris Dataset", y=1.02)
plt.show()

# --- Histogramas ---
df[iris.feature_names].hist(figsize=(10, 6), bins=15, color='skyblue', edgecolor='black')
plt.suptitle("Distribuição das Features do Iris Dataset", y=1.02)
plt.show()

# --- Heatmap de correlação ---
plt.figure(figsize=(8, 6))
corr = df[iris.feature_names].corr()
sns.heatmap(corr, annot=True, cmap="Blues", fmt=".2f")
plt.title("Matriz de Correlação das Features")
plt.show()

# ===============================================================
# 3. Pré-processamento dos Dados
# ===============================================================

# Divide o dataset em features (X) e alvo (y)
X = df[iris.feature_names]
y = df['target']

# Divide em treino e teste (70% treino, 30% teste)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# ===============================================================
# 4. Treinamento e Avaliação da Árvore de Decisão
# ===============================================================

# Cria o modelo de Árvore de Decisão
clf = DecisionTreeClassifier(random_state=42)

# Treina o modelo
clf.fit(X_train, y_train)

# Faz previsões
y_pred = clf.predict(X_test)

# Avalia o modelo
acc = accuracy_score(y_test, y_pred)
print(f"\nAcurácia do modelo: {acc:.2f}")

# Matriz de confusão
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)
disp.plot(cmap="Blues")
plt.title("Matriz de Confusão - Árvore de Decisão")
plt.show()
