#!/usr/bin/python
import socket
#from socket import *
import os
import time
import platform
import subprocess, sys

ips_activas = set()
list_ips_activas = []
variable_control = []
relacionip_ports = {}
def limpiar_pantalla(): # FUNCION PARA LIMPIAR PANTALLA WINDOWS / LINUX
    time.sleep(1)
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')



def ping_rangos(): # FUNCION PARA DESCUBRIR HOSTS EN LA LAN DENTRO DE UN RANGO ESPECIFICADO
    global list_ips_activas
    rango_inicial = segmento_red
    rango_final = segmento_red
    primer_valor = int(input(f'Desde {rango_inicial}.'))
    if primer_valor > 255:
        print('Error de coordenada')
        return
    listprimer_valor = [primer_valor]
    segundo_valor = int(input(f'Hasta {rango_final}.'))
    if segundo_valor > 255:
        print('Error de coordenada')
        return
    listsegundivalor = [segundo_valor]
    rangos= [listprimer_valor, listsegundivalor]
    if rangos[0] > rangos[1]:
        print('Error de Rango')
        return
    print('Buscando IPs Activas ...')
    time.sleep(2)
    if (platform.system() == "Linux"):
        consola_ping = 'ping -c 1 ' + segmento_red + '.'
        for i in range(primer_valor, segundo_valor + 1):
            comando = consola_ping + str(i)
            ip = segmento_red + '.' + str(i)
            respuesta = os.popen(comando)
            for line in respuesta.readlines():
                if ('ttl' in line.lower()):
                    ips_activas.add(ip)
                    print(f'{ip} Host Activo. ', end='')
                    if ('ttl=128' in line.lower()):
                        print('SO Windows')
                    elif ('ttl=64' in line.lower()):
                        print('SO Linux')
                    else:
                        print('Desconocido')
                    break
        print('Fin del escaneo')
        time.sleep(2)
        limpiar_pantalla()
        if ips_activas != set():
            list_ips_activas = list(set(ips_activas))
            list_ips_activas.sort()
            print(f'Las IPs Activas son: ')
            print('\n')
            for ips in list_ips_activas:
                print(ips)

        else:
            print('No hay Host Activos')
    else:
        consola_ping = 'ping -n 1 ' + segmento_red + '.'
        for i in range(primer_valor, segundo_valor + 1):
            comando = consola_ping + str(i)
            ip = segmento_red + '.' + str(i)
            respuesta = os.popen(comando)
            for line in respuesta.readlines():
                if ('ttl' in line.lower()):
                    ips_activas.add(ip)
                    print(f'{ip} Host Activo. ', end='')
                    if ('ttl=128' in line.lower()):
                        print('SO Windows')
                    elif ('ttl=64' in line.lower()):
                        print('SO Linux')
                    else:
                        print('Desconocido')
                    break
        print('Fin del escaneo')
        time.sleep(2)
        limpiar_pantalla()
        if ips_activas != set():
            list_ips_activas = list(set(ips_activas))
            list_ips_activas.sort()
            print(f'Las IPs Activas son: ')

            for ips in list_ips_activas:
                print(ips)

        else:
            print('No hay Host Activos')

    return
