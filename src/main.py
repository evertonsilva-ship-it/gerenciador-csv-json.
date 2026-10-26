"""Menu de terminal para o gerenciador CSV/JSON."""
from pathlib import Path
from arquivos import (
    ErroPersistencia,
    atualizar_registro,
    converter_csv_para_json,
    converter_json_para_csv,
    ler_csv,
    ler_json,
)

RAIZ = Path(__file__).resolve().parent.parent
DADOS = RAIZ / "dados"
BACKUPS = RAIZ / "backups"


def mostrar_menu() -> None:
    while True:
        print("\n=== Gerenciador de arquivos CSV e JSON ===")
        print("1. Ler e exibir CSV")
        print("2. Converter CSV para JSON")
        print("3. Converter JSON para CSV")
        print("4. Atualizar campo de produto no JSON")
        print("5. Ler e exibir JSON")
        print("0. Sair")
        opcao = input("Escolha uma opção: ").strip()

        try:
            if opcao == "1":
                registros = ler_csv(DADOS / "produtos.csv")
                for registro in registros:
                    print(registro)
                print(f"Total de registros: {len(registros)}")
            elif opcao == "2":
                backup = converter_csv_para_json(
                    DADOS / "produtos.csv", DADOS / "produtos.json", BACKUPS
                )
                print("Conversão CSV → JSON concluída.")
                print(f"Backup criado: {backup}" if backup else "Destino novo; não havia arquivo anterior para copiar.")
            elif opcao == "3":
                backup = converter_json_para_csv(
                    DADOS / "produtos.json", DADOS / "produtos_convertidos.csv", BACKUPS
                )
                print("Conversão JSON → CSV concluída.")
                print(f"Backup criado: {backup}" if backup else "Destino novo; não havia arquivo anterior para copiar.")
            elif opcao == "4":
                identificador = input("Campo identificador (ex.: id): ").strip()
                valor_id = input("Valor do identificador (ex.: 1): ").strip()
                campo = input("Campo a atualizar (ex.: quantidade): ").strip()
                novo_valor = input("Novo valor (será salvo como texto): ").strip()
                backup = atualizar_registro(
                    DADOS / "produtos.json", identificador, valor_id,
                    campo, novo_valor, BACKUPS
                )
                print("Atualização concluída.")
                print(f"Backup criado: {backup}" if backup else "Não havia arquivo anterior para copiar.")
            elif opcao == "5":
                for registro in ler_json(DADOS / "produtos.json"):
                    print(registro)
            elif opcao == "0":
                print("Encerrando.")
                break
            else:
                print("Opção inválida. Escolha uma opção do menu.")
        except ErroPersistencia as erro:
            print(f"Não foi possível concluir a operação: {erro}")
        except PermissionError:
            print("Não foi possível acessar ou gravar o arquivo: permissão negada.")
        except OSError as erro:
            print(f"Erro de entrada/saída: {erro}")


if __name__ == "__main__":
    mostrar_menu()
