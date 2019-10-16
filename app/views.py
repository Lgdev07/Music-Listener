from flask import request, render_template, redirect, send_file
from .__init__ import app
from .models import Playlist, Music
from .helpers import playlists, musicas
import pafy
import os

@app.route('/')
def oi():
    return render_template('home.html')

@app.route('/playlist', methods=['POST', ])
def playlist():
    playlists(request.form['url2'])
    return render_template('playlist.html', titulo='Playlist', musicas=lista_nome)

@app.route('/musica', methods=["POST"])
def musica():
    lista_musicas = musicas()
    return render_template(
        'musica.html',
        titulo='Musica', 
        musicas_simples=lista_musicas,
    )

@app.route('/musica/download')
def download_pafy():
    link = request.args.get('link')
    pafy_object = pafy.new(link)

    title = pafy_object.title.replace(' ','_').translate(dict.fromkeys(map(ord, u"()")))
    best_audio = pafy_object.getbestaudio()

    BESTFILE = os.getcwd() + "/" + str(title) + "." + str(best_audio.extension)
    MP3FILE = os.getcwd() + "/" + str(title) + ".mp3"

    best_audio.download(BESTFILE)

    command = "ffmpeg -i "+str(BESTFILE)+" -vn -ab 128k -ar 44100 -y "+str(MP3FILE)
    import subprocess
    subprocess.call(command, shell=True)

    os.remove(BESTFILE)

    return render_template(
        'download.html',
        titulo='Download Musica', 
    )
