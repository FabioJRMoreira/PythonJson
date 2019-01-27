import json
import urllib.request
import datetime



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

def busca_empresa(estado, produto):
    tam = []
    try:
        for comp in carrega_json():
            if(produto in comp and estado in comp):
                tam.append(comp)
                print(comp)
        tamanho = len(tam)
        compId = tam[0][0]
        grava_busca(tam, tamanho, compId)
    except IndexError:
        print("erro na leitura da lista")

def grava_busca(companias,tamanho,id):
    data = datetime.datetime.now()
    nome = str(data.date())+str(id)+str(tamanho)+".txt"
    print(nome)
    try:
        arquivo = open('C:\\Temp\\'+nome, 'w')
        for empresa in companias:
            arquivo.writelines(empresa)

    except FileNotFoundError:
        arquivo = open(nome, 'w')
        arquivo.writelines(u'Arquivo criado pois nao existia')
    arquivo.close()
#teste commite
busca_empresa('SP','mousse')