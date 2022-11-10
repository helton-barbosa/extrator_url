url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
# print(f'URL completa: {url}')

indice_interrogacao = url.find('?')

url_base = url[:indice_interrogacao]
# print(f'URB base: {url_base}')

url_parametros = url[indice_interrogacao+1:]
print(f'URL parâmetros: {url_parametros}')

parametro_de_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parametro_de_busca)
indice_valor = indice_parametro + len(parametro_de_busca) + 1
valor = url_parametros[indice_valor:]
print(valor)