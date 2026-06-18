# Recomendador de carreras a partir de test RIASEC 


# Integrantes:
- Clara Baietti
- Micaela Cohen
- Guadalupe Silva
- Sol Pilpis
- Olivia Salmoyraghi

# Objetivo:
El objetivo del programa es abordar la problemática de la elección de carreras, para eso realiza preguntas del test RIASEC, en base a al puntaje que  obtiene cada letra las ordena de forma específica (por ejemplo SIAREC) y lo cruza con un dataset donde están las carreras cada una con un orden distinto de las letras y en base a eso te recomienda 5 posibles principales. El trabajo fue dividió en 5 partes + el main:
- Clara: calcular_score / generar_ranking / mostrar_ranking / main.py
- Micaela: generar_codigo_riasec
- Guadalupe: hacer_cuestionario / Armado de datasets.
- Sol: filtrar_carreras
- Olivia: cargar_datos / graficar_perfil / graficar_top5

# Descripcion de los datos:
El csv de carreras argentinas fue extraído con la ayuda de la IA de la siguiente página del gobierno: https://guiadecarreras.siu.edu.ar/
Después con código y uso de IA, se le agregaron columnas para cruzar la información con el test RIASEC y mejorar la experiencia del usuario.
El csv del test RIASEC está basado en las traducciones oficiales al español del O*NET Interest Profiler Short Form que utiliza el gobierno estadounidense en su plataforma de exploración de carreras para hispanohablantes, llamada "Mi Próximo Paso". 

# Carreras argentinas:
- id sistema: es el id con el que esta identificada cada universidad
- universidad: es la universidad
- titulo: es el nombre del titulo con el que te recibis
- tipo: si es una carrera de grado, intermedio, tecnicatura, etc.
- duracion: cuantos años dura la carrera
- ingreso: si hay que hacer curso de ingreso, examen, o cualquier otra condicion de ingreso a la universidad
- domicilio: donde queda la universidad
- telefono: telefono de contacto de la univeridad
- web: pagina web de la universidad
- mail: mail de contacto para el ingreso
- tipo de gestion: Publica o privada
- RIASEC_codes: son las posibles combinaciones de las letras RIASEC dependiendo del score
- disciplian principal: descripcion general del area de desempeño de la carrera

#Test RIASEC
- ID: id con el que se identifica cada pregunta; por ejemplo P = pregunta 01 = numero de pregunta 
- texto de la pregunta: es la pregunta que se le hace al participante 
- dimension RIASEC: que letra se le asigna dependiendo de la respuesta 


# Instrucciones para ejecutar el programa: 
1) Clonar el repositorio: Descarga o clona este repositorio en tu computadora local.

2) Instalar dependencias: Abre tu terminal, navega hasta la carpeta raíz del proyecto y ejecuta el siguiente comando para instalar las librerías necesarias: pip install -r requirements.txt

3) Copia las rutas de los archivos Database_Carreras_Argentinas y Test_RIASEC de tu computadora. Pegalos en el main.py en:
ruta_carreras = "La ruta del csv de las carreras."
ruta_test = "La ruta del test RIASEC."
según corresponda.

4) Ejecución: En la terminal, ejecuta el archivo principal con el comando: python main.py

5) Interacción: Una vez que el programa inicie en la consola, deberás ingresar tus preferencias (provincia y tipo de gestión), y luego responder a las preguntas del test RIASEC calificando del 1 al 5 según tu grado de afinidad. Finalmente, el sistema te mostrará tu código, las carreras recomendadas y los gráficos de tu perfil.

Nota: Si el programa se ejecuta desde entornos como Spyder y los gráficos no se muestran, se recomienda correrlo desde la consola (CMD/Terminal).

# Librerias utilizadas
- pandas
- matplotlib
- seaborn

# Estructura del repositorio 
- datos
    - Database_Carreras_Argentinas
    - Test_RIASEC.xlsx
- src
   - funciones.py
   - visualizaciones.py
- requirements.txt
- README.md
- main.py

# Explicación breve de las funciones principales
- cargar_datos: Lee la base de datos desde un archivo CSV con pandas, recorre las columnas y limpia los espacios en blanco de las columnas principales
- test_riasec: le hace las preguntas del test RIASEC al usuario, calificando las respuestas del 1-5, verifica que las respuestas sean validas y suma en un diccionario el valor que se le indica a cada letra
- filtrar_carreras: Pide al usuario una provincia y un tipo de gestión (Pública/Privada), filtra el DataFrame recibido y devuelve solo las filas que coinciden.
- calcular_score: Compara la combinación de letras del usuario con las de una carrera y calcula un puntaje de afinidad, otorgando más puntos si coinciden en las primeras posiciones.
- generar_codigo_riasec: ordena las letras del mayor al menor puntaje obtenido
- generar_ranking: evalúa la afinidad de todas las carreras filtradas contra el perfil del usuario, elimina opciones duplicadas y las 5 mejores recomendaciones.
- mostrar_ranking: muestra en consola las carreras recomendadas y le pide al usuario el numero de la carrera elegida y en base a eso y a la base de datos ya filtrada por la función filtrar_carreras, le muestra el titulo, la duracion, donde la pueden estudiar, etc.
  
# Resultados, salidas, métricas, gráficos o funcionalidades generadas, según corresponda
muestra por consola las carreras recomendadas, la duracion, el titulo, donde se estudia. muestra un grafico de barras comparando el perfil riasec (afinidad del 1 al 10 en el eje y, carreras eje x) , otro con el top 5 carreras recomendadas (eje y) y la duracion minima (eje x)

# Diagramas de diseño.
Ubicados en la carpeta "diagramas".

# Declaración de uso de IA
Durante el desarrollo de este proyecto, utilizamos herramientas de Inteligencia Artificial  como asistentes de programación y estructuración de datos. Su uso se dividió en dos áreas principales:

1. Armado y limpieza del Dataset:
Utilizamos IA para estructurar y extraer el dataset conjunto de carreras argentinas basado en la web del gobierno, y para generar la lógica de cruce con los perfiles RIASEC.

2. Asistencia en código y librerías:
Consultamos a la IA para resolver dudas específicas sobre métodos de la librería pandas y para optimizar la configuración visual de los gráficos generados con matplotlib y seaborn. Además, se utilizó para detectar y resolver errores que nosotras no encontrábamos.  

#  Notas o explicaciones adicionales para correr correctamente el programa
Descubrimos limitaciones del test RIASEC durante el desarrollo de este proyecto. Debido a su poca especificidad, la recomendación de carreras puede ser mala a veces.
