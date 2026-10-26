# Gerenciador de Arquivos CSV e JSON

## Identificação

- **Aluno:** Everton Felipe Cirqueira Da Silva
- **Instituição:** Centro Universitário UNIBALSAS
- **Curso:** Análise e Desenvolvimento de Sistemas
- **Disciplina:** Algoritmos e Programação Avançada
- **Professor:** Alex
- 

## 1. Descrição do projeto

O Gerenciador de Arquivos CSV e JSON é um projeto desenvolvido em Python para realizar a leitura, a gravação e a conversão de dados entre os formatos CSV e JSON. O sistema também permite atualizar registros e criar cópias de segurança antes de sobrescrever arquivos existentes.

O projeto aplica conceitos de programação modular, manipulação de arquivos, tratamento de exceções e testes automatizados.

## 2. Funcionalidades

- Leitura e exibição de arquivos CSV.
- Leitura e exibição de arquivos JSON.
- Conversão de CSV para JSON.
- Conversão de JSON para CSV.
- Atualização de registros.
- Criação de backups antes de sobrescrever arquivos existentes.
- Tratamento de erros de leitura e gravação.
- Testes automatizados com `unittest`.

## 3. Estrutura do projeto

```text
gerenciador-csv-json/
├── src/
│   ├── arquivos.py
│   ├── backup.py
│   └── main.py
├── dados/
│   ├── produtos.csv
│   └── produtos.json
├── backups/
├── tests/
│   └── test_arquivos.py
├── evidencias/
├── .gitignore
└── README.md
```

## 4. Requisitos

- Python 3 instalado.
- Git, caso seja necessário clonar o repositório.

## 5. Como executar

Abra o terminal na pasta do projeto e execute:

```bash
python src/main.py
```

No menu apresentado, selecione a operação desejada e siga as instruções exibidas pelo programa.

## 6. Como executar os testes

Na pasta principal do projeto, execute:

```bash
python -m unittest discover -s tests -v
```

O comando executa os testes automatizados disponíveis na pasta `tests`.

## 7. Arquivos e backups

Os arquivos de exemplo ficam na pasta `dados/`. Antes de sobrescrever um arquivo existente, o sistema cria uma cópia de segurança na pasta `backups/`.

Os backups possuem extensão `.bak` e são ignorados pelo Git para evitar o envio de cópias de segurança desnecessárias ao repositório.

## 8. Tratamento de erros

O sistema prevê situações como arquivos inexistentes, falta de permissão, problemas de codificação e conteúdo JSON inválido. Quando ocorre um erro previsto, o programa apresenta uma mensagem explicativa.

## 9. Tecnologias utilizadas

- Python 3
- Módulos `csv`, `json`, `pathlib`, `shutil` e `unittest`
- Git e GitHub

## 10. Autor

**Everton Felipe Cirqueira Da Silva**

Projeto acadêmico desenvolvido individualmente para a disciplina de Algoritmos e Programação Avançada do Centro Universitário UNIBALSAS.