def ping_General(): # FUNCION QUE PERMITE BUSCAR HOSTS ACTIVOS EN EL SEGMENTO DENTRO DE LAS 255 POSIBILIDADES
    global list_ips_activas
    print('Buscando IPs Activas ...')
    time.sleep(2)
    if (platform.system() == "Linux"):
            consola_ping = 'ping -c 1 '+ segmento_red + '.'
            for i in range (1,256):
                comando = consola_ping + str(i)
                ip = segmento_red + '.' + str(i)
                respuesta = os.popen(comando)
                for line in respuesta.readlines():
                    if ('ttl' in line.lower()):
                        ips_activas.add(ip)
                        print(f'{ip} Host Activo. ', end='')
                        if ('ttl=128' in line.lower()):
                            print('SO Windows')
                        elif ('ttl=64' in line.lower()):
                            print('SO Linux')
                        else:
                            print('Desconocido')
                        break
            print('Fin del escaneo')
            time.sleep(2)
            limpiar_pantalla()
            if ips_activas != set():
                list_ips_activas = list(set(ips_activas))
                list_ips_activas.sort()
                print(f'Las IPs Activas son: ')
                print('\n')
                for ips in list_ips_activas:
                    print(ips)

            else:
                print('No hay Host Activos')
    else:
            consola_ping = 'ping -n 1 '+ segmento_red + '.'
            for i in range (1,256):
                comando = consola_ping + str(i)
                ip = segmento_red + '.'+str(i)
                respuesta = os.popen(comando)
                for line in respuesta.readlines():
                    if ('ttl' in line.lower()):
                        ips_activas.add(ip)
                        print(f'{ip} Host Activo. ',end='')
                        if ('ttl=128' in line.lower()):
                            print('SO Windows')
                        elif ('ttl=64' in line.lower()):
                            print('SO Linux')
                        else:
                            print('Desconocido')
                        break
            print('Fin del escaneo')
            time.sleep(2)
            limpiar_pantalla()
            if ips_activas != set():
                list_ips_activas = list(set(ips_activas))
                list_ips_activas.sort()
                print(f'Las IPs Activas son: ')
                print('\n')
                for ips in list_ips_activas:
                    print(ips)

            else:
                print('No hay Host Activos')

def sub_menu (): # FUNCION QUE CREA UN MENU COMO APOYO CUANDO FINALIZA ALGUN TIPO DE ESCANEO GENERAL O POR RANGOS
    menu3 = [
        'Volver a escanear otro rango',
        'Ver Ips Activas Identificadas',
        'Volver al menu principal',
        'Salir del programa'

    ]
    for c, d in enumerate(menu3, 1):
        print(c, ':', d)
    seleccion_opcion = int(input('Seleccione una Opción: '))
    if seleccion_opcion not in [1, 2, 3, 4]:
        print('Opción fuera del rango')
    elif seleccion_opcion == 1:
        ping_rangos()
        sub_menu()
    elif seleccion_opcion == 2:
        print('Los Hosts Identificados como activos hasta el momento son: ')
        ips_identificadas =list_ips_activas

        for num,posicion in enumerate(ips_identificadas,1):
            print(num, ':', posicion)
        print('\n')
        return
    elif seleccion_opcion == 3:
        return
    else:
        print('Hasta Pronto')
        exit()


