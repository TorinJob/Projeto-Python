from playsound import playsound

print("Iniciando a reprodução da música...")

arquivo_de_audio = "teste-aula18.mp3"

try:

    playsound(arquivo_de_audio)
    print("Repodção terminada!")

except Exception as e:
    print(f"Ocorreu um erro ao tentar tocar o audio: {e}")

