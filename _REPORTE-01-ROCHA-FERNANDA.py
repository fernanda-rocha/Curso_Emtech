#!/usr/bin/env python
# coding: utf-8

# # Instrucciones
# 
# ### El administrador podrá acceder a las siguientes funciones:
# - Ver los productos más vendidos y más buscados por categoría
# - Ver productos menos vendidos y menos buscados
# - Ver productos por reseña
# - Total de ingresos y ventas
# - Añadir nuevos usuarios
# 
# El usuario del administrador es **Admin** y la contraseña es **0000**
# 
# ### Los usuarios normales solo podrán acceder a las siguientes funciones:
# - Ver los productos más vendidos y más buscados por categoría
# - Ver productos menos vendidos y menos buscados
# 
# Los siguientes usuarios ya están registrados
# - Usuario: **Fer**, contraseña: **1234**
# - Usuario: **Miranda2**,contraseña: **asdfg**
# - Usuario: **Sal01**,contraseña: **chocobo**
# 

# In[1]:


##Se carga el archivo lifestore_file.py
import sys

sys.path.append(r"\Users\Fer\Desktop\Curso Emtech\lifestore_file")
import lifestore_file


# In[2]:


##Se importan las listas lifestore_products, lifestore_sales, lifestore_searches
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches


# In[3]:


##Contador de las ventas totales 
contador_ventas = 0
total_ventas =[]

for productoV in lifestore_products:
    for venta in lifestore_sales:
        if productoV[0] == venta[1]:
            contador_ventas += 1
            
    tot_ventas = [productoV[1],contador_ventas, productoV[3]]
    total_ventas.append(tot_ventas)
    contador_ventas = 0
    


# In[33]:


'''
Contador de las ventas multiplicadas por los precios 
para sacar las ganancias anuales y la ganancia promedio mensual 
'''
contador_precios = 0
total_precios =[]
tot_precios = 0
suma_precios =0 

for productoP in lifestore_products:
    for ventaP in lifestore_sales:
        if productoP[0] == ventaP[1] and ventaP[4] ==0:
            contador_precios += 1
    if contador_precios != 0:
        tot_precios = contador_precios*productoP[2]
        suma_precios = tot_precios + suma_precios
        total_precios.append([contador_precios,productoP[2],tot_precios,suma_precios])
    contador_precios=0
    tot_precios=0
suma_precios =0
promedio_mensual = total_precios[-1][3] / 8


# In[5]:


def mayorVenta(categoria_mV):
    '''
    Función que ordena las ventas de mayor a menor por categoría de producto
    '''
    totalMayor = []
    for categoria in total_ventas:
        if categoria[2] == categoria_mV:           
            totalMayor.append(categoria)

    ordenar_mV = []
    while totalMayor:
        mayor_venta = totalMayor[0][1]
        lista_mayorV = totalMayor[0]
        for mayorV in totalMayor:
            if mayorV[1] > mayor_venta:
                mayor_venta = mayorV[1]
                lista_mayorV = mayorV
        ordenar_mV.append(lista_mayorV)
        totalMayor.remove(lista_mayorV)
    print("\nEstos son los",categoria_mV, "ordenados de mayor a menor venta\n")
    for or_mV in ordenar_mV:
        print('\n',or_mV,'\n')


# In[6]:


def menorVenta(categoria_meV):
    '''
    Función que ordena las ventas de menor a mayor por categoría de producto
    '''
    totalMenor = []
    for categoriaMe in total_ventas:
        if categoriaMe[2] == categoria_meV:           
            totalMenor.append(categoriaMe)

    ordenar_meV = []
    while totalMenor:
        menor_venta = totalMenor[0][1]
        lista_menorV = totalMenor[0]
        for menorV in totalMenor:
            if menorV[1] < menor_venta:
                menor_venta = menorV[1]
                lista_menorV = menorV
        ordenar_meV.append(lista_menorV)
        totalMenor.remove(lista_menorV)
    print("\nEstos son los",categoria_meV, "ordenados de menor a mayor venta\n")
    for or_meV in ordenar_meV:
        print('\n',or_meV,'\n')


