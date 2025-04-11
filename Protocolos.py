
OSPF = 110
RIP = 120
EIGRP = 90
BGP = 20

protocolo = input("Ingrese el nombre del protocolo que desea saber la Distancia administrativa(OSPF, RIP, EIGRP, BGP): ").upper()

if protocolo == "OSPF":
    print(f"La distancia administrativa de OSPF es {OSPF}.")
elif protocolo == "RIP":
    print(f"La distancia administrativa de RIP es {RIP}.")
elif protocolo == "EIGRP":
    print(f"La distancia administrativa de EIGRP es {EIGRP}.")
elif protocolo == "BGP":
    print(f"La distancia administrativa de BGP es {BGP}.")
else:
    print("Protocolo no reconocido. Por favor, ingrese un protocolo válido (OSPF, RIP, EIGRP, BGP).")