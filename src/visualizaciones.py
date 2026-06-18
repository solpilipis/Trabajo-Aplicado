import matplotlib.pyplot as plt
import seaborn as sns

def mostrar_ranking(df_ranking, df_filtrado):

    '''
    Muestra las 5 carreras recomendadas y permite
    al usuario elegir una para obtener más información.
    '''
    TOPE = 20  # máximo de carreras a mostrar aunque el empate sea más grande
    mostrando = 5
 
    while True:
 
       carreras_mostradas = df_ranking.head(mostrando)
       cantidad = len(carreras_mostradas)
 
       print("\n🏅 TOP CARRERAS RECOMENDADAS 🏅\n")
 
       for i in range(cantidad):
           print(f"{i+1}. {carreras_mostradas.iloc[i]['Disciplina_Principal']}")
 
       hay_empate = (
           mostrando < TOPE
           and len(df_ranking) > mostrando
           and df_ranking.iloc[mostrando - 1]["Score"] == df_ranking.iloc[mostrando]["Score"]
       )
 
       if hay_empate:
           opcion_ver_mas = cantidad + 1
           opcion_finalizar = cantidad + 2
           print(f"{opcion_ver_mas}. Ver más carreras (hay empate con la última)")
       else:
           opcion_ver_mas = None
           opcion_finalizar = cantidad + 1
 
       print(f"{opcion_finalizar}. Finalizar")
 
       while True:
 
           opcion = input("\nIngrese una opción: ").strip() 
           
           if not opcion.isdigit():
               print("Error: Debe ingresar un número.")
               continue
 
           opcion = int(opcion)
 
           if opcion < 1 or opcion > opcion_finalizar:
               print(f"Error: Debe ingresar un número entre 1 y {opcion_finalizar}.")
               continue
 
           break
 
       if opcion == opcion_finalizar:
 
           print("\n¡Gracias por usar el recomendador de carreras! 👋")
           break
 
       elif hay_empate and opcion == opcion_ver_mas:
 
           mostrando = min(mostrando + 5, len(df_ranking))
           continue
 
       else:
 
           carrera = carreras_mostradas.iloc[opcion - 1]["Disciplina_Principal"]
 
           print(f"\nOpciones para estudiar {carrera}:\n") 
           
           for i in df_filtrado.index:
 
                if df_filtrado.loc[i, "Disciplina_Principal"] == carrera:
 
                    print(f"Universidad: {df_filtrado.loc[i, 'Universidad']}")
                    print(f"Título: {df_filtrado.loc[i, 'Título']}")
                    print(f"Duración: {df_filtrado.loc[i, 'Duración']}")
                    print(f"Dirección: {df_filtrado.loc[i, 'Domicilio']}")  
                    print(f"Teléfono: {df_filtrado.loc[i, 'Teléfono']}")   
                    print(f"Mail: {df_filtrado.loc[i, 'Mail']}")  
                    print(f"Sitio web: {df_filtrado.loc[i, 'Web']}")
                    print()
           
           print() 
           input("Presione Enter para volver al menú.") 
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
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        