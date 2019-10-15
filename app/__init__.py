from flask import Flask, request, render_template, redirect, send_file
import pafy
import urllib.request
import urllib.parse
import re
import pdb

app = Flask(__name__)

class Playlist():
    def __init__(self, nome, stream_audio, download_audio, stream_video, thumbnail, views, duracao):
        self.nome = nome
        self.stream_audio = stream_audio
        self.download_audio = download_audio
        self.stream_video = stream_video
        self.thumbnail = thumbnail
        self.views = f'Views: {views}'
        self.duracao = f'Duração: {duracao}'


lista_nome = []

def playlists(x):
    lista_nome.clear()
    plurl = x
    playlist = pafy.get_playlist(plurl)
    tamanho = len(playlist['items'])
    for i in range(tamanho):
        musica = Playlist(playlist['items'][i]['pafy'].title,
                          playlist['items'][i]['pafy'].getbestaudio().url,
                          playlist['items'][i]['pafy'].getbestaudio(),
                          playlist['items'][i]['pafy'].getbest().url,
                          playlist['items'][i]['pafy'].bigthumb,
                          playlist['items'][i]['pafy'].viewcount,
                          playlist['items'][i]['pafy'].duration)
        lista_nome.append(musica)

lista_musicas = []

def musicas():
    lista_musicas.clear()
    query_string = urllib.parse.urlencode({"search_query": request.form['pesquisa']})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())[:5]
    lista_resultados = set([f'http://www.youtube.com/watch?v={i}' for i in search_results])

    for link in lista_resultados:
        x = pafy.new(link)
        lista_musicas.append(
            Playlist(
            x.title,
            x.getbestaudio().url,
            x.getbestaudio(),
            x.getbest().url,
            x.bigthumb,
            x.viewcount,
            x.duration
        ))
    lista_resultados.clear()

@app.route('/')
def oi():
    return render_template('home.html')

@app.route('/playlist', methods=['POST', ])
def playlist():
    playlists(request.form['url2'])
    return render_template('playlist.html', titulo='Playlist', musicas=lista_nome)

@app.route('/musica', methods=['POST', ])
def musica():
    musicas()
    return render_template(
        'musica.html',
        titulo='Musica', 
        musicas_simples=lista_musicas,
    )