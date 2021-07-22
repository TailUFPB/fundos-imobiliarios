# Rankeamento e Classificação de fundos imobiliários
[Link do Notebook utilizado](https://colab.research.google.com/drive/12asbcKcgaOM7lKSvSdKx826zLF22HqLn?usp=sharing)
## Rankeamento dos fundos

O objetivo desse projeto é rankear os fundos imobiliários disponíveis no mercado brasileiro usando os seus diversos atributos, tanto no momento atual, como ao longo dos últimos anos.

Para fazer isso, foi dado a cada fundo uma nota, obtida, resumidamente, por meio da soma da nota de cada um dos seus atributos, cada uma delas sendo a diferença entre o atributo e a média daquele campo no dataset, multiplicada por um peso, que reflete a importância daquele campo para a análise.

Com esse método de avaliação em mãos, podemos aplicá-lo aos fundos ao longo dos anos, e, por fim, somar todas essas notas(as mais antigas possuindo um peso menor), para obter o rankeamento final dos 193 fundos.

Por exemplo, aqui são os que obteram as 10 melhores pontuações:

![10 melhores fundos segundo o nosso ranking](https://github.com/TailUFPB/fundos-imobiliarios/blob/main/Top10.PNG?raw=true)
