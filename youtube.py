from pytube import YouTube
from pydub import AudioSegment
import os

def download_youtube_audio(video_url, output_path):
    try:
        # Descargar el video de YouTube
        yt = YouTube(video_url)
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=output_path)

        # Convertir el archivo descargado a MP3
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'

        audio = AudioSegment.from_file(out_file)
        audio.export(new_file, format="mp3")

        # Eliminar el archivo original
        os.remove(out_file)

        print(f"Descarga completada: {new_file}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# URL del video de YouTube
video_url = "https://www.youtube.com/watch?v=eqLBBRTSai4&t=4957s"

# Ruta de salida donde se guardará el archivo MP3
output_path = "."

download_youtube_audio(video_url, output_path)
