import ipaddress

def order_subnet(subnets):
    """
    Ordena las subredes de menor a mayor cantidad de host disponibles.
    """
    return dict(sorted(subnets.items(), key=lambda x: x[1]['hosts'],reverse=True))

def calculate_usable_bits(subnet):
    """
    Calcula la cantidad de bits usables para la creación de subredes.
    """

    number_of_hosts = subnet['hosts']
    bits = 0
    n = 2
    while(True):
        bits = 2**n
        if bits > number_of_hosts:
            return n
        n += 1

def calculate_util_hosts(n):
    """
    Calcula la cantidad de hosts útiles para una subred.
    """
    return 2**n - 2

def calculate_mask(n):
    """
    Calcula el valor de la mascara de red
    """
    return 32 - n

def calculate_magic_number_aux(mask_number):
    """
    Convierte el valor mask_number en una máscara de subred binaria de 32 bits.
    """
    # Crear una cadena de 'n' bits 1 seguidos de (32 - n) bits 0
    bits = '1' * mask_number + '0' * (32 - mask_number)
    
    # Dividir la cadena en grupos de 8 para representar los octetos
    octetos = [bits[i:i+8] for i in range(0, 32, 8)]
    
    # Devolver la representación en bloques de octetos separados por puntos
    return '.'.join(octetos)

def calculate_magic_number(mask_number):
    """
    Calcula el número mágico de una máscara de subred.
    """

    bits = calculate_magic_number_aux(mask_number).replace('.', '')
    last_seven = bits[-8:]
    n = int(last_seven, 2)
    return 256 - n

def modify_last_octet(ip_address, new_value):
    """
    Modifica el último octeto de una dirección IP y lo reemplaza con el nuevo valor.
    """
    # Dividir la dirección IP en octetos
    octets = ip_address.split('.')
    
    # Asegurarse de que el nuevo valor esté en el rango válido
    if not (0 <= new_value <= 255):
        raise ValueError("El nuevo valor debe estar entre 0 y 255.")
    
    # Modificar el último octeto
    octets[-1] = str(new_value)
    
    # Juntar los octetos en una nueva dirección IP
    new_ip_address = '.'.join(octets)
    
    return new_ip_address

def get_last_octet(ip_address):
    """
    Obtiene el último octeto de una dirección IP.
    """
    # Dividir la dirección IP en octetos
    octets = ip_address.split('.')
    
    # Obtener el último octeto
    return int(octets[-1])

def get_first_last_borad_ips(network_ip, last_octect, magic_number):
    """
    Obtiene el IP de la primera, última dirección y el broadcast de una subred.
    """
    
    # Obtener la primera dirección IP utilizable
    first_ip = modify_last_octet(network_ip, last_octect+1)
    
    # Obtener la última dirección IP utilizable
    last_ip = modify_last_octet(network_ip, last_octect+magic_number-2)

    # Obtener la dirección de broadcast
    broadcast_ip = modify_last_octet(network_ip, last_octect+magic_number-1)
    
    return first_ip, last_ip, broadcast_ip


def calculate_subnet_table(subnet_ip, subnet_hosts, mask_number):
    """
    Genera la tabla con Subred, ID de Red, Máscara, Primera Dirección, Última Dirección y Broadcast.
    """
    # Calcular los bits necesarios para los hosts
    usable_bits = calculate_usable_bits(subnet_hosts)
    hosts = calculate_util_hosts(usable_bits)
    mask = calculate_mask(usable_bits)
    magic_number = calculate_magic_number(mask)
    substraction = 256 - magic_number
    mask_value = modify_last_octet(mask_number,substraction)
    last_octect = get_last_octet(subnet_ip)
    first_ip, second_ip, broadcast_ip = get_first_last_borad_ips(subnet_ip, last_octect, magic_number)
    modified_ip = modify_last_octet(subnet_ip, get_last_octet(broadcast_ip)+1)

    table = f"""
    Id de la red: {subnet_ip}
    Máscara: {mask_value}
    Primera: {first_ip}
    Última: {second_ip}
    Broadcast: {broadcast_ip} 

    """
    
    return table, modified_ip

def vlsm_calculator(net_ip, mask_number, subnets):
     """
     Calculadora VLSM que genera la tabla de subredes para una red dada.
     """
     subnet_ip = net_ip
     order_subnets = order_subnet(subnets)
     for subnet_key, data in order_subnets.items():
        table, subnet_ip = calculate_subnet_table(subnet_ip, data, mask_number)
        print(f"Tabla para {subnet_key}:\n{table}")

if __name__ == '__main__':
    # Subredes
    subnets = {'A': {'hosts': 25}, 'B': {'hosts': 10}, 'C': {'hosts': 50}, 'D': {'hosts': 80}}

    # Dirección de la subred
    subnet_ip = '192.168.1.0' 

    # Máscara de red
    mask_number = '255.255.255.0'

    vlsm_calculator(subnet_ip, mask_number, subnets) 
   