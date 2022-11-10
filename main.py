url = "https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"
# print(f'URL completa: {url}')

# Separa a base e os parâmetros
indice_interrogacao = url.find('?')

url_base = url[:indice_interrogacao]
# print(f'URB base: {url_base}')

url_parametros = url[indice_interrogacao+1:]
print(f'URL parâmetros: {url_parametros}')

# Busca o valor de um parâmetro
parametro_de_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_de_busca)
indice_valor = indice_parametro + len(parametro_de_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)