def opcion_ports(): # FUNCION QUE PERMITE BUSCAR PUERTOS EN TODAS LAS IPS O IPS ESPECIFICADAS DEL SEGMENTO LAN
    global relacionip_ports
    menu_rangos_puertos = [
        'Escanear todos los puertos',
        'Escanear Puertos en Particular',
        'Regresar al Inicio'
    ]
    for pos, opcion in enumerate(menu_rangos_puertos, 1):
        print(f'{pos}: {opcion}')

    opcion_rango_port = int(input('Ingrese Una Opción: '))
    if opcion_rango_port not in [1, 2, 3]:
        print('Error de Opción')
        return
    if opcion_rango_port == 3:
        return
    else:
        if opcion_rango_port == 1:
            abirtos = []
            if len(list_ips_activas) > 1:
                for i in list_ips_activas:
                    print(f'Escaneando {i}')
                    ipequipo = socket.gethostbyname(i)
                    print('Comenzando el escaneo a puertos...')
                    for puertos in range(1, 65536):
                        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        respuesta = client.connect_ex((ipequipo, puertos))
                        if (respuesta == 0):
                            client.close()
                            abirtos.append(puertos)
                            print(f'Puerto abierto {puertos}')
                    if abirtos != []:
                        print(f'Los puertos abiertos de {i} son: ', end='')
                        for n in abirtos:
                            print(f'{n} ', end='')
                        relacionip_ports[list_ips_activas] = list(abirtos)
                        abirtos.clear()
                    else:
                        print('No hay Puertos Abiertos')

                    print('\n')
                print('Escaneo Finalizado')
            else:
                for i in list_ips_activas:
                    print(f'Escaneando {i}')
                    ipequipo = socket.gethostbyname(i)
                    print('Comenzando el escaneo a puertos...')
                    for puertos in range(1, 65536):
                        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        respuesta = client.connect_ex((ipequipo, puertos))
                        if (respuesta == 0):
                            client.close()
                            abirtos.append(puertos)
                            print(f'Puerto abierto {puertos}')
                    if abirtos != []:
                        print(f'Los puertos abiertos de {i} son: ', end='')
                        for n in abirtos:
                            print(f'{n}, ', end='')
                        relacionip_ports[i] = list(abirtos)
                        abirtos.clear()
                    else:
                        print('No hay Puertos Abiertos')

                    print('\n')
                print('Escaneo Finalizado')

        elif opcion_rango_port == 2:
            separador = ','
            abirtos = []
            print('Introdude los puertos separados por "," Ejemplo: 80,445,3389')
            opcion = (input('Introduce los puertos a escanear: '))
            lista_p = opcion
            v_enteros = []
            separados = lista_p.split(separador)
            lista_p = separados
            portconjunto = set(lista_p)
            ordenados = list(portconjunto)
            ordenados.sort()

            if len(list_ips_activas) < 2:
                    try:
                        print('\n')
                        for i in list_ips_activas:
                            print(f'Escaneando {i}')
                            ipequipo = socket.gethostbyname(i)
                            print('Comenzando el escaneo a puertos...')
                            for puertos in range(len(ordenados)):
                                v_enteros = int(ordenados[puertos])
                                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                respuesta = client.connect_ex((ipequipo, v_enteros))
                                if (respuesta == 0):
                                    client.close()
                                    abirtos.append(v_enteros)
                                    print(f'Puerto abierto {v_enteros}')
                                else:
                                    print(f'Puerto Cerrado {v_enteros}')

                            if abirtos != []:
                                print(f'Los puertos abiertos de {i} son: ', end='')
                                for n in abirtos:
                                    print(f'{n}, ', end='')
                                relacionip_ports[i] = list(abirtos)
                                abirtos.clear()
                            else:
                                print('No hay Puertos Abiertos')
                            print('\n')
                            print('Escaneo Finalizado')
                    except ValueError:
                        print('Error de Opción')
            else:
                for i in list_ips_activas:
                    try:
                        print('\n')
                        print(f'Escaneando {i}')
                        ipequipo = socket.gethostbyname(i)
                        print('Comenzando el escaneo a puertos...')
                        for puertos in range(len(ordenados)):
                            v_enteros = int(ordenados[puertos])
                            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            respuesta = client.connect_ex((ipequipo, v_enteros))
                            if (respuesta == 0):
                                client.close()
                                abirtos.append(v_enteros)
                                print(f'Puerto abierto {v_enteros}')
                            else:
                                print(f'Puerto Cerrado {v_enteros}')

                        if abirtos != []:
                            print(f'Los puertos abiertos de {i} son: ', end='')
                            for n in abirtos:
                                print(f'{n}, ', end='')
                            relacionip_ports[i] = list(abirtos)
                            abirtos.clear()
                        else:
                            print('No hay Puertos Abiertos')

                        print('\n')
                        print('Escaneo Finalizado')
                    except ValueError:
                        print('Error de Opción')
