-- TB CONVÊNIO

insert into tb_convenio(id_convenio, ds_convenio) values (0, 'Convênio');
insert into tb_convenio(id_convenio, ds_convenio) values (17, 'Glosa');
insert into tb_convenio(id_convenio, ds_convenio) values (18, 'Unimed Odonto');


-- TB ESTADO CIVIL

insert into tb_estado_civil(id_estado_civil, ds_estado_civil) values ('0', 'Escolha o estado civil');
insert into tb_estado_civil(id_estado_civil, ds_estado_civil) values ('Casado(a)', 'Casado(a)');
insert into tb_estado_civil(id_estado_civil, ds_estado_civil) values ('Solteiro(a)', 'Solteiro(a)');
insert into tb_estado_civil(id_estado_civil, ds_estado_civil) values ('Divorciado(a)', 'Divorciado(a)');
insert into tb_estado_civil(id_estado_civil, ds_estado_civil) values ('União Estavel', 'União Estavel');
insert into tb_estado_civil(id_estado_civil, ds_estado_civil) values ('Viúvo(a)', 'Viúvo(a)');


-- TB ESTADO

insert into tb_estado(id_estado, ds_estado) values ('0', 'Escolha o estado');
insert into tb_estado(id_estado, ds_estado) values ('AC', 'Acre');
insert into tb_estado(id_estado, ds_estado) values ('AL', 'Alagoas');
insert into tb_estado(id_estado, ds_estado) values ('AM', 'Amazonas');
insert into tb_estado(id_estado, ds_estado) values ('AP', 'Amapá');
insert into tb_estado(id_estado, ds_estado) values ('BH', 'Bahia');
insert into tb_estado(id_estado, ds_estado) values ('CE', 'Ceará');
insert into tb_estado(id_estado, ds_estado) values ('DF', 'Distrito Federal');
insert into tb_estado(id_estado, ds_estado) values ('ES', 'Espírito Santo');
insert into tb_estado(id_estado, ds_estado) values ('GO', 'Goias');
insert into tb_estado(id_estado, ds_estado) values ('MA', 'Maranhão');
insert into tb_estado(id_estado, ds_estado) values ('MG', 'Minas Gerais');
insert into tb_estado(id_estado, ds_estado) values ('MS', 'Mato Grosso do Sul');
insert into tb_estado(id_estado, ds_estado) values ('MT', 'Mato Grosso');
insert into tb_estado(id_estado, ds_estado) values ('PA', 'Para');
insert into tb_estado(id_estado, ds_estado) values ('PB', 'Paraíba');
insert into tb_estado(id_estado, ds_estado) values ('PE', 'Pernambuco');
insert into tb_estado(id_estado, ds_estado) values ('PI', 'Piauí');
insert into tb_estado(id_estado, ds_estado) values ('PR', 'Paraná');
insert into tb_estado(id_estado, ds_estado) values ('RJ', 'Rio de Janeiro');
insert into tb_estado(id_estado, ds_estado) values ('RN', 'Rio Grande do Norte');
insert into tb_estado(id_estado, ds_estado) values ('RO', 'Rondonia');
insert into tb_estado(id_estado, ds_estado) values ('RR', 'Roraima');
insert into tb_estado(id_estado, ds_estado) values ('RS', 'Rio Grande do Sul');
insert into tb_estado(id_estado, ds_estado) values ('SC', 'Santa Catarina');
insert into tb_estado(id_estado, ds_estado) values ('SE', 'Sergipe');
insert into tb_estado(id_estado, ds_estado) values ('SP', 'São Paulo');


-- TB CIDADE

insert into tb_cidade(id_cidade, ds_cidade) values(0, 'Cidade');
insert into tb_cidade(id_cidade, ds_cidade) values(6, 'Belford Roxo');
insert into tb_cidade(id_cidade, ds_cidade) values(5, 'Caxias');
insert into tb_cidade(id_cidade, ds_cidade) values(3, 'Mesquita');
insert into tb_cidade(id_cidade, ds_cidade) values(4, 'Nilopolis');
insert into tb_cidade(id_cidade, ds_cidade) values(2, 'Nova Iguaçu');
insert into tb_cidade(id_cidade, ds_cidade) values(7, 'Queimados');
insert into tb_cidade(id_cidade, ds_cidade) values(8, 'Rio De Janeiro');
insert into tb_cidade(id_cidade, ds_cidade) values(1, 'São João De Meriti');


-- TB BAIRRO

bairros.sql


-- TB MARKETING

