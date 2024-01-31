# Importazione delle librerie necessarie
from flask import Flask, request, render_template
from ultralytics import YOLO
import os
import glob
import shutil
import datetime

# Creazione dell'app Flask
app = Flask(__name__)

# Inizializzazione del modello YOLO
model = YOLO("best.pt")

# Lista delle classi per la classificazione
classNames = ['Ceramic', 'Electrolitic', 'IC', 'LED', 'Resistor', 'Transistor']

# Directory dove YOLO salva le immagini elaborate
YOLO_OUTPUT_FOLDER = 'runs/detect'

# Directory di upload dei file
UPLOAD_FILE_PATH = 'static/uploads'

# Directory statica per le risorse
STATIC_FOLDER = 'static'

# Definizione della rotta principale
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'Nessun file selezionato'
        
        if file:
            # Determina il percorso completo del file da salvare
            basepath = os.path.dirname(__file__)
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            filepath = os.path.join(basepath, UPLOAD_FILE_PATH, timestamp+file.filename)
            
            print("**CARTELLA DI UPLOAD**", filepath)
            
            # Salva il file nell'upload folder
            file.save(filepath)

            # Applicare il modello YOLO alle immagini
            results = model.predict(source=filepath, save=True)

            # Trovare l'ultima immagine elaborata da YOLO
            latest_image_path = find_latest_image(os.path.splitext(file.filename)[1])
            latest_image_filename = os.path.basename(latest_image_path)
            print(latest_image_path)

            # Copia l'immagine elaborata nella cartella static
            static_output_folder = os.path.join(basepath, STATIC_FOLDER)
            if not os.path.exists(static_output_folder):
                os.makedirs(static_output_folder)
            static_output_path = os.path.join(static_output_folder, os.path.basename(latest_image_path))
            shutil.copy(latest_image_path, static_output_path)
            
            # Passare l'immagine al template
            return render_template('result.html', output_image=latest_image_filename)

    return render_template('upload.html')

# Definizione della rotta per la galleria di immagini
@app.route('/gallery')
def gallery():
    static_folder = os.path.join(app.root_path, STATIC_FOLDER)
    images = [filename for filename in os.listdir(static_folder) if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG'))]
    return render_template('gallery.html', images=images)

# Funzione per trovare l'ultima immagine elaborata da YOLO
def find_latest_image(extension):
    # Trovare l'ultima sottocartella in YOLO_OUTPUT_FOLDER
    latest_folder = max(glob.glob(os.path.join(YOLO_OUTPUT_FOLDER, 'predict*/')), key=os.path.getmtime)
    
    # Trovare l'ultima immagine in quella cartella
    latest_image = max(glob.glob(os.path.join(latest_folder, f'*{extension}')), key=os.path.getmtime)
    
    #latest_image_filename = os.path.basename(latest_image)
    
    print("**PATH ULTIMA IMMAGINE ELABORATA**",latest_image)
    
    return latest_image

# Esecuzione dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)