import requests
from bs4 import BeautifulSoup


class Meddent():
    def __init__(self):
        self.CLIENTE_URL = 'http://meddent.com.br/admin/index.php?class=ClientesList&method=onEdit&key='
        self.BASE_URL = 'http://meddent.com.br'
        self.login()

    def login(self):
        self.session = requests.Session()
        data = {
            'nome': 'helga',
            'senha': '123456'
        }

        url = 'http://meddent.com.br/admin/index.php'

        self.session.post(url=url, data=data)

    def get_pagina(self, url):
        r = self.session.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        return soup

    def get_input_value(self, soup, name):
        return soup.find(attrs={'name': name}).get('value')

    def get_select_value(self, soup, name):
        select = soup.find(attrs={'name': name})

        if select.find('option', attrs={'selected': 'selected'}):
            return select.find('option', attrs={'selected': 'selected'}).get('value')

        return select.find('option').get('value')

    def get_radio_value(self, soup, name):
        return soup.find(attrs={'name': name, 'checked': 'checked'}).get('value')

    def get_textarea_value(self, soup, name):
        return soup.find(attrs={'name': name}).text.strip()


class Cliente(Meddent):
    def __init__(self, id_cliente):
        Meddent.__init__(self)
        self.id_cliente = id_cliente
        self.TRATAMENTO_URL = 'http://meddent.com.br/admin/index.php?class=TratamentosClientesList&method=onView&key='

    def set_id_cliente(self, id_cliente):
        self.id_cliente = id_cliente

    def get_info(self):
        url = self.CLIENTE_URL + str(self.id_cliente)
        r = self.session.get(url)

        soup = BeautifulSoup(r.text, 'html.parser')

        if not self.get_input_value(soup, 'id_cliente'):
            return None

        cliente = {
            'id_cliente': self.get_input_value(soup, 'id_cliente'),

            'nome': self.get_input_value(soup, 'nome'),
            'codigo': self.get_input_value(soup, 'codigo'),
            
            'sexo': self.get_radio_value(soup, 'sexo'),
            'dia': self.get_input_value(soup, 'dia'),
            'mes': self.get_input_value(soup, 'mes'),
            'ano': self.get_input_value(soup, 'ano'),
            
            'convenio': self.get_select_value(soup, 'id_cartao'),
            
            'profissao': self.get_input_value(soup, 'profissao'),
            
            'cpf': self.get_input_value(soup, 'cpf'),
            'estado_civil': self.get_select_value(soup, 'estadocivil'),
            
            'nacionalidade': self.get_input_value(soup, 'nacionalidade'),
            'naturalidade': self.get_input_value(soup, 'naturalidade'),
            
            'rg': self.get_input_value(soup, 'rg'),
            'rgorgao': self.get_input_value(soup, 'rgorgao'),
            
            'comercial': self.get_input_value(soup, 'comercial'),
            'residencial': self.get_input_value(soup, 'residencial'),
            
            'celular': self.get_input_value(soup, 'celular'),
            'celular2': self.get_input_value(soup, 'radio'),
            
            'email': self.get_input_value(soup, 'email'),
            
            'endereco': self.get_input_value(soup, 'endereco'),
            'complemento': self.get_input_value(soup, 'complemento'),
            
            'id_cidade': self.get_select_value(soup, 'id_cidade'),
            'id_bairro': self.get_select_value(soup, 'id_bairro'),
            
            'id_estado': self.get_select_value(soup, 'estado'),
            'cep': self.get_input_value(soup, 'cep'),
            
            'id_marketing': self.get_select_value(soup, 'conheceu'),
            'id_dentista': self.get_select_value(soup, 'id_dentista'),
            
            'obs': self.get_textarea_value(soup, 'obs'),

            'responsavel_nome': self.get_input_value(soup, 'responsavel'),
            'responsavel_cpf': self.get_input_value(soup, 'r_cpf'),
            'responsavel_endereco': self.get_input_value(soup, 'r_endereco'),
        }

        return cliente

    def get_pagina_tratamento(self, url=None):
        if not url:
            url = self.TRATAMENTO_URL + str(self.id_cliente)

        r = self.session.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        return soup


    def get_link_tratamento_anterior(self, soup):
        link_tratamento_anterior = None

        if soup.find(id='idOrcamento').find(attrs={'src': '../images/icons/leftmini.gif'}):
            link_tratamento_anterior = self.BASE_URL + soup.find(id='idOrcamento').find(attrs={'src': '../images/icons/leftmini.gif'}).parent.get('href')

        return link_tratamento_anterior


    def get_link_tratamento_posterior(self, soup):
        link_tratamento_proximo = None

        if soup.find(id='idOrcamento').find(attrs={'src': '../images/icons/rightmini.gif'}):
            link_tratamento_proximo = self.BASE_URL + soup.find(id='idOrcamento').find(attrs={'src': '../images/icons/rightmini.gif'}).parent.get('href')

        return link_tratamento_proximo