def opcion_ports_selec(): # FUNCION ADICIONAL PARA BUSCAR PUERTOS EN CASO DE QUE EL USUARIO DESEE DIGITAR UNA IP PARTICULAR ACTIVA DEL SEGMENTO
    menu_rangos_puertos = [
        'Escanear todos los puertos',
        'Escanear Puertos en Particular',
        'Regresar al Inicio'
    ]
    for pos, opcion in enumerate(menu_rangos_puertos, 1):
        print(f'{pos}: {opcion}')

    opcion_rango_port = int(input('Ingrese Una Opción: '))
    if opcion_rango_port not in [1, 2, 3]:
        print('Error de Opción')
        return
    if opcion_rango_port == 3:
        return
    else:
        abiertos = []
        if opcion_rango_port == 1:
            print(f'Escaneando {ip}')
            ipequipo = socket.gethostbyname(ip)
            print('Comenzando el escaneo a puertos...')
            for puertos in range(1, 65536):
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                respuesta = client.connect_ex((ipequipo, puertos))
                if (respuesta == 0):
                    client.close()
                    abiertos.append(puertos)
                    print(f'Puerto abierto {puertos}')
            if abiertos != []:
                print(f'Los puertos abiertos de {ip} son: ', end='')
                for n in abiertos:
                    print(f'{n}, ', end='')
                relacionip_ports[ip] = list(abiertos)
                abiertos.clear()
            else:
                print('No hay Puertos Abiertos')

            print('\n')
            print('Escaneo Finalizado')
        elif opcion_rango_port == 2:
            separador = ','
            abirtos = []
            print('Introdude los puertos separados por "," Ejemplo: 80,445,3389')
            opcion = (input('Introduce los puertos a escanear: '))
            lista_p = opcion
            v_enteros = []
            separados = lista_p.split(separador)
            lista_p = separados
            portconjunto = set(lista_p)
            ordenados = list(portconjunto)
            ordenados.sort()

            try:
                print('\n')
                print(f'Escaneando {ip}')
                ipequipo = socket.gethostbyname(ip)
                print('Comenzando el escaneo a puertos...')
                for puertos in range(len(ordenados)):
                    v_enteros = int(ordenados[puertos])
                    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    respuesta = client.connect_ex((ipequipo, v_enteros))
                    if (respuesta == 0):
                        client.close()
                        abirtos.append(v_enteros)
                        print(f'Puerto abierto {v_enteros}')
                    else:
                        print(f'Puerto Cerrado {v_enteros}')

                if abirtos != []:
                    print(f'Los puertos abiertos de {ip} son: ', end='')
                    for n in abirtos:
                        print(f'{n}, ', end='')
                    relacionip_ports[ip] = abirtos
                    abirtos.clear()

                else:
                    print('No hay Puertos Abiertos')

                print('\n')
                print('Escaneo Finalizado')

            except ValueError:
                print('Error de Opción')
def scanner ():  # FUNCION UTIL PARA RELACIONAR LAS FUNCION PARA ESCANEAR PUERTOS EN CUALQUIERA DE LAS MODALIDADES
    global ip
    if list_ips_activas == variable_control:
        print('No hay Hosts para escanear')
        print('\n')
    else:
        limpiar_pantalla()
        print('Los Host Disponibles para escanear son: ')
        for listaa, num in enumerate(list_ips_activas,1):
            print(listaa,':',num)
        print('\n')

        menu_scanner = [
            'Escanear todos los Hosts',
            'Escanear Ip en particular',
            'Salir al menu anterior'

        ]
        print('\n')
        for num, posicion in enumerate(menu_scanner,1):
            print(num, ':',posicion)

        seleccion_opcion = int(input('Seleccione una Opción: '))

        if seleccion_opcion not in [1,2,3]:
            print('Error de Opción ')
            print('\n')
        elif seleccion_opcion == 1:
            opcion_ports()

        elif seleccion_opcion == 2:
            print('Los Host Disponibles para escanear son: ')
            for num, disponibles in enumerate(list_ips_activas, 1):
                print(f'{num}: {disponibles}')

            ip = input('Por favor digita la IP disponible que quieres escanear: ')
            if ip not in list_ips_activas:
                print('La IP que digistaste no estan en las disponibles')
                return
            else:
                opcion_ports_selec()
        else:
            return
