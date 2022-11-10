url = "https://bytebank.com/cambio?moedaOrigem=real"
print(f'URL completa: {url}')

indice_interrogacao = url.find('?')

url_base = url[:indice_interrogacao]
print(f'URB base: {url_base}')

url_parametros = url[indice_interrogacao+1:]
print(f'URL parâmetros: {url_parametros}')