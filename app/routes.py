from flask import render_template, request
from app import app
from app.utils import algorithm
import json

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            file = request.files['json_file']
            ukuran_dataset = list(map(int, request.form['dataset_sizes'].split(',')))

            json_data = algorithm.baca_json(file=file)
            diagram_path = algorithm.plot_waktu_perbandingan(data=json_data, ukuran_dataset=ukuran_dataset)

            return render_template('index.html', plot_path=diagram_path)
        except json.decoder.JSONDecodeError:
            return render_template('index.html', error="File JSON tidak valid!")
        except Exception as error:
            return render_template('index.html', error=error)
    else:
        return render_template('index.html')