# Pond-M10-3

&emsp; Para começar o projeto, decidi utilizar o Python devido à: Familiaridade com a lingua (Oh boy was I wrong), simplicidade de utilizar documentação e o conhecimento de FastAPI para novamente facilitar a questão de linguagem, mas ainda sim tive vários problemas no meio do caminho.

&emsp;Para começar, como um bom ser humano impulsivo, comecei já definindo as rotas no handler, com todas as rotas do requerimento. As coisas começaram a desacelerar aí, com eu tendo que rever como estruturar o programa no Clean Architecture e separar nos requerimentos.

&emsp;Os principais problemas vieram com relação ao banco de dados, e como eu iria estruturar ele. Passei de SQLite, para Mysql, e, depois de um bom tempo perdido, decidi usar o SQLModel, por ser recomendado pelo criador do FastAPI(inclusive, é o projeto dele mesmo :v ). Nisso, a entity da figurinha mudou de class normal para BaseModel, para ficar de acordo com o Fast, e depois para SQLModel para condizer com a DB

&emsp;Finalizar o Repo com as chamadas ao banco se provou a última dificuldade, principalmente para entender o sistema de chamadas do SQLModel, mas entender a estrutura do "save" e "getAll" com calma facilitou na implementação dos próximos.

## Como rodar

```bash
git clone <repo>
cd Pond-M10-3
python -m venv .venv
source .venv/bin/activate        
pip install -r requirements.txt
cd src
python main.py
``