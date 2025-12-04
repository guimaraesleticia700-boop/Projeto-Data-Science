import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- CARREGAMENTO E TRATAMENTO DOS DADOS ---
try:
    # Lê o arquivo CSV original (base pequena)
    df = pd.read_csv('filmes.csv')
    
    # Preenche valores nulos na coluna de descrição para evitar erros
    # Nota: Se sua coluna chama 'sinopse', mude 'descricao' para 'sinopse' aqui
    df['descricao'] = df['descricao'].fillna('')

except FileNotFoundError:
    print("Erro: O arquivo 'filmes.csv' não foi encontrado.")
    exit()
except KeyError:
    print("Erro: A coluna 'descricao' não foi encontrada. Verifique se no seu CSV o nome é 'sinopse' ou 'overview'.")
    exit()

# --- PROCESSAMENTO (NLP) ---

# Inicializa o vetorizador (sem stop_words='portuguese' para evitar erros de versão)
vetorizar = TfidfVectorizer() 
matriz_tfidf = vetorizar.fit_transform(df['descricao'])

# Calcula a similaridade
similaridade = cosine_similarity(matriz_tfidf, matriz_tfidf)

# --- FUNÇÃO DE RECOMENDAÇÃO ---

def recomendar_filmes(titulo, n=3):
    """
    Busca os 'n' filmes mais similares ao título informado.
    """
    
    # Validação: verifica se o título existe na base
    if titulo not in df['titulo'].values:
        print(f"Filme '{titulo}' não encontrado na base de dados.")
        return

    # Pega o índice do filme
    idx = df[df['titulo'] == titulo].index[0]

    # Calcula scores
    scores = list(enumerate(similaridade[idx]))

    # Ordena do maior para o menor
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    # Pega os top 'n' (pula o primeiro que é ele mesmo)
    scores = scores[1:n+1]

    # Mostra o resultado
    print(f"\nFilmes semelhantes a '{titulo}':")
    for i, score in scores:
        titulo_filme = df.iloc[i]['titulo']
        print(f"- {titulo_filme} (Similaridade: {score:.2f})")

# --- EXECUÇÃO ---
# Mude o nome aqui dentro para testar outros filmes do seu CSV
recomendar_filmes("Matrix")