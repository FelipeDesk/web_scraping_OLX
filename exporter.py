"""Geração e formatação da planilha de anúncios."""

from datetime import datetime
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font


CABECALHO = ["Titulo", "Preço", "Localização", "Data Postada", "Link"]
PASTA_RESULTADOS = Path("resultados")


def ajustar_largura_colunas(planilha):
    """Ajusta cada coluna à maior célula preenchida."""
    for coluna in planilha.columns:
        maior_largura = max(
            (len(str(celula.value)) for celula in coluna if celula.value), default=0
        )
        planilha.column_dimensions[coluna[0].column_letter].width = maior_largura + 2


def gerar_planilha(anuncios, nome_arquivo=None):
    """Cria e salva a planilha, retornando o nome do arquivo gerado."""
    workbook = Workbook()
    planilha = workbook.active
    planilha.title = "Anúncios"
    planilha.append(CABECALHO)

    for celula in planilha[1]:
        celula.font = Font(bold=True)
        celula.alignment = Alignment(horizontal="center")

    for anuncio in anuncios:
        planilha.append(
            [
                anuncio["titulo"],
                anuncio["preco"],
                anuncio["localizacao"],
                anuncio["data_postada"],
                anuncio["link"],
            ]
        )

    for linha in planilha.iter_rows(min_row=2):
        for celula in linha:
            celula.alignment = Alignment(horizontal="left")

    ajustar_largura_colunas(planilha)

    if nome_arquivo is None:
        data_atual = datetime.now().strftime("%d-%m-%y")
        nome_arquivo = PASTA_RESULTADOS / f"anuncios {data_atual}.xlsx"
    else:
        nome_arquivo = Path(nome_arquivo)

    nome_arquivo.parent.mkdir(parents=True, exist_ok=True)
    workbook.save(nome_arquivo)
    return str(nome_arquivo)
