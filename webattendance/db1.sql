/*
SQLyog Community Edition- MySQL GUI v7.01 
MySQL - 5.0.27-community-nt : Database - 042-attendence
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`042-attendence` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `042-attendence`;

/*Table structure for table `answers` */

DROP TABLE IF EXISTS `answers`;

CREATE TABLE `answers` (
  `id` int(255) NOT NULL auto_increment,
  `sid` varchar(255) default NULL,
  `answers` varchar(7000) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `answers` */

insert  into `answers`(`id`,`sid`,`answers`) values (1,'1','lkjlk'),(2,'1','khgyhgiy'),(3,'1','ohuohou'),(4,'1','ouhuh'),(5,'1','hiuhiuh'),(6,'1','sdfsdf'),(7,'1','sdfsdf'),(8,'1','sdfsdf'),(9,'1','sdfsd'),(10,'1','sdfsd'),(11,'1','sdfsdf'),(12,'1','sdfsdf'),(13,'1','sdfsdf'),(14,'1','sdfsd'),(15,'1','sdfsd'),(16,'1','dfsdfsd'),(17,'1','sdfsd'),(18,'1','sdfsdf'),(19,'1','sdfsdf'),(20,'1','sdfsd'),(21,'1','sdfsd '),(22,'1','sdfsdf'),(23,'1','sdgfsdg'),(24,'1','sdgsdg'),(25,'1','sdgsd');

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

insert  into `marking_attendance`(`Tid`,`Roll_no`,`department`,`subject`,`date`,`Attendance`,`classname`,`username`,`teachername`) values (1,'101','Electrical','python','2023-06-20','1','FIRST-YEAR','yash','yash'),(2,'102','Mechanical','python','2023-06-20','0','SECOND-YEAR','sahil','yash'),(3,'101','Electrical','dbms','2023-07-02','1','FIRST-YEAR','yash','yash'),(4,'102','Mechanical','dbms','2023-07-02','0','SECOND-YEAR','sahil','yash'),(5,'101','Electrical','blockchain','2023-06-20','1','FIRST-YEAR','yash','yash'),(6,'102','Mechanical','blockchain','2023-06-20','1','SECOND-YEAR','sahil','yash');

/*Table structure for table `marks` */

DROP TABLE IF EXISTS `marks`;

CREATE TABLE `marks` (
  `id` int(11) NOT NULL auto_increment,
  `sid` varchar(11) default NULL,
  `studname` varchar(11) default NULL,
  `q1` varchar(11) default NULL,
  `q2` varchar(11) default NULL,
  `q3` varchar(11) default NULL,
  `q4` varchar(11) default NULL,
  `q5` varchar(11) default NULL,
  `marks` varchar(11) default NULL,
  `DateTime` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `marks` */

insert  into `marks`(`id`,`sid`,`studname`,`q1`,`q2`,`q3`,`q4`,`q5`,`marks`,`DateTime`) values (2,'101','yash','1.7','1.1','4','2.2','1.7','9','2024-02-02 18:24:32.616812'),(3,'101','yash','1.7','1.1','4','2.2','1.7','9','2024-02-10 10:21:57.948601');

/*Table structure for table `notics` */

DROP TABLE IF EXISTS `notics`;

CREATE TABLE `notics` (
  `ID` int(255) NOT NULL auto_increment,
  `recipient` varchar(255) default NULL,
  `noticeTitle` varchar(255) default NULL,
  `noticeContent` longtext,
  `uploaded_file` varchar(255) default NULL,
  `date` varchar(255) default NULL,
  PRIMARY KEY  (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `notics` */

insert  into `notics`(`ID`,`recipient`,`noticeTitle`,`noticeContent`,`uploaded_file`,`date`) values (1,'teacher','collage reunion form teacher','it seems like you\'ve provided instructions to resolve an issue related to a bug in conda by reassigning the environment variables TEMP and TMP on Windows. If users are experiencing a problem where the temporary path has names with spaces, your solution suggests setting the TEMP and TMP environment variables to a directory without spaces, such as \"C:\\conda_tmp\".','static/Notice\\teacher/image.png','25/12/2020'),(2,'student','collage reunion form students','\r\nIt seems like you\'ve provided instructions to resolve an issue related to a bug in conda by reassigning the environment variables TEMP and TMP on Windows. If users are experiencing a problem where the temporary path has names with spaces, your solution suggests setting the TEMP and TMP environment variables to a directory without spaces, such as \"C:\\conda_tmp\".','static/Notice\\student/WhatsApp_Image_2023-12-12_at_16.41.20.jpeg','25/12/2027');

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

insert  into `teacheregister`(`id`,`Teachername`,`Temailaddress`,`Tpassword`,`Tmobileno`,`file`) values (1,'yash','yash@gmail.com','y','9632587411','static/teacher\\yash/pic-3.png');

/*Table structure for table `test` */

DROP TABLE IF EXISTS `test`;

CREATE TABLE `test` (
  `qid` int(255) NOT NULL auto_increment,
  `Question` varchar(1500) default NULL,
  `Answer` varchar(6000) default NULL,
  `Marks` varchar(11) default '10',
  PRIMARY KEY  (`qid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `test` */

insert  into `test`(`qid`,`Question`,`Answer`,`Marks`) values (1,'What is the capital of France?','Paris','10'),(2,'Who wrote \"To Kill a Mockingbird\"?','Harper Lee','10'),(3,'What is the chemical symbol for water?','H2O','10'),(4,'What is the tallest mountain in the world?','Mount Everest','10'),(5,'Who painted the Mona Lisa?','Leonardo da Vinci','10');

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

insert  into `userdetails`(`id`,`ROLL_ID`,`Username`,`EmailId`,`MobileNo`,`year`,`DEPARTMENT`,`password`,`current_address`,`permant_address`,`pincode`,`DISTICT`,`STATE`,`class1`,`filename1`) values (1,101,'yash','ysh@gmail.com','7894561232','2020-2021','Electrical','123','mum','cgfvbchg','541645','chiplun','maharashtra','FIRST-YEAR','static/data/101/101_3.jpg'),(2,102,'sahil','sahil@gmail.com','9632587414','2020-2021','Mechanical','321','mumai','dfss','7412','Shirpur','gujarat','SECOND-YEAR','static/data/102/102_5.jpg');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
