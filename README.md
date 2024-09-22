# Practica4_Enjambre

## Acerca del programa

El programa usa funciones auxiliares para dividir el trabajo, la funcion principal se llama vlsm_calculator y recibe como parametros las subredes, la mascara de red y la ip de la red inicial


## Ejecución el programa

Para ejecutar el programa solo se necesita usar el comando

```bash
python vlsm_calculator.py
```
El programa le solicitará al usuario la ip de la red principal, despues se le solicitara la cantidad de subredes que se requiere, y al final se le pedirá ingresar el numero de hosts para cada subred. 

<img width="447" alt="image" src="https://github.com/user-attachments/assets/18ba54ec-0829-4d60-a057-4b7e38cacc69">

### Acerca de los parametros de la función

- net_ip: Es la ip de la red inicial en formato string
- mask_number: Es la mascara de red en formato string (Por defecto se usa la máscara de red '255.255.255.0')
- subnets: Diccionario de la forma {1: {'hosts': NumeroDeHosts}, 2: {'hosts': NumeroDeHosts}, ...} que se construye con las entradas del usuario 

### Ejemplo de inputs válidos 

- net_ip = '192.168.1.0'
- cantidad de redes: 4
- Hosts para la red 1: 80
- Hosts para la red 2: 25
- Hosts para la red 1: 20
- Hosts para la red 1: 40

>[!NOTE]
>Como estamos usando una máscara de red por defecto, la cantidad de redes no debe ser mayor a 4, pues el rango de las máscaras en las subredes superarían el 255, lo cual no sería una máscara válida. 
