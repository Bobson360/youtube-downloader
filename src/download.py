from pytube import YouTube
from moviepy.editor import AudioFileClip
import os

def download_option():
    """Returns user's choice for download (video, audio, or both)."""
    print("\nSelecione o que você deseja baixar:")
    print("1 - Vídeo")
    print("2 - Áudio")
    print("3 - Ambos (vídeo e áudio)")
    while True:
        try:
            option = int(input("Digite sua opção (1, 2 ou 3): "))
            if option in [1, 2, 3]:
                return option
            else:
                print("Opção inválida. Por favor, tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def download_video_and_audio_if_not_exists(video, folder_video, folder_audio, option, clean_title):
    """Verifica se o video/audio já foi baixado. Se não, baixa o video e/ou o áudio, conforme a opção."""
    video_stream = video.streams.get_highest_resolution()
    audio_stream = video.streams.get_audio_only()

    filename_video = clean_title(video.title) + '.mp4'
    filename_audio = clean_title(video.title) + '.mp3'
    file_path_video = os.path.join(folder_video, filename_video)
    file_path_audio = os.path.join(folder_audio, filename_audio)

    if option in [1, 3]:  # download video
        if not os.path.isfile(file_path_video):
            print(f"Baixando vídeo: {filename_video}")
            video_stream.download(folder_video)
        else:
            print(f"Vídeo já existe no diretório: {filename_video}")

    if option in [2, 3]:  # download audio
        if not os.path.isfile(file_path_audio):
            print(f"Baixando áudio: {filename_audio}")
            audio_stream.download(folder_audio, filename=clean_title(video.title) + '.mp4')
            # Convert the audio file to mp3
            audio = AudioFileClip(os.path.join(folder_audio, clean_title(video.title) + '.mp4'))
            audio.write_audiofile(os.path.join(folder_audio, clean_title(video.title) + '.mp3'))
            os.remove(os.path.join(folder_audio, clean_title(video.title) + '.mp4'))  # remove the original audio file
        else:
            print(f"Áudio já existe no diretório: {filename_audio}")
