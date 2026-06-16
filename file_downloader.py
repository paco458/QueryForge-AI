import os
import requests


class FileDownloader:

    def __init__(self, directorio_destino):
        self.directorio = directorio_destino
        self.crear_directorio()

    def crear_directorio(self):
        if not os.path.exists(self.directorio):
            os.makedirs(self.directorio)

    def descargar_archivo(self, url):
        try:
            respuesta = requests.get(url, timeout=20)

            nombre_archivo = url.split("/")[-1]

            if not nombre_archivo:
                nombre_archivo = "archivo_descargado"

            ruta_completa = os.path.join(
                self.directorio,
                nombre_archivo
            )

            with open(ruta_completa, "wb") as archivo:
                archivo.write(respuesta.content)

            print(
                f"Archivo {nombre_archivo} "
                f"descargado en {ruta_completa}"
            )

        except Exception as e:
            print(f"Error al descargar {url}: {e}")

    def filtrar_descargar_archivo(
        self,
        urls,
        tipos_archivos=["all"]
    ):

        if tipos_archivos == ["all"]:
            for url in urls:
                self.descargar_archivo(url)

        else:
            for url in urls:
                if any(
                    url.lower().endswith(f".{tipo.lower()}")
                    for tipo in tipos_archivos
                ):
                    self.descargar_archivo(url)
