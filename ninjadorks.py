import os
import sys
import argparse

from dotenv import load_dotenv, set_key

from googlearch import GoogleSearch
from resultados import Resultados
from file_downloader import FileDownloader
from ai_agent import OpenAIGenerator, GPT4AllGenerator, IAAgent


def env_config():
    """Configura la API Key de SerpApi."""

    api_key = input("Introduce tu API KEY de SerpApi: ")

    set_key(".env", "API_KEY_SERPAPI", api_key)

    print("Archivo .env configurado satisfactoriamente.")


def openai_config():
    """Configura la API Key de OpenAI."""

    api_key = input("Introduce la API KEY de OpenAI: ")

    set_key(".env", "OPENAI_API_KEY", api_key)

    print("API Key de OpenAI guardada correctamente.")


def main(
    query,
    configure_env,
    start_page,
    pages,
    lang,
    output_json,
    output_html,
    download,
    gen_dork
):

    if configure_env or not os.path.exists(".env"):
        env_config()
        sys.exit(0)

    load_dotenv()

    serpapi_api_key = os.getenv("API_KEY_SERPAPI")

    # Generación mediante IA
    if gen_dork:

        respuesta_usuario = ""

        while respuesta_usuario.lower() not in ("y", "yes", "n", "no"):
            respuesta_usuario = input(
                "¿Quieres utilizar OpenAI? (yes/no): "
            )

        if respuesta_usuario.lower() in ("y", "yes"):

            if "OPENAI_API_KEY" not in os.environ:
                openai_config()
                load_dotenv()

            generador = OpenAIGenerator()

        else:

            print(
                "Utilizando GPT4All localmente. "
                "Puede tardar varios minutos..."
            )

            generador = GPT4AllGenerator()

        ia_agent = IAAgent(generador)

        resultado = ia_agent.generate_gdork(gen_dork)

        print("\nResultado:")
        print(resultado)

        sys.exit(0)

    # Validación API
    if not serpapi_api_key:
        print(
            "ERROR: No se encontró API_KEY_SERPAPI.\n"
            "Ejecuta el programa con -c para configurarla."
        )
        sys.exit(1)

    # Validación consulta
    if not query:
        print(
            "Indica una consulta con -q.\n"
            "Usa -h para ver la ayuda."
        )
        sys.exit(1)

    # Búsqueda
    gsearch = GoogleSearch(serpapi_api_key)

    resultados = gsearch.search(
        query=query,
        start_page=start_page,
        pages=pages,
        lang=lang,
    )

    rparser = Resultados(resultados)

    # Mostrar resultados
    rparser.mostrar_pantalla()

    # Exportar HTML
    if output_html:
        rparser.exportar_html(output_html)

    # Exportar JSON
    if output_json:
        rparser.exportar_json(output_json)

    # Descargas
    if download:

        file_types = download.split(",")

        urls = [
            resultado["link"]
            for resultado in resultados
            if "link" in resultado
        ]

        fdownloader = FileDownloader("Descargas")

        fdownloader.filtrar_descargar_archivos(
            urls,
            file_types
        )


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Buscador automatizado utilizando SerpApi."
    )

    parser.add_argument(
        "-q",
        "--query",
        type=str,
        help="Consulta a realizar."
    )

    parser.add_argument(
        "-c",
        "--configure",
        action="store_true",
        help="Configurar archivo .env."
    )

    parser.add_argument(
        "--start-page",
        type=int,
        default=1
    )

    parser.add_argument(
        "--pages",
        type=int,
        default=1
    )

    parser.add_argument(
        "--lang",
        type=str,
        default="lang_es"
    )

    parser.add_argument(
        "--json",
        type=str
    )

    parser.add_argument(
        "--html",
        type=str
    )

    parser.add_argument(
        "--download",
        type=str
    )

    parser.add_argument(
        "-gd",
        "--generate-dork",
        type=str,
        help="Genera una consulta de búsqueda avanzada a partir de una descripción."
    )

    args = parser.parse_args()

    main(
        query=args.query,
        configure_env=args.configure,
        start_page=args.start_page,
        pages=args.pages,
        lang=args.lang,
        output_json=args.json,
        output_html=args.html,
        download=args.download,
        gen_dork=args.generate_dork,
    )
