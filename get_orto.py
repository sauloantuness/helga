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
    files = os.listdir('./data/contratos')
    ids = [int(f.split('.')[0]) for f in files]
    return ids

def get_contratos():
    dowloaded_ids = downloaded()

    sys.setrecursionlimit(100000)
    ID_CONTRATO = CONFIG['ID_CONTRATO']
    c = ContratoOrto(ID_CONTRATO)

    while ID_CONTRATO: 
        if ID_CONTRATO in dowloaded_ids:
            print(ID_CONTRATO)
            ID_CONTRATO -= 1
            continue

        begin = datetime.now()

        c.set_id_contrato(ID_CONTRATO)
        contrato = c.get_info()

        if contrato:
            print(contrato['id_contrato'] + ' contrato')
            save_obj(contrato, 'contratos', contrato['id_contrato'])

            for mensalidade in c.get_mensalidades():
                print('\t' + mensalidade['id_mensalidade'] + ' mensalidade')
                save_obj(mensalidade, 'mensalidades', mensalidade['id_mensalidade'])

        else:
            print(str(ID_CONTRATO) + ' invalido')

        ID_CONTRATO -= 1

        end = datetime.now()

        duration = end - begin

        print('Tempo estimado: %d:%02d' % days_hours_minutes(duration * ID_CONTRATO)[1:])


if __name__ == '__main__':
    if not os.path.exists('./data/clientes'):
        os.makedirs('./data/clientes')

    if not os.path.exists('./data/contratos'):
        os.makedirs('./data/contratos')

    if not os.path.exists('./data/mensalidades'):
        os.makedirs('./data/mensalidades')

    get_contratos()
