import logging
import os
from pytube import YouTube, Playlist
from moviepy.editor import AudioFileClip
import re
import pprint

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Create a file handler
handler = logging.FileHandler('app.log')
handler.setLevel(logging.DEBUG)

# Create a logging format
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)


project_info = {
    "author": "Robson Rodrigues",
    "date": "29/05/2023",
    "contact": {
        "email": "bobson278@gmail.com"
    },
    "Links":{
        "github": "https://github.com/Bobson360/youtube-downloader",
        "Linkedin": "https://www.linkedin.com/in/robson-rodrigues-2a973a165/"
    },
    "Description": [
            "Insira uma playlista valida e publica com os vídeos de deseja baixar.",
            "O programa pode criar duas pastas, uma para vídeo e outra para áudio, a playlist",
            "Escolha o que deseja baixar, 1 para vídeo, 2 para audio e 3 para ambos",
            "Caso o item ja exista no diretório video|áudio, não será baixado novamente"
        ]
            
}


pprint.pprint(project_info, sort_dicts=False)
print("\n\n")

def clean_title(title):
    """Removes invalid characters from title to use as filename."""
    return re.sub(r'[\\/*?:"<>|]', "", title)


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


def download_video_and_audio_if_not_exists(video, folder_video, folder_audio, option):
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

def isPlaylist(URL):
    try:
        if URL.find('playlist') > 0:
            return True
        elif URL.find('watch?v') > 0:
            print("Você inseriu o link para um video, no momento a ferramenta ainda não tem o suporte para baixar video individualmente!")
        else:
            raise

    except Exception as e:
        print('\nVocê não inseriu um link invalido.\n'
            + '\nVocê pode inserir dois tipos de link'
            + '\n1º - Link de playlist - Baixa a lista de videos em diretorio de mesmo nome da playlist'
            + '\n2º - Link de video - Baixa o video no diretorio video'
            + '\n\nVerifique seu link e tente novamente.\n')
        logger.exception("Error occurred!")
        user_input = input("Pressione 'c' para tentar novamente ou qualquer outra tecla para encerrar: ")
        if user_input.lower() != 'c':
            exit()
        else:
            init()

def init():
        # PLAYLIST_URL = input("Insira a URL da playlist que deseja baixar e aperte ENTER: ")
    PLAYLIST_URL = input("Insira a URL da playlist que deseja baixar e aperte ENTER: ")
    isPlaylist(PLAYLIST_URL)
    try:
        playlist = Playlist(PLAYLIST_URL)

        # Creates folders with the name of the playlist for video and audio
        folder_video = os.path.join('video', playlist.title)
        folder_audio = os.path.join('audio', playlist.title)

        if not os.path.exists(folder_video):
            os.makedirs(folder_video)
        if not os.path.exists(folder_audio):
            os.makedirs(folder_audio)

        download_choice = download_option()

        for url in playlist.video_urls:
            video = YouTube(url)
            download_video_and_audio_if_not_exists(video, folder_video, folder_audio, download_choice)

        # Log the total downloaded files and total files in directory
        with open('download_log.txt', 'a', encoding='utf-8') as log_file:
            total_files_count_video = len([name for name in os.listdir(folder_video) if os.path.isfile(os.path.join(folder_video, name))])
            total_files_count_audio = len([name for name in os.listdir(folder_audio) if os.path.isfile(os.path.join(folder_audio, name))])
            log_file.write(f'Total files in video directory: {total_files_count_video}\n')
            log_file.write(f'Total files in audio directory: {total_files_count_audio}\n')

    except KeyError as e:
        if 'sidebar' in str(e):
            print('\nOcorreu um erro ao processar a playlist.\n'
                  + '\nParece que a playlist que está tentando baixar não está acessivel.' 
                  + '\nIsso pode ocorrer por dois motivos conhecidos:'
                  + '\n1º - a playlist está com visibilidade particular (mude a visibilidade para pública)'
                  + '\n2º - a playlist não existe.'
                  + '\n\nVerifique e tente novamente.\n')
            logger.exception("Error occurred!")
            user_input = input("Pressione 'c' para tentar novamente ou qualquer outra tecla para encerrar: ")
            if user_input.lower() != 'c':
                exit()
            else:
                init()

    except Exception as e:
        print("falhou")
        logger.exception("Unexpected error occurred!")
        user_input = input("Um erro inesperado ocorreu. Pressione 'c' para continuar ou qualquer outra tecla para encerrar: ")
        if user_input.lower() != 'c':
            exit()

init()