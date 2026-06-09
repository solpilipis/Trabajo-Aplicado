import pandas as pd

def filtrar_carreras(df_carreras):
    """
    Pide al usuario una provincia y un tipo de gestión (Pública/Privada),
    filtra el DataFrame recibido y devuelve solo las filas que coinciden.
    """
    
    # Solicitar inputs al usuario
    provincia = input("Ingrese la provincia de interés: ").strip()
    tipo = input("Ingrese el tipo de universidad (Pública/Privada): ").strip()
    
    # Aplicar mascaras booleanas con pandas
    # Usamos .str.casefold() o .str.lower() para evitar problemas con mayusculas/minusculas
    condicion_provincia = df_carreras['Provincia'].str.lower() == provincia.lower()
    condicion_tipo = df_carreras['Tipo'].str.lower() == tipo.lower()
    
    # Filtrar el DataFrame original
    df_filtrado = df_carreras[condicion_provincia & condicion_tipo]
    
    # Devolver el DataFrame resultante
    return df_filtrado