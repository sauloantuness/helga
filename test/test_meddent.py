import unittest
from meddent.meddent import Meddent, Cliente, Tratamento, Pagamento, ContratoOrto

class TestMeddent(unittest.TestCase):

    def test_deve_retornar_secao_autenticada(self):
        m = Meddent()
        r = m.session.get('http://meddent.com.br/admin/index.php')
        m.session.close()

        self.assertTrue('Helga' in r.text)

    def test_info_cliente(self):
        c = Cliente(3024)
        cliente = c.get_info()
        c.session.close()

        self.assertEqual(cliente['id_cliente'], '3024')

        self.assertEqual(cliente['nome'], 'Lindaci')
        self.assertEqual(cliente['codigo'], '132351')
        
        self.assertEqual(cliente['sexo'], 'M')
        self.assertEqual(cliente['dia'], '00')
        self.assertEqual(cliente['mes'], '00')
        self.assertEqual(cliente['ano'], '0000')
        
        self.assertEqual(cliente['convenio'], '0')

        self.assertEqual(cliente['profissao'], 'profissao')

        self.assertEqual(cliente['cpf'], '111.111.111-11')
        self.assertEqual(cliente['estado_civil'], 'Casado(a)')
        
        self.assertEqual(cliente['nacionalidade'], 'nacionalidade')
        self.assertEqual(cliente['naturalidade'], 'Naturalidade')
        
        self.assertEqual(cliente['rg'], 'rg')
        self.assertEqual(cliente['rgorgao'], 'orgao')
        
        self.assertEqual(cliente['comercial'], '(37) 1111-1111')
        self.assertEqual(cliente['residencial'], '(11) 1111-1111')
        
        self.assertEqual(cliente['celular'], '(37) 9999-9999')
        self.assertEqual(cliente['celular2'], '(99) 9999-9999')
        
        self.assertEqual(cliente['email'], 'email@email.com')

        self.assertEqual(cliente['endereco'], 'Endereco')
        self.assertEqual(cliente['complemento'], 'complemento')
        
        self.assertEqual(cliente['id_cidade'], '1')
        self.assertEqual(cliente['id_bairro'], '1')

        self.assertEqual(cliente['id_estado'], 'RJ')
        self.assertEqual(cliente['cep'], '30.000-000')

        self.assertEqual(cliente['id_marketing'], '0')
        self.assertEqual(cliente['id_dentista'], '0')

        self.assertEqual(cliente['obs'], 'obs')


    def test_cliente_responsavel(self):
        c = Cliente(11861)
        cliente = c.get_info()
        c.session.close()

        self.assertEqual(cliente['responsavel_nome'], 'Viviane Fernandes')


    def test_tratamento_link_tratamento_anterior(self):
        c = Cliente(8941)
        soup = c.get_pagina_tratamento()
        c.session.close()
        
        link_tratamento_anterior = 'http://meddent.com.br/admin/index.php?class=TratamentosClientesList&method=onMudaTratamentoMenos&key=8941&tratamento=14244'

        self.assertEqual(c.get_link_tratamento_anterior(soup), link_tratamento_anterior)
        self.assertEqual(c.get_link_tratamento_posterior(soup), None)


    def test_tratamento_link_tratamento_posterior(self):
        c = Cliente(8941)
        soup = c.get_pagina_tratamento('http://meddent.com.br/admin/index.php?class=TratamentosClientesList&method=onMudaTratamentoMenos&key=8941&tratamento=13514')
        c.session.close()
        
        link_tratamento_proximo = 'http://meddent.com.br/admin/index.php?class=TratamentosClientesList&method=onMudaTratamentoMais&key=8941&tratamento=13099'

        self.assertEqual(c.get_link_tratamento_posterior(soup), link_tratamento_proximo)
        self.assertEqual(c.get_link_tratamento_anterior(soup), None)


    def test_tratamento_link_tratamento_posterior_e_anterior(self):
        c = Cliente(8941)
        soup = c.get_pagina_tratamento('http://meddent.com.br/admin/index.php?class=TratamentosClientesList&method=onMudaTratamentoMenos&key=8941&tratamento=14244')
        c.session.close()
        
        link_tratamento_anterior = 'http://meddent.com.br/admin/index.php?class=TratamentosClientesList&method=onMudaTratamentoMenos&key=8941&tratamento=13852'
        link_tratamento_proximo = 'http://meddent.com.br/admin/index.php?class=TratamentosClientesList&method=onMudaTratamentoMais&key=8941&tratamento=13852'

        self.assertEqual(c.get_link_tratamento_posterior(soup), link_tratamento_proximo)
        self.assertEqual(c.get_link_tratamento_anterior(soup), link_tratamento_anterior)

    def test_tratamento_link_tratamento_vazio(self):
        c = Cliente(11861)
        soup = c.get_pagina_tratamento()
        c.session.close()
        
        self.assertEqual(c.get_link_tratamento_posterior(soup), None)
        self.assertEqual(c.get_link_tratamento_anterior(soup), None)


    def test_procedimentos_do_tratamento(self):
        c = Cliente(8941)
        soup = c.get_pagina_tratamento('http://meddent.com.br/admin/index.php?class=TratamentosClientesList&method=onMudaTratamentoMais&key=8941&tratamento=13852')
        c.session.close()

        t = Tratamento(soup)

        procedimentos = [
            {
                'id_tratamento': '14244',
                'id_cliente': '8941',
                'data': '08/12/2016',
                'procedimento': 'Coroa De Cerômero',
                'especialidade': 'Pró.',
                'valor': 'R$ 1.200,00',
                'quantidade': '1',
                'total': 'R$ 1.200,00',
            }
        ]

        self.assertEqual(t.get_procedimentos(), procedimentos)

    def test_procedimentos_do_tratamento_2(self):
        c = Cliente(8941)
        soup = c.get_pagina_tratamento('http://meddent.com.br/admin/index.php?class=TratamentosClientesList&method=onMudaTratamentoMenos&key=8941&tratamento=14244')
        c.session.close()

        t = Tratamento(soup)

        procedimentos = [
            {
                'id_tratamento': '13852',
                'id_cliente': '8941',
                'data': '11/11/2016',
                'procedimento': 'Cirurgia',
                'especialidade': 'Imp.',
                'valor': 'R$ 1.200,00',
                'quantidade': '1',
                'total': 'R$ 1.200,00',
            },
            {
                'id_tratamento': '13852',
                'id_cliente': '8941',
                'data': '11/11/2016',
                'procedimento': 'Orçamento',
                'especialidade': 'Imp.',
                'valor': 'R$ 1.100,00',
                'quantidade': '1',
                'total': 'R$ 1.100,00',
            },
        ]

        self.assertEqual(t.get_procedimentos(), procedimentos)

    def test_procedimentos_do_tratamento_3(self):
        c = Cliente(8941)
        soup = c.get_pagina_tratamento('http://meddent.com.br/admin/index.php?class=TratamentosClientesList&method=onView&key=11861')
        c.session.close()

        t = Tratamento(soup)

        procedimentos = []

        self.assertEqual(t.get_procedimentos(), procedimentos)

    def test_pagamentos_vazio(self):
        c = Cliente(11861)
        soup = c.get_pagina_tratamento()
        c.session.close()

        p = Pagamento(soup)
        pagamentos = []

        self.assertEqual(p.get_pagamentos(soup), pagamentos)

    def test_pagamentos(self):
        c = Cliente(8941)
        soup = c.get_pagina_tratamento('http://meddent.com.br/admin/index.php?class=TratamentosClientesList&method=onMudaTratamentoMais&key=11816&tratamento=17717')
        c.session.close()

        p = Pagamento(soup)
        pagamentos = [
            {
                'id_tratamento': '17718',
                'id_pagamento': '44805',
                'data': '18/09/2017',
                'tipo': 'Dinheiro',
                'valor': 'R$ 45,00',    
            },
            {
                'id_tratamento': '17718',
                'id_pagamento': '44806',
                'data': '18/10/2017',
                'tipo': 'Valeska Crédito',
                'valor': 'R$ 80,00',    
            }
        ]

        self.assertEqual(p.get_pagamentos(soup), pagamentos)

    def test_contrato_orto(self):
        c = ContratoOrto(1353)
        c.session.close()

        contrato = {
            'id_contrato': '1353',
            'cliente': 'Aline De Lima Rodrigues',
            'dentista': 'Dra. A Camila Da Silva Calabria',
            'codigo': '171170',
            'valor': 'R$ 100,00',
            'tempo': '1 mês',
            'multa': '0%',
            'juros': '0%',
            'primeira_mensalidade': '20/09/2017',
            'registro': '20/09/2017',
            'status': 'Ativo',
            'obs': 'Mensal',
        }

        self.assertEqual(c.get_info(), contrato)


    def test_mensalidades(self):
        mensalidades = [
            {
                'id_contrato': '1338',
                'status': '../images/icons/newpaga.jpg',
                'id_mensalidade': '38383',
                'vencimento': '13/09/2017',
                'valor': 'R$ 100,00',
                'multa': 'R$ 0,00',
                'pagamento': '80,00',
                'desconto': '20,00',
                'residuo': 'R$ 0,00',
                'obs':  'Mensalidade',
            }
        ]

        c = ContratoOrto(1338)
        c.session.close()

        self.assertEqual(c.get_mensalidades(), mensalidades)

    def test_mensalidades_vazio(self):
        mensalidades = []

        c = ContratoOrto(1349)
        c.session.close()

        self.assertEqual(c.get_mensalidades(), mensalidades)

    def test_deve_retornar_ultimo_id_cliente(self):
        m = Meddent()
        r = m.session.get('http://meddent.com.br/admin/index.php')
        id_cliente = m.get_ultimo_id_cliente()
        m.session.close()

        self.assertEqual(11945, id_cliente)

    def test_deve_retornar_ultimo_id_contrato(self):
        m = Meddent()
        r = m.session.get('http://meddent.com.br/admin/index.php')
        id_contrato = m.get_ultimo_id_contrato()
        m.session.close()

        self.assertEqual(1359, id_contrato)

if __name__ == '__main__':
    unittest.main()
