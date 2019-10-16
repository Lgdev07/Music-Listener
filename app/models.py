

class Playlist():
    def __init__(self, nome, stream_audio, link, stream_video, thumbnail, views, duracao):
        self.nome = nome
        self.stream_audio = stream_audio
        self.link = link
        self.stream_video = stream_video
        self.thumbnail = thumbnail
        self.views = f'Views: {views}'
        self.duracao = f'Duração: {duracao}'

class Music():
    def __init__(self, nome, stream_audio, download_audio, stream_video, thumbnail, views, duracao):
        self.nome = nome
        self.stream_audio = stream_audio
        self.download_audio = download_audio
        self.stream_video = stream_video
        self.thumbnail = thumbnail
        self.views = f'Views: {views}'
        self.duracao = f'Duração: {duracao}'