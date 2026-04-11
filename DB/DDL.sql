# Nome do banco, mesmo do projeto geral.
drop database SENAI_HORAS_EXTENSAO;
create database SENAI_HORAS_EXTENSAO;
use SENAI_HORAS_EXTENSAO;

#OBS.:
# Tabelas com ids em UUID são as que se temem utilizar grande volume
# Tabelas com ids em Integer são simples e que não demandam grande quantia

create table curso (
	id char(36) primary key default (UUID()),
    titulo varchar(255) not null, #Unique?
    periodo_inicio Date not null,
    periodo_fim Date not null,
    
    # Horas totais de extensão
    carga_horas_extensao int unsigned null
);

create table turma(
	id char(36) primary key default (UUID()),
    
    # Não tornar única
    # Um curso pode ter várias turmas
    id_curso char(36) not null, 
    foreign key (id_curso) references curso(id),
    
    # Também não tornar único.
    nome varchar(50) not null
);

# Conteúdo geral do usuário
# Não deve possuir tipo de usuário nesta tabela
# Cada tipo de usuário deve ter sua própria tabela e referenciar esta
create table usuario(
	#identificação em uuid pela quantidade de pessoas possíveis a longo prazo
	id char(36) primary key default (UUID()),
    nome varchar(255) not null, #Obrigatório
    email varchar(255) not null unique, #Obrigatório
    telefone char(11) null unique, # Talvez não
    
    # Campos com largo espaço para criptografia
    cpf varchar(255) not null unique, # Obrigatório
    senha varchar(255) not null # Obrigatório
);

create table administrador(
	id_usuario char(36) unique not null, 
    foreign key (id_usuario) references usuario(id)
);

create table docente(
	id_usuario char(36) unique not null, 
    foreign key (id_usuario) references usuario(id)
    
    # Talvez adicionar turmas ao docente. TALVEZ!
);

create table aluno(
	id_usuario char(36) unique not null, 
    foreign key (id_usuario) references usuario(id),
    
    id_turma char(36) unique not null, 
    foreign key (id_turma) references turma(id)
);

create table projeto(
	id char(36) primary key default (UUID()),
    id_docente char(36) not null,
		foreign key (id_docente) references docente(id_usuario),
        
    id_curso char(36) not null,
		foreign key (id_curso) references curso(id),
    
    titulo varchar(255) not null, #Unique?
    descricao text not null,
    
    
    horas_previstas int unsigned null
);

# Permite determinar como as horas serão registradas no sistema.
# Atrelada às horas dos alunos
create table status_horas(
	id integer unsigned primary key auto_increment not null,
	valor varchar(100) not null
);

# Solicitação de horas
create table solicitacao_horas_aluno(
	id char(36) primary key default (UUID()),
    id_projeto char(36) not null,
    	foreign key (id_projeto) references projeto(id),
        
    id_status int unsigned not null,
		foreign key (id_status) references status_horas(id),
        
    id_aluno char(36) not null,
		foreign key (id_aluno) references aluno(id_usuario),
    
    data_postagem DateTime not null,
    # Talvez haja a necessidade de horas adicionais ou subtraídas do total em circunstâncias especiais
    # Uma vez que estas horas estão indicadas, ignora-se a hora prevista no projeto
    # Utiliza-se então um status especial
    horas_homologadas int unsigned null,
    comprovante varchar(255) not null,
    observacao_aluno text null,
    comentario_docente text null,
    data_processamento DateTime null
);