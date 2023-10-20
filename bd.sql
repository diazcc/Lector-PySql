CREATE DATABASE datosdb;

USE datosdb;

CREATE TABLE informacion (
    codigo INT AUTO_INCREMENT,
    nombrearchivo VARCHAR(30),
    cantlineas INT(15),
    cantpalabras INT(15),
    cantcaracteres INT(15),
    fecharegistro TIMESTAMP,
    PRIMARY KEY (codigo)
);