def versiones(): # FUNCION IMPORTANTE QUE RELACIONA NMAP Y LOS RESULTADOS DE IPS Y PUERTOS DEL SCRIPT, PARA BUSCAR POSIBLES VULNS Y VERSIONES DE SERVICIOS
    comando = "nmap -sV --script=vuln "
    listaa = []
    seleccion = []
    #def menu():
    menu_rangos_puertos = [
        'Escanear todos los puertos abiertos de todas las IPs',
        'Escanear Puertos en Particular de IPs',
        'Regresar al Inicio'
    ]
    for pos, opcion in enumerate(menu_rangos_puertos, 1):
        print(f'{pos}: {opcion}')
    opcion_rango_port = int(input('Ingrese Una Opción: '))
    if opcion_rango_port not in [1, 2, 3]:
        print('Error de Opción')
        return
    if opcion_rango_port == 3:
        return
    else:
        if opcion_rango_port == 1:

            for b in relacionip_ports.values():
                for c in b:
                    listaa.append(str(c))
                    listaa.sort()

                for i in relacionip_ports:
                    ejecucion = comando + i + ' ' + '-p' + ' ' + ','.join(listaa)
                    os.system(ejecucion)
                listaa.clear()
        if opcion_rango_port == 2:
            print('IPs identificadas con puertos: ')
            for i, j in enumerate(relacionip_ports.keys(), 1):
                print(f'{i} : {j}')
            print('\n')
            selec = input('Digite la IP que desea escanear: ')
            if selec not in relacionip_ports.keys():
                print('IP erronea')

            elif selec == '':
                print('Introduce algun valor:')
                return
            else:
                print(f'la IP {selec} tiene estos puertos abiertos: ')
                ports = relacionip_ports.get(selec)
                for i in ports:
                    print(i)
                selec1 = input('Seleccione que puerto(s) desea escanear: \n Si son varios puertos deben estar separados por "," ejemplo: 22,80')
                if len(selec1) > 0 and len(selec1) <= 2:
                    seleccion.append(selec1)
                    print(f'Comenzando el escaneo de {selec}\n')
                    v = comando + selec + ' ' + '-p' + ' ' + ''.join(seleccion)
                    os.system(v)
                else:
                    separados = selec1.split(',')
                    print('Comenzando el escaneo ... \n')
                    ports1 = ''.join(separados)
                    v = comando + selec + ' ' + '-p' + ' ' + ''.join(ports1)
                    os.system(v)
