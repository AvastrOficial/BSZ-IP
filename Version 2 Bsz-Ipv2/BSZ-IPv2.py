import time
import sys
import requests
import ipinfo
from colorama import Fore, Style, init

# Inicializar colorama
init()

def fetch_ip_address_info():
    print(f"""
{Fore.GREEN}
▀█████████▄     ▄████████  ▄███████▄             ▄█     ▄███████▄ 
  ███    ███   ███    ███ ██▀     ▄██           ███    ███    ███ 
  ███    ███   ███    █▀        ▄███▀           ███▌   ███    ███ 
 ▄███▄▄▄██▀    ███         ▀█▀▄███▀▄▄           ███▌   ███    ███ 
▀▀███▀▀▀██▄  ▀███████████   ▄███▀   ▀           ███▌ ▀█████████▀  
  ███    ██▄          ███ ▄███▀                 ███    ███        
  ███    ███    ▄█    ███ ███▄     ▄█           ███    ███        
▄█████████▀   ▄████████▀   ▀████████▀           █▀    ▄████▀   

    By @AvaStrOficial    / Version : 0.0.2 /                                                             
{Style.RESET_ALL}
    """)

    access_token = "6b1f42952f063e"
    handler = ipinfo.getHandler(access_token)
    ip = input("Ingrese la dirección IP: ")

    for i in range(11):
        time.sleep(0.1)
        color = Fore.RED if i % 3 == 0 else (Fore.YELLOW if i % 3 == 1 else Fore.BLUE)
        sys.stdout.write(f"\rObteniendo información de la IP... [{color}{'='*i}{Style.RESET_ALL}{' '*(10-i)}] {Fore.GREEN}{i*10}%{Style.RESET_ALL}")
        sys.stdout.flush()

    print("\n")

    try:
        # Obtener datos de la primera fuente (ipinfo)
        details = handler.getDetails(ip)
        data1 = details.all

        # Obtener datos de la segunda fuente (ipapi.co)
        response = requests.get(f"https://ipapi.co/{ip}/json/")
        if response.status_code == 200:
            data2 = response.json()
        else:
            data2 = {}

        # Obtener datos de la tercera fuente (ip2location.io)
        response = requests.get(f"https://api.ip2location.io/?key=3C93D50C65D44735DF3C48A56FFD9899&ip={ip}")
        if response.status_code == 200:
            data3 = response.json()
        else:
            data3 = {}

        # Combinar datos de las tres fuentes
        combined_data = {**data1, **data2, **data3}

        # Mostrar la información combinada
        display_ip_info(combined_data)

    except ipinfo.exceptions.RequestQuotaExceededError:
        print("Se ha excedido el límite de solicitudes de la API.")
    except ipinfo.exceptions.AuthenticationError:
        print("Error de autenticación. Asegúrate de que tu token de acceso sea válido.")
    except Exception as e:
        print(f"Error: {str(e)}")

