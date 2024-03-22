import nmap

class Kraken:
    def menu_opc(self):
        print("---------------Configuracion inicial---------------")
        self.host = input("Ingrese el host: ")

        print("1 - Exploración completa.")
        print("2 - Escaneo de puertos.")
        print("3 - Detectar sistema operativo y servicios.")

        opc = input("Ingrese la opción: ")
        if opc.strip() == "":
            print("Debe ingresar una opción válida.")
            self.menu_opc()  # Vuelve a llamar a menu_opc() si la entrada está vacía
            return

        opc = int(opc)

        if opc == 1:
            conf = input("¿Desea escanear todos los puertos? (S/n): ").lower()
            if conf == 's':
                self.t_config = "-p- -sV -O --script vuln"
            else:
                self.t_config = "-sV -O --script vuln"
        elif opc == 2:
            self.t_config = "-p 1-65535 -sV -O --script vuln"
        elif opc == 3:
            self.t_config = "-sV -O --script vuln"
        else:
            print("Opción no válida.")

    def __init__(self):
        # Crear un objeto de escaneo
        nm = nmap.PortScanner()
        self.menu_opc()  # Llamamos a menu_opc() usando self
        
        # Escanear un host o una red (en este caso, localhost)
        nm.scan(hosts=self.host, arguments=self.t_config)
    
        # Iterar sobre los resultados del escaneo
        for host in nm.all_hosts():
            print('----------------------------------------------------')
            print('Host : %s (%s)' % (host, nm[host].hostname()))
            print('Estado : %s' % nm[host].state())

            # Iterar sobre los protocolos
            for proto in nm[host].all_protocols():
                print('Protocolo : %s' % proto)

                # Iterar sobre los puertos
                for port in nm[host][proto]:
                    if nm[host][proto][port]['state'] == 'open':
                        print('Puerto : %s\tEstado : %s\tNombre del Servicio: %s\tVersión: %s' % (
                            port,
                            nm[host][proto][port]['state'],
                            nm[host][proto][port]['name'],
                            nm[host][proto][port]['product']
                        ))

# Crear una instancia de la clase Kraken
Kraken()
