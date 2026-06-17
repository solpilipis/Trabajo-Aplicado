import pandas as pd  
import streamlit as st

@st.cache_data  #Carga el archivo CSV y guarda la tabla en la memoria caché de Streamlit para que la página no tenga que releer el archivo del disco cada vez que el usuario mueve un slider o interactúa con la web.
def cargar_datos(ruta_csv):
    """

    Parameters
    ----------
    ruta_csv : scr
        La ruta del archivo con la informacion de todas las carreras y el restluado RIASEC

    Returns
    -------
    df : pandas.Dataframe
        Devuelve ua tabla de panda con toda la informacion del archivo ruta_csv

    """
    df = pd.read_csv(ruta_csv)
    for col in ['Universidad', 'Facultad', 'Título', 'Tipo', 'Duración', 'Tipo_Gestion', 'RIASEC_Codes', 'Disciplina_Principal', 'Provincia']:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()
    return df

def test_riasec(ruta):
    """
    Le hace el test RIASEC al usuario y devuelve los resultados.

    Parameters
    ----------
    ruta : string
    Ruta del excel que tiene las preguntas del test.

    Returns
    -------
    resultados : dict
    Diccionario cuyas claves son las letras de RIASEC y cuyos valroes son la suma de las respuestas del usuario para cada letra.

    """
    df = pd.read_excel(ruta)
    df['Dimensión RIASEC'] = df['Dimensión RIASEC'].str[0]
    
    resultados = {"R": 0, "I": 0, "A": 0, "S": 0, "E": 0, "C": 0}
    
    print("Test RIASEC")
    
    print("INSTRUCCIONES")
    
    print("Califica qué tanto disfrutarías hacer cada actividad.")
    print("⚠️ Reglas antes de responder:")
    print("  1. Ignora el sueldo: no pienses si paga bien o mal.")
    print("  2. Ignora tus estudios: no importa si aún no sabes hacerlo.")
    
    print("Escala:")
    print("  [ 1 ] = Me disgusta mucho")
    print("  [ 2 ] = Me disgusta")
    print("  [ 3 ] = Neutral")
    print("  [ 4 ] = Me gusta")
    print("  [ 5 ] = Me gusta mucho")
    
    for indice, fila in df.iterrows():
        pregunta = fila['Texto de la Pregunta (¿Qué tanto te gustaría...)']
        dimension = fila['Dimensión RIASEC']
        while True:
            try:
                respuesta = int(input(f"{pregunta}: "))
               
                if respuesta < 1 or respuesta > 5:
                    print("El valor debe ser entre 1 y 5.")
                    
                else:
                    resultados[dimension] += respuesta
                    break
                    
            except ValueError:
                print("La respuesta debe ser un número.")
    
    return resultados


def filtrar_carreras(df_carreras):
    """
    Pide al usuario una provincia y un tipo de gestión (Pública/Privada),
    filtra el DataFrame recibido y devuelve solo las filas que coinciden.

    Parametros
    -------------
    df_carreras : DataFrame
        DataFrame con la informacion a filtrar de las carreras

    Returns
    -------------
    df_filtrado : DataFrame
        Dataframe nuevo y mas chico que contiene unicamente la informacion que cumplen las dos condiciones que ingreso el usuario
        
    """
    #filtro provincia 
    
    while True:
 
        provincia = input("Ingrese la provincia de interés: ").strip().lower()
 
        condicion_provincia = (df_carreras["Provincia"].str.lower().str.contains(provincia))
 
        if condicion_provincia.any(): 
            
            break 
        
        print("Error: La provincia ingresada no es válida.") 
        
    #filtro gestión

    while True:
 
        tipo_gestion = input("Ingrese el tipo de universidad (Pública/Privada): ").strip().lower()
 
        if tipo_gestion == "publica":
            tipo_gestion = "pública"
 
        if tipo_gestion in list(df_carreras["Tipo_Gestion"].str.lower()): 
            
            break
 
        print("Error: Debe ingresar Pública o Privada.") 
        
    #filtro tipo de título

    while True:
 
        tipo_titulo = input("Ingrese el tipo de título que busca (Grado/Título Intermedio/Otro): ").strip().lower()
 
        if tipo_titulo == "titulo intermedio":
            tipo_titulo = "título intermedio"
 
        if tipo_titulo in ("grado", "título intermedio", "otro"): 
            
            break
 
        print("Error: Debe ingresar Grado, Título Intermedio u Otro.")
 
    if tipo_titulo == "grado":
 
        condicion_titulo = (df_carreras["Tipo"].str.lower() == "grado") 
 
    elif tipo_titulo == "título intermedio":
 
        condicion_titulo = (df_carreras["Tipo"].str.lower() == "título intermedio") 
        
    else:
 
        condicion_titulo = ((df_carreras["Tipo"].str.lower() != "grado") & (df_carreras["Tipo"].str.lower() != "título intermedio"))

    #filtro duración máxima
    
    while True:
 
        entrada_duracion = input("Ingrese la duración máxima deseada (en años): ").strip()
 
        try: 
            
            duracion_max = float(entrada_duracion) 
            
            break 
        
        except ValueError: 
            
            print("Error: La duración debe ser un número.") 
    
    duraciones = df_carreras["Duración"].str.extract(r'(\d+(?:\.\d+)?)')[0].astype(float) 
    
    # el extract hace que solo se quede con el numero, sacando la plabra "año" o "año" y todo el texto que pueda haber.

    condicion_gestion = (df_carreras["Tipo_Gestion"].str.lower() == tipo_gestion.lower())
 
    condicion_duracion = (duraciones <= duracion_max)
 
    df_filtrado = df_carreras[condicion_provincia & condicion_gestion & condicion_titulo & condicion_duracion]
 
    return df_filtrado 

