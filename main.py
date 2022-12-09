"""
Miguel Tapia
22-0357
Refinando Codigp
Publicar un codigo y refinarlo utilizando Github
"""


def listas_codigo():
    archives = open('gift_costs.txt', 'r')
    gift_costs = list(archives)
    gift_costs = [int(c) for c in gift_costs]  # funcion int
    archives.close()  # terminar con el archivo
    return gift_costs


def totales(gift_costs):
    precio_total = 0
    for cost in gift_costs:
        if cost > 1000:
            precio_total += cost * 1.16  # agrega impuestos
        else:
            precio_total += cost  # los costos menores a 1000 no se le agrega impuesto

    return precio_total


def main():
    print(totales(listas_codigo()))
    # llama a los dos funciones y luego imprime el resultado

if __name__ == '_main_':
    main()