class Tratamento():
    def __init__(self, soup):
        self.soup = soup

    def get_procedimento(self, soup_tr):
        return {
            'id_tratamento': self.soup.find(attrs={'name':'id_tratamento'}).get('value'),
            'id_cliente': self.soup.find(attrs={'name':'id_cliente'}).get('value'),
            'data': soup_tr.find_all('td')[1].text.strip(),
            'procedimento': soup_tr.find_all('td')[3].text.strip(),
            'especialidade': soup_tr.find_all('td')[4].text.strip(),
            'valor': soup_tr.find_all('td')[5].text.strip(),
            'quantidade': soup_tr.find_all('td')[6].text.strip(),
            'total': soup_tr.find_all('td')[7].text.strip(),
        }

    def get_procedimentos(self):
        if len(self.soup.find(id='idOrcamento').find_all('tr')) == 4:
            return []

        procedimentos = self.soup.find(id='idOrcamento').find_all('tr')[3:-1]
        procedimentos = filter(lambda tr: len(tr.find_all('td')) == 8, procedimentos)


        return list(map(self.get_procedimento, procedimentos))


class Pagamento():
    def __init__(self, soup):
        self.soup = soup

    def get_pagamento(self, tr):
        return {
            'id_tratamento': self.soup.find(attrs={'name':'id_tratamento'}).get('value'),
            'id_pagamento': tr.find_all('td')[1].text.strip(),
            'data': tr.find_all('td')[2].text.strip(),
            'tipo': tr.find_all('td')[3].text.strip(),
            'valor': tr.find_all('td')[4].text.strip(),
        }

    def get_pagamentos(self):
        if len(self.soup.find_all('table')) != 16:
            return []

        trs = self.soup.find_all('table')[5].find_all('tr')[1:]

        trs = filter(lambda tr: len(tr.find_all('td')) == 5, trs)

                
        return list(map(self.get_pagamento, trs))


class ContratoOrto(Meddent):
    def __init__(self, id_contrato):
        Meddent.__init__(self)
        self.id_contrato = id_contrato
        self.ORTO_CLIENTE_URL = 'http://meddent.com.br/admin/index.php?class=ClientesOrtoList&method=onView&key='
        self.soup = self.get_pagina(self.ORTO_CLIENTE_URL + str(id_contrato))

    def set_id_contrato(self, id_contrato):
        self.id_contrato = id_contrato
        self.soup = self.get_pagina(self.ORTO_CLIENTE_URL + str(id_contrato))


    def get_info(self):
        div = self.soup.find(class_='cellCliente')

        if not div.find_all('tr')[0].find_all('td')[0].find_all('p')[0].find('b').text.strip():
            return None
        
        return {
            'id_contrato': div.find_all('tr')[0].find_all('td')[0].find_all('p')[0].find('b').text.strip(),
            'dentista': div.find_all('tr')[0].find_all('td')[0].find_all('p')[1].find('b').text.strip(),
            'cliente': div.find_all('tr')[0].find_all('td')[0].find_all('p')[2].find('b').contents[0],
            'codigo': div.find_all('tr')[0].find_all('td')[0].find_all('p')[3].find('b').text.strip(),
            'valor': div.find_all('tr')[0].find_all('td')[2].find('span').text.strip(),
            'tempo': div.find_all('tr')[0].find_all('td')[4].find('span').text.strip(),
            'multa': div.find_all('tr')[1].find_all('td')[1].find('span').text.strip(),
            'juros': div.find_all('tr')[1].find_all('td')[3].find('span').text.strip(),
            'primeira_mensalidade': div.find_all('tr')[2].find_all('td')[1].find('span').text.strip(),
            'registro': div.find_all('tr')[2].find_all('td')[3].find('span').text.strip(),
            'status': div.find_all('tr')[3].find_all('td')[1].find('span').text.strip(),
            'obs': div.find_all('tr')[3].find_all('td')[3].find('span').text.strip(),
        }


    def get_mensalidade(self, tr):
        return {
            'id_contrato': str(self.id_contrato),
            'status': tr.find_all('td')[0].find('img').get('src'),
            'id_mensalidade': tr.find_all('td')[1].text.strip(),
            'vencimento': tr.find_all('td')[2].text.strip(),
            'valor': tr.find_all('td')[3].text.strip(),
            'multa': tr.find_all('td')[4].text.strip(),
            'pagamento': tr.find_all('td')[5].text.strip(),
            'desconto': tr.find_all('td')[6].text.strip(),
            'residuo': tr.find_all('td')[7].text.strip(),
            'obs': tr.find_all('td')[8].text.strip(),
        }

    def get_mensalidades(self):
        historico = self.soup.find(id='s1_2')

        if not historico:
            return []

        trs = historico.find_all('tr')[1:]

        return list(map(self.get_mensalidade, trs))