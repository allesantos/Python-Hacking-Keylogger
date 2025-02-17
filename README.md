# Keylogger Educacional

Este projeto contém um **script poderoso** em Python, capaz de registrar todas as teclas digitadas no teclado. Além de capturar as entradas, o script envia os dados coletados para o e-mail configurado pelo usuário que controla o keylogger.

**Atenção:** Este projeto é **apenas para fins educacionais** e deve ser utilizado como ferramenta de teste e aprendizado para estudantes e profissionais da área de Segurança da Informação. O uso indevido deste script em ambientes sem autorização é ilegal e antiético.

---

## 📌 Índice
- [🚀 Recursos](#-recursos)
- [🛠 Tecnologias](#-tecnologias)
- [✅ Pré-requisitos](#-pré-requisitos)
- [💾 Instalação](#-instalação)
- [▶️ Uso](#-uso)
- [🤝 Contribuição](#-contribuição)
- [📄 Licença](#-licença)

---

## ⚡ Recursos
- **Captura de teclas:** Registra em tempo real todas as teclas digitadas.
- **Envio automático:** Transmite os dados capturados para um e-mail pré-configurado.
- **Configuração personalizável:** Permite ajustar as variáveis, como o endereço de e-mail e intervalos de envio.
- **Código modular:** Facilita a compreensão e a personalização do script para diferentes necessidades.

---

## 🛠 Tecnologias
- **Python 3.x:** Linguagem principal utilizada no desenvolvimento.
- **Bibliotecas:**
  - `pynput` para captura dos eventos do teclado.
  - `smtplib` para envio de e-mails.
  - Outras bibliotecas padrão do Python.

---

## 📋 Pré-requisitos
- **Python 3.6+** instalado no sistema.
- Acesso à internet para envio dos dados.
- Uma conta de e-mail configurada para o envio das informações (preferencialmente com configurações de segurança adequadas).

---

## 🔧 Instalação
1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu_usuario/nome_do_repositorio.git

2. **Navegue até o diretório do projeto:**
   ```bash
   cd nome_do_repositorio

3. **Instale as bibliotecas necessárias como por exemplo:**

     ```bash
     pip install pynput
     ```

---

## 💻 Uso  
1. Configure o e-mail:

   - Abra o script keylogger.py e insira as credenciais do e-mail que receberá os dados.
     
2. Execute o script:

     ```
      python keylogger.py
    ```

3. Monitoramento:

   - O script iniciará a captura de todas as teclas digitadas e enviará periodicamente os dados para o e-mail configurado.

       - Abaixo, você confere na imagem, um arquivo de log gerado pelo keylogger exibindo algumas informações capturadas.

Aviso: Utilize este script somente em ambientes de teste e com autorização explícita. O uso não autorizado pode acarretar sérias consequências legais.

---

## 🤝 Contribuição
Contribuições são bem-vindas! Para contribuir:

1. Fork este repositório.
2. Crie uma nova branch:

    ```
    git checkout -b minha-contribuicao
    ```

3. Faça suas alterações e commite:

    ```
    git commit -m "Minha contribuição"
    ```

4. Abra um Pull Request.

---

## 📜 Licença
Este projeto está licenciado sob a **MIT License** – veja o arquivo [LICENSE](LICENSE) para mais detalhes.

Nota: Este script foi desenvolvido exclusivamente para fins educacionais e de teste na área de Segurança da Informação. Qualquer uso indevido é de inteira responsabilidade do usuário.

📌 Desenvolvido com ❤️ por Alexandre Santos
