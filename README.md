# Rankeamento e Classificação de fundos imobiliários
[Link do Notebook utilizado](https://colab.research.google.com/drive/12asbcKcgaOM7lKSvSdKx826zLF22HqLn?usp=sharing)
## Rankeamento dos fundos

O objetivo desse projeto é rankear os fundos imobiliários disponíveis no mercado brasileiro usando os seus diversos atributos, tanto no momento atual, como ao longo dos últimos anos.

Para fazer isso, foi dado a cada fundo uma nota, obtida, resumidamente, por meio da soma da nota de cada um dos seus atributos, cada uma delas sendo a diferença entre o atributo e a média daquele campo no dataset, multiplicada por um peso, que reflete a importância daquele campo para a análise.

Com esse método de avaliação em mãos, podemos aplicá-lo aos fundos ao longo dos anos, e, por fim, somar todas essas notas(as mais antigas possuindo um peso menor), para obter o rankeamento final dos 193 fundos.

Por exemplo, aqui são os que obteram as 10 melhores pontuações:

![10 melhores fundos segundo o nosso ranking](https://github.com/TailUFPB/fundos-imobiliarios/blob/main/Top10.PNG?raw=true)

## Classificação dos fundos

Além disso, o outro objetivo do projeto é a criação de um modelo de Machine Learning que consiga classificar um fundo em bom, médio ou ruim, baseado em suas características.

Para fazer isso, vamos usar alguns momentos diferentes dos fundos para termos uma quantidade grande de dados, a fim de treinar e testar o nosso modelo. Primeiramente, aplicamos nossas funções da primeira parte nesse dataset, para que cada fundo obtenha uma nota, depois, baseando-se nessa nota, podemos separar os fundos em ruim, médio e bom.

Assim, temos nosso dataset pronto e podemos usar a biblioteca Pycaret para aplicar diversos modelos de Machine Learning, com o intuito de descobrirmos o com maior acurácia. Depois de alguns testes, concluímos que o modelo ExtraTreesClassifier é o que geralmente obtém melhores resultados, com a média perto de 88%, portanto, é o que iremos utilizar.

Por fim, podemos ver nosso modelo em ação pegando um dataset não utilizado anteriormente e fazendo nosso modelo classificar alguns fundos, algo que ele fez da forma que era esperada, atestando sua precisão.
