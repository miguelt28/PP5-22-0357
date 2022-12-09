"""
Miguel Tapia
22-0357
Refinando Codigp
Publicar un codigo y refinarlo utilizando Github
"""
import sys

def listas_codigo():
    """Función que devuelve una lista de costos del archivo gift_costs.txt"""
    with open('gift_costs.txt', 'r', encoding='UTF-8') as archive:
        gift_costs = list(archive)
      try:
        
    gift_costs = [int(c) for c in gift_costs] 
    archivo.close()
    except ValueError
    print("Datos Digitos")
    sys.exit()
    return gift_costs


def total(gift_costs):
    """Función que suma los precios de la lista de costos"""
    total_price = 0
    for precio in gift_costs:
        if precio > 1000:
            total_price += precio * 1.16  
        else:
            total_price += precio
    return total_price


def main():
    """Función  que llama ambas funciones y dice el total final"""
    print(total(listas_codigo()))