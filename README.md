# 🎬 Sistema de Recomendação de Filmes com Python

Este é um projeto de estudo desenvolvido para criar um **Sistema de Recomendação de Filmes** baseado em conteúdo. Utilizando técnicas de Processamento de Linguagem Natural (NLP), o algoritmo analisa as sinopses dos filmes e sugere títulos semelhantes ao que o usuário gostou.

## 🧠 Como funciona? (Explicação Didática)

O sistema não "assiste" aos filmes, ele "lê" as sinopses! O processo acontece em três etapas principais:

1.  **Vetorização (TF-IDF):** O computador não entende palavras, apenas números. Usamos o `TfidfVectorizer` para transformar os textos das sinopses em uma matriz numérica.
    * *TF (Term Frequency):* Quantas vezes uma palavra aparece.
    * *IDF (Inverse Document Frequency):* Diminui o peso de palavras muito comuns (como "o", "de", "que") e aumenta o peso de palavras raras e importantes para o contexto.
2.  **Cálculo de Distância (Similaridade de Cosseno):** Imagine que cada filme é um ponto em um gráfico. O algoritmo calcula o ângulo entre esses pontos. Quanto menor o ângulo (ou seja, quanto mais próximo de 1 for o cosseno), mais parecidos são os filmes.
3.  **Recomendação:** O programa ordena os filmes mais próximos e devolve os top 3 resultados.

## 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem base do projeto.
* **Pandas:** Para carregar e manipular a tabela de dados (CSV).
* **Scikit-learn:** Para realizar os cálculos matemáticos e de aprendizado de máquina (TF-IDF e Cosseno).
* **VS Code:** Ambiente de desenvolvimento.

## 📋 Pré-requisitos

Para rodar este projeto, você precisa ter o **Python** instalado na sua máquina. Além disso, é necessário instalar as bibliotecas usadas.

No seu terminal (ou no terminal do VS Code), execute:

```bash
pip install pandas scikit-learn
