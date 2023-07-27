FastAPI Docker Example
Este é um exemplo de projeto usando o framework FastAPI com suporte a Docker para criação de uma API com dois endpoints simples: /usuarios e /grupos.

Pré-requisitos:
Antes de começar, certifique-se de ter o Docker instalado em seu sistema. Se você ainda não tem o Docker instalado, siga as instruções em https://docs.docker.com/get-docker/ para instalar a versão adequada ao seu sistema operacional.

Executando o projeto
Para executar o projeto, siga os seguintes passos:

1 - Clone o repositório para o seu ambiente local:
git clone https://github.com/IgorCamposGD/Projeto1.git

2 - Acesse o diretório do projeto:
cd Projeto 1

3 - Em seguida, você pode executar o comando(deixando-o em execução em segundo plano (deixando-o em execução em segundo plano (-d)):
docker-compose up -d

Após seguir esses passos, a aplicação estará disponível em http://localhost:8080.

Endpoints da API:
GET /usuarios: Retorna uma lista de usuários cadastrados.
GET /grupos: Retorna uma lista de grupos cadastrados.

http://localhost:8080/usuarios
http://localhost:8080/grupos