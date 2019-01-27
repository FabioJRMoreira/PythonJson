import json
import urllib.request


def carrega_json():
    arquivo = urllib.request.urlopen('https://api-sandbox.contabilizei.com/ds/customers')

    js = arquivo.read()

    info = json.loads(js.decode("utf-8"))

    companias = []

    for intens in info:
        cp=[]
        cp.append(intens['company_Id'])
        for stat in intens['company_state']:
            cp.append(stat)
        for produtos in intens['Products_list']:
            for produto in produtos['product']:
                cp.append(produto)
            cp.append(produtos['product_price'])
        companias.append(cp)
    return companias

def busca_empresa(estado ,produto):
    for comp in carrega_json():
        if(produto in comp and estado in  comp):
            print(comp)
#teste commite
busca_empresa('ctba','mousse')