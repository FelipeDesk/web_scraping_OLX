"""Coleta anúncios de imóveis na OLX."""

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


BASE_URL = "https://www.olx.com.br/imoveis/aluguel/estado-sp?f=p&o={pagina}"
AD_SELECTOR = "//section[contains(@class, 'olx-adcard__horizontal')]"


def extrair_texto(anuncio, xpath):
    """Retorna o texto de um elemento do anúncio ou uma string vazia."""
    try:
        return anuncio.find_element(By.XPATH, xpath).text
    except Exception:
        return ""


def extrair_link(anuncio):
    """Retorna o link do anúncio ou uma string vazia."""
    try:
        return anuncio.find_element(
            By.XPATH, ".//a[contains(@class, 'olx-adcard__link')]"
        ).get_attribute("href")
    except Exception:
        return ""


def extrair_anuncios(anuncios):
    """Converte elementos da página em dicionários com os dados do anúncio."""
    dados = []
    for anuncio in anuncios:
        dados.append(
            {
                "titulo": extrair_texto(
                    anuncio, ".//h2[contains(@class, 'olx-adcard__title')]"
                ),
                "preco": extrair_texto(
                    anuncio, ".//h3[contains(@class, 'olx-adcard__price')]"
                ),
                "localizacao": extrair_texto(
                    anuncio, ".//p[contains(@class, 'olx-adcard__location')]"
                ),
                "data_postada": extrair_texto(
                    anuncio, ".//p[contains(@class, 'olx-adcard__date')]"
                ),
                "link": extrair_link(anuncio),
            }
        )
    return dados


def coletar_anuncios(paginas=4, tempo_espera=10):
    """Abre as páginas da OLX e retorna os anúncios encontrados."""
    driver = webdriver.Chrome()
    anuncios_coletados = []

    try:
        for pagina in range(1, paginas + 1):
            print(f"📄 Coletando página {pagina}...")
            driver.get(BASE_URL.format(pagina=pagina))
            sleep(tempo_espera)

            anuncios = driver.find_elements(By.XPATH, AD_SELECTOR)
            anuncios_coletados.extend(extrair_anuncios(anuncios))
    finally:
        driver.quit()

    return anuncios_coletados
