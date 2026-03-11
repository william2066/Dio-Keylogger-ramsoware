Para o GitHub, o segredo é usar a linguagem Markdown da forma correta para que o texto fique escaneável, com blocos de código destacados e uma estrutura profissional que mostre que você não é apenas um estudante, mas um profissional de segurança em formação.

Aqui está o código Markdown pronto. Você pode copiar o conteúdo abaixo e colar diretamente no seu arquivo README.md:

Markdown
# 🛡️ Cybersecurity Lab: Simulação de Malware e Estratégias de Defesa

Este repositório contém o projeto prático desenvolvido durante meu bootcamp de Cibersegurança. O objetivo principal é a exploração educacional do funcionamento interno de ameaças digitais modernas, utilizando a linguagem **Python** para simular comportamentos de Ransomware e Keylogger em ambientes controlados.

---

## 📋 Sobre o Projeto

O projeto é dividido em dois pilares técnicos que simulam as fases de um ataque real: a captura de informações (Spyware) e o sequestro de dados (Ransomware). Além da implementação técnica, o projeto foca na **análise defensiva** e detecção de Indicadores de Comprometimento (IoCs).



---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

* **Linguagem:** Python 3.x
* **Criptografia:** `cryptography` (Biblioteca Fernet para AES-128)
* **Monitoramento de Periféricos:** `pynput`
* **Protocolos de Rede:** `smtplib` (SMTP para exfiltração de dados via TLS)
* **Ambiente de Teste:** Máquinas Virtuais (Kali Linux e Windows 7) isoladas da rede principal.

---

## 🚀 Implementações Realizadas

### 1. Ransomware Simulado
Um script capaz de realizar a criptografia simétrica de arquivos em um diretório alvo.
* **Criptografia:** Localiza arquivos de extensões variadas e os sobrescreve utilizando uma chave de 128 bits.
* **Mensagem de Resgate:** Gera automaticamente um arquivo `.txt` com instruções para a vítima.
* **Recuperação:** Implementação de um script "Decrypter" para restauração dos arquivos originais.

### 2. Keylogger com Exfiltração via E-mail
Um script furtivo para monitorar entradas de teclado e enviar logs remotamente.
* **Captura:** Interceptação de teclas em tempo real, tratando caracteres especiais (Enter, Backspace, Espaço).
* **Exfiltração:** Uso de **Threads** (biblioteca `threading`) para enviar logs por e-mail a cada 60 segundos de forma automatizada, simulando um servidor de Comando e Controle (C2).



---

## 🛡️ Reflexão sobre Defesa e Mitigação

A parte mais importante deste laboratório é entender como parar essas ameaças. Abaixo, elenco as estratégias de defesa exploradas:

### Camadas de Proteção
1.  **Antivírus/EDR:** Identificação de assinaturas e comportamento de *API Hooking* (comum em Keyloggers).
2.  **Firewall de Rede:** Monitoramento de conexões SMTP (porta 587) saindo de máquinas que não deveriam realizar esse tráfego.
3.  **FIM (File Integrity Monitoring):** Monitoramento de alterações em massa em diretórios sensíveis para detectar Ransomware precocemente.
4.  **Princípio do Privilégio Mínimo:** Garantir que o usuário não rode scripts como administrador, limitando o alcance da criptografia.
