create table curso (
	id char(36) primary key default (UUID()),
    titulo varchar(255) not null, #Unique?
    periodo_inicio Date not null,
    periodo_fim Date not null,
    carga_horas_extensao int unsigned null
);

create table turma(
	id char(36) primary key default (UUID()),
    id_curso char(36) not null, 
    foreign key (id_curso) references curso(id),
    nome varchar(50) not null
);

create table tipo_usuario(
	id integer unsigned primary key auto_increment not null,
	valor varchar(100) not null
);

create table usuario(
	id char(36) primary key default (UUID()),
	
    role ENUM('Aluno', 'Docente', 'Administrador') NOT NULL,
    
    nome varchar(255) not null,
    email varchar(255) not null unique,
    telefone char(11) null unique,
    cpf varchar(255) not null unique,
    senha varchar(255) not null
);

create table projeto(
	id char(36) primary key default (UUID()),
    id_docente char(36) not null,
		foreign key (id_docente) references usuario(id),
    id_curso char(36) not null,
		foreign key (id_curso) references curso(id),
    titulo varchar(255) not null,
    descricao text not null,
    
    
    horas_previstas int unsigned null
);

create table status_horas(
	id integer unsigned primary key auto_increment not null,
	valor varchar(100) not null
);

create table solicitacao_horas_aluno(
	id char(36) primary key default (UUID()),
    id_projeto char(36) not null,
    	foreign key (id_projeto) references projeto(id),
    status ENUM('Pendente', 'Validade', 'Negado') NOT NULL,  
    id_aluno char(36) not null,
		foreign key (id_aluno) references usuario(id),
    data_postagem DateTime not null,
    horas_homologadas int unsigned null,
    comprovante varchar(255) not null,
    observacao_aluno text null,
    comentario_docente text null,
    data_processamento DateTime null
);