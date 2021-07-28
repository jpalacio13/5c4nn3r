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
def limpiar_pantalla():
    time.sleep(1)
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')



def ping_rangos():
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
        #lista_ips_activas = ','.join(ips_activas)
        if ips_activas != set():
            list_ips_activas = list(set(ips_activas))
            list_ips_activas.sort()
            print(f'Las IPs Activas son: ')

            for ips in list_ips_activas:
                print(ips)

        else:
            print('No hay Host Activos')

    return
def ping_General():
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

def sub_menu ():
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

def versiones ():
    import os

    NMAP_CMD = "nmap -sV  192.168.150.130 -p 21,22"
    respuesta = os.system(NMAP_CMD)


def opcion_ports():
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
                            print(f'{n}', sep=',', end='')
                        relacionip_ports[list_ips_activas] = list(abirtos)
                        abirtos.clear()
                    else:
                        print('No hay Puertos Abiertos')

                    print('\n')
                print('Escaneo Finalizado')
            else:
                for i in list_ips_activas: ## Corrigiendo verificando
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
                            print(f'{n}', sep=',', end='')
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
                                    print(f'{n}', sep=',', end='')
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
                                print(f'{n},', end='')
                            relacionip_ports[i] = list(abirtos)
                            abirtos.clear()
                        else:
                            print('No hay Puertos Abiertos')

                        print('\n')
                        print('Escaneo Finalizado')
                    except ValueError:
                        print('Error de Opción')
def opcion_ports_selec():
    menu_rangos_puertos = [
        'Escanear todos los puertos',
        'Escanear Puertos en Particular',
        'Regresar al Inicio'
    ]
    for pos, opcion in enumerate(menu_rangos_puertos, 1):
        print(f'{pos}: {opcion}')

    opcion_rango_port = int(input('Ingrese Una Opcion: '))
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
                print(f'Los puertos abiertos de {i} son: ', end='')
                for n in abiertos:
                    print(f'{n}', sep=',', end='')
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
                        print(f'{n}',',', end='')
                    relacionip_ports[ip] = abirtos
                    abirtos.clear()

                else:
                    print('No hay Puertos Abiertos')

                print('\n')
                print('Escaneo Finalizado')

            except ValueError:
                print('Error de Opción')
def scanner ():
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
while True:
    nombre_usuario = input('Ingrese su nombre: ')
    if nombre_usuario != '':
        print(f'Hola {nombre_usuario}, Bienvenido al programa de Scanner FUAA')
        myhost = socket.gethostname()
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
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
            'Conectarse a FTP o SSH de Ips Activas',
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
                            'Buscar IPs entre un rango especifico del segmento',
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
                            ping_rangos()
                            sub_menu()


                        elif seleccion_opcion == 2:
                            ping_General()
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
                    scanner()

                elif opcion_usuario == 3:
                    if relacionip_ports == {}:
                        print('No se han identificado Ips Activas con puertos abiertos \n')
                    else:
                        print(relacionip_ports)
                        print('Esta Opción solo permite conexiones a FTP y SSH de Ips Activas \n')

                        menuconect = [
                            'Conectarse a FTP',
                            'Coectarse a SSH',
                            'Conectarse a RDP'
                        ]
                        for pos, i in enumerate(menuconect, 1):
                            print(f'{pos},{i}')
                        opcionconnet = int(input('Seleccione una Opción: '))
                        if opcionconnet == 1:
                            conftp = []
                            for i, n in relacionip_ports.items():
                                for e in n:
                                    if e == 21:
                                        conftp.append(i)
                            conftp.sort()
                            if conftp == []:
                                print('No hay Ips con puerto FTP por defecto abierto')
                            else:
                                print('IPs disponibles para conectarse por FTP')
                                for u in conftp:
                                    print(u ,'\n')



            except ValueError:
                print('Error de Opción')
    else:
        limpiar_pantalla()
        print('Por favor Introduce un nombre ')


