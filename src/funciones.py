import pandas as pd  

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
    Ruta del csv que tiene las preguntas del test.

    Returns
    -------
    resultados : dict
    Diccionario cuyas claves son las letras de RIASEC y cuyos valroes son la suma de las respuestas del usuario para cada letra.

    """
    df = pd.read_csv(ruta) #Lee el csv y lo guarda en un dataframe.
    df['Dimensión RIASEC'] = df['Dimensión RIASEC'].str[0] #Renombra las dimensiones para que sean tan solo la primera letra (R, I, A, S, E o C)
    
    resultados = {"R": 0, "I": 0, "A": 0, "S": 0, "E": 0, "C": 0}
    
    total_preguntas = len(df)
    numero_pregunta = 1
    
    print("Test RIASEC")
    print()
    print("INSTRUCCIONES") 
    print()
    
    print("Califica qué tanto disfrutarías hacer cada actividad.") 
    print()
    print("⚠️ Reglas antes de responder:") 
    print()
    print("  1. Ignora el sueldo: no pienses si paga bien o mal.")
    print("  2. Ignora tus estudios: no importa si aún no sabes hacerlo.")
    
    
    for indice, fila in df.iterrows(): #Recorre fila por fila.
        
        print()
        print()
        print(f"PREGUNTA {numero_pregunta} DE {total_preguntas}")
        print()
        print("Escala:") 
        print()
        print("  [ 1 ] = Me disgusta mucho")
        print("  [ 2 ] = Me disgusta")
        print("  [ 3 ] = Neutral")
        print("  [ 4 ] = Me gusta")
        print("  [ 5 ] = Me gusta mucho") 
        print() 
        
        pregunta = fila['Texto de la Pregunta (¿Qué tanto te gustaría...)']
        dimension = fila['Dimensión RIASEC'] 
        
        while True:
            try:
                respuesta = int(input(f"{pregunta}: "))
               
                if respuesta < 1 or respuesta > 5: 
                    print()
                    print("Error: El valor debe ser entre 1 y 5.") 
                    print()
                    
                else:
                    resultados[dimension] += respuesta
                    break
                    
            except ValueError: 
                print()
                print("Error: La respuesta debe ser un número.") 
                print()
        numero_pregunta += 1
    
    return resultados


def filtrar_carreras(df_carreras):
    # La funcion reduce el DataFrame ingresado (df_carreras) basandose en 4 criterios especificos (provincia, gestion, titulo, duracion)
    # A traves de la consola, le hace preguntas al usuario (manejando los posibles errores de tipeo (minusculas y tildes))
    # Devuelve un DataFrame mas pequeño con solo las opciones que cumplan todos los requisitos simultaneamente
    
    """
    Pide al usuario una provincia, un tipo de gestión (Pública/Privada), un tipo de titulo (Grado, Titulo intermedio, otro) y la duracion maxima deseada
    filtra el DataFrame recibido y devuelve uno acotando solo las filas que coinciden

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
    
    provincias_validas = ["Buenos Aires", "Catamarca", "Chaco", "Chubut", 
    "Ciudad Autonoma de Buenos Aires", "Córdoba", "Corrientes", "Entre Ríos", "Formosa", 
    "Jujuy", "La Pampa", "La Rioja", "Mendoza", "Misiones", "Neuquén", "Río Negro", "Salta",
    "San Juan", "San Luis", "Santa Cruz", "Santa Fé", "Santiago Del Estero", "Tierra Del Fuego", "Tucumán"]
    
    print("Lista de provincias:") 
    print()
    print(
       " 1. Buenos Aires                  2. Catamarca                   3. Chaco\n"
       " 4. Chubut                        5. Ciudad Autonoma de BA       6. Córdoba\n"
       " 7. Corrientes                    8. Entre Ríos                  9. Formosa\n"
       "10. Jujuy                        11. La Pampa                   12. La Rioja\n"
       "13. Mendoza                      14. Misiones                   15. Neuquén\n"
       "16. Río Negro                    17. Salta                      18. San Juan\n"
       "19. San Luis                     20. Santa Cruz                 21. Santa Fé\n"
       "22. Santiago Del Estero          23. Tierra Del Fuego           24. Tucumán"
    )
    print()
    
    while True:
 
        try:
 
            opcion = int(input("Ingrese el número de la provincia en la que te gustaría estudiar: ")) 
            print()
 
            if opcion < 1 or opcion > len(provincias_validas):
                print(f"Error: Ingrese un número entre 1 y {len(provincias_validas)}.") 
                print()
 
            else:
                provincia_elegida = provincias_validas[opcion - 1]
                condicion_provincia = (df_carreras["Provincia"].str.split(",").str[-1].str.strip() == provincia_elegida)
                break
 
        except ValueError: 
            
            print("Error: Debe ingresar un número válido.") 
            print()
        
    #filtro gestión
    
    print("Tipo de universidad:")
    print()
    print("  1. Pública")
    print("  2. Privada")
    print()

    while True:
        
        try: 
            opcion_gestion = int(input("Ingrese el número del tipo de universidad que prefiere: "))
            print()
 
            if opcion_gestion == 1:
                tipo_gestion = "pública"
                break
            
            elif opcion_gestion == 2:
                tipo_gestion = "privada"
                break
            
            else:
                print("Error: Ingrese 1 o 2.") 
                print()
 
        except ValueError:
            print("Error: Debe ingresar un número.")
            print()
        
    #filtro tipo de título
    print("Tipo de título:") 
    print()
    print("  1. Grado")
    print("  2. Título Intermedio")
    print("  3. Otro")
    print()
 
    while True:
        
        try: 
            opcion_titulo = int(input("Ingrese el número del tipo de título que busca: "))
            print()
        
            if opcion_titulo == 1:
                tipo_titulo = "grado"
                break 
        
            elif opcion_titulo == 2:
                tipo_titulo = "título intermedio"
                break
        
            elif opcion_titulo == 3:
                tipo_titulo = "otro"
                break
        
            else: 
                print("Error: Ingrese 1, 2 o 3.")
                print()
 
        except ValueError: 
            print("Error: Debe ingresar un número.") 
            print()
    
    if tipo_titulo == "grado":
 
        condicion_titulo = (df_carreras["Tipo"].str.lower() == "grado") 
 
    elif tipo_titulo == "título intermedio":
 
        condicion_titulo = (df_carreras["Tipo"].str.lower() == "título intermedio") 
        
    else:
 
        condicion_titulo = ((df_carreras["Tipo"].str.lower() != "grado") & (df_carreras["Tipo"].str.lower() != "título intermedio"))
   
    #filtro duración máxima
    
    while True:
 
        entrada_duracion = input("Ingrese la duración máxima (en años) deseada (entre 1 a 10): ").strip() 
        print()
 
        try: 
            
            duracion_max = float(entrada_duracion)  
            
            if duracion_max < 1 or duracion_max > 10:  
                
                print("Error: La duración debe ser un número entre 1 y 10.")  
                print()
            
            else: 
                
                break
        
        except ValueError: 
            
            print("Error: La duración debe ser un número.")  
            print()
    
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
        
        score = 0 
        
        for i in range(6): 
        
            if codigo_usuario[i] == codigo[i]: 
            
                score += puntos[i]  
                
        if score > mejor_score: 
            
            mejor_score = score
            
    return mejor_score  

    
def generar_ranking(codigo_usuario, df_filtrado):  
    
    ''' 
    Ordena las carreras de mayor a menor punataje, dada su similitud con el perfil RIASEC
    del usuario. 
    
    Parameters 
    ---------- 
    codigo_usuario: str. Código RIASEC de 6 caracteres asociado al usuario según sus respuestas 
                    al cuestionario 
    Returns
    ------- 
    df_ranking: dataframe con disciplinas principales y su score correspondiente respecto al perfil
                del usuario. 
    ''' 
    df_ranking = df_filtrado.copy()

    df_ranking["Score"] = 0

    for i in df_ranking.index:

       codigos_carrera = df_ranking.loc[i, "RIASEC_Codes"]

       score = calcular_score(codigo_usuario, codigos_carrera)

       df_ranking.loc[i, "Score"] = score

    df_ranking = df_ranking.sort_values(by="Score", ascending=False)

    df_ranking = df_ranking.drop_duplicates(subset="Disciplina_Principal")

    return df_ranking 
