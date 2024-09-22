# Practica4_Enjambre

## Acerca del programa

El programa usa funciones auxiliares para dividir el trabajo, la funcion principal se llama vlsm_calculator y recibe como parametros las subredes, la mascara de red y la ip de la red inicial

### Acerca de los parametros de la función

- net_ip: Es la ip de la red inicial en formato string
- mask_number: Es la mascara de red en formato string
- subnets: Diccionario de la forma {'NombreSubRed': {'hosts': NumeroDeHosts}}

### Ejemplo de parametros validos

- net_ip = '192.168.1.0'
- subnets = {'A': {'hosts': 25}, 'B': {'hosts': 10}, 'C': {'hosts': 50}, 'D': {'hosts': 80}}

## Para ejecutar el programa

Para ejecutar el programa solo se necesita usar el comando

```bash
python vlsm_calculator.py
```
El programa le solicitará al usuario la ip de la red principal, despues se le solicitara la cantidad de subredes que se requiere, y al final se le pedirá ingresar el numero de hosts para cada subred. 
