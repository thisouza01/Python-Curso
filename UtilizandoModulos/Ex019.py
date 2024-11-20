# abre um audio e reproduza em MP3

from pygame import mixer 

# Inicializar o mixer
mixer.init()

# Caminho do arquivo
caminho_mp3 = 'c:/Users/tihso/Downloads/test_tone.mp3'

mixer.music.load(caminho_mp3)
mixer.music.play()
print("Reproduzindo o áudio. Pressione Enter para parar...")
input()
mixer.music.stop()