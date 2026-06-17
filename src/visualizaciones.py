#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 14:19:43 2026

@author: clarabaietti
"""

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

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
        La función no retrona ningún valor, dibuja el gráfico dierctamente en streamlit.  

    """

    st.subheader("📊 Tu Perfil Vocacional")
    
    dimensiones = list(resultados.keys())
    puntajes = list(resultados.values())
   
    fig, ax = plt.subplots(figsize=(8, 4))
    
    sns.barplot(x=dimensiones, y=puntajes, palette="Blues_d", ax=ax)
    
    ax.set_title("Puntajes por Dimensión", fontsize=12, fontweight='bold')
    ax.set_ylabel("Puntaje")
    ax.set_ylim(0, max(puntajes) + 5)
    
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='center', xytext=(0, 8), 
                    textcoords='offset points', fontweight='bold')

    st.pyplot(fig)


def dibujar_grafico_top5(top_5_filtrado):
    """
    Dibuja un gráfico que compara la duración estimada de las carreras recomendadas. Muestra visualemente el tiempo mínimo base y la variación de años extras según la universidad.  

    Parameters
    ----------
    top_5_filtrado : 
       DESCRIPTION

    Raises
    ------
    ValueError
        DESCRIPTION.

    Returns
    -------
    None.
        La función no retrona ningún valor, dibuja el gráfico dierctamente en streamlit.  

    """
    if top_5_filtrado is None or top_5_filtrado.empty:
        raise ValueError("No hay datos disponibles para generar el gráfico.")

    st.header("🎯 Tus Carreras Recomendadas")
    st.write("Comparativa de duración estimada en tu provincia (Base mínima en azul, variación por universidad en naranja):")
    
    df_rangos = top_5_filtrado.groupby('Título', as_index=False)['Duracion_Num'].agg(['min', 'max'])
    df_rangos['variacion'] = df_rangos['max'] - df_rangos['min']
    
    fig, ax = plt.subplots(figsize=(9, 3.5))
    ax.barh(y=df_rangos['Título'], width=df_rangos['min'], left=0, color='#4a90e2', label='Duración Mínima')
    ax.barh(y=df_rangos['Título'], width=df_rangos['variacion'], left=df_rangos['min'], 
            color='#f5a623', alpha=0.8, edgecolor='black', linestyle='--', label='Variación según Universidad')
    
    ax.set_xlim(0, df_rangos['max'].max() + 1)
    ax.set_xlabel("Años")
    ax.legend(loc="lower right")
    ax.grid(axis='x', linestyle=':', alpha=0.6)
    st.pyplot(fig)


def mostrar_listado_universidades(top_5_filtrado):
    """
    Crea un sistema interactivo de pestañas para explorar las universidades disponibles. Permite al usuario ver las sedes, requisitos y contactos de las facultades en su provincia.

    Parameters
    ----------
    top_5_filtrado : TYPE
        DESCRIPTION.

    Raises
    ------
    ValueError
        DESCRIPTION.

    Returns
    -------
    None.
        La función no retorna ningún valor, despliega las pestañas y tarjetas en Streamlit.

    """
    if top_5_filtrado is None or top_5_filtrado.empty:
        raise ValueError("No hay datos disponibles para listar las universidades.")

    st.header("🏛️ Dónde podés estudiar")
    st.write("Hacé clic en las pestañas para ver las universidades de tu provincia que dictan cada carrera:")
    
    carreras_unicas = list(top_5_filtrado['Título'].unique())
    pestanas = st.tabs([carrera.upper() for carrera in carreras_unicas])
    
    for i, carrera in enumerate(carreras_unicas):
        with pestanas[i]:
            universidades_de_carrera = top_5_filtrado[top_5_filtrado['Título'] == carrera]
            st.info(f"Opciones locales para **{carrera}**:")
            
            for _, fila in universidades_de_carrera.iterrows():
                with st.container(border=True):
                    st.subheader(f"🏛️ {fila['Universidad']}")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**🏢 Facultad/Sede:** {fila['Facultad']}")
                        st.markdown(f"**⚖️ Gestión:** {fila['Gestion']}")
                        st.markdown(f"**⏳ Duración en esta sede:** {fila['Duración']}")
                    with col2:
                        st.markdown(f"**🚪 Ingreso:** {fila['Ingreso']}")
                        st.markdown(f"**📍 Dirección:** {fila['Domicilio']}")
                    
                    contactos = []
                    if pd.notna(fila['Teléfono']): contactos.append(f"📞 {fila['Teléfono']}")
                    if pd.notna(fila['Web']): contactos.append(f"🌐 [{fila['Web']}](http://{fila['Web']})")
                    if pd.notna(fila['Mail']): contactos.append(f"📧 {fila['Mail']}")
                    
                    if contactos:
                        st.caption("Vías de Contacto: " + " | ".join(contactos))
                    else:
                        st.caption("⚠️ *No se registraron datos de contacto para esta sede.*")
                    
                    st.write("")
                        
                        
                        
                        
                        
                        