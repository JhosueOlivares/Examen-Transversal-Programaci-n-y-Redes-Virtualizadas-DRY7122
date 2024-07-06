# Pedir al usuario que ingrese el número de VLAN
vlan = int(input("Ingrese el número de VLAN: "))

# Determinar si la VLAN está en el rango normal o extendido
if 1 <= vlan <= 1005:
    print(f"La VLAN {vlan} está en el rango normal.")
elif 1006 <= vlan <= 4094:
    print(f"La VLAN {vlan} está en el rango extendido.")
else:
    print(f"La VLAN {vlan} está fuera del rango permitido.")