# In[7]:


##Contador de las búsquedas totales
contador_busquedas = 0
total_busquedas =[]

for productoS in lifestore_products:
    for busqueda in lifestore_searches:
        if productoS[0] == busqueda[1]:
            contador_busquedas += 1
            
    tot_busquedas = [productoS[1],contador_busquedas, productoS[3]]
    total_busquedas.append(tot_busquedas)
    contador_busquedas = 0


# In[8]:


def mayorBusqueda(categoria_mB):
    '''
    Función que ordena las búsquedas de mayor a menor por categoría de producto
    '''
    totalMayorB = []
    for categoriaB in total_busquedas:
        if categoriaB[2] == categoria_mB:           
            totalMayorB.append(categoriaB)

    ordenar_mB = []
    while totalMayorB:
        mayor_busqueda = totalMayorB[0][1]
        lista_mayorB = totalMayorB[0]
        for mayorB in totalMayorB:
            if mayorB[1] > mayor_busqueda:
                mayor_busqueda = mayorB[1]
                lista_mayorB = mayorB
        ordenar_mB.append(lista_mayorB)
        totalMayorB.remove(lista_mayorB)
    print("\nEstos son los",categoria_mB, "ordenados de mayor a menor búsqueda\n")
    for or_mB in ordenar_mB:
        print('\n',or_mB,'\n')


# In[9]:


def menorBusqueda(categoria_meB):
    '''
    Función que ordena las búsquedas de menor a mayor por categoría de producto
    '''
    totalMenorB = []
    for categoriaMeB in total_busquedas:
        if categoriaMeB[2] == categoria_meB:           
            totalMenorB.append(categoriaMeB)

    ordenar_meB = []
    while totalMenorB:
        menor_busqueda = totalMenorB[0][1]
        lista_menorB = totalMenorB[0]
        for menorB in totalMenorB:
            if menorB[1] < menor_busqueda:
                menor_busqueda = menorB[1]
                lista_menorB = menorB
        ordenar_meB.append(lista_menorB)
        totalMenorB.remove(lista_menorB)
    print("\nEstos son los",categoria_meB, "ordenados de menor a mayor búsqueda\n")
    for or_meB in ordenar_meB:
        print('\n',or_meB,'\n')


# In[10]:


'''
Contador de las reseñas de los productos vendidos
Además saca el promedio de reseña de cada producto
'''
cont_resenas =0
cont_promedio=0
resenas =[]
ceros =[]

for productoR in lifestore_products:
    for ventasR in lifestore_sales:
        if productoR[0] == ventasR[1]:
            cont_promedio += 1
            cont_resenas = ventasR[2] + cont_resenas
    if cont_promedio == 0 or cont_resenas == 0:
            ceros.append([productoR[1], cont_promedio,cont_resenas])
    else:
        promedios = cont_resenas/cont_promedio
        tot_resenas = [productoR[1],promedios]
        resenas.append(tot_resenas)
    
    cont_promedio = 0
    cont_resenas = 0
    


# In[11]:


##Copias de la lista de reseñas 
resenas_copia = resenas.copy()
resenas_copia2 = resenas.copy()


# In[12]:


'''
Ordenar el promedio de reseñas de la más alta a la más baja
'''
ordenar_resenaAlta = []
while resenas_copia:
    mejor_resena = resenas_copia[0][1]
    lista_mejorR = resenas_copia[0]
    for mejorR in resenas_copia:
        if mejorR[1] > mejor_resena:
            mejor_resena = mejorR[1]
            lista_mejorR = mejorR
    ordenar_resenaAlta.append(lista_mejorR)
    resenas_copia.remove(lista_mejorR)


# In[13]:


