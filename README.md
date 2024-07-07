# Projeto de reprodução para a disciplina Fundamentos de Pesquica em Ciência da Computação 2 da Universidade Federal de Campina Grande

O artigo selecionado para reprodução foi o "Conversão Texto-Fala para o Português Brasileiro Utilizando Tacotron 2 com Vocoder Griffin-Lim" de Rodrigo Kobashikawa Rosa, Danilo Silva. Nele os autores treinam o modelo Tacotron para gerar TTS para audio em português brasileiro. Algo que o modelo original Tacotron não era capaz de fazer.

Nele os autores se utilizam de um conjunto de dados chamado Common Voice para treinar o modelo Tacotron e gerar audio em português brasileiro.

[Para exemplos do modelo é possível acessar este link do github pages.](https://thomazdiniz.github.io/tts/)

## Avaliação

No artigo os autores avaliam a qualidade do modelo a partir de contagens manuais de "palavras puladas" (palavras que foram ignoradas pelo tacotron no momento da sintetização de voz) e palavras pronunciadas de maneira incorreta.

O artigo pode ser lido no DOI:10.14209/sbrt.2021.1570727280 e [ele acompanha deste repositório no github.](https://github.com/rodrigokrosa/tacotron2-GL-brazillian-portuguese).

## Esta reprodução

Ao tentar executar os passos definidos no artigo tivemos bastante problemas de compatibilidade com o hardware para executar as funções, portanto nesta reprodução nos ateremos a utilizar uma outra implementação e outro modelo, mas avaliar de maneira manual este outro modelo da mesma maneira que foi avaliada no artigo (contagem de erros de pronúncia e palavras ignoradas pelo modelo). Utilizamos neste artigo modelos TTS que são multilinguais (modelos com capacidade de gerar para diversas linguas, inclusive português em alguns casos).

Avaliamos separadamente alguns modelos da mesma forma que o artigo original para avaliar a capacidade destes modelos de gerar sentenças em português brasileiro.

## Rodando este projeto

1. Esta reprodução foi feita no windows, não há garantias para distribuição linux/mac.
2. Instale o python 3
3. Instale o Conda, abra o CMD conda
4. No terminal Conda rode:

		python -m venv .venv
		.venv\scripts\activate
		pip install setuptools wheel
		python.exe -m pip install --upgrade pip
		pip install TTS
		python tts.py

Com isso você deverá estar rodando o script de geração de áudios, a partir disso é só fazer o processo manual de avaliação dos áudios.

5. Caso você queira ver os modelos possíveis para ser utizado em uma reprodução de TTS. Poderá rodar `python list_models.py`. 

6. O código necessário para rodar o mínimo é:

		#imports
		from TTS.api import TTS
		tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)
		#generate speech by cloning a voice using default settings
		tts.tts_to_file(text="Nunca tinha tido coragem de cantar, mas agora tudo isto mudou",
		                file_path="output2.wav",
		                split_sentences=True
		                )






