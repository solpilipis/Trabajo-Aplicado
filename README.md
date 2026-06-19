## Recomendador de carreras a partir del test RIASEC 


# Integrantes:
- Clara Baietti
- Micaela Cohen
- Guadalupe Silva
- Sol Pilpis
- Olivia Salmoyraghi

# Objetivo:
El objetivo del programa es abordar la problemática de la elección de carreras. Para ello, se realizan preguntas del test RIASEC y, basándose en el puntaje que obtiene cada dimensión, se ordena de forma específica el perfil del usuario (por ejemplo, SIAREC). Luego, esto se cruza con un dataset de carreras, cada una con un código RIASEC asignado, y en base a la compatibilidad, el sistema recomienda las 5 opciones principales.

El trabajo se dividió en 5 partes principales:

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
- ID_SISTEMA: Es el id con el que esta identificada cada universidad.
- Universidad: Es la universidad.
- Título: Es el nombre del título de la carrera.
- Tipo: Determina si es una carrera de grado, un título intermedio, una tecnicatura, etc.
- Duración: Duración en años de la carrera.
- Ingreso: Condición de entrada a la universidad.
- Domicilio: Ubicación de la universidad.
- Telefono: Telefono de contacto de la universidad.
- Web: Página web de la universidad.
- Mail: Mail de contacto para el ingreso.
- Tipo_Gestion: Pública o privada.
- RIASEC_codes: Perfiles RIASEC a los cuales se les recomendaría la carrera.
- Disciplina_Principal: Descripción general del área de desempeño de la carrera.
- Provincia: Provincia donde se ubica la universidad.

#Test RIASEC
- ID: Id con el que se identifica cada pregunta (número de pregunta).
- Texto de la Pregunta (¿Qué tanto te gustaría...): Pregunta del test RIASEC.
- Dimensión RIASEC: Dimensión RIASEC representada por la primera letra de su nombre y su aclaración.


# Instrucciones para ejecutar el programa: 
1) Clonar el repositorio: Descarga o clona este repositorio en tu computadora local.

2) Instalar dependencias: Instala las librerías necesarias nombradas en requirements.txt

3) Copia las rutas de los archivos Database_Carreras_Argentinas y Test_RIASEC de tu computadora. Pegalos en el main.py en:

- ruta_carreras = "La ruta del csv de las carreras."
- ruta_test = "La ruta del test RIASEC."

según corresponda.

4) Ejecutar el código.

5) Interacción: Una vez que el programa inicie en la consola, deberás ingresar tus preferencias (provincia, tipo de gestión, duracion maxima y tipo de titulo), y luego responder a las preguntas del test RIASEC calificando del 1 al 5 según tu grado de afinidad. Finalmente, el sistema te mostrará tu código, las carreras recomendadas y los gráficos de tu perfil.

Nota: Si el programa se ejecuta desde entornos como Spyder y los gráficos no se muestran, se recomienda correrlo desde la consola (CMD/Terminal).

# Librerias utilizadas
- pandas
- matplotlib
- seaborn

# Estructura del repositorio 
- datos
    - Database_Carreras_Argentinas.csv
    - Test_RIASEC.csv
- src
   - funciones.py
   - visualizaciones.py
- requirements.txt
- README.md
- main.py

# Explicación breve de las funciones principales
- cargar_datos: Lee la base de datos desde un archivo CSV con pandas, recorre las columnas y limpia los espacios en blanco de las columnas principales.
- test_riasec: Le hace las preguntas del test RIASEC al usuario, calificando las respuestas del 1-5. Verifica que las respuestas sean válidas y suma en un diccionario el valor que se le indica a cada letra (dimensión).
- filtrar_carreras: Pide al usuario una provincia, un tipo de gestión (Pública o privada), un tipo de título (de grado, intermedio o tecnicatura) y una duración máxima en años. Filtra el DataFrame recibido y devuelve solo las filas que coinciden.
- calcular_score: Compara la combinación de letras del usuario (su perfil) con las de una carrera y calcula un puntaje de afinidad, otorgando más puntos si coinciden en las primeras posiciones.
- generar_codigo_riasec: Ordena las letras del perfil del mayor al menor puntaje obtenido.
- generar_ranking: Evalúa la afinidad de todas las carreras filtradas con el perfil del usuario, elimina opciones duplicadas y devuelve las 5 mejores recomendaciones.
- mostrar_ranking: Muestra por consola las carreras recomendadas y le pide al usuario el número de la carrera elegida y en base a eso y a la base de datos ya filtrada por la función filtrar_carreras, le muestra el titulo, la duración, donde la pueden estudiar, etc.
- mostrar_perifl:
- mostrar_grafico_top5: 
# Resultados, salidas, métricas, gráficos o funcionalidades generadas, según corresponda
Muestra por consola las carreras recomendadas, la duración, el título, donde se estudia. Muestra un gráfico de barras comparando el perfil RIASEC (afinidad del 1 al 10 en el eje y, dimensiones de RIASEC en el eje x) , otro con el top 5 carreras recomendadas (eje y) y la duración de cada carrera (eje x) donde aparece la duracion minima en un color y la variacion en otro.

# Diagramas de diseño.
Ubicados en la carpeta "diagramas".

# Declaración de uso de IA
Durante el desarrollo de este proyecto, utilizamos herramientas de Inteligencia Artificial  como asistentes de programación y estructuración de datos. Su uso se dividió en dos áreas principales:

1. Armado y limpieza del Dataset:
Utilizamos IA para estructurar y extraer el dataset conjunto de carreras argentinas basado en la web del gobierno, y para generar la lógica de cruce con los perfiles RIASEC.

2. Asistencia en código y librerías:
Consultamos a la IA para resolver dudas específicas sobre métodos de la librería pandas y para optimizar la configuración visual de los gráficos generados con matplotlib y seaborn. Además, se utilizó para detectar y resolver errores que nosotras no encontrábamos.  

#  Notas o explicaciones adicionales para correr correctamente el programa
Durante el desarrollo de este proyecto descubrimos algunas limitaciones metodológicas del test RIASEC. Debido a su naturaleza generalista y poca especificidad, la recomendación final de carreras puede resultar poco precisa en algunas ocasiones.