# Simulação de Malwares em Python: Ransomware e Keylogger

## 🎯 Sobre o Projeto
Este repositório documenta o desafio prático de simulação de malwares utilizando a linguagem **Python**. O objetivo é puramente educacional: entender o comportamento de ameaças digitais comuns (Ransomware e Keyloggers) em um ambiente controlado, para que possamos compreender como atuam e, o mais importante, como nos defender.

Todos os testes foram executados com scripts restritos a arquivos de teste locais, garantindo a segurança do sistema host.



## 🦠 Malwares Simulados

### 1. Ransomware Simulado (Criptografia de Arquivos)
O Ransomware é um software malicioso que "sequestra" os dados da vítima usando criptografia forte, exigindo um pagamento (geralmente em criptomoedas) para liberar a chave de descriptografia.
* **Como simulamos:** Utilizamos a biblioteca `cryptography.fernet` do Python para gerar uma chave simétrica. O script lê arquivos `.txt` específicos (como simulação de documentos importantes do usuário), criptografa seu conteúdo em Base64 e sobrescreve os arquivos originais.
* **Impacto real:** Perda total de acesso a documentos, bancos de dados e fotos caso não haja backup externo.



### 2. Keylogger Simulado (Captura de Teclado)
O Keylogger atua de forma furtiva, registrando cada tecla pressionada pelo usuário. O objetivo do atacante é capturar senhas, conversas, e-mails e dados de cartão de crédito.
* **Como simulamos:** Usamos a biblioteca `pynput` do Python para criar um ouvinte (*listener*) de eventos de teclado. Tudo o que é digitado no sistema operacional enquanto o script roda é salvo secretamente em um arquivo `teclas_capturadas.txt`. 
* **Evolução do ataque:** Em um cenário real, o script poderia esconder sua janela no Windows e utilizar a biblioteca `smtplib` para enviar o arquivo de log para o e-mail do atacante de tempos em tempos.

## 🛡️ Reflexão sobre Defesa e Prevenção

Desenvolver esses scripts nos mostra o quão simples pode ser a lógica por trás de um ataque destrutivo. Para nos protegermos no mundo real, as seguintes medidas são essenciais:

1. **Defesa contra Ransomware:**
   * **Backup Offline:** Ter cópias de segurança em HDs externos ou serviços de nuvem com versionamento (que não estejam mapeados como um disco local no PC).
   * **Princípio do Menor Privilégio:** O usuário do dia a dia não deve usar uma conta de Administrador. Se o malware rodar sem privilégios, ele não consegue criptografar arquivos críticos do sistema.

2. **Defesa contra Keyloggers:**
   * **Antivírus / EDR / Sandboxing:** Soluções de segurança modernas identificam o comportamento de programas que tentam "injetar" ganchos (hooks) no teclado ou fazer conexões estranhas de rede.
   * **Teclados Virtuais e Gerenciadores de Senhas:** Usar gerenciadores (como Bitwarden, 1Password) que preenchem as senhas automaticamente evita que você precise digitá-las no teclado físico, burlando o Keylogger.
   * **MFA (Múltiplos Fatores):** Mesmo que o keylogger roube sua senha, o invasor não terá o código gerado no seu celular.

3. **Conscientização:** A maioria desses scripts chega nas empresas através de Engenharia Social (Phishing). Não clicar em links suspeitos ou baixar anexos inesperados é a primeira e mais forte linha de defesa.
