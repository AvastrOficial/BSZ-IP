import time
import sys
import ipinfo

def fetch_ip_address_info():
    # Banner 3D
    print("""
▀█████████▄     ▄████████  ▄███████▄             ▄█     ▄███████▄ 
  ███    ███   ███    ███ ██▀     ▄██           ███    ███    ███ 
  ███    ███   ███    █▀        ▄███▀           ███▌   ███    ███ 
 ▄███▄▄▄██▀    ███         ▀█▀▄███▀▄▄           ███▌   ███    ███ 
▀▀███▀▀▀██▄  ▀███████████   ▄███▀   ▀           ███▌ ▀█████████▀  
  ███    ██▄          ███ ▄███▀                 ███    ███        
  ███    ███    ▄█    ███ ███▄     ▄█           ███    ███        
▄█████████▀   ▄████████▀   ▀████████▀           █▀    ▄████▀      
                                                                     
    """)

    access_token = "6b1f42952f063e"  # Reemplaza con tu propio token de acceso
    handler = ipinfo.getHandler(access_token)
    ip = input("Ingrese la dirección IP: ")

    # Simulación de carga
    for _ in range(10):
        time.sleep(0.1)
        sys.stdout.write("\rObteniendo información de la IP... [%-10s] %d%%" % ('='*_, _*10))
        sys.stdout.flush()

    print("\n")

    try:
        details = handler.getDetails(ip)
        display_ip_info(details.all)
    except ipinfo.exceptions.IPNotFoundException:
        print("La dirección IP ingresada no se encontró en la base de datos.")
    except ipinfo.exceptions.RequestQuotaExceededError:
        print("Se ha excedido el límite de solicitudes de la API.")
    except ipinfo.exceptions.AuthenticationError:
        print("Error de autenticación. Asegúrate de que tu token de acceso sea válido.")

def display_ip_info(data):
    print(f'''
        Información de la IP: {data.get('ip', "No disponible")}
        🏝️ País: {data.get('country_name', "No disponible")}
        🗺️ Región: {data.get('region', "No disponible")}
        🌆 Ciudad: {data.get('city', "No disponible")}
        📮 Código postal: {data.get('postal', "No disponible")}
        🌍 Latitud: {data.get('latitude', "No disponible")}
        🌍 Longitud: {data.get('longitude', "No disponible")}
        ⏰ Zona horaria: {data.get('timezone', "No disponible")}
        💼 ISP: {data.get('org', "No disponible")}
        📞 Código de llamada de país: {data.get('country_calling_code', "No disponible")}
        🌐 Lenguaje: {data.get('languages', "No disponible")}
        📊 Código ISO 3166-1 alfa-2: {data.get('country_code', "No disponible")}
        📊 Código ISO 3166-1 alfa-3: {data.get('country_code_iso3', "No disponible")}
        🏠 Código postal seguro: {"Sí" if data.get('in_eu', False) else "No"}
        🖧 ASN: {data.get('asn', "No disponible")}
        🔹 Versión de IP: {data.get('version', "No disponible")}
        🔹 Tipo de IP: {data.get('type', "No disponible")}
        🔹 Clase de IP: {data.get('ip_class', "No disponible")}
        🔹 Proxy: {"Sí" if data.get('proxy', False) else "No"}
        🔹 Tipo de uso: {data.get('usage_type', "No disponible")}
        🔹 IPv4: {data.get('ip', "No disponible")}
        🔹 Secure Proxy: {"Sí" if data.get('secure_proxy', False) else "No"}
        🔹 Seguridad: {data.get('security', "No disponible")}
        🔹 Velocidad de conexión: {data.get('connection_speed', "No disponible")}
        🔹 Tipo de red móvil: {data.get('mobile_type', "No disponible")}
        🔹 Propósito de uso de la IP: {data.get('ip_purpose', "No disponible")}
        🔹 Hora local: {data.get('localtime', "No disponible")}
        🔹 Tipo de conexión móvil: {data.get('mobile_type', "No disponible")}
        🔹 Carrier móvil: {data.get('carrier', "No disponible")}
        🔹 Proveedor de Hosting: {data.get('hosting', "No disponible")}
        🔹 Tipo de mercado: {data.get('market', "No disponible")}
        🔹 Descripción del mercado: {data.get('market_description', "No disponible")}
        🔹 URL: {data.get('url', "No disponible")}
        🔹 Código de país telefónico: {data.get('country_calling_code', "No disponible")}
        🔹 Dominio: {data.get('domain', "No disponible")}
        🔹 Utiliza VPN: {"Sí" if data.get('vpn', False) else "No"}
        🔹 Código de área: {data.get('area_code', "No disponible")}
        🔹 Código de red móvil: {data.get('mobile', "No disponible")}
        🔹 Tipo de dispositivo: {data.get('device_type', "No disponible")}
        🔹 Tipo de navegador: {data.get('browser', "No disponible")}
        🔹 Código de país: {data.get('country_code', "No disponible")}
        🔹 Región de la Unión Europea: {data.get('in_eu', "No disponible")}
        🔹 Ciudad en la Unión Europea: {data.get('eu_city', "No disponible")}
        🔹 Código postal en la Unión Europea: {data.get('eu_postal', "No disponible")}
        🔹 Código de área telefónica: {data.get('area_code', "No disponible")}
    ''')

fetch_ip_address_info()
