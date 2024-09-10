# arqiovp EXE "\dist\salvar_videos_youtube.exe"

import yt_dlp as ytdlp
from tkinter import filedialog as fd
from tkinter import messagebox as mbox
import customtkinter as ctk

class VideoDownloaderApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("600x250")
        self.root.title("Vídeo Downloader")
        
        self.title_texto = "Vídeo Downloader"
        self.create_widgets()

    def create_widgets(self):
        # Configuração dos widgets
        self.title_label = ctk.CTkLabel(self.root, bg_color="gray", text=self.title_texto)
        self.title_label.place(relx=0.01, rely=0.01, relwidth=0.98)

        self.url_label = ctk.CTkLabel(self.root, bg_color="gray", text="URL")
        self.url_label.place(relx=0.01, rely=0.2, relwidth=0.1)
        self.url_entry = ctk.CTkEntry(self.root, placeholder_text="url do vídeo")
        self.url_entry.place(relx=0.12, rely=0.2, relwidth=0.86)

        self.destino_label = ctk.CTkLabel(self.root, bg_color="gray", text="Destino")
        self.destino_label.place(relx=0.01, rely=0.4, relwidth=0.1)
        self.destino_entry = ctk.CTkEntry(self.root, placeholder_text="destino do download")
        self.destino_entry.place(relx=0.12, rely=0.4, relwidth=0.65)

        self.selecionar_pasta_btn = ctk.CTkButton(self.root, text="Selecionar pasta", command=self.selecionar_destino)
        self.selecionar_pasta_btn.place(relx=0.78, rely=0.4, relwidth=0.2)

        self.baixar_btn = ctk.CTkButton(self.root, text="Baixar vídeo", command=self.baixar_video)
        self.baixar_btn.place(relx=0.35, rely=0.7, relwidth=0.3)

        self.progress_text = ctk.StringVar()
        self.progress_label = ctk.CTkLabel(self.root, textvariable=self.progress_text, bg_color="gray")
        self.progress_label.place(relx=0.01, rely=0.9, relwidth=0.98)

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            percent = d.get('percent', 0)
            eta = d.get('eta', 0)
            self.progress_text.set(f"Baixando: {percent:.1f}% - ETA: {eta} segundos")
        elif d['status'] == 'finished':
            self.progress_text.set(f"Download concluído!")

    def baixar_video(self, event=None):
        url = self.url_entry.get()
        destino_baixar = self.destino_entry.get()

        if not url or not destino_baixar:
            mbox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        try:
            ydl_opts = {
                'format': 'mp4',
                'outtmpl': f'{destino_baixar}/%(title)s.%(ext)s',
                'progress_hooks': [self.progress_hook],
            }
            with ytdlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            mbox.showinfo("Sucesso", "Vídeo baixado com sucesso!")

        except Exception as e:
            mbox.showerror("Erro", f"Erro ao baixar o vídeo: {str(e)}")

    def selecionar_destino(self):
        pasta_destino = fd.askdirectory(title="Selecione a pasta de destino")
        if pasta_destino:
            self.destino_entry.delete(0, ctk.END)
            self.destino_entry.insert(0, pasta_destino)

    def run(self):
        self.root.mainloop()

# Criação e execução da aplicação
if __name__ == "__main__":
    app = VideoDownloaderApp()
    app.run()
