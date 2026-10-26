"""Testes automatizados básicos do módulo de persistência."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from arquivos import (  # noqa: E402
    ErroPersistencia,
    atualizar_registro,
    converter_csv_para_json,
    converter_json_para_csv,
    ler_csv,
    ler_json,
)


class TestPersistencia(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.raiz = Path(self.temp.name)
        self.dados = self.raiz / "dados"
        self.backups = self.raiz / "backups"
        self.dados.mkdir()
        self.csv = self.dados / "produtos.csv"
        self.json = self.dados / "produtos.json"
        with self.csv.open("w", encoding="utf-8", newline="") as arquivo:
            arquivo.write(
                "id,nome,categoria,preco,quantidade\n"
                "1,Café especial,Bebidas,25.90,12\n"
                "2,Creatina,Suplementos,89.90,7\n"
            )

    def tearDown(self):
        self.temp.cleanup()

    def test_leitura_csv_preserva_acentos(self):
        registros = ler_csv(self.csv)
        self.assertEqual(registros[0]["nome"], "Café especial")
        self.assertEqual(len(registros), 2)

    def test_csv_para_json(self):
        converter_csv_para_json(self.csv, self.json, self.backups)
        dados = ler_json(self.json)
        self.assertEqual(dados[1]["nome"], "Creatina")
        self.assertEqual(len(dados), 2)

    def test_json_para_csv(self):
        with self.json.open("w", encoding="utf-8") as arquivo:
            json.dump([{"id": 1, "nome": "Pão de queijo"}], arquivo, ensure_ascii=False)
        destino = self.dados / "resultado.csv"
        converter_json_para_csv(self.json, destino, self.backups)
        self.assertEqual(ler_csv(destino)[0]["nome"], "Pão de queijo")

    def test_backup_antes_de_sobrescrever_destino(self):
        with self.json.open("w", encoding="utf-8") as arquivo:
            arquivo.write('[{"versao": "antiga"}]')
        converter_csv_para_json(self.csv, self.json, self.backups)
        backups = list(self.backups.glob("*.bak"))
        self.assertEqual(len(backups), 1)
        with backups[0].open("r", encoding="utf-8") as arquivo:
            conteudo_backup = arquivo.read()
        with self.json.open("r", encoding="utf-8") as arquivo:
            conteudo_atual = arquivo.read()
        self.assertIn("antiga", conteudo_backup)
        self.assertNotIn("antiga", conteudo_atual)

    def test_arquivo_inexistente(self):
        with self.assertRaises(ErroPersistencia):
            ler_csv(self.dados / "nao_existe.csv")

    def test_atualizacao_cria_backup(self):
        converter_csv_para_json(self.csv, self.json, self.backups)
        atualizar_registro(self.json, "id", "1", "quantidade", "20", self.backups)
        self.assertEqual(ler_json(self.json)[0]["quantidade"], "20")
        self.assertTrue(list(self.backups.glob("*.bak")))

    def test_json_invalido(self):
        with self.json.open("w", encoding="utf-8") as arquivo:
            arquivo.write("{nao é JSON}")
        with self.assertRaises(ErroPersistencia):
            ler_json(self.json)


if __name__ == "__main__":
    unittest.main(verbosity=2)
