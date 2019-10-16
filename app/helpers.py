from .models import Playlist, Music
from flask import request
import pafy
import urllib.request
import urllib.parse
import re

def playlists(x):
    lista_nome = []
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
    return lista_nome

def musicas():
    lista_musicas = []
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
            link,
            x.getbest().url,
            x.bigthumb,
            x.viewcount,
            x.duration
        ))
    lista_resultados.clear()
    return lista_musicas
