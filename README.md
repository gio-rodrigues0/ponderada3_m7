# ponderada3_m7

## Construção do Modelo

### Pré-processamento

Foi escolhido um dataset referente a características de um cliente e qual seria o seu score como consumidor.
No pré-processamento foi retirada a coluna de ID do cliente, por ter sido considerada irrelevante para definir o score. A coluna de gênero era categórica, logo, diferenciava masculino e feminino por meio da palavra em si, então, foi feita uma substituição por 0 (masculino) e 1 (feminino). As demais colunas eram numéricas, mas precisavam ser normalizadas, consequentemente, foram transformadas numa escala entre 0 e 1.

### Pycaret

O target do nosso modelo é o score de consumidor, que é medido entre 0 e 100, então, precisávamos de um modelo de regressão, para decidir qual seria, utilizei o Pycaret, que treinou vários modelos de regressão e me retornou aqueles que possuiam o melhor resultado. Sendo esse o Extra Trees Regressor.

### Modelo

Os dados foram divididos entre features e target, para depois serem separados entre dados de treino e teste. Então, o modelo foi treinado.
Então, ele é exportado para que pudesse ser utilizado na API.

## Desenvolvimento da API

### API

Utilizando FastAPI para a construção do backend e HTML/CSS para o frontend, temos uma API que recebe os dados de idade, renda anual e gênero e nos retorna o score de consumidor dessa pessoa por meio da rota "predict".

### Documentação

Em models, foi construída a documentação da nossa API, podendo ser acessada adicionando /docs como endpoint. Foi feita por meio do Pydantic.

## Dockerização

Primeiro, o arquivo Dockerfile é criado, possuindo todos os passos que devem ser recriados para a construção da aplicação. Isso inclui os seguintes:

- Utilização da imagem base do Python
- Criação de um diretório
- Cópia do arquivo requirementes.txt e instalação das suas dependências
- Cópia dos demais arquivos
- Exposição das portas que serão utilizadas
- Comando que inicializa o servidor

Após, uma imagem é criada com base nesse Dockerfile, ela foi enviada para o DockerHub para que possa ser utilizada localmente por outras pessoas. 

## Como rodar

Para baixar a imagem que se encontra no DockerHub e rodá-la, utilize o seguinte comando:

```
docker run -dp 8000:8000 giovanna0/ponderada3:tudo
```