'''
Ordenar el promedio de reseñas de la más baja a la más alta
'''
ordenar_resenaBaja = []
while resenas_copia2:
    peor_resena = resenas_copia2[0][1]
    lista_peorR = resenas_copia2[0]
    for peorR in resenas_copia2:
        if peorR[1] < peor_resena:
            peor_resena = peorR[1]
            lista_peorR = peorR
    ordenar_resenaBaja.append(lista_peorR)
    resenas_copia2.remove(lista_peorR)


# In[32]:


#Filtro de ventas por mes
enero = []
febrero = []
marzo = []
abril = []
mayo = []
junio = []
julio = []
agosto = []
septiembre = []
octubre = []
noviembre = []
diciembre = []
for mes in lifestore_sales:
    if mes[3][4] == '1' and mes[3][3] == '0' and mes[4] == 0:
        enero.append([mes[1], mes[3]]) 
    elif mes[3][4] == '2' and mes[3][3] == '0' and mes[4] == 0: 
        febrero.append([mes[1], mes[3]]) 
    elif mes[3][4] == '3' and mes[3][3] == '0' and mes[4] == 0: 
        marzo.append([mes[1], mes[3]])
    elif mes[3][4] == '4' and mes[3][3] == '0' and mes[4] == 0: 
        abril.append([mes[1], mes[3]])
    elif mes[3][4] == '5' and mes[3][3] == '0' and mes[4] == 0: 
        mayo.append([mes[1], mes[3]])
    elif mes[3][4] == '6' and mes[3][3] == '0' and mes[4] == 0: 
        junio.append([mes[1], mes[3]])
    elif mes[3][4] == '7' and mes[3][3] == '0' and mes[4] == 0: 
        julio.append([mes[1], mes[3]])
    elif mes[3][4] == '8' and mes[3][3] == '0' and mes[4] == 0: 
        agosto.append([mes[1], mes[3]])
    elif mes[3][4] == '9' and mes[3][3] == '0' and mes[4] == 0: 
        septiembre.append([mes[1], mes[3]])
    elif mes[3][4] == '0' and mes[3][3] == '1' and mes[4] == 0: 
        octubre.append([mes[1], mes[3]])
    elif mes[3][4] == '1' and mes[3][3] == '1' and mes[4] == 0: 
        noviembre.append([mes[1], mes[3]])
    elif mes[3][4] == '2' and mes[3][3] == '1' and mes[4] == 0: 
        diciembre.append([mes[1], mes[3]])


# In[21]:


def totalMes(meses): 
    '''
    Función que saca las ganancias por cada mes
    '''
    contador_ingresos = 0
    dinero = 0
    suma_dinero=0
    total_ingresos =[]
    for productoI in lifestore_products:
        for ventaI in meses:
            if productoI[0] == ventaI[0]:
                contador_ingresos += 1
                dinero = contador_ingresos*productoI[2]    
        if contador_ingresos != 0:
            suma_dinero = dinero + suma_dinero
            total_ingresos.append([contador_ingresos,productoI[2],dinero,suma_dinero]) 

        contador_ingresos = 0
        dinero=0
    suma_dinero=0
    
    print("El total de ganancias fue de",total_ingresos[-1][3],"pesos")


# In[22]:


##Cuentas de administrador y de usuarios
usuarios_normales = [["Fer","1234"],["Miranda2","asdfg"],["Sal01","chocobo"]]
admin = [["Admin","0000"]]


# In[39]:


##Bloque principal del programa
print("Bienvenido al sistema de datos de LifeStore")

