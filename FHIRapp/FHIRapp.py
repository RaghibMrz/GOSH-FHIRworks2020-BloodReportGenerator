import tkinter as tk
import requests
import json
from docGenerator import generateHealthDoc

root = tk.Tk()


# gets patient data and displays relevant buttons and labels on tkinter frame
def printer():
    uid = inp.get()
    try:
        res = requests.get("http://localhost:8000/" + uid)
        if res.status_code == 404:
            print("Error code 404")
            return
        patientData = json.loads(res.text)
        label.config(text="Patient:\n" + patientData['Name'])
        canvas.create_window(120, 220, window=label)
        genButton.config(
            text="Generate Health Document",
            command=lambda: generateHealthDoc(patientData),
            state="normal"
        )
        canvas.create_window(280, 220, window=genButton)
    except (requests.exceptions.InvalidSchema, TypeError) as e:
        genButton.config(
            state="disabled",
        )
        label.config(text="Patient not found!")
        canvas.create_window(120, 220, window=label)


canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()
promptLabel = tk.Label(root, text="Enter the Patient's UUID")
canvas.create_window(200, 80, window=promptLabel)
inp = tk.Entry(root)
canvas.create_window(200, 120, window=inp)
button = tk.Button(text='Enter', command=printer)
canvas.create_window(200, 160, window=button)
label = tk.Label(root, text="")
genButton = tk.Button()
canvas.mainloop()

# Test ID:
# e3d4ce63-c4c0-4dd2-ab9b-6cc3e43f0e25
