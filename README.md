# Recomendador de carreras a partir de test RIASEC 


# Integrantes:
- Clara Baietti
- Micaela Cohen
- Guadalupe Silva
- Sol Pilpis
- Olivia Salmoyraghi

# Objetivo:
El objetivo del programa es abordar la problemática de la elección de carreras, para eso realiza preguntas del test RIASEC, en base a al puntaje que  obtiene cada letra las ordena de forma específica (por ejemplo SIAREC) y lo cruza con un dataset donde están las carreras cada una con un orden distinto de las letras y en base a eso te recomienda 5 posibles principales. El trabajo fue dividio en 5 partes + el main:
- Clara: calcular_score / generar_ranking / main
- Micaela: generar_codigo_riasec
- Guadalupe: hacer_cuestionario / armado de base de datos
- Sol: filtrar_carreras
- Olivia: cagar_datos / graficar_perfil / graficar_top5

# Descripcion de la fuente de datos:

#Carreras argentinas:
- id sistema: es el id con el que esta identificada cada universidad
- universidad: es la universidad
- titulo: es el nombre del titulo con el que te recibis
- tipo: si es una carrera de grado, intermedio, tecnicatura, etc.
- duracion: cuantos añso dura la carrera
- ingreso: si hay que hacer curso de ingreso, examen, o cualquier otra condicion de ingreso a la universidad
- domicilio: donde queda la universidad
- telefono: telefono de contacto de la univeridad
- web: pagina web de la universidad
- mail: mail de contacto para el ingreso
- tipo de gestion: Publica o privada
- RIASEC_codes: son las posibles combinaciones de las letras RIASEC dependiendo del score
- disciplian principal: descripcion geenral del area de desempeño de la carrera

#Test RIASEC
- ID: id con el que se indentifica cada pregunta; por ejemplo P = pregunta 01 = numero de pregunta 
- texto de la pregunta: es la pregunta que se le hace al participante 
- dimension RIASEC: que letra se le asigna dependiendo de la respuesta 


# Instrucciones para ejecutar el programa: 
el usuario debe primero responder preguntas sobre preferencias, ubicación y otras relevantes para la recomendacion de la universidad y luego responder el test RIASEC

# Librerias utilizadas
- pandas
- seaborn
- streamlit
- matplotlib.pyplot

# Estructura del repositorio 
- datos
    - DS_Store
    - Carreras_argentinas_con_provincias
    - TestRIASE.xlsx
- src
   - DS_Store
   - funciones.py
   - visualizaciones.py
- DS_store
- README.md 
- main.py
- diagramas
  - main
  - calcular_score
  - dibujar_grafico_top5
  - filtrar_carreras
  - generar_codigo_riasec
  - generar_ranking
  - mostrar_listado_universidades
  - mostrar_perfil
  - test_riasec

# Explicación breve de las funciones principales
- cargar_datos: Lee la base de datos desde un archivo CSV con pandas, recorre las columnas y limpia los espacios en blanco de las columnas principales
- test_riasec: le hace las preguntas del test RIASEC al usuario, calificando las rspuestas del 1-5, verifica que las respuestas sean validas y suma en un diccionario el valor que se le indica a cada letra
- filtrar_carreras: Pide al usuario una provincia y un tipo de gestión (Pública/Privada), filtra el DataFrame recibido y devuelve solo las filas que coinciden.
- calcular_score: Compara la combinación de letras del usuario con las de una carrera y calcula un puntaje de afinidad, otorgando más puntos si coinciden en las primeras posiciones.
- generar_codigo_riasec: ordena las letras del mayor al menor puntaje obtenido
- generar_ranking: evalúa la afinidad de todas las carreras filtradas contra el perfil del usuario, elimina opciones duplicadas y las 5 mejores recomendaciones.
- mostrar_ranking: muestra en consola las carreras recomendadas y le pide al usuario el numero de la carrera elegida y en base a eso y a la base de datos ya filtrada por la función filtrar_carreras, le muestra el titulo, la duracion, donde la puende estudiar, etc.
  
# Resultados, salidas, métricas, gráficos o funcionalidades generadas, según corresponda
muestra por consola las carreras recomendadas, la duracion, el titulo, donde se estudia. muestra un grafico de barras comparando el perfil riasec (afinidad del 1 al 10 en el eje y, carreras eje x) , otro con el top 5 carreras recomendadas (eje y) y la duracion minima (eje x)

# Diagramas de diseño.
- calcular_score: "C:\Users\guadi\Desktop\GitHub\Trabajo-Aplicado\diagramas\calcular_score.png"
- dibujar_grafico_top5: "C:\Users\guadi\Desktop\GitHub\Trabajo-Aplicado\diagramas\dibujar_grafico_top5.png"
- filtrar_carreras: "C:\Users\guadi\Desktop\GitHub\Trabajo-Aplicado\diagramas\filtrar_carreras.png"
- generar_codigo_riasec: "C:\Users\guadi\Desktop\GitHub\Trabajo-Aplicado\diagramas\generar_codigo_riasec.png"
- generar_ranking: "C:\Users\guadi\Desktop\GitHub\Trabajo-Aplicado\diagramas\generar_ranking.png"
- main: "C:\Users\guadi\Desktop\GitHub\Trabajo-Aplicado\diagramas\main.png"
- mostrar_listado_universidades: "C:\Users\guadi\Desktop\GitHub\Trabajo-Aplicado\diagramas\mostrar_listado_universidades.png"
- mostrar_perfil: "C:\Users\guadi\Desktop\GitHub\Trabajo-Aplicado\diagramas\mostrar_perfil.png"
- test_riasec: "C:\Users\guadi\Desktop\GitHub\Trabajo-Aplicado\diagramas\test_riasec.png"

# Declaración de uso de IA
Utilizamos la IA para poder armar el dataset conjunto que usamos para el proyecto. Además, le pedimos métodos de pandas y streamlit para llevar a cabo el proyecto,
sobretodo en filtrar_carreras y en las visualizaciones.m
#  Notas o explicaciones adicionales para correr correctamente el programa

