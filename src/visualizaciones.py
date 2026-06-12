def mostrar_ranking(df_ranking, df_filtrado):

    '''
    Muestra las 5 carreras recomendadas y permite
    al usuario elegir una para obtener más información.
    '''

    print("\nTOP 5 CARRERAS RECOMENDADAS\n")

    for i in range(len(df_ranking)):

        print(f"{i+1}. {df_ranking.iloc[i]['Disciplina_Principal']}") 
        
    opcion = input("\nIngrese el número de la carrera: ")
    
    if not opcion.isdigit(): 
        
        raise ValueError("Debe ingresar un número")  
    
    opcion = int(opcion)
        
    if opcion < 1 or opcion > len(df_ranking): 
        
        raise ValueError(f"Debe ingresar un número entre 1 y {len(df_ranking)}.") 
        
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
            

           




