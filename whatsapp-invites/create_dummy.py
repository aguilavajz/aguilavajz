import pandas as pd
import os

df = pd.DataFrame({
    'Nombre': ['Ejemplo Tio Juan', 'Ejemplo Prima Ana'],
    'Telefono': ['5512345678', '5587654321']
})

if not os.path.exists("contacts.csv"):
    df.to_csv("contacts.csv", index=False)
    print("contacts.csv created.")
else:
    print("contacts.csv already exists.")
