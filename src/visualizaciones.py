import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def mostrar_ranking(df_ranking, df_filtrado):
    """
    Muestra las 5 carreras recomendadas y permite
    al usuario elegir una para obtener más información.

    Parameters
    ----------
    df_ranking : pandas.Dataframe
        Tabla que ocntiene el listado resumido de las 5 carreras recomendadas. 
    df_filtrado : pandas.Dataframe
        Tabla completa con las opciones académicas filtradas previamente según las 
        preferencias del usuario (localidad, tipo de gestión, tipo de título y duración máxima).

    Raises
    ------
    ValueError
        Si el usuario ingresa un texto en lugar de un número, o si el número seleccionado 
        está fuera del rango válido de opciones (menor a 1 o mayor al tamaño del ranking).

    Returns
    -------
    None.
    La función no retorna ningún valor; imprime los datos directamente en la terminal.

    """

    
    print()
    print("\n 🏅TOP 5 CARRERAS RECOMENDADAS 🏅 \n") 
    print()

    for i in range(len(df_ranking)):

        print(f"{i+1}. {df_ranking.iloc[i]['Disciplina_Principal']}") 
    
    while True: 
        
        print()
        opcion = input("\nIngrese el número de la carrera deseada para obtener más información: ")
        print()
        
        if not opcion.isdigit(): 
        
            raise ValueError("Debe ingresar un número") 
            continue
    
        opcion = int(opcion)
        
        if opcion < 1 or opcion > len(df_ranking): 
          
            raise ValueError(f"Debe ingresar un número entre 1 y {len(df_ranking)}.")  
            continue 
        
        break
        
    carrera = df_ranking.iloc[opcion-1]["Disciplina_Principal"]

    print(f"\nOpciones para estudiar {carrera}:\n")

    for i in df_filtrado.index:

        if df_filtrado.loc[i, "Disciplina_Principal"] == carrera:

            print(f"Universidad: {df_filtrado.loc[i, 'Universidad']}")

            print(f"Título: {df_filtrado.loc[i, 'Título']}")
            
            print(f"Duración: {df_filtrado.loc[i, 'Duración']}") 
            
            print(f"Ubicada en: {df_filtrado.loc[i, 'Provincia']}")

            print(f"Sitio web: {df_filtrado.loc[i, 'Web']}") 
            
            print()
            

def mostrar_perfil(resultados):
    """
    Dibuja el gráfico de barras verticales del perfil RIASEC del usuario.

    Parameters
    ----------
    resultados : diccionario
    Contiene como clave las seis dimensiones del test y como valor el puntaje numérico obtenido por la persona en cada una

    Returns
    -------
    None.
        La función no retorna ningún valor; procesa los datos y abre una ventana emergente conel gráfico.

    """

    print("\n📊 Tu Perfil Vocacional\n")

    dimensiones = list(resultados.keys())
    puntajes = list(resultados.values())
   
    fig, ax = plt.subplots(figsize=(8, 4))
    
    sns.barplot(x=dimensiones, y=puntajes, color="0f8b5d", ax=ax)
    
    ax.set_title("Puntajes por Dimensión", fontsize=12, fontweight='bold')
    ax.set_ylabel("Puntaje")
    ax.set_ylim(0, max(puntajes) + 5)
    
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='center', xytext=(0, 8), 
                    textcoords='offset points', fontweight='bold')

    plt.show()


def mostrar_grafico_top5(top_5_filtrado):
    """
    Dibuja un gráfico que compara la duración estimada de las carreras recomendadas. 
    Muestra visualemente el tiempo mínimo base y la variación de años extras según la universidad.  

    Parameters
    ----------
    top_5_filtrado : pandas.Dataframe
       Una tabal de datos de las carreras recomendadas. 

    Raises
    ------
    ValueError
        Si el DataFrame es None o está vacío, interrumpiendo 
        la ejecución para evitar fallos en el dibujado.  

    Returns
    -------
    None.
        La función no retorna ningún valor; procesa los datos y abre una ventana emergente conel gráfico.  

    """
    if top_5_filtrado is None or top_5_filtrado.empty:
        raise ValueError("No hay datos disponibles para generar el gráfico.")

    print("\n🎯 Tus Carreras Recomendadas\n")
    print("Comparativa de duración estimada en tu provincia (Base mínima en azul, variación por universidad en naranja):")

    top_5_filtrado = top_5_filtrado.copy()
    top_5_filtrado['Duracion_Num'] = (
        top_5_filtrado['Duración'].str.extract(r'(\d+(?:\.\d+)?)')[0].astype(float)
    )

    df_rangos = top_5_filtrado.groupby('Título', as_index=False)['Duracion_Num'].agg(['min', 'max'])
    df_rangos['variacion'] = df_rangos['max'] - df_rangos['min']
    
    fig, ax = plt.subplots(figsize=(9, 3.5))
    ax.barh(y=df_rangos['Título'], width=df_rangos['min'], left=0, color='#0f8b5d', label='Duración Mínima')
    ax.barh(y=df_rangos['Título'], width=df_rangos['variacion'], left=df_rangos['min'], 
            color='#f3b0b3', alpha=0.8, edgecolor='black', linestyle='--', label='Variación según Universidad')
    
    ax.set_xlim(0, df_rangos['max'].max() + 1)
    ax.set_xlabel("Años")
    ax.legend(loc="lower right")
    ax.grid(axis='x', linestyle=':', alpha=0.6)
    plt.tight_layout()
    plt.show()
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        