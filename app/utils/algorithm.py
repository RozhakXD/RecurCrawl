import matplotlib.pyplot as plt
import matplotlib
import json
import os
import time
import pandas as pd
matplotlib.use('Agg')

def plot_waktu_perbandingan(data: list, ukuran_dataset: list) -> tuple:
    sorted_data = sorted(data, key=lambda x: x["create_at"], reverse=True)
    hasil = ukur_waktu(data=sorted_data, ukuran=ukuran_dataset)

    ukuran = [item["size"] for item in hasil]
    waktu_iteratif = [item["iterative_time"] for item in hasil]
    waktu_rekursif = [item["recursive_time"] for item in hasil]

    plt.figure(figsize=(10, 6))
    plt.plot(ukuran, waktu_iteratif, label="Iterative")
    plt.plot(ukuran, waktu_rekursif, label="Recursive")
    plt.xlabel("Ukuran Data")
    plt.ylabel("Waktu (s)")
    plt.title("Perbandingan Waktu Iteratif dan Rekursif")
    plt.legend()
    plt.grid(True)

    diagram_dir = os.path.join(os.path.dirname(__file__), '..', 'static', 'images')
    diagram_path = os.path.join(diagram_dir, 'diagram.png')
    plt.savefig(diagram_path)
    plt.close()

    data = {
        "Ukuran Data": ukuran,
        "Iterative Time": waktu_iteratif,
        "Recursive Time": waktu_rekursif
    }
    df = pd.DataFrame(data)
    fig, ax = plt.subplots(figsize=(len(df.columns) * 2, len(df) * 0.5))
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

    tabel_path = os.path.join(diagram_dir, 'tabel.png')
    plt.savefig(tabel_path, bbox_inches='tight')
    plt.close()

    return (
        '/static/images/diagram.png',
        '/static/images/tabel.png'
    )

def ukur_waktu(data: list, ukuran: list) -> list:
    hasil = []
    for ukuran_data in ukuran:
        sampel_data = data[:ukuran_data]

        waktu_mulai = time.time()
        iteratif(sampel_data=sampel_data)
        waktu_selesai = time.time()
        waktu_iteratif = waktu_selesai - waktu_mulai

        waktu_mulai = time.time()
        for postingan in sampel_data:
            rekursif(postingan=postingan)
        waktu_selesai = time.time()
        waktu_rekursif = waktu_selesai - waktu_mulai

        hasil.append(
            {
                "size": ukuran_data,
                "iterative_time": waktu_iteratif,
                "recursive_time": waktu_rekursif
            }
        )
    from rich.console import Console
    from rich.table import Table

    console = Console()
    table = Table(title="Perbandingan Waktu Iteratif dan Rekursif")
    table.add_column("Ukuran Data", style="cyan", no_wrap=True)
    table.add_column("Iterative Time", style="magenta")
    table.add_column("Recursive Time", style="green")
    for item in hasil:
        table.add_row(
            str(item["size"]),
            str(item["iterative_time"]),
            str(item["recursive_time"])
        )
    console.print(table)

    return hasil

def rekursif(postingan: dict) -> dict:
    hasil = {
        "username": postingan["username"],
        "post_link": postingan["post_link"],
        "id_post": postingan["id_post"],
        "create_at": postingan["create_at"],
        "like_count": postingan["like_count"],
        "reply_count": postingan["reply_count"],
        "replies": []
    }
    def ambil_balasan(balasan):
        for balas in balasan:
            hasil["replies"].append(
                {
                    "username": balas["username"],
                    "reply_text": balas["reply_text"]
                }
            )

    ambil_balasan(postingan["reply"])
    return hasil

def iteratif(sampel_data: list) -> list:
    hasil = []
    for postingan in sampel_data:
        data_postingan = {
            "username": postingan["username"],
            "post_link": postingan["post_link"],
            "id_post": postingan["id_post"],
            "create_at": postingan["create_at"],
            "like_count": postingan["like_count"],
            "reply_count": postingan["reply_count"],
            "replies": []
        }
        for balas in postingan["reply"]:
            data_postingan["replies"].append(
                {
                    "username": balas["username"],
                    "reply_text": balas["reply_text"]
                }
            )
        hasil.append(data_postingan)
    return hasil

def baca_json(file) -> list:
    json_data = json.load(file)
    return json_data