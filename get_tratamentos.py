import os, sys
import pickle
from meddent.meddent import *
from meddent.config import *
from pprint import pprint
from datetime import datetime

def save_obj(obj, folder, name):
    with open('data/'+ folder + '/' + name + '.pkl', 'wb') as f:
        pickle.dump(obj, f)

def load_obj(folder, name):
    with open('data/' + folder + '/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def days_hours_minutes(td):
    return td.days, td.seconds//3600, (td.seconds//60)%60

def downloaded():
    files = os.listdir('./data/clientes')
    ids = [int(f.split('.')[1]) for f in files]
    return ids

def get_contratos():
    dowloaded_ids = downloaded()

    sys.setrecursionlimit(100000)
    ID_CLIENTE = CONFIG['ID_CLIENTE']
    link_pagina_tratamento = None
    cliente = Cliente(ID_CLIENTE)

    while ID_CLIENTE:
        if ID_CLIENTE in dowloaded_ids:
            print(ID_CLIENTE)
            ID_CLIENTE -= 1
            continue

        begin = datetime.now()

        cliente.set_id_cliente(ID_CLIENTE)
        soup = cliente.get_pagina_tratamento(link_pagina_tratamento)
        link_pagina_tratamento = None

        tratamento = Tratamento(soup)
        procedimentos = tratamento.get_procedimentos()

        if procedimentos:
            tratamento = {
                'id_cliente': procedimentos[0]['id_cliente'],
                'id_tratamento': procedimentos[0]['id_tratamento'],
                'dentista': soup.find(id='idOrcamento').find_all('tr')[2].text.split('-')[1].strip(),
                'procedimentos': procedimentos,
            }

            print(tratamento['id_tratamento'] + ' tratamento')
            save_obj(tratamento, 'tratamentos', tratamento['id_tratamento'])

            pagamento = Pagamento(soup)
            pagamentos = pagamento.get_pagamentos()

            for pagamento in pagamentos:
                print('\t' + pagamento['id_pagamento'] + ' pagamento')
                save_obj(pagamento, 'pagamentos', pagamento['id_pagamento'])


            link_pagina_tratamento = cliente.get_link_tratamento_anterior(soup)
        else:
            print(str(ID_CLIENTE) + ' invalido')


        if not link_pagina_tratamento:
            ID_CLIENTE -= 1

        end = datetime.now()
        duration = end - begin
        print('Tempo estimado: %d:%02d' % days_hours_minutes(duration * ID_CLIENTE)[1:])


if __name__ == '__main__':
    if not os.path.exists('./data/clientes'):
        os.makedirs('./data/clientes')

    if not os.path.exists('./data/contratos'):
        os.makedirs('./data/contratos')

    if not os.path.exists('./data/mensalidades'):
        os.makedirs('./data/mensalidades')

    if not os.path.exists('./data/pagamentos'):
        os.makedirs('./data/pagamentos')

    if not os.path.exists('./data/tratamentos'):
        os.makedirs('./data/tratamentos')

    get_contratos()
#   pprint(load_obj('tratamentos', '15236'))
#   pprint(load_obj('pagamentos', '35163'))
