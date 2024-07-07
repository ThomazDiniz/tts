'''
OPEN ANACONDA COMMAND LINE
python -m venv .venv
.venv\scripts\activate
pip install setuptools wheel
python.exe -m pip install --upgrade pip
pip install TTS
'''
from TTS.api import TTS

def generate_sentences(sentences,model_path,model,training):
    final_model_path = model_path + model[0]
    tts = TTS(final_model_path, gpu=False)
    i = 0
    for sentence in sentences:
        tts.tts_to_file(text=sentence, file_path=".\\results\\" + model[0] + "\\" + str(i) + ".wav", speaker_wav=training, language=model[1], split_sentences=True)
        i += 1

    tts.tts_to_file(text="A frase está em inglês, primo.", file_path=".\\testing\\0_" + model[0] + ".wav", speaker_wav=training, language=model[1], split_sentences=True)
    
training = [".\\training\\1.wav",".\\training\\2.wav",".\\training\\3.wav",".\\training\\4.wav",".\\training\\5.wav",".\\training\\6.wav",".\\training\\7.wav",".\\training\\8.wav",".\\training\\9.wav",".\\training\\10.wav"]

sentences = []
with open('.\\sentences.txt','r', encoding="utf-8") as topo_file:
    for line in topo_file:
        sentences.append(line.strip().replace(".", ""))

print(sentences)

models = [("xtts_v2","pt"), ("your_tts","pt-br")] 
model_path = "tts_models/multilingual/multi-dataset/"

for model in models:
    generate_sentences(sentences,model_path,model,training)


#tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)
#tts = TTS("tts_models/multilingual/multi-dataset/your_tts", gpu=False)
#tts = TTS("tts_models/en/ek1/tacotron2", gpu=False)



'''
'''



'''
Lista de modelos:
[
    "tts_models/multilingual/multi-dataset/xtts_v2",
    "tts_models/multilingual/multi-dataset/xtts_v1.1",
    "tts_models/multilingual/multi-dataset/your_tts",
    "tts_models/multilingual/multi-dataset/bark",
    "tts_models/bg/cv/vits",
    "tts_models/cs/cv/vits",
    "tts_models/da/cv/vits",
    "tts_models/et/cv/vits",
    "tts_models/ga/cv/vits",
    "tts_models/en/ek1/tacotron2",
    "tts_models/en/ljspeech/tacotron2-DDC",
    "tts_models/en/ljspeech/tacotron2-DDC_ph",
    "tts_models/en/ljspeech/glow-tts",
    "tts_models/en/ljspeech/speedy-speech",
    "tts_models/en/ljspeech/tacotron2-DCA",
    "tts_models/en/ljspeech/vits",
    "tts_models/en/ljspeech/vits--neon",
    "tts_models/en/ljspeech/fast_pitch",
    "tts_models/en/ljspeech/overflow",
    "tts_models/en/ljspeech/neural_hmm",
    "tts_models/en/vctk/vits",
    "tts_models/en/vctk/fast_pitch",
    "tts_models/en/sam/tacotron-DDC",
    "tts_models/en/blizzard2013/capacitron-t2-c50",
    "tts_models/en/blizzard2013/capacitron-t2-c150_v2",
    "tts_models/en/multi-dataset/tortoise-v2",
    "tts_models/en/jenny/jenny",
    "tts_models/es/mai/tacotron2-DDC",
    "tts_models/es/css10/vits",
    "tts_models/fr/mai/tacotron2-DDC",
    "tts_models/fr/css10/vits",
    "tts_models/uk/mai/glow-tts",
    "tts_models/uk/mai/vits",
    "tts_models/zh-CN/baker/tacotron2-DDC-GST",
    "tts_models/nl/mai/tacotron2-DDC",
    "tts_models/nl/css10/vits",
    "tts_models/de/thorsten/tacotron2-DCA",
    "tts_models/de/thorsten/vits",
    "tts_models/de/thorsten/tacotron2-DDC",
    "tts_models/de/css10/vits-neon",
    "tts_models/ja/kokoro/tacotron2-DDC",
    "tts_models/tr/common-voice/glow-tts",
    "tts_models/it/mai_female/glow-tts",
    "tts_models/it/mai_female/vits",
    "tts_models/it/mai_male/glow-tts",
    "tts_models/it/mai_male/vits",
    "tts_models/ewe/openbible/vits",
    "tts_models/hau/openbible/vits",
    "tts_models/lin/openbible/vits",
    "tts_models/tw_akuapem/openbible/vits",
    "tts_models/tw_asante/openbible/vits",
    "tts_models/yor/openbible/vits",
    "tts_models/hu/css10/vits",
    "tts_models/el/cv/vits",
    "tts_models/fi/css10/vits",
    "tts_models/hr/cv/vits",
    "tts_models/lt/cv/vits",
    "tts_models/lv/cv/vits",
    "tts_models/mt/cv/vits",
    "tts_models/pl/mai_female/vits",
    "tts_models/pt/cv/vits",
    "tts_models/ro/cv/vits",
    "tts_models/sk/cv/vits",
    "tts_models/sl/cv/vits",
    "tts_models/sv/cv/vits",
    "tts_models/ca/custom/vits",
    "tts_models/fa/custom/glow-tts",
    "tts_models/bn/custom/vits-male",
    "tts_models/bn/custom/vits-female",
    "tts_models/be/common-voice/glow-tts",
    "vocoder_models/universal/libri-tts/wavegrad",
    "vocoder_models/universal/libri-tts/fullband-melgan",
    "vocoder_models/en/ek1/wavegrad",
    "vocoder_models/en/ljspeech/multiband-melgan",
    "vocoder_models/en/ljspeech/hifigan_v2",
    "vocoder_models/en/ljspeech/univnet",
    "vocoder_models/en/blizzard2013/hifigan_v2",
    "vocoder_models/en/vctk/hifigan_v2",
    "vocoder_models/en/sam/hifigan_v2",
    "vocoder_models/nl/mai/parallel-wavegan",
    "vocoder_models/de/thorsten/wavegrad",
    "vocoder_models/de/thorsten/fullband-melgan",
    "vocoder_models/de/thorsten/hifigan_v1",
    "vocoder_models/ja/kokoro/hifigan_v1",
    "vocoder_models/uk/mai/multiband-melgan",
    "vocoder_models/tr/common-voice/hifigan",
    "vocoder_models/be/common-voice/hifigan",
    "voice_conversion_models/multilingual/vctk/freevc24"
]

tts.tts_to_file(text="Maria Madalena foi a roça comprar diamante",
                file_path="output2.wav",
                split_sentences=True
                )
'''