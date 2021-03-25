drop database if exists sqlinjdemo;
DROP TABLE if exists sqlinjdemo.sqlinj;


create database sqlinjdemo;
create table sqlinj(
	UserName varchar(50),
    UserPass varchar(50),
    type varchar(20),
    AccountBalance integer,
    id int auto_increment,
    primary key (id)
);

insert into sqlinj(UserName, UserPass, type, AccountBalance)
values('Yegor', 'admin123', 'Developer', 10000),
		('Pranee', '123admin', 'Developer',30000),
        ('Wendy', '123admin', 'Web-Developer',20000),
        ('Muhammad', '123admin', 'Backend Developer',2000),
        ('Marek', '123admin', 'Manager',50000);
        
select * from sqlinj;