insert into tb_marketing(id_marketing, ds_marketing) values('0', 'Como Conheceu a Clínica');
insert into tb_marketing(id_marketing, ds_marketing) values('Campanha', 'Campanha');
insert into tb_marketing(id_marketing, ds_marketing) values('Convênio', 'Convênio');
insert into tb_marketing(id_marketing, ds_marketing) values('Indicação', 'Indicação');
insert into tb_marketing(id_marketing, ds_marketing) values('Letreiro', 'Letreiro');
insert into tb_marketing(id_marketing, ds_marketing) values('Propaganda', 'Propaganda');
insert into tb_marketing(id_marketing, ds_marketing) values('Telemarketing', 'Telemarketing');
insert into tb_marketing(id_marketing, ds_marketing) values('Outros', 'Outros');


-- TB INDICACAO

insert into tb_indicacao(id_indicacao, ds_indicacao) values(0, 'Quem Indicou');
insert into tb_indicacao(id_indicacao, ds_indicacao) values(6, 'Camila Da Silva Calabria Corte Real');
insert into tb_indicacao(id_indicacao, ds_indicacao) values(4, 'Danusa Gomes Barros');
insert into tb_indicacao(id_indicacao, ds_indicacao) values(2, 'Fernando Polinati');
insert into tb_indicacao(id_indicacao, ds_indicacao) values(5, 'Glauco Gomes Vilar');
insert into tb_indicacao(id_indicacao, ds_indicacao) values(7, 'Maria Do Carmo');
insert into tb_indicacao(id_indicacao, ds_indicacao) values(8, 'Ursula Lopes');
insert into tb_indicacao(id_indicacao, ds_indicacao) values(3, 'Valeska Santos Da Silva Bigi');
insert into tb_indicacao(id_indicacao, ds_indicacao) values(1, 'Vânia Regina Botelho Soares');


-- TB DENTISTA

insert into tb_dentista(id_dentista, ds_dentista) values(0, 'Dentista');
insert into tb_dentista(id_dentista, ds_dentista) values(21, 'Dr. A Aparelho Extra Orto');
insert into tb_dentista(id_dentista, ds_dentista) values(10, 'Dra. A Camila Da Silva Calabria ');
insert into tb_dentista(id_dentista, ds_dentista) values(3, 'Dra. A Danusa Gomes Barros');
insert into tb_dentista(id_dentista, ds_dentista) values(41, 'Dra. A Danusa Gomes Barros Unimed');
insert into tb_dentista(id_dentista, ds_dentista) values(23, 'A Dra. Marcelle');
insert into tb_dentista(id_dentista, ds_dentista) values(29, 'Dr. A Fernando Implante');
insert into tb_dentista(id_dentista, ds_dentista) values(5, 'Dr. A Fernando Polinati');
insert into tb_dentista(id_dentista, ds_dentista) values(35, 'Dra. A Gabrielle Dos Santos Andrade');
insert into tb_dentista(id_dentista, ds_dentista) values(1, 'Dr. A Glauco Gomes Vilar');
insert into tb_dentista(id_dentista, ds_dentista) values(40, 'Dra. A Izabel ');
insert into tb_dentista(id_dentista, ds_dentista) values(7, 'Dra. A Maria Do Carmo');
insert into tb_dentista(id_dentista, ds_dentista) values(18, 'A Pasta De Orto Dr.glauco');
insert into tb_dentista(id_dentista, ds_dentista) values(16, 'Dra. A Pasta De Orto.camila');
insert into tb_dentista(id_dentista, ds_dentista) values(8, 'Dr. A Pasta Orto Rx');
insert into tb_dentista(id_dentista, ds_dentista) values(32, 'Dr. A Protese ');
insert into tb_dentista(id_dentista, ds_dentista) values(43, 'Dr. A Reserva');
insert into tb_dentista(id_dentista, ds_dentista) values(6, 'Dr. A Rodrigo Von Kap-hernr De Oliveira');
insert into tb_dentista(id_dentista, ds_dentista) values(2, 'Dra. A Vânia Regina Botelho Soares');
insert into tb_dentista(id_dentista, ds_dentista) values(12, 'Dr. Comissão De  Orto');
insert into tb_dentista(id_dentista, ds_dentista) values(42, 'Dra. Lorraine Fernandes');
insert into tb_dentista(id_dentista, ds_dentista) values(17, 'Pasta De Orto Dra.valeska');
insert into tb_dentista(id_dentista, ds_dentista) values(11, 'Dra. Sobra De Caixa');
insert into tb_dentista(id_dentista, ds_dentista) values(13, 'Dra. Valeska Santos Da Silva Bigi');
insert into tb_dentista(id_dentista, ds_dentista) values(38, 'Dra. Wanderleya Becker M.f.manso');
