# Busca por Similaridade com LLM

Aplicação desenvolvida em **Python** para realizar **busca por similaridade em textos** utilizando **embeddings semânticos**.  
O projeto foi criado para a disciplina de **Tópicos Avançados em IA**.

## Dupla

- **Carlos Borba** — RA: `00000853621`
- **Guilherme Martins** — RA: `00000851789`

## Sobre o projeto

A aplicação faz buscas semânticas em conteúdos da documentação do **scikit-learn**, usando páginas relacionadas a **Machine Learning**.

O fluxo do sistema é:

1. coleta textos de páginas do site;
2. limpa o conteúdo;
3. divide o texto em **chunks**;
4. gera embeddings para cada chunk;
5. recebe uma consulta do usuário;
6. compara a consulta com os chunks;
7. retorna os trechos mais similares.

Assim, em vez de buscar apenas palavras iguais, o sistema tenta recuperar textos com **significado semelhante**.

## Tema escolhido

**Machine Learning**

## Tecnologias utilizadas

- Python
- Flask
- Requests
- BeautifulSoup
- Sentence Transformers
- Scikit-learn
- NumPy
- HTML

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
Como executar
1. Clonar o repositório
git clone URL_DO_REPOSITORIO
cd av-2-pesquisa-por-similaridade-com-llm-v2-llm_machinelearning   2. Criar e ativar o ambiente virtual
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
Exemplos de consultas
o que é aprendizado supervisionado
métodos de agrupamento
seleção de características
avaliação de modelos
como escolher atributos importantes
Resultado esperado

A aplicação retorna os trechos mais parecidos com a consulta, mostrando:

nível de similaridade;
link da página de origem;
trecho recuperado.
Observação

Projeto desenvolvido para fins acadêmicos, com foco em demonstrar de forma prática o uso de LLM + embeddings em busca semântica textual.