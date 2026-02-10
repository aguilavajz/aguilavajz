import pandas as pd
import subprocess
import urllib.parse
import time
import os
import random



# --- CONFIGURACIÓN ---
# Mensaje base. Puedes usar {nombre} para personalizarlo si la columna se llama 'Nombre'.
MENSAJE_BASE = """Hola,

Muy pronto nuestra hija María Inés celebrará sus XV años y nos encantaría que formes parte de este día tan especial. Pronto te haremos llegar la invitación formal con todos los detalles.

Si por alguna razón no podrás acompañarnos, avísanos por favor para tomarlo en cuenta en la organización. 🙏

https://savedate.mx/ev/xvmariaines"""

# Nombre del archivo CSV
ARCHIVO_CSV = "contacts.csv"

# Código de país por defecto (si el número no lo tiene). Ejemplo: 52 para México, 34 España, 1 USA.
CODIGO_PAIS_DEFAULT = "52" 
# ---------------------

def limpiar_telefono(telefono):
    """Limpia el número de teléfono dejando solo dígitos."""
    telefono = str(telefono).split('.')[0] # Quitar decimales si existen
    telefono = "".join(filter(str.isdigit, telefono))
    
    # Si no tiene código de país (asumiendo longitud < 10 es error, 10 es local MX, >10 puede tener pais)
    # Ajusta esta lógica según tu país.
    if len(telefono) == 10:
        telefono = CODIGO_PAIS_DEFAULT + telefono
        
    return telefono

def main():
    print("=== Automatización de Invitaciones WhatsApp (Modo Asistido) ===")
    
    if not os.path.exists(ARCHIVO_CSV):
        print(f"Error: No se encontró el archivo '{ARCHIVO_CSV}'. Asegúrate de crearlo.")
        return

    try:
        # Leer el archivo CSV
        df = pd.read_csv(ARCHIVO_CSV, dtype={'Telefono': str}) # Forzar teléfono como texto
        
        # Validar columnas
        if 'Nombre' not in df.columns or 'Telefono' not in df.columns:
            print("Error: El CSV debe tener las columnas 'Nombre' y 'Telefono'.")
            print(f"Columnas encontradas: {df.columns.tolist()}")
            return

        total = len(df)
        print(f"Se encontraron {total} contactos.")
        print("-" * 50)

        for index, row in df.iterrows():
            nombre = row['Nombre']
            telefono_raw = row['Telefono']
            
            # Validación básica
            if pd.isna(telefono_raw) or pd.isna(nombre):
                print(f"[{index+1}/{total}] Saltando fila vacía.")
                continue

            telefono = limpiar_telefono(telefono_raw)
            
            # Personalizar mensaje
            mensaje = MENSAJE_BASE.format(nombre=nombre)
            mensaje_encoded = urllib.parse.quote(mensaje)
            
            # USO APP DE ESCRITORIO
            url = f"whatsapp://send?phone={telefono}&text={mensaje_encoded}"
            
            print(f"[{index+1}/{total}] Preparando mensaje para: {nombre} ({telefono})")
            print(f"    Mensaje: {mensaje[:50]}...")
            
            # Abrir usando el comando nativo de macOS 'open'
            subprocess.run(["open", url])
            
            # Pausa aleatoria de seguridad
            tiempo_espera = random.randint(5, 20)
            print(f"    Esperando {tiempo_espera} segundos para evitar ban (seguridad)...")
            time.sleep(tiempo_espera)
            
            # Pausa para control manual (opcional)
            # input(">>> Presiona ENTER si ya enviaste (o espera la siguiente)...")
            print("    Continuando...")
            print("-" * 50)

        print("¡Proceso finalizado!")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()
