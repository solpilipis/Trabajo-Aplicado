import pandas as pd  
import streamlit as st

@st.cache_data  
def cargar_datos(ruta_csv):
    df = pd.read_csv(ruta_csv)
    for col in ['Universidad', 'Título', 'Gestion', 'RIASEC']:
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
    """
    
    provincia = input("Ingrese la provincia de interés: ").strip()

    tipo_gestion = input(
        "Ingrese el tipo de universidad (Pública/Privada): "
    ).strip()

    tipo_titulo = input(
        "Ingrese el tipo de título: "
    ).strip()

    duracion_max = int(
        input("Ingrese la duración máxima deseada (en años): ")
    )

    condicion_provincia = (
        df_carreras["Provincia"].str.lower()
        == provincia.lower()
    )

    condicion_gestion = (
        df_carreras["Tipo_Gestion"].str.lower()
        == tipo_gestion.lower()
    )

    condicion_titulo = (
        df_carreras["Tipo"].str.lower()
        == tipo_titulo.lower()
    )

    condicion_duracion = (
        df_carreras["Duracion"]
        <= duracion_max
    )

    df_filtrado = df_carreras[condicion_provincia & condicion_gestion & condicion_titulo & condicion_duracion]

    return df_filtrado

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
        
        score = 0 
        
        for i in range(6): 
        
            if codigo_usuario[i] == codigo[i]: 
            
                score += puntos[i]  
                
        if score > mejor_score: 
            
            mejor_score = score
            
    return mejor_score  
    


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
    for i in range (6): #ciclo por 6 porq son las siglas RIASEC
        valor_mayor = -1 #valor incializado 
        letra = ""
        diccio = datos_dic.copy()
        codigo_usuario = ""
        
        for clave, valor in diccio.items():
            if valor > valor_mayor :
                valor_mayor = valor 
                letra = clave 
                
        codigo_usuario += letra #le sumo al str la letra mayor 
        
        diccio.pop(letra) #elimino la letra que ya use 
        
    return codigo_usuario 
    
def generar_ranking(codigo_usuario, df_filtrado):  
    
    ''' 
    Genera un ranking de las 5 carreras con mayor puntaje de similitud con el perfil RIASEC 
    del usuario. 
    
    Parameters 
    ---------- 
    
    Returns
    -------
    ''' 
    df_ranking = df_filtrado.copy()

    df_ranking["Score"] = 0

    for i in df_ranking.index: 
        
       codigos_carrera = df_ranking.loc[i, "RIASEC_Codes"]

       score = calcular_score(codigo_usuario, codigos_carrera) 
       
       df_ranking.loc[i, "Score"] = score

 

    df_ranking = df_ranking.sort_values(
        
       by="Score",
       ascending=False 
       
      )

 

    df_ranking = df_ranking.drop_duplicates( 
        
      subset="Carrera_Base"
  )



    return df_ranking.head(5)
    

