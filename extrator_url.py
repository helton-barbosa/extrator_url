import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not bool(self.url):
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("A URL não é válida")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_de_busca):
        indice_parametro = self.get_url_parametros().find(parametro_de_busca)
        indice_valor = indice_parametro + len(parametro_de_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url

url = "https://www.bytebank.com/cambio?moedaDestino=real&quantidade=25&moedaOrigem=dolar"
extrator_url = ExtratorURL(url)
# extrator_url_2 = ExtratorURL(url)
# print("O tamanho da URL: ", len(extrator_url))
# print(extrator_url)
# valor_quantidade = extrator_url.get_valor_parametro("quantidade")
# print(valor_quantidade)
# print(extrator_url == extrator_url_2)
# print(id(extrator_url))
# print(id(extrator_url_2))


moeda_dolar = 5.53
origem = extrator_url.get_valor_parametro("moedaOrigem")
destino = extrator_url.get_valor_parametro("moedaDestino")
valor = extrator_url.get_valor_parametro("quantidade")
conversao = None

if origem == "real" and destino == "dolar":
    conversao = int(valor) / moeda_dolar
    print(f'R${valor} é igual a ${str(conversao)}.')
elif origem == "dolar" and destino == "real":
    conversao = int(valor) * moeda_dolar
    print(f'${valor} é igual a R${str(conversao)}.')
else:
    print(f"Não foi possível calcular o câmbio de {origem} para {destino}.")