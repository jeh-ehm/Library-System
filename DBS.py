create database mydb;      

use mydb;
                                                
create table books(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30)); 

create table books_issued(bid varchar(20) primary key, issueto varchar(30));