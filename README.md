# Analisador Léxico Simples em Python

Este projeto implementa um analisador léxico básico em Python. Ele recebe uma string de entrada (representando um código fonte simplificado de uma linguagem hipotética) e a divide em uma lista de tokens e lexemas reconhecidos com base em regras pré-definidas.

Este projeto serve como um exemplo didático dos primeiros passos na construção de um compilador ou interpretador.

## Funcionalidades

* Reconhecimento de palavras-chave específicas: `while`, `var`, `to`, `then`, `string`, `real`, `read`, `program`, `inicio`, `fim`.
* Reconhecimento de símbolos: `{`, `}`, `;`.
* Reconhecimento de literais string delimitados por aspas duplas (`"`).
* Ignora espaços em branco fora de strings.
* Gera uma lista de tokens (representados por códigos numéricos) e os lexemas correspondentes.
* Indica a linha onde cada token foi encontrado (atualmente fixo em Linha 1, pois a entrada é uma única string).

## Pré-requisitos

Antes de começar, garanta que você tem instalado:

* [Python](https://www.python.org/downloads/) (versão 3.x recomendada)
* [Git](https://git-scm.com/downloads/)

## Instalação e Configuração

Siga estes passos para configurar o ambiente de desenvolvimento:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/GabrielAtanasio/analys-system.git
    ```

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd analys-system
    ```

3.  **Crie um ambiente virtual:**
    ```bash
    python -m venv venv
    ```

4.  **Ative o ambiente virtual:**
    * **Linux/macOS (bash/zsh):**
        ```bash
        source venv/bin/activate
        ```
    * **Windows (Prompt de Comando):**
        ```bash
        venv\Scripts\activate.bat
        ```
    * **Windows (PowerShell):**
        ```bash
        venv\Scripts\Activate.ps1
        ```
    * **Windows (Git Bash):**
        ```bash
        source venv/Scripts/activate
        ```
    _Seu prompt de comando deve mudar para indicar que o ambiente `(venv)` está ativo._

5.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
6.  * **Desativar o Ambiente**
    ```bash
    deactivate
    ```

## Uso

Com o ambiente virtual ativado, você pode executar o analisador léxico.

1.  **Entrada:** Atualmente, a string a ser analisada está definida diretamente no código, na variável `palavra` dentro do arquivo `analisador_lexico.py`.
    ```python
    # Exemplo no código:
    palavra = 'void main {inicio ; "fim" }'
    ```
    _Você pode modificar esta linha para testar diferentes entradas._

2.  **Execução:**
    ```bash
    python analisador_lexico.py
    ```

3.  **Saída:** O script imprimirá no console a lista de tokens reconhecidos, seus lexemas correspondentes e a linha (fixa em 1). Para a entrada de exemplo `'void main {inicio ; "fim" }'`, a saída será:

    ```
    Token: 39 - Lexema: { - Linha: 1
    Token: 15 - Lexema: inicio - Linha: 1
    Token: 40 - Lexema: ; - Linha: 1
    Token: 5 - Lexema: "fim" - Linha: 1
    Token: 38 - Lexema: } - Linha: 1
    ```
    _Nota: As palavras `void` e `main` na entrada de exemplo não possuem regras de tokenização definidas no script atual e são ignoradas na saída._

## Tecnologias Utilizadas

* [Python 3](https://www.python.org/)
* [NumPy](https://numpy.org/) - Utilizado para converter a lista final de tokens (embora não seja estritamente necessário para a lógica principal de tokenização mostrada).

## Próximos Passos Possíveis

* Ler a entrada a partir de um arquivo de texto.
* Implementar o reconhecimento de identificadores (nomes de variáveis).
* Adicionar reconhecimento de números (inteiros, reais).
* Implementar tratamento de erros léxicos.
* Adicionar mais palavras-chave e operadores.
* Contabilizar corretamente o número das linhas.

---

_Este README foi gerado para auxiliar na documentação do projeto._