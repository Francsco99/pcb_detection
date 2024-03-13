from ultralytics import YOLO

# Inizializzazione del modello YOLO
model = YOLO("best.pt")

# Lista delle classi per la classificazione
classNames = ['Ceramic', 'Electrolitic', 'IC', 'LED', 'Resistor', 'Transistor']

results = model.predict(source="0",show=True)