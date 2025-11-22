create database teste_bd;
use teste_bd;

create table tb_funcionario(
	Matricula INT NOT NULL PRIMARY KEY,
    Nome_Funcionario VARCHAR(100) NOT NULL
);

select * from tb_funcionario;
