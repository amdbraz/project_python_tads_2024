import time
def time_devagar(texto, intervalo=0.07):
    for caractere in texto:
        print(caractere, end='', flush=True)
        time.sleep(intervalo)
