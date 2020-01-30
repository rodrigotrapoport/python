#ATENCION PROFESOR
#Existen dos usuarios con sus respectivos password
#Usuario 1: 12345 y su password es 12345
#Usuario 2: 67890 y su password es 67890

#necesitamos importar el modulo del tiempo para poder dictaminar las fechas de las operaciones mas adelante
from datetime import date
tiempo = date.today()
#para obtener la fecha de hoy se pide con tiempo.date()

#estoy refactorizando el Ejercicio 2 de unidad de Funciones de Python, en el caso que recuerde de lo que estamos trabajando en la misma
#se esta llamando a la api de binance
import requests
_ENDPOINT = "https://api.binance.com"
def _url(api):
    return _ENDPOINT+api

#funcion para obtener el precio de cualquier moneda que va ser utilizada posteriormente
def get_price(cripto):
    return requests.get(_url("/api/v3/ticker/price?symbol="+cripto))

#funcion de mostrar las opciones del menu principal
def mostrar_menu():
    print("")
    print("EL MENU ES:")
    print("")
    print("C. Consulta balance general")
    print("")
    print("M. Consulta balance de una moneda")
    print("")
    print("R. Recibir transferencia")
    print("")
    print("S. Enviar una transferencia")
    print("")
    print("W. Mostrar historia de las transferencias")
    print("")
    print("E. Salir de la billetera")
    print("")
    opcion_de_entrada_menu =  input("Ingresa la letra:")
    return opcion_de_entrada_menu
#def balance_general():
    

#No cree un sistema de registro porque el tutor no pedia parte del ejercicio, para que sea facíl el recorrido de la información,
#la lista_de_usuarios esta relacionado con la misma posición de la lista_de_passwords, las mismas podrías tener una función de registro y guardarse en un archivo, 
#pero no son parte del ejercicio. Para el mismo, se crea dos usuarios para obtener un proceso de transferencia entre los mismos
lista_de_usuarios = [12345,67890]
lista_de_passwords =["12345","67890"]
#Obtenemos los datos del usuario
entrada_usuario = int(input("Codigo de usuario:"))
entrada_de_password_de_usuario = input("Password de Usuario:")
#La idea es validar primero la existencia del usuario, posteriormente la ubicación en la lista para después validar el
#password en la posición respectiva
while not entrada_usuario in lista_de_usuarios:
    #Si el usuario no es valido
    print("Usuario invalido")
    entrada_usuario = int(input("Iniciar usuario nuevamente su codigo de usuario:"))
    entrada_de_password_de_usuario = input("Password de Usuario:")
