/*
SQLyog Community Edition- MySQL GUI v7.01 
MySQL - 5.0.27-community-nt : Database - attendance
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`attendance` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `attendance`;

/*Table structure for table `marking_attendance` */

DROP TABLE IF EXISTS `marking_attendance`;

CREATE TABLE `marking_attendance` (
  `Tid` int(255) NOT NULL auto_increment,
  `Roll_no` varchar(255) NOT NULL,
  `department` varchar(255) default NULL,
  `subject` varchar(355) default NULL,
  `date` varchar(255) default NULL,
  `Attendance` varchar(255) default NULL,
  `classname` varchar(255) default NULL,
  `username` varchar(255) default NULL,
  `teachername` varchar(255) default NULL,
  PRIMARY KEY  (`Tid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `marking_attendance` */

insert  into `marking_attendance`(`Tid`,`Roll_no`,`department`,`subject`,`date`,`Attendance`,`classname`,`username`,`teachername`) values (1,'101','Computer','dbms','2023-06-21','1','FINAL-YEAR','shruti','abc'),(2,'107','Computer','dbms','2023-06-21','1','FINAL-YEAR','sampada','abc'),(3,'108','Computer','dbms','2023-06-21','1','FINAL-YEAR','dhanashri','abc'),(4,'109','Computer','dbms','2023-06-21','1','FINAL-YEAR','prerna','abc'),(5,'102','Computer','dbms','2023-06-21','1','FINAL-YEAR','nikita','abc'),(6,'101','Computer','dbms','2023-06-21','1','FINAL-YEAR','shruti','abc'),(7,'109','Computer','dbms','2023-06-21','1','FINAL-YEAR','prerna','abc'),(8,'101','Computer','dbms','2023-06-21','1','FINAL-YEAR','shruti','abc'),(9,'109','Computer','dbms','2023-06-21','1','FINAL-YEAR','prerna','abc'),(10,'102','Computer','dbms','2023-06-21','1','FINAL-YEAR','nikita','abc'),(11,'101','Computer','dbms','2023-06-21','1','FINAL-YEAR','shruti','abc'),(12,'107','Computer','dbms','2023-06-21','1','FINAL-YEAR','sampada','abc'),(13,'109','Computer','dbms','2023-06-21','1','FINAL-YEAR','prerna','abc'),(14,'102','Computer','dbms','2023-06-21','1','FINAL-YEAR','nikita','abc'),(15,'110','Computer','dbms','2023-06-21','1','FINAL-YEAR','bhagyashri','abc'),(16,'111','Computer','dbms','2023-06-21','1','FINAL-YEAR','sakshi','abc'),(17,'101','Computer','dbms','2023-06-21','1','FINAL-YEAR','shruti','abc'),(18,'102','Computer','dbms','2023-06-21','1','FINAL-YEAR','nikita','abc'),(19,'101','Computer','dbms','2023-06-21','1','FINAL-YEAR','shruti','abc'),(20,'109','Computer','dbms','2023-06-21','1','FINAL-YEAR','prerna','abc'),(21,'107','Computer','dbms','2023-06-21','1','FINAL-YEAR','sampada','abc'),(22,'108','Computer','dbms','2023-06-21','1','FINAL-YEAR','dhanashri','abc'),(23,'102','Computer','dbms','2023-06-21','1','FINAL-YEAR','nikita','abc'),(24,'104','Computer','dbms','2023-06-21','0','FINAL-YEAR','manoj','abc'),(25,'105','Computer','dbms','2023-06-21','0','FINAL-YEAR','humera','abc'),(26,'106','Computer','dbms','2023-06-21','0','FINAL-YEAR','akshay','abc');

/*Table structure for table `teacheregister` */

DROP TABLE IF EXISTS `teacheregister`;

CREATE TABLE `teacheregister` (
  `id` int(255) NOT NULL auto_increment,
  `Teachername` varchar(255) default NULL,
  `Temailaddress` varchar(255) default NULL,
  `Tpassword` varchar(255) default NULL,
  `Tmobileno` varchar(255) default NULL,
  `file` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `teacheregister` */

insert  into `teacheregister`(`id`,`Teachername`,`Temailaddress`,`Tpassword`,`Tmobileno`,`file`) values (1,'nikita','nikitapawar202001@gmail.com','nikitapawar20200','7894561232','static/teacher\\nikita/pic-4.png'),(2,'shruti','1951641245015.nikitaa@gmail.com','s','1234567890','static/teacher\\shruti/contact-img.png'),(3,'humera','girasemohit3@gmail.com','m','1234567890','static/teacher\\humera/course-1-2.png'),(4,'dhanashri','nikitagirase20@gmail.com','n','1234567890','static/teacher\\dhanashri/course-2-4.jpg'),(5,'abc','abc@gmail.com','abc','7894561232','static/teacher\\abc/as.jpg');

/*Table structure for table `userdetails` */

DROP TABLE IF EXISTS `userdetails`;

CREATE TABLE `userdetails` (
  `id` int(255) NOT NULL auto_increment,
  `ROLL_ID` int(255) NOT NULL,
  `Username` varchar(255) default NULL,
  `EmailId` varchar(255) default NULL,
  `MobileNo` varchar(255) default NULL,
  `year` varchar(255) default NULL,
  `DEPARTMENT` varchar(255) default NULL,
  `password` varchar(255) default NULL,
  `current_address` varchar(255) default NULL,
  `permant_address` varchar(255) default NULL,
  `pincode` varchar(255) default NULL,
  `DISTICT` varchar(255) default NULL,
  `STATE` varchar(255) default NULL,
  `class1` varchar(255) default NULL,
  `filename1` varchar(255) default NULL,
  PRIMARY KEY  (`id`,`ROLL_ID`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `userdetails` */

insert  into `userdetails`(`id`,`ROLL_ID`,`Username`,`EmailId`,`MobileNo`,`year`,`DEPARTMENT`,`password`,`current_address`,`permant_address`,`pincode`,`DISTICT`,`STATE`,`class1`,`filename1`) values (5,101,'shruti','shrutiagrawal2081@gmail.com','9370003686','2022-2023','Computer','101','shahada','shahada','425409','None','None','FINAL-YEAR','static/data/101/101_11.jpg'),(6,102,'nikita','1951641245015.nikitaa@gmail.com','9860512337','2022-2023','Computer','102','pimpri','pimpri','425432','None','None','FINAL-YEAR','static/data/102/102_14.jpg'),(8,104,'manoj','patilmanoj4294@gmail.com','1234567890','2022-2023','Computer','123','shahada','shahada','425409','None','None','FINAL-YEAR','static/data/104/104_14.jpg'),(10,105,'humera','humerashaikh0704@gmail.com','9021272706','2022-2023','Computer','105','Mhasawad','Mhasawad','425432','None','None','FINAL-YEAR','static/data/105/105_16.jpg'),(11,106,'akshay','ak2haypatil@gmail.com','7057026024','2022-2023','Computer','106','raikhed','raikhed','425409','None','None','FINAL-YEAR','static/data/106/106_2.jpg'),(12,107,'sampada','sampadapatil053@gmail.com','5226152718','2022-2023','Computer','107','shahada','shahada','425409','None','None','FINAL-YEAR','static/data/107/107_0.jpg'),(16,108,'dhanashri','dhanup351@gmail.com','5613764728','2022-2023','Computer','108','lambola','lambola','425409','None','None','FINAL-YEAR','static/data/108/108_0.jpg'),(17,109,'prerna','prernamarathe02@gmail.com','635764289','2022-2023','Computer','109','Mhasawad','Mhasawad','425432','None','None','FINAL-YEAR','static/data/109/109_4.jpg'),(18,110,'bhagyashri','patilbhagyashri944@gmail.com','9022962205','2022-2023','Computer','110','lonkheda','lonkheda','425409','None','None','FINAL-YEAR','static/data/110/110_4.jpg'),(19,111,'sakshi','sakkipatil1@gmail.com','8378879601','2022-2023','Computer','111','shahada','shahada','425409','None','None','FINAL-YEAR','static/data/111/111_7.jpg');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
