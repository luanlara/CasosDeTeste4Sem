-- -----------------------------------------------------
-- Schema farmaticos
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `farmaticos` DEFAULT CHARACTER SET utf8 ;
USE `farmaticos` ;

-- -----------------------------------------------------
-- Table `farmaticos`.`Farmacia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `farmaticos`.`farmacia` (
  `idfarmacia` INT NOT NULL,
  `nomefarmacia` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idfarmacia`));


-- -----------------------------------------------------
-- Table `farmaticos`.`Medicamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `farmaticos`.`medicamento` (
  `idmedicamento` INT NOT NULL,
  `nomemedicamento` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idmedicamento`));


-- -----------------------------------------------------
-- Table `farmaticos`.`Preco`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `farmaticos`.`preco` (
  `idpreco` INT NOT NULL AUTO_INCREMENT,
  `numpreco` DATETIME NOT NULL,
  `preco` DECIMAL(9,2) NOT NULL,
  `idfarmacia` INT NOT NULL,
  `idmedicamento` INT NOT NULL,
  PRIMARY KEY (`idpreco`),
  INDEX `idpreco_idfarmacia_idx` (`idfarmacia` ASC) VISIBLE,
  INDEX `idpreco_idmedicamento_idx` (`idmedicamento` ASC) VISIBLE,
  CONSTRAINT `idpreco_idfarmacia`
    FOREIGN KEY (`idfarmacia`)
    REFERENCES `farmaticos`.`farmacia` (`idfarmacia`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idpreco_idmedicamento`
    FOREIGN KEY (`idmedicamento`)
    REFERENCES `farmaticos`.`medicamento` (`idmedicamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Farmacia
-- -----------------------------------------------------

SELECT * FROM farmaticos.farmacia;
INSERT INTO farmaticos.farmacia (idfarmacia, nomefarmacia)
VALUES (1, 'Pague Menos');

INSERT INTO farmaticos.farmacia (idfarmacia, nomefarmacia)
VALUES (2, 'Drogaraia');

INSERT INTO farmaticos.farmacia (idfarmacia, nomefarmacia)
VALUES (3, 'Drogaria São Paulo');

-- -----------------------------------------------------
-- Medicamento
-- -----------------------------------------------------

SELECT * FROM farmaticos.medicamento;
INSERT INTO farmaticos.medicamento (idmedicamento, nomemedicamento)
VALUES (1, 'Dipirona');

INSERT INTO farmaticos.medicamento (idmedicamento, nomemedicamento)
VALUES (2, 'Advil');

INSERT INTO farmaticos.medicamento (idmedicamento, nomemedicamento)
VALUES (3, 'Engov');

INSERT INTO farmaticos.medicamento (idmedicamento, nomemedicamento)
VALUES (4, 'Neosadina');

INSERT INTO farmaticos.medicamento (idmedicamento, nomemedicamento)
VALUES (5, 'Dorflex');

INSERT INTO farmaticos.medicamento (idmedicamento, nomemedicamento)
VALUES (6, 'Novalgina');

INSERT INTO farmaticos.medicamento (idmedicamento, nomemedicamento)
VALUES (7, 'Eno');

INSERT INTO farmaticos.medicamento (idmedicamento, nomemedicamento)
VALUES (8, 'Neosoro');

INSERT INTO farmaticos.medicamento (idmedicamento, nomemedicamento)
VALUES (9, 'Merthiolate');

INSERT INTO farmaticos.medicamento (idmedicamento, nomemedicamento)
VALUES (10, 'Estomazil');

INSERT INTO farmaticos.medicamento (idmedicamento, nomemedicamento)
VALUES (11, 'Allegra');

INSERT INTO farmaticos.medicamento (idmedicamento, nomemedicamento)
VALUES (12, 'Vick VapoRub');

INSERT INTO farmaticos.medicamento (idmedicamento, nomemedicamento)
VALUES (13, 'Polaramine');

INSERT INTO farmaticos.medicamento (idmedicamento, nomemedicamento)
VALUES (14, 'DraminB6');

INSERT INTO farmaticos.medicamento (idmedicamento, nomemedicamento)
VALUES (15, 'Espironolactona');

INSERT INTO farmaticos.medicamento (idmedicamento, nomemedicamento)
VALUES (16, 'Insulina');