# Synthwave 🎶

**Synthwave** es una herramienta de línea de comandos (CLI) para:
- Descargar compilaciones desde YouTube.
- Dividir archivos de audio en pistas según un tracklist.
- Etiquetar automáticamente con metadatos (álbum, artista, año, género, portada).
- Normalizar portadas a proporción 1:1.
- Limpiar directorios de descarga.
- Verificar dependencias externas como `ffmpeg` y `yt-dlp`.

---

## 🚀 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/gabrielbaute/synthwave.git
cd synthwave
```

### 2. Instalar dependencias con Poetry
```bash
poetry install
```

> Alternativamente, puedes usar `pip install -r requirements.txt`.

### 3. Dependencias externas
Synthwave requiere que tengas instalados:
- **FFmpeg** → para conversión y división de audio.
- **yt-dlp** → para descargar desde YouTube.

Verifica dependencias con:
```bash
synth check
```

Ejemplo de salida:
```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                   Dependency Check                            ┃
┡━━━━━━━━━━━━━━━┯━━━━━━━━━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│   Dependency  │    Status     │          Description           │
├───────────────┼───────────────┼───────────────────────────────┤
│      ffmpeg   │ ✓ Installed   │ Required for audio conversion │
│      yt-dlp   │ ✓ Installed   │ Required for downloading      │
└───────────────┴───────────────┴───────────────────────────────┘
```

---

## 🛠️ Uso

### Mostrar ayuda
```bash
synth -h
```

### 📂 Comandos disponibles

#### 1. `split`
Divide un archivo de audio en pistas según un tracklist.

```bash
synth split tracklist.txt full_audio.mp3 \
  --output tracks \
  --album "Synthwave Compilation" \
  --artist "Various Artists" \
  --year 2025 \
  --genre "Synthwave" \
  --cover cover.jpg
```

#### 2. `download`
Descarga audio desde YouTube y normaliza la portada.

```bash
synth download "https://www.youtube.com/watch?v=XXXX" \
  --format mp3 \
  --output downloads
```

#### 3. `clean`
Limpia el directorio de descargas.

```bash
# Elimina miniaturas y archivos temporales
synth clean --output downloads

# Elimina todo el directorio y lo recrea vacío
synth clean --output downloads --all
```

#### 4. `check`
Verifica dependencias externas necesarias.

```bash
synth check
```

#### 5. `version`
Muestra información de versión y metadatos del proyecto.

```bash
synth version
```

---

## 📝 Licencia

MIT © Gabriel Baute  
Repositorio: [github.com/gabrielbaute/synthwave](https://github.com/gabrielbaute/synthwave)

---