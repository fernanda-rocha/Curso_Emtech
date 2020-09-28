#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Importar pandas y leer el archivo csv
import pandas as pd

archivo = pd.read_csv("synergy_logistics_database.csv")


# In[3]:


#Sacar cada país con sus diferentes rutas
filtro = archivo.groupby(['direction','origin','destination','transport_mode'])['total_value'].sum()


# In[4]:


#Guardar nuestra nueva tabla en un csv
filtro.to_csv("filtro.csv")


# In[5]:


#leer el nuevo csv
datos_filtrados = pd.read_csv("filtro.csv")


# In[6]:


#Separar las tablas en exportaciones e importaciones
rutas_exp = archivo[archivo['direction'] == 'Exports']
rutas_imp = archivo[archivo['direction']=='Imports']


# In[7]:


#Calcular las rutas más usadas en las exportaciones
rutas_usadas_exp = rutas_exp.groupby(['origin','destination']).size().reset_index().rename(columns={0:'rutas_exportaciones'})
top_rutas_exp = rutas_usadas_exp.sort_values('rutas_exportaciones',ascending=False)


# In[8]:


#Calcular las rutas más usadas en las importaciones
rutas_usadas_imp = rutas_imp.groupby(['origin','destination']).size().reset_index().rename(columns={0:'rutas_importaciones'})
top_rutas_imp = rutas_usadas_imp.sort_values('rutas_importaciones',ascending=False)


# In[9]:


#Generar una tabla de exportaciones
exportaciones = datos_filtrados[datos_filtrados['direction'] == 'Exports']


# In[10]:


#Generar una tabla de importaciones
importaciones = datos_filtrados[datos_filtrados['direction'] == 'Imports']


# In[11]:


#Ordenar los datos para sacar las rutas de exportación que generan más dinero
mejores_exp = exportaciones.sort_values('total_value',ascending=False)


# In[12]:


#Ordenar los datos para sacar las rutas de importación que generan más dinero
mejores_imp = importaciones.sort_values('total_value',ascending=False)


# In[13]:


#Calcular el número de veces que se utilizó cada medio de transporte
filtro_t = archivo.groupby(['direction','transport_mode']).agg(Total_transporte=('transport_mode', 'count'), Total_dinero=('total_value', 'sum'))


# In[14]:


#Calcular los países que generaron más dinero con las exportaciones 
filtro_pais_exp = exportaciones.groupby(['origin']).agg(Total_pais_origen=('origin','count'), Dinero_pais_origen=('total_value','sum'))
ganancias_exp = filtro_pais_exp.sort_values('Dinero_pais_origen',ascending=False)


# In[18]:


#Calcular los países que generaron más dinero con las importaciones 
filtro_pais_imp = importaciones.groupby(['destination']).agg(Total_pais_destino=('destination','count'), Dinero_pais_destino=('total_value','sum'))
ganancias_imp = filtro_pais_imp.sort_values('Dinero_pais_destino',ascending=False)


# In[19]:


opciones = 1
while opciones:
    
    print("\t1 Rutas de importación y exportación con mayor ganancia")
    print("\t2 Rutas de importación y exportación más usadas")
    print("\t3 Medio de transporte utilizado")
    print("\t4 Valor total de importaciones y exportaciones")
    print("\t5 Salir")
    opcion_menu = input("\nSeleccionar una opción: \n")
    
    
    if opcion_menu == '1':
        print("\nRutas de exportación con mayores ganancias\n")
        mejores_exp = exportaciones.sort_values('total_value',ascending=False)
        print(mejores_exp[0:11])
        print("\nRutas de importación con mayores ganancias\n")
        mejores_imp = importaciones.sort_values('total_value',ascending=False)
        print(mejores_imp[0:11],"\n")
        
    elif opcion_menu == '2':
        print("\nRutas de exportación más utilizadas")
        print(top_rutas_exp[0:11])
        print("\nRutas de importación más utilizadas")
        print(top_rutas_imp[0:11],"\n")
        
    elif opcion_menu == '3':
        print("\nEste es el número de veces que se utilizó cada transporte:\n")
        filtro_t = archivo.groupby(['direction','transport_mode']).agg(Total_transporte=('transport_mode', 'count'), Total_dinero=('total_value', 'sum'))
        print(filtro_t,"\n")
        
    elif opcion_menu == '4':
        print("\nPaíses que generaron más dinero con las exportaciones: \n")
        print(ganancias_exp)
        print("\nPaíses que generaron más dinero con las importaciones: \n")
        print(ganancias_imp, "\n")
    
    elif opcion_menu == '5':
        break
    else:
        print("Esta opción no existe")


# In[ ]:




