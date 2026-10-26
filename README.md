# Gerenciador de arquivos CSV e JSON

## Objetivo
Projeto acadêmico em Python para praticar leitura, escrita, conversão e atualização de dados persistidos em CSV e JSON, com uso de `with open()`, UTF-8, tratamento de exceções e backup antes de sobrescrever arquivos existentes.

## Autor
- Nome completo: **PREENCHER COM SEU NOME**
- Instituição: **PREENCHER**
- Curso: **PREENCHER**
- Disciplina: **PREENCHER**

> A atividade foi proposta para dupla. Confirme com o professor se a entrega individual está autorizada e siga a orientação recebida.

## Funcionalidades
- Leitura de CSV e JSON.
- Conversão CSV → JSON e JSON → CSV.
- Atualização de campo de um registro JSON.
- Backup binário do arquivo de destino antes de sobrescrevê-lo.
- Tratamento de erros comuns de leitura, codificação e formato.
- Testes automatizados com `unittest`.

## Requisitos
- Python 3.11 ou superior.
- Não são necessárias bibliotecas externas.

## Como executar no Windows (PowerShell)
1. Abra esta pasta no VS Code.
2. Crie e ative o ambiente virtual:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Execute o menu:

   ```powershell
   python src\main.py
   ```

## Como executar os testes
Na raiz do projeto, execute:

```powershell
python -m unittest discover -s tests -v
```

## Estrutura
- `src/`: código da aplicação.
- `dados/`: arquivos de exemplo.
- `backups/`: cópias criadas durante as operações (arquivos gerados não devem ser versionados por padrão em projetos reais).
- `tests/`: testes automatizados.
- `evidencias/`: local sugerido para guardar capturas reais da execução.

## Observações sobre os dados
Os valores lidos de CSV são textos, comportamento padrão de `csv.DictReader`. A conversão para JSON preserva esses valores como strings. Ao converter JSON para CSV, os valores são serializados em texto; CSV não armazena tipos como inteiro, decimal ou booleano de forma nativa.

## Checklist antes da entrega
- [ ] Preencher os dados de identificação.
- [ ] Executar os testes e guardar os resultados reais.
- [ ] Testar as opções do menu.
- [ ] Capturar evidências reais para o relatório.
- [ ] Conferir o relatório PDF e as instruções do professor.
- [ ] Confirmar se a entrega individual foi autorizada.
- [ ] Publicar o repositório e testar o link em uma janela anônima.
