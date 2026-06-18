from funciones import cargar_datos, test_riasec, filtrar_carreras, generar_codigo_riasec, generar_ranking

from visualizaciones import mostrar_ranking, mostrar_grafico_top5, mostrar_perfil

print()
print("🎓📚 RECOMENDADOR DE CARRERAS 🎓📚  ") 
print("=====================================")  
print()

ruta_carreras = "La ruta del csv de las carreras."
ruta_test = "La ruta del test RIASEC."

df_carreras = cargar_datos(ruta_carreras) 

print()
print("Selecciona tus preferencias ✅:") 
print("-------------------------------")  
print() 

while True:
 
    df_filtrado = filtrar_carreras(df_carreras) 
 
    if df_filtrado.empty:
        
        print()
        print("⚠️ No se encontraron carreras para los filtros seleccionados.")
        print("Intenta ampliar la duración máxima o cambiar el tipo de título.")
        print()
    
    else:
        
        break

print()         
print("📚 Test RIASEC: Responde las siguientes preguntas para obtener tu perfil.")  
print("-------------------------------------------------------------------------")  
print() 

resultados = test_riasec(ruta_test)

codigo_usuario = generar_codigo_riasec(resultados) 

print()
print("🤔 Tu perfil RIASEC es:", codigo_usuario)

df_ranking = generar_ranking(codigo_usuario, df_filtrado) 
 
top_5_filtrado = df_filtrado[df_filtrado["Disciplina_Principal"].isin(df_ranking["Disciplina_Principal"])]
 
print()  
mostrar_perfil(resultados) 
print()
mostrar_grafico_top5(top_5_filtrado) 
print()
 
while True:
 
        try:
 
            mostrar_ranking(df_ranking, df_filtrado) 
            
            break
 
        except ValueError as error:
 
            print("Error: ", error)

