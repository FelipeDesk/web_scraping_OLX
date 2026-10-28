# Web Scraping de Anúncios de Imóveis

## O que o projeto faz

Este projeto utiliza Python e Selenium para acessar páginas de anúncios de imóveis (nesse projeto, foi utilizada a plataforma OLX), extrair informações como título, preço, localização, data de publicação e link, e salvar os resultados em uma planilha Excel (`.xlsx`).

## Tecnologias utilizadas

- **Python 3**
- **Selenium** — automatização do navegador e extração de dados das páginas.
- **openpyxl** — criação e formatação da planilha Excel.
- **Google Chrome** — navegador utilizado pelo Selenium.

## Requisitos

- Python 3 instalado.
- Google Chrome instalado.
- Dependências do projeto instaladas pelo `requirements.txt`.

## Como executar

1. Abra a pasta do projeto no VS Code.
2. Abra o terminal e crie um ambiente virtual:

   ```bash
   python -m venv .venv
   ```

3. Ative o ambiente virtual no Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

4. Instale as dependências:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Execute o programa:

   ```bash
   python main.py
   ```

A planilha gerada será salva na pasta `resultados/`.

## Aviso de uso responsável

Este projeto é destinado ao estudo de automação e processamento de dados. Antes de coletar informações de qualquer site, verifique os termos de uso, as permissões e as regras aplicáveis. Respeite os limites de acesso e a privacidade. Não contorne mecanismos de proteção. Quando a coleta não for autorizada, utilize uma API ou conjunto de dados com permissão para o uso pretendido.
