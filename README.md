# Gerenciador de arquivos CSV e JSON

## Descrição
Projeto acadêmico em Python (atividade TED 03) para praticar leitura, escrita, conversão e atualização de dados persistidos em arquivos CSV e JSON, com uso de `with open()`, codificação UTF-8, tratamento de exceções de entrada e saída e backup automático antes de sobrescrever arquivos existentes.

## Identificação
- Instituição: Centro Universitário UNIBALSAS
- Curso: Análise e Desenvolvimento de Sistemas
- Disciplina: Algoritmos e Programação Avançada
- Professor: Alex
- Integrantes da dupla:
  - Everton Felipe Cirqueira da Silva
  - NOME COMPLETO DO PARCEIRO DE DUPLA

## Funcionalidades
- Leitura e exibição de arquivos CSV e JSON.
- Conversão de CSV para JSON e de JSON para CSV, sem perda de registros ou de valores (os valores do CSV são mantidos como texto).
- Atualização de um campo de um registro do JSON.
- Backup automático (cópia binária `.bak` com data e hora) do arquivo de destino antes de qualquer gravação sobre um arquivo existente.
- Tratamento de `FileNotFoundError`, `PermissionError`, erros de codificação (`UnicodeDecodeError`), CSV malformado e JSON inválido, com mensagens claras e sem encerrar o programa.
- Testes automatizados com `unittest`.

## Requisitos
- Python 3.11 ou superior.
- Nenhuma biblioteca externa.

## Como executar (Windows, PowerShell)
1. Abra a pasta do projeto no VS Code.
2. Crie e ative o ambiente virtual:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Execute o menu:

   ```powershell
   python src\main.py
   ```

### Menu
| Opção | Ação |
|---|---|
| 1 | Ler e exibir `dados/produtos.csv` |
| 2 | Converter CSV para JSON (`dados/produtos.json`) |
| 3 | Converter JSON para CSV (`dados/produtos_convertidos.csv`) |
| 4 | Atualizar um campo de um produto no JSON (informar campo identificador, valor do identificador, campo a atualizar e novo valor) |
| 5 | Ler e exibir `dados/produtos.json` |
| 0 | Sair |

Exemplo da opção 4: identificador `id`, valor `2`, campo `preco`, novo valor `89.90`.

## Como executar os testes
Na raiz do projeto:

```powershell
python -m unittest discover -s tests -v
```

Os testes usam uma pasta temporária e não alteram os arquivos de `dados/`.

## Como reproduzir o teste de erro
Renomeie temporariamente `dados/produtos.csv` para `dados/produtos_off.csv`, execute o menu e escolha a opção 1. O programa deve exibir "Arquivo CSV não encontrado" e voltar ao menu. Depois, restaure o nome original do arquivo.

## Estrutura do repositório
```
gerenciador-csv-json/
├── src/
│   ├── main.py          # menu de terminal
│   ├── arquivos.py      # leitura, escrita, conversão, atualização e exceções
│   └── backup.py        # criação do backup (.bak)
├── tests/
│   └── test_arquivos.py # testes automatizados
├── dados/               # arquivos CSV e JSON de exemplo
├── backups/             # cópias geradas automaticamente
├── evidencias/          # capturas de tela
├── README.md
└── TED03_Relatorio_Everton.pdf   # relatório técnico
```

## Observações sobre os dados
O módulo `csv` trata todos os valores como texto. A conversão para JSON preserva esses valores como strings, o que evita alterações ou arredondamentos. Ao converter JSON para CSV, os valores são gravados como texto, pois o CSV não armazena tipos como inteiro ou decimal. Na atualização de campo (opção 4), o novo valor também é salvo como texto, sem validação de formato.
