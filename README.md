# Busca por Similaridade com LLM

Aplicação desenvolvida em **Python** para realizar **busca por similaridade em textos** utilizando **embeddings semânticos**.  
O projeto foi criado para a disciplina de **Tópicos Avançados em IA**.

## Dupla

- **Carlos Borba** — RA: `00000853621`
- **Guilherme Martins** — RA: `00000851789`

## Sobre o projeto

A aplicação realiza buscas semânticas em textos sobre **Machine Learning**, a partir de páginas em português coletadas por scraping.

O fluxo do sistema é:

1. coleta textos de páginas da web;
2. limpa o conteúdo extraído;
3. divide o texto em **chunks**;
4. gera embeddings para cada chunk;
5. recebe uma consulta do usuário;
6. compara a consulta com os chunks;
7. retorna os trechos mais similares.

Dessa forma, o sistema não busca apenas palavras exatas, mas também **conteúdo com significado semelhante**.

## Tema escolhido

**Machine Learning**

## Fontes utilizadas no scraping

- IBM Brasil
- AWS em português
- Alura

## Tecnologias utilizadas

- Python
- Flask
- Requests
- BeautifulSoup
- Sentence Transformers
- Scikit-learn
- NumPy
- HTML
- CSS

## Estrutura do projeto

```bash
├── app/
│   ├── __init__.py
│   ├── scraper.py
│   ├── chunker.py
│   ├── embeddings.py
│   └── search.py
├── templates/
│   └── index.html
├── static/
├── data/
├── requirements.txt
├── main.py
└── README.md

Como executar:
1. Clonar o repositório
git clone URL_DO_REPOSITORIO
cd av-2-pesquisa-por-similaridade-com-llm-v2-llm_machinelearning

2. Criar e ativar o ambiente virtual
macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
Windows PowerShell
python -m venv .venv
.venv\Scripts\Activate.ps1

3. Instalar dependências
pip install --upgrade pip
pip install -r requirements.txt

4. Executar a aplicação
python main.py

5. Abrir no navegador
http://127.0.0.1:5000

Exemplos de consultas:
o que é aprendizado supervisionado
o que é aprendizado não supervisionado
qual a diferença entre aprendizado supervisionado e não supervisionado
o que é machine learning
o que é agrupamento de dados

Resultado esperado
A aplicação retorna os trechos mais parecidos com a consulta, exibindo:
nível de similaridade;
link da página de origem;
trecho recuperado.
Observação:
Projeto desenvolvido para fins acadêmicos, com foco em demonstrar na prática o uso de LLM + embeddings em busca semântica textual.