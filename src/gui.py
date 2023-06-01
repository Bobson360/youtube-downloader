import tkinter as tk
from tkinter import messagebox
from .youtube_downloader import download_playlist

def gui_main():
    def start_download():
        url = url_entry.get()
        option = var.get()
        if url and option:
            try:
                download_playlist(url, option)  # Função a ser implementada
                messagebox.showinfo("Success", "Download completed successfully!")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please fill in all fields!")

    root = tk.Tk()
    root.title("YouTube Playlist Downloader")

    url_label = tk.Label(root, text="Playlist URL:")
    url_label.pack()

    url_entry = tk.Entry(root, width=50)
    url_entry.pack()

    var = tk.IntVar()
    video_radio = tk.Radiobutton(root, text="Video", variable=var, value=1)
    video_radio.pack()

    audio_radio = tk.Radiobutton(root, text="Audio", variable=var, value=2)
    audio_radio.pack()

    both_radio = tk.Radiobutton(root, text="Both", variable=var, value=3)
    both_radio.pack()

    download_button = tk.Button(root, text="Start Download", command=start_download)
    download_button.pack()

    root.mainloop()