def generar_codigo_riasec(datos_dic):
    """ 
    devuelve un codigo de 6 letras de las diferentes combinaciones RIASEC en base a
    los puntajes objetidos 
    
    parametros
    ----------
    datos_dic : dic
        diccionario con las letras RIASEC como clave y el puntaje de cada una como valor 
        
    reeturns
    ---------
    codigo_usuario: str 
        combinación de las letras RIASEC en base a sus puntajes ordenadas de mayor a menor 
    
    """    
    diccio = datos_dic.copy()
    
    codigo_usuario = ""
    
    
    for i in range (6): #ciclo por 6 porq son las siglas RIASEC
    
        valor_mayor = -1 #valor incializado 
        
        letra = ""
        
        for clave, valor in diccio.items():
            
            if valor > valor_mayor :
                
                valor_mayor = valor 
                
                letra = clave 
                
        codigo_usuario += letra #le sumo al str la letra mayor 
        
        diccio.pop(letra) #elimino la letra que ya use 
        
    return codigo_usuario  

def calcular_score(codigo_usuario, codigos_carrera):    
    
    '''  
    Calcula el mejor puntaje de similitud entre el código RIASEC del usuario y los distintos códigos
    RIASEC asociados a una carrera. 
    
    Parameters
    ---------- 
    codigo_usuario : str. Código RIASEC de 6 caracteres asociado al usuario según sus respuestas 
                    al cuestionario 
                    
    codigos_carrera : str. Perfiles RIASEC asociados a la carrera en el dataframe. 
    
    Returns 
    ------- 
    mejor_score : int. Mejor puntaje de similitud obtenido entre todos los perfiles RIASEC de la carrera. 
    '''
    
    mejor_score = 0 
    
    puntos = [6, 5, 4, 3, 2 ,1] 
    
    codigos = codigos_carrera.split("|") 
     
    for codigo in codigos: 
        
        codigo = codigo.strip() 
        
        if len(codigo) != 6: 
            
            continue 
        
        score = 0 
        
        for i in range(6): 
        
            if codigo_usuario[i] == codigo[i]: 
            
                score += puntos[i]  
                
        if score > mejor_score: 
            
            mejor_score = score
            
    return mejor_score  

    
def generar_ranking(codigo_usuario, df_filtrado):  
    
    ''' 
    Genera un ranking de las 5 carreras con mayor puntaje de similitud con el perfil RIASEC 
    del usuario. 
    
    Parameters 
    ---------- 
    codigo_usuario: str. Código RIASEC de 6 caracteres asociado al usuario según sus respuestas 
                    al cuestionario 
    Returns
    ------- 
    df_filtrado: dataframe filtrado según las preferencias del usuario elegidas en filtrar_carreras()
    ''' 
    df_ranking = df_filtrado.copy()

    df_ranking["Score"] = 0

    for i in df_ranking.index:

       codigos_carrera = df_ranking.loc[i, "RIASEC_Codes"]

       score = calcular_score(codigo_usuario, codigos_carrera)

       df_ranking.loc[i, "Score"] = score

    df_ranking = df_ranking.sort_values(by="Score", ascending=False)

    df_ranking = df_ranking.drop_duplicates(subset="Carrera_Base")

    return df_ranking.head(5)

