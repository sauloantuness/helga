from meddent.meddent import Meddent
from meddent.config import *
from pprint import pprint
import pyodbc


server = '192.168.15.58'
#server = 'r13.ddns.me'
port = '49841' 
database = CONFIG['DATABASE']
username = 'sa'
password = 'r13r13r13'

cnxn = pyodbc.connect('DRIVER=FreeTDS;SERVER='+server+';PORT='+port+';DATABASE='+database+';UID='+username+';PWD='+ password + ';TDS_Version=7.2;')
cursor = cnxn.cursor()



def basic_insert(tabela, id, ds):
    sql = 'INSERT INTO tb_{0} (id_{0}, ds_{0}) values (?, ?);'.format(tabela)
    cursor.execute(sql, id, ds)
    cursor.commit()

def get_options(name, soup):
    items = []

    for option in soup.find(attrs={'name': name}).find_all('option'):
        items.append({
            'id': option.get('value'),
            'ds': option.text.strip(),
        })

    return items

auxiliares = [
    {
        'name': 'id_cartao',
        'tabela': 'convenio'
    },
    {
        'name': 'estadocivil',
        'tabela': 'estado_civil'
    },
    {
        'name': 'conheceu',
        'tabela': 'marketing'
    },
    {
        'name': 'id_dentista',
        'tabela': 'indicacao'
    },
]


m = Meddent()
soup = m.get_pagina(m.CLIENTE_LIST_URL)


for auxiliar in auxiliares:
    options = get_options(auxiliar['name'], soup)

    for option in options:
        pprint(option)
        basic_insert(auxiliar['tabela'], **option)
    print()


soup = m.get_pagina(m.TRATAMENTO_LIST_URL + '&method=onView')

auxiliares = [
    {
        'name': 'id_dentista',
        'tabela': 'dentista'
    },
]


for auxiliar in auxiliares:

    options = get_options(auxiliar['name'], soup)

    for option in options:
        pprint(option)
        basic_insert(auxiliar['tabela'], **option)
    print()
