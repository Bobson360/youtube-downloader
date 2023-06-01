import os
from .download import download_video_and_audio_if_not_exists, download_option
from .utils import clean_title
from pytube import YouTube, Playlist

def cli_main():
    PLAYLIST_URL = input("Insira a URL da playlist que deseja baixar e aperte ENTER: ")
    playlist = Playlist(PLAYLIST_URL)

    # TODO Create folder after choose download type
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
        download_video_and_audio_if_not_exists(video, folder_video, folder_audio, download_choice, clean_title)