print('''
 .d8888b.   .d8888b.         d8888 888b    888 888b    888 8888888888 8888888b.              
d88P  Y88b d88P  Y88b       d88888 8888b   888 8888b   888 888        888   Y88b             
Y88b.      888    888      d88P888 88888b  888 88888b  888 888        888    888             
 "Y888b.   888            d88P 888 888Y88b 888 888Y88b 888 8888888    888   d88P             
    "Y88b. 888           d88P  888 888 Y88b888 888 Y88b888 888        8888888P"              
      "888 888    888   d88P   888 888  Y88888 888  Y88888 888        888 T88b               
Y88b  d88P Y88b  d88P  d8888888888 888   Y8888 888   Y8888 888        888  T88b              
 "Y8888P"   "Y8888P"  d88P     888 888    Y888 888    Y888 8888888888 888   T88b             
                                                                                             
                                                                                          
                    
                                           
AUTOR: JUAN CAMILO PALACIO
FECHA: 30-07-2021
DIRIGIDO: PROYECTO FUAA
CODIGO: PYTHON 3
                    
''')
while True: # CICLO INFINITO DE EJECUCION
    nombre_usuario = input('Ingrese su nombre: ')
    if nombre_usuario != '':
        print(f'Hola {nombre_usuario}, Bienvenido al programa de Scanner FUAA')
        myhost = socket.gethostname()
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # OBTENER IP DEL EQUIPO A TRAVES DE LA INTERFAZ QUE ACTUAMENTE ESTA SALIENDO DE INTERNET
        s.connect(("8.8.8.8", 80))
        ip = (s.getsockname()[0])
        s.close()

        print(f'Tu Equipo es: {myhost} y tu IP es: {ip} ')
        ipfrag = ip.split(".")
        segmento = ipfrag
        del (segmento[-1])
        segmento_red = '.'.join(segmento)

        menu = [
            'Buscar IPs Activas en el segmento',
            'Escanear Puertos de Ips Activas',
            'Buscar Información de Puertos (Version, Vulns)',
            'Salir'

        ]
        while True:
            try:
                for i, j in enumerate(menu, 1):
                    print(i, ':', j)

                opcion_usuario = int(input('Seleccione una Opción: '))
                if opcion_usuario not in [1, 2, 3, 4]:
                    print('Opción fuera del rango')
                    continue
                elif opcion_usuario == 4:
                    print('Hasta Pronto')
                    exit()
                elif opcion_usuario == 1:
                    try:
                        limpiar_pantalla()

                        print(f'El segmento en el que estas es: {segmento_red}.0/24')
                        menu2 = [
                            'Buscar IPs entre un rango especifico del segmento', # MENU PRINCIPAL
                            'Buscar en todo el segmento',
                            'Ver IPs ya Identificadas',
                            'Volver Menu Anterior',
                            'Salir del programa'

                        ]

                        for a, b in enumerate(menu2, 1):
                            print(a, ':', b)
                        seleccion_opcion = int(input('Seleccione una Opción: '))
                        if seleccion_opcion not in [1, 2, 3, 4,5]:
                            print('Opción fuera del rango')
                        elif seleccion_opcion == 1:
                            ping_rangos() # LLAMADA DE LA FUNCION ping_rangos
                            sub_menu() # llamada de la funcion sub_menu


                        elif seleccion_opcion == 2:
                            ping_General() # llamada de la funcion ping_General
                        elif seleccion_opcion == 3:
                            if list_ips_activas == []:
                                print('No hay Host Activos')
                            else:
                                print('Los hosts activos son:')
                                print('\n')
                                for ips in list_ips_activas:
                                    print(ips)

                        elif seleccion_opcion == 4:
                            continue
                        else:
                            print('Hasta Pronto')
                            exit()
                    except ValueError:
                        print('Error de Opción')

                elif opcion_usuario == 2:
                    scanner() # llamada de la funcion scanner

                elif opcion_usuario == 3:
                    try:
                        print('IPs disponibles para escanear: ')
                        if list_ips_activas == []:
                            print('Todavia no se han identificado Hosts activos \n')
                            continue
                        else:
                            if relacionip_ports == {}:
                                print('Todavia no se han identificado IPs con puertos abiertos \n')
                                continue
                            else:
                                for i in relacionip_ports:
                                    print(i)

                                print('\n')
                                menu6 = [
                                    'Escanear Todas las IPs',
                                    'Seleccione una IP especifica',
                                    'Regresar al menu anterior',
                                    'Salir del programa'
                                ]

                                for i, j in enumerate(menu6, 1):
                                    print(f'{i} : {j}')
                                seleccioneop = int(input('Seleccione una opción: '))

                                if seleccioneop not in [1, 2, 3,4]:
                                    print('Error de Opción')
                                    continue
                                else:
                                    if seleccioneop == 1 or 2:
                                        versiones() # llamada de la funcion versiones
                                    elif seleccioneop == 3:
                                        continue
                                    else:
                                        seleccioneop == 4
                                        exit()
                    except ValueError:
                        print('Error')
                        continue
            except ValueError:
                print('Error de Opción')
    else:
        limpiar_pantalla()
        print('Por favor Introduce un nombre ')


