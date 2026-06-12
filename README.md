# Recomendador de carreras a partir de test RIASEC

Interantes:
- clara Baietti
- Micaela Cohen
- Guadalupe Silva
- Sol Pilpis
- Olivia Salmoyraghi

Objetivo:
El objetivo del programa es abordar la problemática de la elección de carreras, para eso realiza preguntas del test RIASEC, en base a al puntaje que  obtiene cada letra las ordena de forma específica (por ejemplo SIAREC) y lo cruza con un dataset donde están las carreras cada una con un orden distinto de las letras y en base a eso te recomienda 5 posibles principales. El trabajo fue dividio en 5 partes + el main:
- Clara: calcular_score / generar_ranking
- Micaela: geneerar_codigo_riasec
- Guadalupe: hacer_cuestionario
- Sol: filtrar_carreras
- Olivia: cagas_datos / graficar_perfil / graficar_top5

Descripcion de los datos 
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


