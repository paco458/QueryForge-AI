#  QueryForge AI

> Generate • Search • Analyze

**QueryForge AI** es una herramienta de línea de comandos desarrollada en Python que combina **SerpApi**, **OpenAI** y **GPT4All** para automatizar búsquedas avanzadas, generar consultas mediante IA, exportar resultados y descargar recursos encontrados.

---

## Características

- Búsquedas automatizadas mediante SerpApi.
- Generación de consultas de búsqueda a partir de lenguaje natural usando OpenAI o GPT4All.
- Exportación de resultados a JSON.
- Exportación de resultados a HTML.
- Descarga automática de archivos encontrados en los resultados.
- Soporte para múltiples idiomas.
- Ejecución completamente desde terminal.
- Compatible con modelos locales (GPT4All) y modelos en la nube (OpenAI).

---

## Tecnologías aplicadas

- Python 3.11+
- OpenAI API
- GPT4All
- SerpApi
- Requests
- Python Dotenv

---

## Instalación

### Clonar repositorio

```bash
git clone https://github.com/paco458/QueryForge-AI.git

cd QueryForge-AI
```

### Crear entorno virtual

```bash
python -m venv venv

source venv/bin/activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuración inicial

Antes de usar la herramienta debes configurar tus credenciales.

```bash
python ninjadorks.py -c
```

Se solicitará:

```text
API_KEY_SERPAPI
```

Si utilizas OpenAI para generar consultas también se solicitará:

```text
OPENAI_API_KEY
```

Las claves se almacenan automáticamente en el archivo:

```text
.env
```

---

#  Guía de uso

## Realizar una búsqueda

```bash
python ninjadorks.py -q "python programming pdf"
```

Realiza una búsqueda utilizando SerpApi y muestra los resultados encontrados.

---

## Generar una consulta mediante IA

```bash
python ninjadorks.py -gd "Documentos PDF sobre programación en Python"
```

La IA transformará la descripción proporcionada en una consulta optimizada para búsqueda.

---

# Opciones disponibles

| Opción | Descripción |
|----------|----------|
| `-q`, `--query` | Consulta que se enviará al motor de búsqueda. |
| `-c`, `--configure` | Configura o actualiza el archivo `.env`. |
| `--start-page` | Página inicial desde la cual comenzar a obtener resultados. |
| `--pages` | Número total de páginas de resultados a consultar. |
| `--lang` | Idioma de búsqueda. Por defecto: `lang_es`. |
| `--json` | Exporta los resultados obtenidos a un archivo JSON. |
| `--html` | Exporta los resultados obtenidos a un archivo HTML. |
| `--download` | Descarga archivos encontrados según las extensiones indicadas. |
| `-gd`, `--generate-dork` | Genera una consulta de búsqueda a partir de una descripción en lenguaje natural utilizando IA. |

---

# Ejemplos prácticos

## Buscar documentos PDF

```bash
python ninjadorks.py \
-q "python programming filetype:pdf"
```

---

## Buscar múltiples páginas

```bash
python ninjadorks.py \
-q "machine learning" \
--pages 5
```

---

## Exportar resultados a JSON

```bash
python ninjadorks.py \
-q "redes TCP/IP" \
--json resultados.json
```

---

## Exportar resultados a HTML

```bash
python ninjadorks.py \
-q "ciberseguridad" \
--html reporte.html
```

---

## Descargar archivos encontrados

```bash
python ninjadorks.py \
-q "programming pdf" \
--download pdf
```

---

## Generar consulta con IA

```bash
python ninjadorks.py \
-gd "Presentaciones universitarias sobre inteligencia artificial"
```

---

# Estructura del proyecto

```text
QueryForge-AI/
│
├── ai_agent.py
├── file_downloader.py
├── googlearch.py
├── ninjadorks.py
├── resultados.py
├── plantilla.html
├── requirements.txt
├── .env
└── README.md
```

---

# 👨‍💻 Autor

**Salazar Custodio**

Proyecto desarrollado con Python, IA y automatización de búsquedas como parte de mi proceso de aprendizaje en desarrollo de software, inteligencia artificial y automatización.
