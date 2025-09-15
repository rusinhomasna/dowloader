from flask import Flask, request, render_template_string
from yt_dlp import YoutubeDL

app = Flask(__name__)

HTML = """
<form method="POST">
  URL de YouTube: <input type="text" name="url"><br>
  <input type="submit" value="Descargar">
</form>
<p>{{ mensaje }}</p>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    mensaje = ""
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            try:
                ydl_opts = {"format": "bestaudio/best"}
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                mensaje = "✅ Descarga completada"
            except Exception as e:
                mensaje = f"Error: {e}"
        else:
            mensaje = "Por favor pega un link de YouTube"
    return render_template_string(HTML, mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)