def display_ip_info(data):
    def get_nested(data, keys, default="No disponible"):
        for key in keys:
            if isinstance(data, dict):
                data = data.get(key, default)
            else:
                return default
        return data

    asn = data.get('asn', "No disponible")
    asn_url = f"https://ipinfo.io/AS{asn}" if asn != "No disponible" else "No disponible"

    print(f'''
    🏝️ País: {data.get('country_name', "No disponible")}
    🗺️ Región: {data.get('region', data.get('region_name', "No disponible"))}
    🌆 Ciudad: {data.get('city', data.get('city_name', "No disponible"))}
    📮 Código postal: {data.get('postal', data.get('zip_code', "No disponible"))}
    🌍 Latitud: {data.get('latitude', "No disponible")}
    🌍 Longitud: {data.get('longitude', "No disponible")}
    ⏰ Zona horaria: {data.get('timezone', data.get('time_zone', "No disponible"))}
    ⏰ Zona horaria (olson): {get_nested(data, ['time_zone_info', 'olson'])}
    ⏰ Hora actual: {get_nested(data, ['time_zone_info', 'current_time'])}
    ⏰ GMT offset: {get_nested(data, ['time_zone_info', 'gmt_offset'])}
    ⏰ DST: {"Sí" if get_nested(data, ['time_zone_info', 'is_dst'], False) else "No"}
    🌅 Amanecer: {get_nested(data, ['time_zone_info', 'sunrise'])}
    🌇 Atardecer: {get_nested(data, ['time_zone_info', 'sunset'])}
    💼 ISP: {data.get('org', data.get('isp', "No disponible"))}
    📞 Código de llamada de país: {data.get('country_calling_code', data.get('idd_code', "No disponible"))}
    🌐 Lenguaje: {data.get('languages', get_nested(data, ['country', 'language', 'name']))}
    📊 Código ISO 3166-1 alfa-2: {data.get('country_code', get_nested(data, ['country', 'alpha2_code']))}
    📊 Código ISO 3166-1 alfa-3: {data.get('country_code_iso3', get_nested(data, ['country', 'alpha3_code']))}
    🔒 Código postal seguro: {"Sí" if data.get('in_eu', False) else "No"}
    📡 ASN: {asn} (URL: {asn_url})
    📶 Tipo de conexión: {data.get('connection_type', data.get('net_speed', "No disponible"))}
    🌐 Dominio: {data.get('domain', "No disponible")}
    🛡️ Utiliza VPN: {"Sí" if data.get('vpn', data.get('is_proxy', False)) else "No"}
    ☎️ Código de área: {data.get('area_code', "No disponible")}
    📶 Código de red móvil: {data.get('mobile', data.get('mcc', "No disponible"))}
    🖥️ Tipo de dispositivo: {data.get('device_type', "No disponible")}
    🌐 Tipo de navegador: {data.get('browser', "No disponible")}
    🇪🇺 Región de la Unión Europea: {"Sí" if data.get('in_eu', False) else "No"}
    🏙️ Ciudad en la Unión Europea: {data.get('eu_city', data.get('city_name', "No disponible"))}
    🏙️ Código postal en la Unión Europea: {data.get('eu_postal', data.get('zip_code', "No disponible"))}
    ☎️ Código de área telefónica: {data.get('area_code', "No disponible")}
    🏢 Tipo de uso: {data.get('usage_type', "No disponible")}
    🌍 IPv4: {data.get('ip', "No disponible")}
    🌍 Versión de IP: {data.get('version', "No disponible")}
    🌍 Tipo de IP: {data.get('type', data.get('address_type', "No disponible"))}
    🌍 Clase de IP: {data.get('ip_class', "No disponible")}
    🌐 Proxy: {"Sí" if data.get('proxy', data.get('is_proxy', False)) else "No"}
    🏢 Dominio secundario: {data.get('domain_secondary', "No disponible")}
    🔢 Número de bloque de IP: {data.get('ip_block', "No disponible")}
    🔒 Secure Proxy: {"Sí" if data.get('secure_proxy', False) else "No"}
    🛡️ Seguridad: {data.get('security', "No disponible")}
    🌐 Velocidad de conexión: {data.get('connection_speed', "No disponible")}
    📶 Tipo de red móvil: {data.get('mobile_type', "No disponible")}
    🎯 Propósito de uso de la IP: {data.get('ip_purpose', "No disponible")}
    📅 Fecha y hora de la consulta: {data.get('request_time', "No disponible")}
    ⏰ Hora local: {data.get('localtime', get_nested(data, ['time_zone_info', 'current_time']))}
    🏢 Organización: {data.get('org', data.get('isp', "No disponible"))}
    📡 Carrier móvil: {data.get('carrier', "No disponible")}
    🏢 Proveedor de Hosting: {data.get('hosting', "No disponible")}
    🏪 Tipo de mercado: {data.get('market', "No disponible")}
    🏪 Descripción del mercado: {data.get('market_description', "No disponible")}
    🌐 URL: {data.get('url', "No disponible")}
    ''')

fetch_ip_address_info()