opciones = 1
opciones_admin = 1
opciones_usuario = 1
opciones_opciones = 1
while opciones:
    print("\t1 Ingresar como administrador")
    print("\t2 Ingresar como usuario")
    print("\t3 Salir")
    opcion_menu = input("\nSeleccione una opción de login: ")
    
    
    if opcion_menu == '1':
        user_admin = input("\nIngresa tu nombre de usuario: ")
        password_admin = input("\nIngresa tu contraseña: ")
        for usuario_admin in admin:
            if usuario_admin[0] == user_admin and usuario_admin[1] == password_admin:
                print("\nBienvenido administrador")
                opciones = 0
                while opciones_admin:
                    print("\t1 Ver los productos más vendidos y más buscados por categoría")
                    print("\t2 Ver productos menos vendidos y menos buscados por categoría")
                    print("\t3 Ver productos por reseña")
                    print("\t4 Total de ingresos y ventas")
                    print("\t5 Añadir nuevo usuario")
                    print("\t6 Salir")
                    menu_admin = input("\nSeleccione lo que desea hacer: ")
                    
                    if menu_admin == '1':
                        while opciones_opciones:
                            print("\t1 Procesadores")
                            print("\t2 Tarjetas de video")
                            print("\t3 Tarjetas madre")
                            print("\t4 Discos duros")
                            print("\t5 Memorias usb")
                            print("\t6 Pantallas")
                            print("\t7 Bocinas")
                            print("\t8 Audífonos")
                            accion = input("\nElija la categoría que le gustaría ver: ")
                            if accion == '1':
                                mayorVenta('procesadores')
                                mayorBusqueda('procesadores')
                                opciones_opciones = 0
                            elif accion == '2':
                                mayorVenta('tarjetas de video')
                                mayorBusqueda('tarjetas de video')
                                opciones_opciones = 0
                            elif accion == '3':
                                mayorVenta('tarjetas madre')
                                mayorBusqueda('tarjetas madre')
                                opciones_opciones = 0
                            elif accion == '4':
                                mayorVenta('discos duros')
                                mayorBusqueda('discos duros')
                                opciones_opciones = 0
                            elif accion == '5':
                                mayorVenta('memorias usb')
                                mayorBusqueda('memorias usb')
                                opciones_opciones = 0
                            elif accion == '6':
                                mayorVenta('pantallas')
                                mayorBusqueda('pantallas')
                                opciones_opciones = 0
                            elif accion == '7':
                                mayorVenta('bocinas')
                                mayorBusqueda('bocinas')
                                opciones_opciones = 0
                            elif accion == '8':
                                mayorVenta('audifonos')
                                mayorBusqueda('audifonos')
                                opciones_opciones = 0
                            else:
                                print("\nEl producto está mal escrito\n")
                        opciones_admin = 0       
                        
                    elif menu_admin == '2':
                        while opciones_opciones:
                            print("\nElija la categoría que le gustaría ver: ")
                            print("\t1 Procesadores")
                            print("\t2 Tarjetas de video")
                            print("\t3 Tarjetas madre")
                            print("\t4 Discos duros")
                            print("\t5 Memorias usb")
                            print("\t6 Pantallas")
                            print("\t7 Bocinas")
                            print("\t8 Audífonos")
                            accion = input("\nElija la categoría que le gustaría ver: ")
                            if accion == '1':
                                menorVenta('procesadores')
                                menorBusqueda('procesadores')
                                opciones_opciones = 0
                            elif accion == '2':
                                menorVenta('tarjetas de video')
                                menorBusqueda('tarjetas de video')
                                opciones_opciones = 0
                            elif accion == '3':
                                menorVenta('tarjetas madre')
                                menorBusqueda('tarjetas madre')
                                opciones_opciones = 0
                            elif accion == '4':
                                menorVenta('discos duros')
                                menorBusqueda('discos duros')
                                opciones_opciones = 0
                            elif accion == '5':
                                menorVenta('memorias usb')
                                menorBusqueda('memorias usb')
                                opciones_opciones = 0
                            elif accion == '6':
                                menorVenta('pantallas')
                                menorBusqueda('pantallas')
                                opciones_opciones = 0
                            elif accion == '7':
                                menorVenta('bocinas')
                                menorBusqueda('bocinas')
                                opciones_opciones = 0
                            elif accion == '8':
                                menorVenta('audifonos')
                                menorBusqueda('audifonos')
                                opciones_opciones = 0
                            else:
                                print("\nEl producto está mal escrito\n")
                        opciones_admin = 0       
                        
                    elif menu_admin == '3':
                        
                        print("\nEste es el top 20 de productos con mejor promedio de reseñas\n")
                        for i in range(20):
                            print( ordenar_resenaAlta[i],'\n')
                        print("\nEste es el top 20 de productos con peor promedio de reseñas\n")    
                        for index in range(20):
                            print( ordenar_resenaBaja[index],'\n')   
                        opciones_admin = 0  
                        
                    elif menu_admin == '4':
                        while opciones_opciones:
                            print("\nSe pueden ver las ganancias de forma mensual o anual ")
                            print("\t1 Enero")
                            print("\t2 Febrero")
                            print("\t3 Marzo")
                            print("\t4 Abril")
                            print("\t5 Mayo")
                            print("\t6 Junio")
                            print("\t7 Julio")
                            print("\t8 Agosto")
                            print("\t9 Septiembre")
                            print("\t10 Octubre")
                            print("\t11 Noviembre")
                            print("\t12 Diciembre")
                            print("\t13 Anual")
                            accion = input("\nElija las ganancias que quiere ver:\n ")
                            if accion == '1':
                                totalMes(enero)
                                opciones_opciones = 0
                            elif accion == '2':
                                totalMes(febrero)
                                opciones_opciones = 0
                            elif accion == '3':
                                totalMes(marzo)
                                opciones_opciones = 0
                            elif accion == '4':
                                totalMes(abril)
                                opciones_opciones = 0
                            elif accion == '5':
                                totalMes(mayo)
                                opciones_opciones = 0
                            elif accion == '6':
                                totalMes(junio)
                                opciones_opciones = 0
                            elif accion == '7':
                                totalMes(julio)
                                opciones_opciones = 0
                            elif accion == '8':
                                totalMes(agosto)
                                opciones_opciones = 0
                            elif accion == '9':
                                totalMes(septiembre)
                                print("\nAún no hay ganancias este mes\n")
                            elif accion == '10':
                                print("\nAún no hay ganancias este mes\n")
                                opciones_opciones = 0
                            elif accion == '11':
                                print("\nEn este mes solo hubo una venta y después se devolvió\n")
                                opciones_opciones = 0
                            elif accion == '12':
                                print("\nAún no hay ganancias este mes\n")
                                opciones_opciones = 0
                            elif accion == '13':
                                print("\nLa ganancia anual fue de ", total_precios[-1][3],"pesos\n")
                                print("\nEl promedio mensual de ganancias es de ",promedio_mensual,"pesos\n")
                                opciones_opciones = 0
                            else:
                                print("\nEsta opción no está disponible\n")
                        opciones_admin = 0       
                        
                    elif menu_admin == '5':
                        nuevo_usuario = input("\nIngresa un nombre de usuario: ")
                        nuevo_password = input("\nIngresa una contraseña: ")
                        
                        usuarios_normales.append([nuevo_usuario,nuevo_password])
                    
                    elif menu_admin == '6':
                        opciones_admin = 0
                        
                    else:
                        print("\nError. Intente de nuevo")
                
            else:
                print("\nDatos incorrectos")
        
        
    elif opcion_menu == '2':
        user = input("\nIngresa tu nombre de usuario: ")
        password = input("\nIngresa tu contraseña: ")
        for usuario in usuarios_normales:
            if usuario[0] == user and usuario[1] == password:
                opciones = 0
                while opciones_usuario:
                    print("\t1 Ver los productos más vendidos y más buscados por categoría")
                    print("\t2 Ver los productos menos vendidos y menos buscados por categoría")
                    print("\t3 Salir")
                    
                    menu_usuario = input("\nSeleccione lo que desea hacer: ")
                    
                    if menu_usuario == '1':
                        while opciones_opciones:
                            print("\t1 Procesadores")
                            print("\t2 Tarjetas de video")
                            print("\t3 Tarjetas madre")
                            print("\t4 Discos duros")
                            print("\t5 Memorias usb")
                            print("\t6 Pantallas")
                            print("\t7 Bocinas")
                            print("\t8 Audífonos")
                            accion = input("\nElija la categoría que le gustaría ver: ")
                            if accion == '1':
                                mayorVenta('procesadores')
                                mayorBusqueda('procesadores')
                                opciones_opciones = 0
                            elif accion == '2':
                                mayorVenta('tarjetas de video')
                                mayorBusqueda('tarjetas de video')
                                opciones_opciones = 0
                            elif accion == '3':
                                mayorVenta('tarjetas madre')
                                mayorBusqueda('tarjetas madre')
                                opciones_opciones = 0
                            elif accion == '4':
                                mayorVenta('discos duros')
                                mayorBusqueda('discos duros')
                                opciones_opciones = 0
                            elif accion == '5':
                                mayorVenta('memorias usb')
                                mayorBusqueda('memorias usb')
                                opciones_opciones = 0
                            elif accion == '6':
                                mayorVenta('pantallas')
                                mayorBusqueda('pantallas')
                                opciones_opciones = 0
                            elif accion == '7':
                                mayorVenta('bocinas')
                                mayorBusqueda('bocinas')
                                opciones_opciones = 0
                            elif accion == '8':
                                mayorVenta('audifonos')
                                mayorBusqueda('audifonos')
                                opciones_opciones = 0
                            else:
                                print("\nEl producto no existe\n")
                        opciones_usuario = 0          
                    elif menu_usuario == '2':
                        while opciones_opciones:
                            print("\nElija la categoría que le gustaría ver: ")
                            print("\t1 Procesadores")
                            print("\t2 Tarjetas de video")
                            print("\t3 Tarjetas madre")
                            print("\t4 Discos duros")
                            print("\t5 Memorias usb")
                            print("\t6 Pantallas")
                            print("\t7 Bocinas")
                            print("\t8 Audífonos")
                            accion = input("\nElija la categoría que le gustaría ver: ")
                            if accion == '1':
                                menorVenta('procesadores')
                                menorBusqueda('procesadores')
                                opciones_opciones = 0
                            elif accion == '2':
                                menorVenta('tarjetas de video')
                                menorBusqueda('tarjetas de video')
                                opciones_opciones = 0
                            elif accion == '3':
                                menorVenta('tarjetas madre')
                                menorBusqueda('tarjetas madre')
                                opciones_opciones = 0
                            elif accion == '4':
                                menorVenta('discos duros')
                                menorBusqueda('discos duros')
                                opciones_opciones = 0
                            elif accion == '5':
                                menorVenta('memorias usb')
                                menorBusqueda('memorias usb')
                                opciones_opciones = 0
                            elif accion == '6':
                                menorVenta('pantallas')
                                menorBusqueda('pantallas')
                                opciones_opciones = 0
                            elif accion == '7':
                                menorVenta('bocinas')
                                menorBusqueda('bocinas')
                                opciones_opciones = 0
                            elif accion == '8':
                                menorVenta('audifonos')
                                menorBusqueda('audifonos')
                                opciones_opciones = 0
                            else:
                                print("\nEl producto no existe\n")
                        opciones_usuario = 0       
                        
                        
                    elif menu_usuario == '3':
                        opciones_usuario = 0
                
            elif opciones == 1:
                print("\mDatos incorrectos. Intente otra vez o comuníquese con el administrador")
                continue
            
    elif opcion_menu == '3':
        opciones = 0
    
    else:
        print("\nError. Intente de nuevo")


# In[ ]:




