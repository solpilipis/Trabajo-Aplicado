# Recomendador de carreras a partir de test RIASEC 


# Interantes:
- clara Baietti
- Micaela Cohen
- Guadalupe Silva
- Sol Pilpis
- Olivia Salmoyraghi

# Objetivo:
El objetivo del programa es abordar la problemática de la elección de carreras, para eso realiza preguntas del test RIASEC, en base a al puntaje que  obtiene cada letra las ordena de forma específica (por ejemplo SIAREC) y lo cruza con un dataset donde están las carreras cada una con un orden distinto de las letras y en base a eso te recomienda 5 posibles principales. El trabajo fue dividio en 5 partes + el main:
- Clara: calcular_score / generar_ranking
- Micaela: geneerar_codigo_riasec
- Guadalupe: hacer_cuestionario
- Sol: filtrar_carreras
- Olivia: cagas_datos / graficar_perfil / graficar_top5

# Descripcion de los datos:

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

# Liberrias utilizadas
- Pandas

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

# Explicación breve de las funciones principales
- cargar_datos: Lee la base de datos desde un archivo CSV con pandas, recorre las columnas y limpia los espacios en blanco de las columnas principales
- test_riasec: le hace las preguntas del test RIASEC al usuario, calificando las rspuestas del 1-5, verifica que las respuestas sean validas y suma en un diccionario el valor que se le indica a cada letra
- filtrar_carreras: Pide al usuario una provincia y un tipo de gestión (Pública/Privada), filtra el DataFrame recibido y devuelve solo las filas que coinciden.
- calcular_score: Compara la combinación de letras del usuario con las de una carrera y calcula un puntaje de afinidad, otorgando más puntos si coinciden en las primeras posiciones.
- generar_codigo_riasec: ordena las letras del mayor al menor puntaje obtenido
- generar_ranking: evalúa la afinidad de todas las carreras filtradas contra el perfil del usuario, elimina opciones duplicadas y las 5 mejores recomendaciones.
- mostrar_ranking: muestra en consola las carreras recomendadas y le pide al usuario el numero de la carrera elegida y en base a eso y a la base de datos ya filtrada por la función filtrar_carreras, le muestra el titulo, la duracion, donde la puende estudiar, etc. 
