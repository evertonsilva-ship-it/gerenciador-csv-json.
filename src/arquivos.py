"""Leitura, escrita e conversão entre CSV e JSON."""
import csv
import json
from pathlib import Path
from typing import Any

from backup import criar_backup


class ErroPersistencia(Exception):
    """Erro controlado para operações de persistência."""


def ler_csv(caminho: str | Path) -> list[dict[str, str]]:
    """Lê um CSV UTF-8 e retorna uma lista de dicionários."""
    caminho = Path(caminho)
    try:
        with caminho.open("r", encoding="utf-8-sig", newline="") as arquivo:
            leitor = csv.DictReader(arquivo)
            if leitor.fieldnames is None:
                raise ErroPersistencia("O CSV está vazio ou não possui cabeçalho.")
            return [dict(registro) for registro in leitor]
    except FileNotFoundError as erro:
        raise ErroPersistencia(f"Arquivo CSV não encontrado: {caminho}") from erro
    except PermissionError as erro:
        raise ErroPersistencia(f"Sem permissão para ler: {caminho}") from erro
    except UnicodeDecodeError as erro:
        raise ErroPersistencia(
            f"Não foi possível decodificar {caminho} como UTF-8."
        ) from erro
    except csv.Error as erro:
        raise ErroPersistencia(f"Erro ao interpretar o CSV: {erro}") from erro


def ler_json(caminho: str | Path) -> list[dict[str, Any]]:
    """Lê um JSON cuja estrutura principal é uma lista de objetos."""
    caminho = Path(caminho)
    try:
        with caminho.open("r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        if not isinstance(dados, list) or any(not isinstance(item, dict) for item in dados):
            raise ErroPersistencia("O JSON deve conter uma lista de objetos.")
        return dados
    except FileNotFoundError as erro:
        raise ErroPersistencia(f"Arquivo JSON não encontrado: {caminho}") from erro
    except PermissionError as erro:
        raise ErroPersistencia(f"Sem permissão para ler: {caminho}") from erro
    except UnicodeDecodeError as erro:
        raise ErroPersistencia(f"Não foi possível decodificar {caminho} como UTF-8.") from erro
    except json.JSONDecodeError as erro:
        raise ErroPersistencia(f"JSON inválido (linha {erro.lineno}, coluna {erro.colno}).") from erro


def _gravar_json(caminho: Path, dados: list[dict[str, Any]], pasta_backups: Path) -> Path | None:
    backup = criar_backup(caminho, pasta_backups)
    with caminho.open("w", encoding="utf-8", newline="") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        arquivo.write("\n")
    return backup


def _gravar_csv(caminho: Path, dados: list[dict[str, Any]], pasta_backups: Path) -> Path | None:
    if not dados:
        raise ErroPersistencia("Não é possível criar CSV sem registros para definir as colunas.")
    campos = list(dados[0].keys())
    if any(list(registro.keys()) != campos for registro in dados):
        raise ErroPersistencia("Os registros do JSON possuem campos diferentes ou em ordem diferente.")
    backup = criar_backup(caminho, pasta_backups)
    with caminho.open("w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos, extrasaction="raise")
        escritor.writeheader()
        escritor.writerows(dados)
    return backup


def converter_csv_para_json(
    origem: str | Path, destino: str | Path, pasta_backups: str | Path
) -> Path | None:
    """Converte CSV para JSON; retorna o backup criado, se havia destino."""
    registros = ler_csv(origem)
    return _gravar_json(Path(destino), registros, Path(pasta_backups))


def converter_json_para_csv(
    origem: str | Path, destino: str | Path, pasta_backups: str | Path
) -> Path | None:
    """Converte JSON para CSV; valores são representados como texto no CSV."""
    registros = ler_json(origem)
    return _gravar_csv(Path(destino), registros, Path(pasta_backups))


def atualizar_registro(
    caminho_json: str | Path,
    identificador: str,
    valor_identificador: str,
    campo: str,
    novo_valor: Any,
    pasta_backups: str | Path,
) -> Path | None:
    """Atualiza um campo do primeiro registro que corresponda ao identificador."""
    caminho = Path(caminho_json)
    registros = ler_json(caminho)
    encontrado = False

    for registro in registros:
        if str(registro.get(identificador)) == valor_identificador:
            if campo not in registro:
                raise ErroPersistencia(f"O campo '{campo}' não existe no registro.")
            registro[campo] = novo_valor
            encontrado = True
            break

    if not encontrado:
        raise ErroPersistencia(
            f"Nenhum registro encontrado com {identificador} = '{valor_identificador}'."
        )

    return _gravar_json(caminho, registros, Path(pasta_backups))
