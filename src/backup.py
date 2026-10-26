"""Funções para criar cópias de segurança de arquivos existentes."""
from datetime import datetime
from pathlib import Path


def criar_backup(caminho: str | Path, pasta_backups: str | Path) -> Path | None:
    """Copia um arquivo existente para a pasta de backups e retorna o caminho.

    Retorna None quando o arquivo original ainda não existe.
    Se a cópia falhar, propaga a exceção para impedir a alteração do original.
    """
    origem = Path(caminho)
    destino_dir = Path(pasta_backups)

    if not origem.exists():
        return None

    destino_dir.mkdir(parents=True, exist_ok=True)
    instante = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    destino = destino_dir / f"{origem.stem}_{instante}{origem.suffix}.bak"

    # O conteúdo é copiado em modo binário para preservar os bytes originais.
    with origem.open("rb") as arquivo_origem:
        conteudo = arquivo_origem.read()

    with destino.open("wb") as arquivo_backup:
        arquivo_backup.write(conteudo)

    return destino