else:
    #ubicación del usuario en la lista    
    x = lista_de_usuarios.index(entrada_usuario)
    #validacion del usuario
    if lista_de_usuarios[x]==entrada_usuario:   
        #validacion del password
        while not entrada_de_password_de_usuario==lista_de_passwords[x]:
            print("Password invalido")
            entrada_de_password_de_usuario = input("Ingrese el Password de Usuario nuevamente:")
        #si el usuario y el password es valido se accede al menu de opciones
        else:
            print("Felicidades! Ingreso valido!")
            #APERTURA DEL WHILE PARA EL MENU
            #el usuario visualiza el menu y puede seleccionar una opción
            letra = mostrar_menu()
            while letra == "C" or letra == "c" or letra == "M" or letra == "m" or letra == "R" or letra == "r" or letra == "S" or letra == "s" or letra == "W" or letra == "w":
                if letra == "C" or letra == "c":
                    print(
                        "Procesos de opción de menu de Consulta de balance general en dolares")
                    print("")
                    print("CONSULTA DE BALANCE POR GENERAL DE TODAS LAS BILLETERAS")
                    entrada_usuario_str = str(entrada_usuario)
                    #cada moneda tiene su balance por archivo
                    #se abre el archivo, se guarda como lista, se toma la última posición para obtener el valor del estado de la cuenta para despues calcular e imprimir la cantidad que tiene en dolares, con un cierre del archivo para evitar problemas con otras funciones
                    file_btc = open(
                        "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_str+"/btc.txt", "r")
                    lista_billetera_btc = file_btc.readlines()
                    #debemos de asegurarnos que sea un float lo que obtenemos en la lista
                    estado_billetera_btc = float(lista_billetera_btc[-1])
                    #obtenemos el precio de Binance
                    BTCUSD = get_price("BTCUSDT").json()
                    #debemos de asegurarnos que sea un float lo que obtenemos del json
                    monto_btc_usd = estado_billetera_btc * \
                        float(BTCUSD["price"])
                    print("Tu saldo en BTC es: ")
                    print(estado_billetera_btc)
                    print("Tu saldo en BTC en USD es: ")
                    print(monto_btc_usd)
                    file_btc.close()
                    print("")
                    #se abre el archivo, se guarda como lista, se toma la última posición para obtener el valor del estado de la cuenta para despues calcular e imprimir la cantidad que tiene en dolares, con un cierre del archivo para evitar problemas con otras funciones
                    file_eth = open(
                        "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_str+"/eth.txt", "r")
                    lista_billetera_eth = file_eth.readlines()
                    #debemos de asegurarnos que sea un float lo que obtenemos en la lista
                    estado_billetera_eth = float(lista_billetera_eth[-1])
                    #obtenemos el precio de Binance
                    ETHUSD = get_price("ETHUSDT").json()
                    #debemos de asegurarnos que sea un float lo que obtenemos del json
                    monto_eth_usd = estado_billetera_eth * \
                        float(ETHUSD["price"])
                    print("Tu saldo en ETH es: ")
                    print(estado_billetera_eth)
                    print("Tu saldo en ETH en USD es: ")
                    print(monto_eth_usd)
                    file_eth.close()
                    #se abre el archivo, se guarda como lista, se toma la última posición para obtener el valor del estado de la cuenta para despues calcular e imprimir la cantidad que tiene en dolares, con un cierre del archivo para evitar problemas con otras funciones
                    file_ltc = open(
                        "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_str+"/ltc.txt", "r")
                    lista_billetera_ltc = file_ltc.readlines()
                    #debemos de asegurarnos que sea un float lo que obtenemos en la lista
                    estado_billetera_ltc = float(lista_billetera_ltc[-1])
                    #obtenemos el precio de Binance
                    LTCUSD = get_price("LTCUSDT").json()
                    #debemos de asegurarnos que sea un float lo que obtenemos del json
                    monto_ltc_usd = estado_billetera_ltc * \
                        float(LTCUSD["price"])
                    print("Tu saldo en LTC es: ")
                    print(estado_billetera_ltc)
                    print("Tu saldo en LTC en USD es: ")
                    print(monto_ltc_usd)
                    file_ltc.close()
                    #se abre el archivo, se guarda como lista, se toma la última posición para obtener el valor del estado de la cuenta para despues calcular e imprimir la cantidad que tiene en dolares, con un cierre del archivo para evitar problemas con otras funciones
                    file_usdt = open(
                        "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_str+"/usdt.txt", "r")
                    lista_billetera_usdt = file_usdt.readlines()
                    #debemos de asegurarnos que sea un float lo que obtenemos en la lista
                    estado_billetera_usdt = float(lista_billetera_usdt[-1])
                    #a diferencia de las demas cuentas el USD o USDT es una stable coin
                    monto_usdt = estado_billetera_usdt
                    print("Tu saldo en USD es: ")
                    print(monto_usdt)
                    print("Tu balance en dolares incluyendo todas tus billeteras es:")
                    monto_total_en_dolares = monto_usdt+monto_ltc_usd+monto_eth_usd+monto_btc_usd
                    print(monto_total_en_dolares)
                    file_usdt.close()
                    letra = mostrar_menu()
                elif letra == "M" or letra == "m":
                    print("")
                    print("CONSULTA DE BALANCE POR MONEDA")
                    entrada_usuario_str = str(entrada_usuario)
                    #cada moneda tiene su balance por archivo
                    print("")
                    moneda = input(
                        "Ingrese la moneda a consultar (BTC, LTC o ETH o USD): ")
                    if moneda == "BTC" or moneda == "btc" or moneda == "ETH" or moneda == "eth" or moneda == "LTC" or moneda == "ltc" or moneda == "USD" or moneda == "usd":
                        if moneda == "BTC" or moneda == "btc":
                            #se abre el archivo, se guarda como lista, se toma la última posición para obtener el valor del estado de la cuenta para despues calcular e imprimir la cantidad que tiene en dolares, con un cierre del archivo para evitar problemas con otras funciones
                            file_btc = open(
                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_str+"/btc.txt", "r")
                            lista_billetera_btc = file_btc.readlines()
                            #debemos de asegurarnos que sea un float lo que obtenemos en la lista
                            estado_billetera_btc = float(
                                lista_billetera_btc[-1])
                            #obtenemos el precio de Binance
                            BTCUSD = get_price("BTCUSDT").json()
                            #debemos de asegurarnos que sea un float lo que obtenemos del json
                            monto_btc_usd = estado_billetera_btc * float(BTCUSD["price"])
                            print("Tu saldo en BTC es: ")
                            print(estado_billetera_btc)
                            print("Tu saldo en BTC en USD es: ")
                            print(monto_btc_usd)
                            file_btc.close()
                            print("")
                            letra = mostrar_menu()
                        elif moneda == "ETH" or moneda == "eth":
                            #se abre el archivo, se guarda como lista, se toma la última posición para obtener el valor del estado de la cuenta para despues calcular e imprimir la cantidad que tiene en dolares, con un cierre del archivo para evitar problemas con otras funciones
                            file_eth = open(
                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_str+"/eth.txt", "r")
                            lista_billetera_eth = file_eth.readlines()
                            #debemos de asegurarnos que sea un float lo que obtenemos en la lista
                            estado_billetera_eth = float(
                                lista_billetera_eth[-1])
                            #obtenemos el precio de Binance
                            ETHUSD = get_price("ETHUSDT").json()
                            #debemos de asegurarnos que sea un float lo que obtenemos del json
                            monto_eth_usd = estado_billetera_eth * float(ETHUSD["price"])
                            print("Tu saldo en ETH es: ")
                            print(estado_billetera_eth)
                            print("Tu saldo en ETH en USD es: ")
                            print(monto_eth_usd)
                            file_eth.close()
                            print("")
                            letra = mostrar_menu()
                        elif moneda == "LTC" or moneda == "ltc":
                            #se abre el archivo, se guarda como lista, se toma la última posición para obtener el valor del estado de la cuenta para despues calcular e imprimir la cantidad que tiene en dolares, con un cierre del archivo para evitar problemas con otras funciones
                            file_ltc = open(
                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_str+"/ltc.txt", "r")
                            lista_billetera_ltc = file_ltc.readlines()
                            #debemos de asegurarnos que sea un float lo que obtenemos en la lista
                            estado_billetera_ltc = float(
                                lista_billetera_ltc[-1])
                            #obtenemos el precio de Binance
                            LTCUSD = get_price("LTCUSDT").json()
                            #debemos de asegurarnos que sea un float lo que obtenemos del json
                            monto_ltc_usd = estado_billetera_ltc * float(LTCUSD["price"])
                            print("Tu saldo en LTC es: ")
                            print(estado_billetera_ltc)
                            print("Tu saldo en LTC en USD es: ")
                            print(monto_ltc_usd)
                            file_ltc.close()
                            print("")
                            letra = mostrar_menu()
                        else:
                            #se abre el archivo, se guarda como lista, se toma la última posición para obtener el valor del estado de la cuenta para despues calcular e imprimir la cantidad que tiene en dolares, con un cierre del archivo para evitar problemas con otras funciones
                            file_usdt = open(
                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_str+"/usdt.txt", "r")
                            lista_billetera_usdt = file_usdt.readlines()
                            #debemos de asegurarnos que sea un float lo que obtenemos en la lista
                            estado_billetera_usdt = float(
                                lista_billetera_usdt[-1])
                            #a diferencia de las demas cuentas el USD o USDT es una stable coin
                            monto_usdt = estado_billetera_usdt
                            print("Tu saldo en USD es: ")
                            print(monto_usdt)
                            file_usdt.close()
                            print("")
                            letra = mostrar_menu()
                    else:
                        print("Error: Solo se permite utilizar BTC, LTC o ETH o USD")
                        print("")
                        letra = mostrar_menu()
                elif letra == "R" or letra == "r":
                    print("PROCESO DE PEDIDO PARA RECEPCIÓN DE TRANSFERENCIA")
                    entrada_usuario_recibe_str = str(entrada_usuario)
                    moneda = input("Ingrese la moneda a que quiere recibir (BTC, LTC o ETH o USD): ")
                    if moneda == "BTC" or moneda == "btc" or moneda == "ETH" or moneda == "eth" or moneda == "LTC" or moneda == "ltc" or moneda == "USD" or moneda == "usd":
                        if moneda == "BTC" or moneda == "btc":
                            #validacion del usuario que envia el dinero
                            entrada_usuario_que_envia = input("Ingrese el Usuario que va pedirle: ")
                            #validacion del usuario
                            while not int(entrada_usuario_que_envia) in lista_de_usuarios:
                                print("Usuario invalido")
                                entrada_usuario_que_envia = input("Ingrese el Usuario que va pedirle nuevamente: ")
                                #si el usuario es valido se accede al menu de opciones
                            else:
                                print("Usuario solicitante valido!")
                                entrada_usuario_que_envia_str = str(entrada_usuario_que_envia)
                                monto_a_recibir = float(input("Ingrese el monto a recibir: "))
                                #QUIEN ENVIA
                                #se abre el archivo del quien envia, se guarda como lista, se toma la última posición para obtener el valor del estado de la cuenta para despues calcular y validar el monto a enviar, con un cierre del archivo para evitar problemas con la posterior escritura
                                file_btc_envia = open("/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/btc.txt", "r")
                                lista_billetera_btc_envia = file_btc_envia.readlines()
                                #debemos de asegurarnos que sea un float lo que obtenemos en la lista
                                estado_billetera_btc_envia = float(lista_billetera_btc_envia[-1])
                                file_btc_envia.close()
                                file_btc_envia = open("/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/btc.txt", "a")
                                while monto_a_recibir > estado_billetera_btc_envia:
                                    print("El usuario no tiene los fondos que le solicita")
                                    monto_a_recibir = float(input("Ingrese el nuevo monto a recibir: "))
                                else:
                                    #Grabar el resto de lo que le queda al QUIEN ENVIA
                                    resto_de_la_billetera_del_envia = estado_billetera_btc_envia - monto_a_recibir
                                    file_btc_envia.write("\n"+str(resto_de_la_billetera_del_envia))
                                    file_btc_envia.close()
                                    #Primero leer y despues escribir la obtención de las nuevas monedas en RECEPTOR
                                    file_btc_receptor = open("/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_recibe_str+"/btc.txt", "r")
                                    lista_billetera_btc_receptor = file_btc_receptor.readlines()
                                    estado_billetera_btc_receptor = float(
                                    lista_billetera_btc_receptor[-1])
                                    monto_nuevo_receptor = estado_billetera_btc_receptor + monto_a_recibir
                                    file_btc_receptor.close()
                                    #se escribe en el archivo
                                    file_btc_receptor = open("/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_recibe_str+"/btc.txt", "a")
                                    valorhoy = get_price("BTCUSDT").json()
                                    monto_en_dolares = float(monto_a_recibir) * float(valorhoy["price"])
                                    file_btc_receptor.write("\n"+str(monto_nuevo_receptor))
                                    print("Usted a recibio en BTC el monto:")
                                    print(monto_a_recibir)
                                    print("Su saldo actual en BTC es:")
                                    print(monto_nuevo_receptor)
                                    print("El valor actual de la recepción en dólares es:")
                                    print(monto_en_dolares)
                                    file_btc_receptor.close()
                                    #Escribir la transacción en el HISTORIAL del RECEPTOR
                                    #Vamos a escribir en el archivo una lista_historial_receptor con el siguiente orden
                                    #fecha, moneda, tipo de operación, código del usuario, cantidad y monto para el momento.
                                    file_historial_receptor = open("/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_recibe_str+"/historial.txt", "a")
                                    file_historial_receptor.write("\n"+"1. Fecha:"+tiempo.strftime("%d/%m/%y")+" - "+"2. Moneda: BTC - "+"3. Tipo de transacción: RECEPCIÓN - "+"4. Usuario: "+entrada_usuario_que_envia_str+" - "+"5. Monto recibido: "+str(monto_a_recibir)+" - "+"6. Monto recibido en dólares: "+str(monto_en_dolares))
                                    file_historial_receptor.close()
                                    #se abre  para escribir el archivo de HISTORIAL del QUIEN ENVIA
                                    file_historial_envia = open("/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/historial.txt", "a")
                                    file_historial_envia.write("\n"+"1. Fecha:"+tiempo.strftime("%d/%m/%y")+" - "+"2. Moneda: BTC - "+"3. Tipo de transacción: ENVIO - "+"4. Usuario: "+entrada_usuario_recibe_str+" - "+"5. Monto enviado: "+str(monto_a_recibir)+" - "+"6. Monto enviado en dólares: "+str(monto_en_dolares))
                                    file_historial_envia.close()
                                    #se vuelve al menu
                                    print("")
                                    #MOSTRAR MENU
                                    letra = mostrar_menu()
                        elif moneda == "ETH" or moneda == "eth":
                            #validacion del usuario que envia el dinero
                            entrada_usuario_que_envia = input("Ingrese el Usuario que va pedirle: ")
                            #validacion del usuario
                            while not int(entrada_usuario_que_envia) in lista_de_usuarios:
                                print("Usuario invalido")
                                entrada_usuario_que_envia = input("Ingrese el Usuario que va pedirle nuevamente: ")
                            #si el usuario es valido se accede al menu de opciones
                            else:
                                print("Usuario solicitante valido!")
                                entrada_usuario_que_envia_str = str(entrada_usuario_que_envia)
                                monto_a_recibir = float(input("Ingrese el monto a recibir: "))
                                #QUIEN ENVIA
                                #se abre el archivo del quien envia, se guarda como lista, se toma la última posición para obtener el valor del estado de la cuenta para despues calcular y validar el monto a enviar, con un cierre del archivo para evitar problemas con la posterior escritura
                                file_eth_envia = open("/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/eth.txt", "r")
                                lista_billetera_eth_envia = file_eth_envia.readlines()
                                #debemos de asegurarnos que sea un float lo que obtenemos en la lista
                                estado_billetera_eth_envia = float(lista_billetera_eth_envia[-1])
                                file_eth_envia.close()
                                file_eth_envia = open("/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/eth.txt", "a")
                                while monto_a_recibir > estado_billetera_eth_envia:
                                    print("El usuario no tiene los fondos que le solicita")
                                    monto_a_recibir = float(input("Ingrese el nuevo monto a recibir: "))
                                else:
                                    #Grabar el resto de lo que le queda al QUIEN ENVIA
                                    resto_de_la_billetera_del_envia = estado_billetera_eth_envia - monto_a_recibir
                                    file_eth_envia.write("\n"+str(resto_de_la_billetera_del_envia))
                                    file_eth_envia.close()
                                    #Primero leer y despues escribir la obtención de las nuevas monedas en RECEPTOR
                                    file_eth_receptor = open("/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_recibe_str+"/eth.txt", "r")
                                    lista_billetera_eth_receptor = file_eth_receptor.readlines()
                                    estado_billetera_eth_receptor = float(lista_billetera_eth_receptor[-1])
                                    monto_nuevo_receptor = estado_billetera_eth_receptor + monto_a_recibir
                                    file_eth_receptor.close()
                                    #se escribe en el archivo
                                    file_eth_receptor = open("/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_recibe_str+"/eth.txt", "a")
                                    valorhoy = get_price("ETHUSDT").json()
                                    monto_en_dolares = float(
                                    monto_a_recibir) * float(valorhoy["price"])
                                    file_eth_receptor.write("\n"+str(monto_nuevo_receptor))
                                    print("Usted a recibio en ETH el monto:")
                                    print(monto_a_recibir)
                                    print("Su saldo actual en ETH es:")
                                    print(monto_nuevo_receptor)
                                    print("El valor actual de la recepción en dólares es:")
                                    print(monto_en_dolares)
                                    file_eth_receptor.close()
                                    #Escribir la transacción en el HISTORIAL del RECEPTOR
                                    #Vamos a escribir en el archivo una lista_historial_receptor con el siguiente orden
                                    #fecha, moneda, tipo de operación, código del usuario, cantidad y monto para el momento.
                                    file_historial_receptor = open("/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_recibe_str+"/historial.txt", "a")
                                    file_historial_receptor.write("\n"+"1. Fecha:"+tiempo.strftime("%d/%m/%y")+" - "+"2. Moneda: ETH - "+"3. Tipo de transacción: RECEPCIÓN - "+"4. Usuario: "+entrada_usuario_que_envia_str+" - "+"5. Monto recibido: "+str(monto_a_recibir)+" - "+"6. Monto recibido en dólares: "+str(monto_en_dolares))
                                    file_historial_receptor.close()
                                    #se abre  para escribir el archivo de HISTORIAL del QUIEN ENVIA
                                    file_historial_envia = open("/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/historial.txt", "a")
                                    file_historial_envia.write("\n"+"1. Fecha:"+tiempo.strftime("%d/%m/%y")+" - "+"2. Moneda: ETH - "+"3. Tipo de transacción: ENVIO - "+"4. Usuario: "+entrada_usuario_recibe_str+" - "+"5. Monto enviado: "+str(monto_a_recibir)+" - "+"6. Monto enviado en dólares: "+str(monto_en_dolares))
                                    file_historial_envia.close()
                                    #se vuelve al menu
                                    print("")
                                    #MOSTRAR MENU
                                    letra = mostrar_menu()
                        elif moneda == "LTC" or moneda == "ltc":
                            #validacion del usuario que envia el dinero
                            entrada_usuario_que_envia = input("Ingrese el Usuario que va pedirle: ")
                            #validacion del usuario
                            while not int(entrada_usuario_que_envia) in lista_de_usuarios:
                                print("Usuario invalido")
                                entrada_usuario_que_envia = input("Ingrese el Usuario que va pedirle nuevamente: ")
                                #si el usuario es valido se accede al menu de opciones
                            else:
                                print("Usuario solicitante valido!")
                                entrada_usuario_que_envia_str = str(entrada_usuario_que_envia)
                                monto_a_recibir = float(input("Ingrese el monto a recibir: "))
                                #QUIEN ENVIA
                                #se abre el archivo del quien envia, se guarda como lista, se toma la última posición para obtener el valor del estado de la cuenta para despues calcular y validar el monto a enviar, con un cierre del archivo para evitar problemas con la posterior escritura
                                file_ltc_envia = open("/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/ltc.txt", "r")
                                lista_billetera_ltc_envia = file_ltc_envia.readlines()
                                #debemos de asegurarnos que sea un float lo que obtenemos en la lista
                                estado_billetera_ltc_envia = float(lista_billetera_ltc_envia[-1])
                                file_ltc_envia.close()
                                file_ltc_envia = open("/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/ltc.txt", "a")
                                while monto_a_recibir > estado_billetera_ltc_envia:
                                    print("El usuario no tiene los fondos que le solicita")
                                    monto_a_recibir = float(input("Ingrese el nuevo monto a recibir: "))
                                else:
                                    #Grabar el resto de lo que le queda al QUIEN ENVIA
                                    resto_de_la_billetera_del_envia = estado_billetera_ltc_envia - monto_a_recibir
                                    file_ltc_envia.write("\n"+str(resto_de_la_billetera_del_envia))
                                    file_ltc_envia.close()
                                    #Primero leer y despues escribir la obtención de las nuevas monedas en RECEPTOR
                                    file_ltc_receptor = open( "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_recibe_str+"/ltc.txt", "r")
                                    lista_billetera_ltc_receptor = file_ltc_receptor.readlines()
                                    estado_billetera_ltc_receptor = float(lista_billetera_ltc_receptor[-1])
                                    monto_nuevo_receptor = estado_billetera_ltc_receptor + monto_a_recibir
                                    file_ltc_receptor.close()
                                    #se escribe en el archivo
                                    file_ltc_receptor = open("/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_recibe_str+"/ltc.txt", "a")
                                    valorhoy = get_price("LTCUSDT").json()
                                    monto_en_dolares = float(monto_a_recibir) * float(valorhoy["price"])
                                    file_ltc_receptor.write("\n"+str(monto_nuevo_receptor))
                                    print("Usted a recibio en LTC el monto:")
                                    print(monto_a_recibir)
                                    print("Su saldo actual en LTC es:")
                                    print(monto_nuevo_receptor)
                                    print("El valor actual de la recepción en dólares es:")
                                    print(monto_en_dolares)
                                    file_ltc_receptor.close()
                                    #Escribir la transacción en el HISTORIAL del RECEPTOR
                                    #Vamos a escribir en el archivo una lista_historial_receptor con el siguiente orden
                                    #fecha, moneda, tipo de operación, código del usuario, cantidad y monto para el momento.
                                    file_historial_receptor = open("/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_recibe_str+"/historial.txt", "a")
                                    file_historial_receptor.write("\n"+"1. Fecha:"+tiempo.strftime("%d/%m/%y")+" - "+"2. Moneda: LTC - "+"3. Tipo de transacción: RECEPCIÓN - "+"4. Usuario: "+entrada_usuario_que_envia_str+" - "+"5. Monto recibido: "+str(monto_a_recibir)+" - "+"6. Monto recibido en dólares: "+str(monto_en_dolares))
                                    file_historial_receptor.close()
                                    #se abre  para escribir el archivo de HISTORIAL del QUIEN ENVIA
                                    file_historial_envia = open("/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/historial.txt", "a")
                                    file_historial_envia.write("\n"+"1. Fecha:"+tiempo.strftime("%d/%m/%y")+" - "+"2. Moneda: LTC - "+"3. Tipo de transacción: ENVIO - "+"4. Usuario: "+entrada_usuario_recibe_str+" - "+"5. Monto enviado: "+str(monto_a_recibir)+" - "+"6. Monto enviado en dólares: "+str(monto_en_dolares))
                                    file_historial_envia.close()
                                    #se vuelve al menu
                                    print("")
                                    #MOSTRAR MENU
                                    letra = mostrar_menu()
                        else:
                            #validacion del usuario que envia el dinero
                            entrada_usuario_que_envia = input("Ingrese el Usuario que va pedirle: ")
                            #validacion del usuario
                            while not int(entrada_usuario_que_envia) in lista_de_usuarios:
                                print("Usuario invalido")
                                entrada_usuario_que_envia = input("Ingrese el Usuario que va pedirle nuevamente: ")
                                #si el usuario es valido se accede al menu de opciones
                            else:
                                print("Usuario solicitante valido!")
                                entrada_usuario_que_envia_str = str(entrada_usuario_que_envia)
                                monto_a_recibir = float(input("Ingrese el monto a recibir: "))
                                #QUIEN ENVIA
                                #se abre el archivo del quien envia, se guarda como lista, se toma la última posición para obtener el valor del estado de la cuenta para despues calcular y validar el monto a enviar, con un cierre del archivo para evitar problemas con la posterior escritura
                                file_usd_envia = open("/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/usdt.txt", "r")
                                lista_billetera_usd_envia = file_usd_envia.readlines()
                                #debemos de asegurarnos que sea un float lo que obtenemos en la lista
                                estado_billetera_usd_envia = float(lista_billetera_usd_envia[-1])
                                file_usd_envia.close()
                                file_usd_envia = open("/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/usdt.txt", "a")
                                while monto_a_recibir > estado_billetera_usd_envia:
                                    print("El usuario no tiene los fondos que le solicita")
                                    monto_a_recibir = float(input("Ingrese el nuevo monto a recibir: "))
                                else:
                                    #Grabar el resto de lo que le queda al QUIEN ENVIA
                                    resto_de_la_billetera_del_envia = estado_billetera_usd_envia - monto_a_recibir
                                    file_usd_envia.write("\n"+str(resto_de_la_billetera_del_envia))
                                    file_usd_envia.close()
                                    #Primero leer y despues escribir la obtención de las nuevas monedas en RECEPTOR
                                    file_usd_receptor = open("/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_recibe_str+"/usdt.txt", "r")
                                    lista_billetera_usd_receptor = file_usd_receptor.readlines()
                                    estado_billetera_usd_receptor = float(
                                    lista_billetera_usd_receptor[-1])
                                    monto_nuevo_receptor = estado_billetera_usd_receptor + monto_a_recibir
                                    file_usd_receptor.close()
                                    #se escribe en el archivo
                                    file_usd_receptor = open("/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_recibe_str+"/usdt.txt", "a")
                                    file_usd_receptor.write("\n"+str(monto_nuevo_receptor))
                                    print("Usted a recibio en USD el monto:")
                                    print(monto_a_recibir)
                                    print("Su saldo actual en USD es:")
                                    print(monto_nuevo_receptor)
                                    file_usd_receptor.close()
                                    #Escribir la transacción en el HISTORIAL del RECEPTOR
                                    #Vamos a escribir en el archivo una lista_historial_receptor con el siguiente orden
                                    #fecha, moneda, tipo de operación, código del usuario, cantidad y monto para el momento.
                                    file_historial_receptor = open("/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_recibe_str+"/historial.txt", "a")
                                    file_historial_receptor.write("\n"+"1. Fecha:"+tiempo.strftime("%d/%m/%y")+" - "+"2. Moneda: USD - "+"3. Tipo de transacción: RECEPCIÓN - "+"4. Usuario: "+entrada_usuario_que_envia_str+" - "+"5 y 6. Monto recibido: "+str(monto_a_recibir))
                                    file_historial_receptor.close()
                                    #se abre  para escribir el archivo de HISTORIAL del QUIEN ENVIA
                                    file_historial_envia = open("/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/historial.txt", "a")
                                    file_historial_envia.write("\n"+"1. Fecha:"+tiempo.strftime("%d/%m/%y")+" - "+"2. Moneda: BTC - "+"3. Tipo de transacción: ENVIO - "+"4. Usuario: "+entrada_usuario_recibe_str+" - "+"5 y 6. Monto enviado: "+str(monto_a_recibir))
                                    file_historial_envia.close()
                                    #se vuelve al menu
                                    print("")
                                    #MOSTRAR MENU
                                    letra = mostrar_menu()
                    else:
                        print("Error: Solo se permite utilizar BTC, LTC o ETH o USD")
                        print("")
                        letra = mostrar_menu()
                elif letra == "S" or letra == "s":
                    print("PROCESO DE ENVIO DE TRANSFERENCIA")
                    entrada_usuario_que_envia_str = str(entrada_usuario)
                    moneda = input(
                        "Ingrese de la billetera que le gustaría enviar (BTC, LTC o ETH o USD): ")
                    if moneda == "BTC" or moneda == "btc" or moneda == "ETH" or moneda == "eth" or moneda == "LTC" or moneda == "ltc" or moneda == "USD" or moneda == "usd":
                        if moneda == "BTC" or moneda == "btc":
                            #validacion del usuario que recibe el dinero
                            entrada_usuario_que_recibe = input(
                                "Ingrese el Usuario que va recibir su transferencia: ")
                            entrada_usuario_recibe_str = str(entrada_usuario_que_recibe)
                            #validacion del usuario
                            while not int(entrada_usuario_que_recibe) in lista_de_usuarios:
                                print("Usuario invalido")
                                entrada_usuario_que_recibe = input(
                                    "Ingrese el Usuario que va recibir su transferencia nuevamente: ")
                                #si el usuario es valido se accede al menu de opciones
                            else:
                                print("Usuario que le va transferir es valido!")
                                entrada_usuario_que_recibe_str = str(entrada_usuario_que_recibe)
                                decision_dolar_cripto = input(
                                    "Usted quiere configurar el monto en dólares o en la criptomoneda? ´D´ para dólares y ´C´ en la criptmonedas: ")
                                #Usuario toma la decision de mandar el monto desde la cantidad de dolares o desde la criptmoneda
                                while decision_dolar_cripto == "D" or decision_dolar_cripto == "d" or decision_dolar_cripto == "C" or decision_dolar_cripto == "c":
                                    #OPCION DOLAR
                                    if decision_dolar_cripto == "D" or decision_dolar_cripto == "d":
                                        monto_a_enviar = float(
                                            input("Ingrese el monto a enviar: "))
                                        #QUIEN ENVIA
                                        #se abre el archivo del quien envia, se guarda como lista, se toma la última posición para obtener el valor del estado de la cuenta para despues calcular y validar el monto a enviar, con un cierre del archivo para evitar problemas con la posterior escritura
                                        file_btc_envia = open(
                                            "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/btc.txt", "r")
                                        lista_billetera_btc_envia = file_btc_envia.readlines()
                                        #debemos de asegurarnos que sea un float lo que obtenemos en la lista
                                        estado_billetera_btc_envia = float(
                                            lista_billetera_btc_envia[-1])
                                        #cerramos el archivo
                                        file_btc_envia.close()
                                        #obtenemos el precio de Binance
                                        btcusd = get_price("BTCUSDT").json()
                                        #debemos de asegurarnos que sea un float lo que obtenemos del json
                                        estado_billetera_btc_usd_envia = estado_billetera_btc_envia * \
                                            float(btcusd["price"])
                                        while monto_a_enviar > estado_billetera_btc_usd_envia:
                                            print("No tiene los fondos que quiere enviar")
                                            monto_a_enviar = float(
                                                input("Ingrese el nuevo monto a enviar: "))
                                        else:
                                            #Grabar el resto de lo que le queda al QUIEN ENVIA
                                            file_btc_envia = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/btc.txt", "a")
                                            monto_a_enviar_en_btc = monto_a_enviar / \
                                                float(btcusd["price"])
                                            resto_de_la_billetera_del_envia = estado_billetera_btc_envia - monto_a_enviar_en_btc
                                            file_btc_envia.write(
                                                "\n"+str(resto_de_la_billetera_del_envia))
                                            file_btc_envia.close()
                                            #Primero leer y despues escribir la obtención de las nuevas monedas en RECEPTOR
                                            file_btc_receptor = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_recibe_str+"/btc.txt", "r")
                                            lista_billetera_btc_receptor = file_btc_receptor.readlines()
                                            estado_billetera_btc_receptor = float(
                                                lista_billetera_btc_receptor[-1])
                                            monto_nuevo_receptor = estado_billetera_btc_receptor + monto_a_enviar_en_btc
                                            file_btc_receptor.close()
                                            #se escribe en el archivo
                                            file_btc_receptor = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_recibe_str+"/btc.txt", "a")
                                            file_btc_receptor.write("\n"+str(monto_nuevo_receptor))
                                            print("Usted a enviado en BTC el monto:")
                                            print(monto_a_enviar_en_btc)
                                            print("Su saldo actual en BTC es:")
                                            print(resto_de_la_billetera_del_envia)
                                            print("El valor actual del envio en dólares es:")
                                            print(monto_a_enviar)
                                            file_btc_receptor.close()
                                            #Escribir la transacción en el HISTORIAL del RECEPTOR
                                            #Vamos a escribir en el archivo una lista_historial_receptor con el siguiente orden
                                            #fecha, moneda, tipo de operación, código del usuario, cantidad y monto para el momento.
                                            file_historial_receptor = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_recibe_str+"/historial.txt", "a")
                                            file_historial_receptor.write("\n"+"1. Fecha:"+tiempo.strftime("%d/%m/%y")+" - "+"2. Moneda: BTC - "+"3. Tipo de transacción: RECEPCIÓN - "+"4. Usuario: " +
                                                                          entrada_usuario_que_envia_str+" - "+"5. Monto recibido: "+str(monto_a_enviar_en_btc)+" - "+"6. Monto recibido en dólares: "+str(monto_a_enviar))
                                            file_historial_receptor.close()
                                            #se abre  para escribir el archivo de HISTORIAL del QUIEN ENVIA
                                            file_historial_envia = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/historial.txt", "a")
                                            file_historial_envia.write("\n"+"1. Fecha:"+tiempo.strftime("%d/%m/%y")+" - "+"2. Moneda: BTC - "+"3. Tipo de transacción: ENVIO - "+"4. Usuario: " +
                                                                       entrada_usuario_que_recibe_str+" - "+"5. Monto enviado: "+str(monto_a_enviar_en_btc)+" - "+"6. Monto enviado en dólares: "+str(monto_a_enviar))
                                            file_historial_envia.close()
                                            #se vuelve al menu
                                            print("")
                                            #MOSTRAR MENU
                                            print("Muchas gracias por usar la billetera")
                                            break
                                            #letra = mostrar_menu()
                                    #OPCION CRIPTOMONEDA
                                    elif decision_dolar_cripto == "C" or decision_dolar_cripto == "c":
                                        monto_a_enviar = float(
                                            input("Ingrese el monto a enviar: "))
                                        file_btc_envia = open(
                                            "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/btc.txt", "r")
                                        lista_billetera_btc_envia = file_btc_envia.readlines()
                                        #debemos de asegurarnos que sea un float lo que obtenemos en la lista
                                        estado_billetera_btc_envia = float(
                                            lista_billetera_btc_envia[-1])
                                        #cerramos el archivo
                                        file_btc_envia.close()
                                        while monto_a_enviar > estado_billetera_btc_envia:
                                            print("El usuario no tiene los fondos que desea enviar")
                                            monto_a_enviar = float(
                                                input("Ingrese el nuevo monto a enviar: "))
                                        else:
                                            #Grabar el resto de lo que le queda al QUIEN ENVIA
                                            file_btc_envia = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/btc.txt", "a")
                                            resto_de_la_billetera_del_envia = estado_billetera_btc_envia - monto_a_enviar
                                            file_btc_envia.write(
                                                "\n"+str(resto_de_la_billetera_del_envia))
                                            file_btc_envia.close()
                                            #Primero leer y despues escribir la obtención de las nuevas monedas en RECEPTOR
                                            file_btc_receptor = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_recibe_str+"/btc.txt", "r")
                                            lista_billetera_btc_receptor = file_btc_receptor.readlines()
                                            estado_billetera_btc_receptor = float(
                                                lista_billetera_btc_receptor[-1])
                                            monto_nuevo_receptor = estado_billetera_btc_receptor + monto_a_enviar
                                            file_btc_receptor.close()
                                            #se escribe en el archivo
                                            file_btc_receptor = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_recibe_str+"/btc.txt", "a")
                                            valorhoy = get_price("BTCUSDT").json()
                                            monto_en_dolares = float(
                                                monto_a_enviar) * float(valorhoy["price"])
                                            file_btc_receptor.write("\n"+str(monto_nuevo_receptor))
                                            #Texto dirigido al quien envia
                                            print("Usted a enviado en BTC el monto:")
                                            print(monto_a_enviar)
                                            print("Su saldo actual en BTC es:")
                                            print(resto_de_la_billetera_del_envia)
                                            print("El valor actual de la recepción en dólares es:")
                                            print(monto_en_dolares)
                                            file_btc_receptor.close()
                                            #Escribir la transacción en el HISTORIAL del RECEPTOR
                                            #Vamos a escribir en el archivo una lista_historial_receptor con el siguiente orden
                                            #fecha, moneda, tipo de operación, código del usuario, cantidad y monto para el momento.
                                            file_historial_receptor = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_recibe_str+"/historial.txt", "a")
                                            file_historial_receptor.write("\n"+"1. Fecha:"+tiempo.strftime("%d/%m/%y")+" - "+"2. Moneda: BTC - "+"3. Tipo de transacción: RECEPCIÓN - "+"4. Usuario: " +
                                                                          entrada_usuario_que_envia_str+" - "+"5. Monto recibido: "+str(monto_a_enviar)+" - "+"6. Monto recibido en dólares: "+str(monto_en_dolares))
                                            file_historial_receptor.close()
                                            #se abre  para escribir el archivo de HISTORIAL del QUIEN ENVIA
                                            file_historial_envia = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/historial.txt", "a")
                                            file_historial_envia.write("\n"+"1. Fecha:"+tiempo.strftime("%d/%m/%y")+" - "+"2. Moneda: BTC - "+"3. Tipo de transacción: ENVIO - "+"4. Usuario: " +
                                                                       entrada_usuario_recibe_str+" - "+"5. Monto enviado: "+str(monto_a_enviar)+" - "+"6. Monto enviado en dólares: "+str(monto_en_dolares))
                                            file_historial_envia.close()
                                            #se vuelve al menu
                                            print("")
                                            print("Muchas gracias por usar la billetera")
                                            break
                                            #MOSTRAR MENU
                                            #letra = mostrar_menu()
                                            #este es el else de la decisión si dolar o cripto
                                else:
                                    print("No esta ingresando correctamente")
                                    decision_dolar_cripto = input(
                                        "Usted quiere configurar el monto en dólares o en la criptomoneda? ´D´ para dólares y ´C´ en la criptmonedas: ")
                        elif moneda == "ETH" or moneda == "eth":
                            #validacion del usuario que recibe el dinero
                            entrada_usuario_que_recibe = input(
                                "Ingrese el Usuario que va recibir su transferencia: ")
                            #validacion del usuario
                            while not int(entrada_usuario_que_recibe) in lista_de_usuarios:
                                print("Usuario invalido")
                                entrada_usuario_que_recibe = input(
                                    "Ingrese el Usuario que va recibir su transferencia nuevamente: ")
                                #si el usuario es valido se accede al menu de opciones
                            else:
                                print("Usuario que le va transferir es valido!")
                                entrada_usuario_que_recibe_str = str(entrada_usuario_que_recibe)
                                decision_dolar_cripto = input(
                                    "Usted quiere configurar el monto en dólares o en la criptomoneda? ´D´ para dólares y ´C´ en la criptmonedas: ")
                                #Usuario toma la decision de mandar el monto desde la cantidad de dolares o desde la criptmoneda
                                while decision_dolar_cripto == "D" or decision_dolar_cripto == "d" or decision_dolar_cripto == "C" or decision_dolar_cripto == "c":
                                    #OPCION DOLAR
                                    if decision_dolar_cripto == "D" or decision_dolar_cripto == "d":
                                        monto_a_enviar = float(
                                            input("Ingrese el monto a enviar: "))
                                        #QUIEN ENVIA
                                        #se abre el archivo del quien envia, se guarda como lista, se toma la última posición para obtener el valor del estado de la cuenta para despues calcular y validar el monto a enviar, con un cierre del archivo para evitar problemas con la posterior escritura
                                        file_eth_envia = open(
                                            "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/eth.txt", "r")
                                        lista_billetera_eth_envia = file_eth_envia.readlines()
                                        #debemos de asegurarnos que sea un float lo que obtenemos en la lista
                                        estado_billetera_eth_envia = float(
                                            lista_billetera_eth_envia[-1])
                                        #cerramos el archivo
                                        file_eth_envia.close()
                                        #obtenemos el precio de Binance
                                        ethusd = get_price("ETHUSDT").json()
                                        #debemos de asegurarnos que sea un float lo que obtenemos del json
                                        estado_billetera_eth_usd_envia = estado_billetera_eth_envia * \
                                            float(ethusd["price"])
                                        while monto_a_enviar > estado_billetera_eth_usd_envia:
                                            print("No tiene los fondos que quiere enviar")
                                            monto_a_enviar = float(
                                                input("Ingrese el nuevo monto a enviar: "))
                                        else:
                                            #Grabar el resto de lo que le queda al QUIEN ENVIA
                                            file_eth_envia = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/eth.txt", "a")
                                            monto_a_enviar_en_eth = monto_a_enviar / \
                                                float(ethusd["price"])
                                            resto_de_la_billetera_del_envia = estado_billetera_eth_envia - monto_a_enviar_en_eth
                                            file_eth_envia.write(
                                                "\n"+str(resto_de_la_billetera_del_envia))
                                            file_eth_envia.close()
                                            #Primero leer y despues escribir la obtención de las nuevas monedas en RECEPTOR
                                            file_eth_receptor = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_recibe_str+"/eth.txt", "r")
                                            lista_billetera_eth_receptor = file_eth_receptor.readlines()
                                            estado_billetera_eth_receptor = float(
                                                lista_billetera_eth_receptor[-1])
                                            monto_nuevo_receptor = estado_billetera_eth_receptor + monto_a_enviar_en_eth
                                            file_eth_receptor.close()
                                            #se escribe en el archivo
                                            file_eth_receptor = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_recibe_str+"/eth.txt", "a")
                                            file_eth_receptor.write("\n"+str(monto_nuevo_receptor))
                                            print("Usted a enviado en ETH el monto:")
                                            print(monto_a_enviar_en_eth)
                                            print("Su saldo actual en ETH es:")
                                            print(resto_de_la_billetera_del_envia)
                                            print("El valor actual del envio en dólares es:")
                                            print(monto_a_enviar)
                                            file_eth_receptor.close()
                                            #Escribir la transacción en el HISTORIAL del RECEPTOR
                                            #Vamos a escribir en el archivo una lista_historial_receptor con el siguiente orden
                                            #fecha, moneda, tipo de operación, código del usuario, cantidad y monto para el momento.
                                            file_historial_receptor = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_recibe_str+"/historial.txt", "a")
                                            file_historial_receptor.write("\n"+"1. Fecha:"+tiempo.strftime("%d/%m/%y")+" - "+"2. Moneda: ETH - "+"3. Tipo de transacción: RECEPCIÓN - "+"4. Usuario: " +
                                                                          entrada_usuario_que_envia_str+" - "+"5. Monto recibido: "+str(monto_a_enviar_en_eth)+" - "+"6. Monto recibido en dólares: "+str(monto_a_enviar))
                                            file_historial_receptor.close()
                                            #se abre  para escribir el archivo de HISTORIAL del QUIEN ENVIA
                                            file_historial_envia = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/historial.txt", "a")
                                            file_historial_envia.write("\n"+"1. Fecha:"+tiempo.strftime("%d/%m/%y")+" - "+"2. Moneda: ETH - "+"3. Tipo de transacción: ENVIO - "+"4. Usuario: " +
                                                                       entrada_usuario_que_recibe_str+" - "+"5. Monto enviado: "+str(monto_a_enviar_en_eth)+" - "+"6. Monto enviado en dólares: "+str(monto_a_enviar))
                                            file_historial_envia.close()
                                            #se vuelve al menu
                                            print("")
                                            #MOSTRAR MENU
                                            #letra = mostrar_menu()
                                            print("Muchas gracias por usar la billetera")
                                            break
                                    #OPCION CRIPTOMONEDA
                                    elif decision_dolar_cripto == "C" or decision_dolar_cripto == "c":
                                        monto_a_enviar = float(
                                            input("Ingrese el monto a enviar: "))
                                        file_eth_envia = open(
                                            "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/eth.txt", "r")
                                        lista_billetera_eth_envia = file_eth_envia.readlines()
                                        #debemos de asegurarnos que sea un float lo que obtenemos en la lista
                                        estado_billetera_eth_envia = float(
                                            lista_billetera_eth_envia[-1])
                                        #cerramos el archivo
                                        file_eth_envia.close()
                                        while monto_a_enviar > estado_billetera_eth_envia:
                                            print("El usuario no tiene los fondos que desea enviar")
                                            monto_a_enviar = float(
                                                input("Ingrese el nuevo monto a enviar: "))
                                        else:
                                            #Grabar el resto de lo que le queda al QUIEN ENVIA
                                            file_eth_envia = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/eth.txt", "a")
                                            resto_de_la_billetera_del_envia = estado_billetera_eth_envia - monto_a_enviar
                                            file_eth_envia.write(
                                                "\n"+str(resto_de_la_billetera_del_envia))
                                            file_eth_envia.close()
                                            #Primero leer y despues escribir la obtención de las nuevas monedas en RECEPTOR
                                            file_eth_receptor = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_recibe_str+"/eth.txt", "r")
                                            lista_billetera_eth_receptor = file_eth_receptor.readlines()
                                            estado_billetera_eth_receptor = float(
                                                lista_billetera_eth_receptor[-1])
                                            monto_nuevo_receptor = estado_billetera_eth_receptor + monto_a_enviar
                                            file_eth_receptor.close()
                                            #se escribe en el archivo
                                            file_eth_receptor = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_recibe_str+"/eth.txt", "a")
                                            valorhoy = get_price("ETHUSDT").json()
                                            monto_en_dolares = float(
                                                monto_a_enviar) * float(valorhoy["price"])
                                            file_eth_receptor.write("\n"+str(monto_nuevo_receptor))
                                            #Texto dirigido al quien envia
                                            print("Usted a enviado en ETH el monto:")
                                            print(monto_a_enviar)
                                            print("Su saldo actual en ETH es:")
                                            print(resto_de_la_billetera_del_envia)
                                            print("El valor actual de la recepción en dólares es:")
                                            print(monto_en_dolares)
                                            file_eth_receptor.close()
                                            #Escribir la transacción en el HISTORIAL del RECEPTOR
                                            #Vamos a escribir en el archivo una lista_historial_receptor con el siguiente orden
                                            #fecha, moneda, tipo de operación, código del usuario, cantidad y monto para el momento.
                                            file_historial_receptor = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_recibe_str+"/historial.txt", "a")
                                            file_historial_receptor.write("\n"+"1. Fecha:"+tiempo.strftime("%d/%m/%y")+" - "+"2. Moneda: ETH - "+"3. Tipo de transacción: RECEPCIÓN - "+"4. Usuario: " +
                                                                          entrada_usuario_que_envia_str+" - "+"5. Monto recibido: "+str(monto_a_enviar)+" - "+"6. Monto recibido en dólares: "+str(monto_en_dolares))
                                            file_historial_receptor.close()
                                            #se abre  para escribir el archivo de HISTORIAL del QUIEN ENVIA
                                            file_historial_envia = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/historial.txt", "a")
                                            file_historial_envia.write("\n"+"1. Fecha:"+tiempo.strftime("%d/%m/%y")+" - "+"2. Moneda: ETH - "+"3. Tipo de transacción: ENVIO - "+"4. Usuario: " +
                                                                       entrada_usuario_que_recibe_str+" - "+"5. Monto enviado: "+str(monto_a_enviar)+" - "+"6. Monto enviado en dólares: "+str(monto_en_dolares))
                                            file_historial_envia.close()
                                            #se vuelve al menu
                                            print("")
                                            print("Muchas gracias por usar la billetera")
                                            break
                                            #MOSTRAR MENU
                                            #letra = mostrar_menu()
                                            #este es el else de la decisión si dolar o cripto
                                else:
                                    print("No esta ingresando correctamente")
                                    decision_dolar_cripto = input(
                                        "Usted quiere configurar el monto en dólares o en la criptomoneda? ´D´ para dólares y ´C´ en la criptmonedas: ")
                        elif moneda == "LTC" or moneda == "ltc":
                            #validacion del usuario que recibe el dinero
                            entrada_usuario_que_recibe = input(
                                "Ingrese el Usuario que va recibir su transferencia: ")
                            #validacion del usuario
                            while not int(entrada_usuario_que_recibe) in lista_de_usuarios:
                                print("Usuario invalido")
                                entrada_usuario_que_recibe = input(
                                    "Ingrese el Usuario que va recibir su transferencia nuevamente: ")
                                #si el usuario es valido se accede al menu de opciones
                            else:
                                print("Usuario que le va transferir es valido!")
                                entrada_usuario_que_recibe_str = str(entrada_usuario_que_recibe)
                                decision_dolar_cripto = input(
                                    "Usted quiere configurar el monto en dólares o en la criptomoneda? ´D´ para dólares y ´C´ en la criptmonedas: ")
                                #Usuario toma la decision de mandar el monto desde la cantidad de dolares o desde la criptmoneda
                                while decision_dolar_cripto == "D" or decision_dolar_cripto == "d" or decision_dolar_cripto == "C" or decision_dolar_cripto == "c":
                                    #OPCION DOLAR
                                    if decision_dolar_cripto == "D" or decision_dolar_cripto == "d":
                                        monto_a_enviar = float(
                                            input("Ingrese el monto a enviar: "))
                                        #QUIEN ENVIA
                                        #se abre el archivo del quien envia, se guarda como lista, se toma la última posición para obtener el valor del estado de la cuenta para despues calcular y validar el monto a enviar, con un cierre del archivo para evitar problemas con la posterior escritura
                                        file_ltc_envia = open(
                                            "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/ltc.txt", "r")
                                        lista_billetera_ltc_envia = file_ltc_envia.readlines()
                                        #debemos de asegurarnos que sea un float lo que obtenemos en la lista
                                        estado_billetera_ltc_envia = float(
                                            lista_billetera_ltc_envia[-1])
                                        #cerramos el archivo
                                        file_ltc_envia.close()
                                        #obtenemos el precio de Binance
                                        ltcusd = get_price("LTCUSDT").json()
                                        #debemos de asegurarnos que sea un float lo que obtenemos del json
                                        estado_billetera_ltc_usd_envia = estado_billetera_ltc_envia * \
                                            float(ltcusd["price"])
                                        while monto_a_enviar > estado_billetera_ltc_usd_envia:
                                            print("No tiene los fondos que quiere enviar")
                                            monto_a_enviar = float(
                                                input("Ingrese el nuevo monto a enviar: "))
                                        else:
                                            #Grabar el resto de lo que le queda al QUIEN ENVIA
                                            file_ltc_envia = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/ltc.txt", "a")
                                            monto_a_enviar_en_ltc = monto_a_enviar / \
                                                float(ltcusd["price"])
                                            resto_de_la_billetera_del_envia = estado_billetera_ltc_envia - monto_a_enviar_en_ltc
                                            file_ltc_envia.write(
                                                "\n"+str(resto_de_la_billetera_del_envia))
                                            file_ltc_envia.close()
                                            #Primero leer y despues escribir la obtención de las nuevas monedas en RECEPTOR
                                            file_ltc_receptor = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_recibe_str+"/ltc.txt", "r")
                                            lista_billetera_ltc_receptor = file_ltc_receptor.readlines()
                                            estado_billetera_ltc_receptor = float(
                                                lista_billetera_ltc_receptor[-1])
                                            monto_nuevo_receptor = estado_billetera_ltc_receptor + monto_a_enviar_en_ltc
                                            file_ltc_receptor.close()
                                            #se escribe en el archivo
                                            file_ltc_receptor = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_recibe_str+"/ltc.txt", "a")
                                            file_ltc_receptor.write("\n"+str(monto_nuevo_receptor))
                                            print("Usted a enviado en LTC el monto:")
                                            print(monto_a_enviar_en_ltc)
                                            print("Su saldo actual en LTC es:")
                                            print(resto_de_la_billetera_del_envia)
                                            print("El valor actual del envio en dólares es:")
                                            print(monto_a_enviar)
                                            file_ltc_receptor.close()
                                            #Escribir la transacción en el HISTORIAL del RECEPTOR
                                            #Vamos a escribir en el archivo una lista_historial_receptor con el siguiente orden
                                            #fecha, moneda, tipo de operación, código del usuario, cantidad y monto para el momento.
                                            file_historial_receptor = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_recibe_str+"/historial.txt", "a")
                                            file_historial_receptor.write("\n"+"1. Fecha:"+tiempo.strftime("%d/%m/%y")+" - "+"2. Moneda: LTC - "+"3. Tipo de transacción: RECEPCIÓN - "+"4. Usuario: " +
                                                                          entrada_usuario_que_envia_str+" - "+"5. Monto recibido: "+str(monto_a_enviar_en_ltc)+" - "+"6. Monto recibido en dólares: "+str(monto_a_enviar))
                                            file_historial_receptor.close()
                                            #se abre  para escribir el archivo de HISTORIAL del QUIEN ENVIA
                                            file_historial_envia = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/historial.txt", "a")
                                            file_historial_envia.write("\n"+"1. Fecha:"+tiempo.strftime("%d/%m/%y")+" - "+"2. Moneda: LTC - "+"3. Tipo de transacción: ENVIO - "+"4. Usuario: " +
                                                                       entrada_usuario_que_recibe_str+" - "+"5. Monto enviado: "+str(monto_a_enviar_en_ltc)+" - "+"6. Monto enviado en dólares: "+str(monto_a_enviar))
                                            file_historial_envia.close()
                                            #se vuelve al menu
                                            print("")
                                            print("Muchas gracias por usar la billetera")
                                            break
                                            #MOSTRAR MENU
                                            #letra = mostrar_menu()
                                    #OPCION CRIPTOMONEDA
                                    elif decision_dolar_cripto == "C" or decision_dolar_cripto == "c":
                                        monto_a_enviar = float(
                                            input("Ingrese el monto a enviar: "))
                                        file_ltc_envia = open(
                                            "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/ltc.txt", "r")
                                        lista_billetera_ltc_envia = file_ltc_envia.readlines()
                                        #debemos de asegurarnos que sea un float lo que obtenemos en la lista
                                        estado_billetera_ltc_envia = float(
                                            lista_billetera_ltc_envia[-1])
                                        #cerramos el archivo
                                        file_ltc_envia.close()
                                        while monto_a_enviar > estado_billetera_ltc_envia:
                                            print("El usuario no tiene los fondos que desea enviar")
                                            monto_a_enviar = float(
                                                input("Ingrese el nuevo monto a enviar: "))
                                        else:
                                            #Grabar el resto de lo que le queda al QUIEN ENVIA
                                            file_ltc_envia = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/ltc.txt", "a")
                                            resto_de_la_billetera_del_envia = estado_billetera_ltc_envia - monto_a_enviar
                                            file_ltc_envia.write(
                                                "\n"+str(resto_de_la_billetera_del_envia))
                                            file_ltc_envia.close()
                                            #Primero leer y despues escribir la obtención de las nuevas monedas en RECEPTOR
                                            file_ltc_receptor = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_recibe_str+"/ltc.txt", "r")
                                            lista_billetera_ltc_receptor = file_ltc_receptor.readlines()
                                            estado_billetera_ltc_receptor = float(
                                                lista_billetera_ltc_receptor[-1])
                                            monto_nuevo_receptor = estado_billetera_ltc_receptor + monto_a_enviar
                                            file_ltc_receptor.close()
                                            #se escribe en el archivo
                                            file_ltc_receptor = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_recibe_str+"/ltc.txt", "a")
                                            valorhoy = get_price("LTCUSDT").json()
                                            monto_en_dolares = float(
                                                monto_a_enviar) * float(valorhoy["price"])
                                            file_ltc_receptor.write("\n"+str(monto_nuevo_receptor))
                                            #Texto dirigido al quien envia
                                            print("Usted a enviado en LTC el monto:")
                                            print(monto_a_enviar)
                                            print("Su saldo actual en LTC es:")
                                            print(resto_de_la_billetera_del_envia)
                                            print("El valor actual de la recepción en dólares es:")
                                            print(monto_en_dolares)
                                            file_ltc_receptor.close()
                                            #Escribir la transacción en el HISTORIAL del RECEPTOR
                                            #Vamos a escribir en el archivo una lista_historial_receptor con el siguiente orden
                                            #fecha, moneda, tipo de operación, código del usuario, cantidad y monto para el momento.
                                            file_historial_receptor = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_recibe_str+"/historial.txt", "a")
                                            file_historial_receptor.write("\n"+"1. Fecha:"+tiempo.strftime("%d/%m/%y")+" - "+"2. Moneda: LTC - "+"3. Tipo de transacción: RECEPCIÓN - "+"4. Usuario: " +
                                                                          entrada_usuario_que_envia_str+" - "+"5. Monto recibido: "+str(monto_a_enviar)+" - "+"6. Monto recibido en dólares: "+str(monto_en_dolares))
                                            file_historial_receptor.close()
                                            #se abre  para escribir el archivo de HISTORIAL del QUIEN ENVIA
                                            file_historial_envia = open(
                                                "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/historial.txt", "a")
                                            file_historial_envia.write("\n"+"1. Fecha:"+tiempo.strftime("%d/%m/%y")+" - "+"2. Moneda: LTC - "+"3. Tipo de transacción: ENVIO - "+"4. Usuario: " +
                                                                       entrada_usuario_que_recibe_str+" - "+"5. Monto enviado: "+str(monto_a_enviar)+" - "+"6. Monto enviado en dólares: "+str(monto_en_dolares))
                                            file_historial_envia.close()
                                            #se vuelve al menu
                                            print("")
                                            print("Muchas gracias por usar la billetera")
                                            break
                                            #MOSTRAR MENU btc
                                            #letra = mostrar_menu()
                                    #este es el else de la decisión si dolar o cripto
                                else:
                                    print("No esta ingresando correctamente")
                                    decision_dolar_cripto = input(
                                        "Usted quiere configurar el monto en dólares o en la criptomoneda? ´D´ para dólares y ´C´ en la criptmonedas: ")
                        else:
                            #validacion del usuario que recibe el dinero
                            entrada_usuario_que_recibe = input(
                                "Ingrese el Usuario que va recibir su transferencia: ")
                            entrada_usuario_que_recibe_str = str(entrada_usuario_que_recibe)
                            #validacion del usuario
                            while not int(entrada_usuario_que_recibe) in lista_de_usuarios:
                                print("Usuario invalido")
                                entrada_usuario_que_recibe = input(
                                    "Ingrese el Usuario que va recibir su transferencia nuevamente: ")
                                #si el usuario es valido se accede al menu de opciones
                            else:
                                print("Usuario que le va transferir es valido!")
                                monto_a_enviar = float(input("Ingrese el monto a enviar: "))
                                entrada_usuario_que_recibe_str = str(entrada_usuario_que_recibe)
                                file_usd_envia = open("/Users/rodrigorapoport/Downloads/proyecto_python/" +
                                                      entrada_usuario_que_envia_str+"/usdt.txt", "r")
                                lista_billetera_usd_envia = file_usd_envia.readlines()
                                #debemos de asegurarnos que sea un float lo que obtenemos en la lista
                                estado_billetera_usd_envia = float(lista_billetera_usd_envia[-1])
                                #cerramos el archivo
                                file_usd_envia.close()
                                while monto_a_enviar > estado_billetera_usd_envia:
                                    print("El usuario no tiene los fondos que desea enviar")
                                    monto_a_enviar = float(
                                        input("Ingrese el nuevo monto a enviar: "))
                                else:
                                    #Grabar el resto de lo que le queda al QUIEN ENVIA
                                    file_usd_envia = open(
                                        "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/usdt.txt", "a")
                                    resto_de_la_billetera_del_envia = estado_billetera_usd_envia - monto_a_enviar
                                    file_usd_envia.write("\n"+str(resto_de_la_billetera_del_envia))
                                    file_usd_envia.close()
                                    #Primero leer y despues escribir la obtención de las nuevas monedas en RECEPTOR
                                    file_usd_receptor = open(
                                        "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_recibe_str+"/usdt.txt", "r")
                                    lista_billetera_usd_receptor = file_usd_receptor.readlines()
                                    estado_billetera_usd_receptor = float(
                                        lista_billetera_usd_receptor[-1])
                                    monto_nuevo_receptor = estado_billetera_usd_receptor + monto_a_enviar
                                    file_usd_receptor.close()
                                    #se escribe en el archivo
                                    file_usd_receptor = open(
                                        "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_recibe_str+"/usdt.txt", "a")
                                    file_usd_receptor.write("\n"+str(monto_nuevo_receptor))
                                    #Texto dirigido al quien envia
                                    print("Usted a enviado en USD el monto:")
                                    print(monto_a_enviar)
                                    print("Su saldo actual en USD es:")
                                    print(resto_de_la_billetera_del_envia)
                                    file_usd_receptor.close()
                                    #Escribir la transacción en el HISTORIAL del RECEPTOR
                                    #Vamos a escribir en el archivo una lista_historial_receptor con el siguiente orden
                                    #fecha, moneda, tipo de operación, código del usuario, cantidad y monto para el momento.
                                    file_historial_receptor = open(
                                        "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_recibe_str+"/historial.txt", "a")
                                    file_historial_receptor.write("\n"+"1. Fecha:"+tiempo.strftime("%d/%m/%y")+" - "+"2. Moneda: USD - "+"3. Tipo de transacción: RECEPCIÓN - " +
                                                                  "4. Usuario: "+entrada_usuario_que_envia_str+" - "+"5 y 6. Monto recibido: "+str(monto_a_enviar)+" - ")
                                    file_historial_receptor.close()
                                    #se abre  para escribir el archivo de HISTORIAL del QUIEN ENVIA
                                    file_historial_envia = open(
                                        "/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_que_envia_str+"/historial.txt", "a")
                                    file_historial_envia.write("\n"+"1. Fecha:"+tiempo.strftime("%d/%m/%y")+" - "+"2. Moneda: USD - "+"3. Tipo de transacción: ENVIO - " +
                                                               "4. Usuario: "+entrada_usuario_que_recibe_str+" - "+"5 y 6. Monto enviado: "+str(monto_a_enviar)+" - ")
                                    file_historial_envia.close()
                                    #se vuelve al menu
                                    print("")
                                    #MOSTRAR MENU btc
                                    letra = mostrar_menu()
                    else:
                        print("Error: Solo se permite utilizar BTC, LTC o ETH o USD")
                        print("")
                        letra = mostrar_menu()
                elif letra == "W" or letra == "w":
                    print("PROCESO DE MOSTRAR EL HISTORIAL DE TRANSFERENCIAS")  
                    entrada_usuario_str = str(entrada_usuario)
                    #el mecanismo es simple, se guarda el archivo en una lista y se recorre la lista con un bucle for
                    file_historial = open("/Users/rodrigorapoport/Downloads/proyecto_python/"+entrada_usuario_str+"/historial.txt", "r")
                    lista_historial = file_historial.readlines()
                    #debemos de asegurarnos que sea un float lo que obtenemos en la lista
                    for x in range(0, len(lista_historial)):
                        print (lista_historial[x])
                    letra = mostrar_menu()
                    #obtenemos el precio de Binance
                else:
                    print("Gracias por usar la billetera, byebye :-) ")



    
    


