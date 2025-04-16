def connect_to(ssid: str, passwd: str) -> str:
    """
    Conecta el microcontrolador a la red indicada y retorna la dirección IP asignada.
    
    Parameters
    ----------
    ssid : str
        Nombre de la red a conectarse.
    passwd : str
        Contraseña de la red.
    
    Returns
    -------
    str
        Dirección IP asignada por el router.
    """
    import network
    from time import sleep

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(ssid, passwd)
        # Espera a que se conecte (ajusta el tiempo si es necesario)
        while not sta_if.isconnected():
            sleep(0.05)
    # Retorna la IP (primer elemento de la tupla ifconfig)
    return sta_if.ifconfig()[0]

import machine
import ssd1306

# Inicializar el bus I2C usando SoftI2C para evitar la advertencia.
i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21))

# Inicializar la pantalla OLED (verifica la resolución de tu pantalla, comúnmente 128x64)
oled = ssd1306.SSD1306_I2C(128, 32, i2c)



# Conectar a la red y obtener la dirección IP.
ip = connect_to("Cooperadora Alumnos", "")

# Mostrar la dirección IP en la pantalla OLED.
oled.text("IP:", 0, 16)
oled.text(ip, 0, 26)
oled.show()
