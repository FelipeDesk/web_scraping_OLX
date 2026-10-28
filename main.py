"""Ponto de entrada do coletor de anúncios da OLX."""

from exporter import gerar_planilha
from scraper import coletar_anuncios


def main():
    anuncios = coletar_anuncios()
    nome_arquivo = gerar_planilha(anuncios)
    print(f"✅ Arquivo '{nome_arquivo}' salvo com sucesso!")


if __name__ == "__main__":
    main()
