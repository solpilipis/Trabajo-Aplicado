from funciones import cargar_datos, test_riasec, filtrar_carreras, generar_codigo_riasec, generar_ranking

from visualizaciones import mostrar_ranking 

print()
print("RECOMENDADOR DE CARRERAS") 
print("-------------------------")  
print()

df_carreras = cargar_datos("/Users/clarabaietti/Documents/Github/Trabajo-Aplicado/datos/Database_Carreras_Argentinas.csv") 

print()
print("Selecciona tus preferencias") 
print("-------------------------")  
print() 

df_filtrado = filtrar_carreras(df_carreras) 

print()         
print("Test RIASEC: Responde las siguientes preguntas para obtener tu perfil.")  
print("-------------------------")  
print() 

resultados = test_riasec("/Users/clarabaietti/Documents/Github/Trabajo-Aplicado/datos/Test_RIASEC.csv")

codigo_usuario = generar_codigo_riasec(resultados) 

print()
print("Tu perfil RIASEC es:", codigo_usuario)
print()

df_ranking = generar_ranking(codigo_usuario, df_filtrado)

while True:

        try:

            mostrar_ranking(df_ranking, df_filtrado) 
            
            break

        except ValueError as error:

            print("Error: ", error)

#faltan visualizaciones