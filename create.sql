drop database meddent;
create database meddent;

create table tb_convenio (
	id_convenio int primary key,
	ds_convenio varchar(255)
);

-- create table tb_sexo (
-- 	id_sexo int primary key,
-- 	ds_sexo varchar(255)
-- );

create table tb_estado_civil (
	id_estado_civil varchar(255) primary key,
	ds_estado_civil varchar(255)
);

create table tb_estado (
	id_estado varchar(2) primary key,
	ds_estado varchar(255)
);

create table tb_cidade (
	id_cidade int primary key,
	ds_cidade varchar(255)
);

create table tb_bairro (
	id_bairro int primary key,
	ds_bairro varchar(255),

	id_cidade int foreign key references tb_cidade(id_cidade)
);

create table tb_marketing (
	id_marketing varchar(255) primary key,
	ds_marketing varchar(255)
);

create table tb_indicacao (
	id_indicacao int primary key,
	ds_indicacao varchar(255)
);

create table tb_dentista (
	id_dentista int primary key,
	ds_dentista varchar(255)
);

create table tb_cliente (
	id_cliente int primary key,

	nome varchar(255),
	codigo int,

	sexo varchar(9),
	nascimento date,

	id_convenio int foreign key references tb_convenio(id_convenio),

	profissao varchar(255),

	cpf varchar(11),
	id_estado_civil varchar(255) foreign key references tb_estado_civil(id_estado_civil),

	nacionalidade varchar(255),
	naturalidade varchar(255),

	rg varchar(255),
	rg_orgao varchar(255),

	telefone_comercial varchar(255),
	telefone_residencial varchar(255),

	celular varchar(255),
	celular_2 varchar(255),

	email varchar(255),

	endereco varchar(255),
	complemento varchar(255),

	id_cidade int foreign key references tb_cidade(id_cidade),
	id_bairro int foreign key references tb_bairro(id_bairro),

	id_estado varchar(2) foreign key references tb_estado(id_estado),
	cep varchar(12),

	id_marketing varchar(255) foreign key references tb_marketing(id_marketing),
	id_indicacao int foreign key references tb_indicacao(id_indicacao),

	obs varchar(255),

	responsavel_nome varchar(255),
	responsavel_cpf varchar(255),
	responsavel_endereco varchar(255)
);

create table tb_tratamento (
	id_tratamento int primary key,

	id_cliente int foreign key references tb_cliente(id_cliente),
	id_dentista int foreign key references tb_dentista(id_dentista)
);

create table tb_procedimento (
	id_procedimento int primary key,
	data date,
	procedimento varchar(255),
	especialidade varchar(255),
	valor decimal,
	quantidade int,
	total decimal,

	id_tratamento int foreign key references tb_tratamento(id_tratamento)
);

create table tb_pagamento (
	id_pagamento int primary key,
	data date,
	tipo varchar(255),
	valor decimal,

	id_tratamento int foreign key references tb_tratamento(id_tratamento)
);

create table tb_contrato (
	id_contrato int primary key,
	valor decimal,
	tempo varchar(255),
	multa varchar(255),
	juros varchar(255),
	primeira_mensalidade date,
	registro date,
	status varchar(255),
	obs varchar(255),

	id_cliente int foreign key references tb_cliente(id_cliente),
	id_dentista int foreign key references tb_dentista(id_dentista)
);

create table tb_mensalidade (
	id_mensalidade int primary key,
	status varchar(255),
	vencimento date,
	valor decimal,
	multa decimal,
	pagamento decimal,
	desconto decimal,
	residuo decimal,
	obs varchar(255),

	id_contrato int foreign key references tb_contrato(id_contrato)
);