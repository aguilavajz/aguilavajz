import pandas as pd
import os

df = pd.DataFrame({
    'Nombre': ['Ejemplo Tio Juan', 'Ejemplo Prima Ana'],
    'Telefono': ['5512345678', '5587654321']
})

if not os.path.exists("contacts.example.csv"):
    df.to_csv("contacts.example.csv", index=False)
    print("contacts.example.csv created.")
else:
    print("contacts.example.csv already exists.")
