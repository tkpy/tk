/*
SQLyog 企业版 - MySQL GUI v7.14 
MySQL - 5.6.23-log : Database - shopping
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`shopping` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `shopping`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `detail` */

DROP TABLE IF EXISTS `detail`;

CREATE TABLE `detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `orderid` int(11) DEFAULT NULL,
  `goodsid` int(11) DEFAULT NULL,
  `name` varchar(32) DEFAULT NULL,
  `price` double(6,2) DEFAULT NULL,
  `num` int(11) DEFAULT NULL,
  `picname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;

/*Data for the table `detail` */

insert  into `detail`(`id`,`orderid`,`goodsid`,`name`,`price`,`num`,`picname`) values (38,31,55,'小米红',1234.00,4,'1506741688.0802736.png'),(39,32,57,'小米黄',1234.00,10,'1506741752.9859958.png'),(40,33,59,'小米',1234.00,4,'1506741817.8919673.png'),(41,34,54,'黑金小米',1234.00,1,'1506741659.1357563.jpg'),(42,35,57,'小米黄',1234.00,1,'1506741752.9859958.png'),(43,36,60,'好辣',1234.00,1,'1506741885.8725455.jpg'),(44,37,55,'小米红',1234.00,5,'1506741688.0802736.png');

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2017-09-06 01:02:34.727678'),(2,'auth','0001_initial','2017-09-06 01:02:35.911428'),(3,'admin','0001_initial','2017-09-06 01:02:36.397955'),(4,'admin','0002_logentry_remove_auto_add','2017-09-06 01:02:36.449071'),(5,'contenttypes','0002_remove_content_type_name','2017-09-06 01:02:36.606250'),(6,'auth','0002_alter_permission_name_max_length','2017-09-06 01:02:36.664822'),(7,'auth','0003_alter_user_email_max_length','2017-09-06 01:02:36.732680'),(8,'auth','0004_alter_user_username_opts','2017-09-06 01:02:36.744037'),(9,'auth','0005_alter_user_last_login_null','2017-09-06 01:02:36.791895'),(10,'auth','0006_require_contenttypes_0002','2017-09-06 01:02:36.795332'),(11,'auth','0007_alter_validators_add_error_messages','2017-09-06 01:02:36.807866'),(12,'auth','0008_alter_user_username_max_length','2017-09-06 01:02:36.853842'),(13,'sessions','0001_initial','2017-09-06 01:02:36.947713');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('63ab0pbgsd4zlsgskn3bcfgkkiaihpu9','NzdkOTNjMDcxZmYyZTU0NmYxNzZjZDE3NTA5OTQ3ZWRkYmZlOWZhZDp7InNob3BsaXN0Ijp7fSwib3JkZXJsaXN0Ijp7IjUyIjp7ImlkIjo1MiwiZ29vZHMiOiJcdTgyZjlcdTY3OWMiLCJwcmljZSI6MTIzLjAsInBpY25hbWUiOiIxNTA0ODM4Mzk1Ljg0NTEwNjEuanBnIiwibnVtIjoxfX0sInZlcmlmeWNvZGUiOiJLVlo5IiwiYWRtaW51c2VyIjoiXHU2ZWQ1XHU1NzY0IiwibXl3ZWJsb2dpbiI6eyJpZCI6MTIsInVzZXJuYW1lIjoidGsxMjM0IiwibmFtZSI6InRrIiwicGFzc3dvcmQiOiJlMTBhZGMzOTQ5YmE1OWFiYmU1NmUwNTdmMjBmODgzZSIsInNleCI6MSwiYWRkcmVzcyI6IjEiLCJjb2RlIjoiIiwicGhvbmUiOiIxMjM0NTY3IiwiZW1haWwiOiIxMjMiLCJzdGF0ZSI6MSwiYWRkdGltZSI6MX0sIjE3Ijp7ImlkIjoyMiwib3JkZXJpZCI6MTcsImdvb2RzaWQiOjUyLCJuYW1lIjoiXHU4MmY5XHU2NzljIiwicHJpY2UiOjEyMy4wLCJudW0iOjMsInBpY25hbWUiOiIxNTA0ODM4Mzk1Ljg0NTEwNjEuanBnIn19','2017-09-25 12:40:37.588977'),('ca8onxcui7du7ofpe7bj8nw1odtnljbj','ODhkMDRhNzE1ZWUyZGE0OTkwYjVjYmNjNDA3ODUxNTZlNGQzZDgxYTp7InZlcmlmeWNvZGUiOiI2REEwIiwiYWRtaW51c2VyIjoiXHU2ZWQ1XHU1NzY0Iiwic2hvcGxpc3QiOnsiNDIiOnsiaWQiOjQyLCJnb29kcyI6Ik9QUE9cdTgzNjNcdTgwMDBcdTllZDEiLCJwcmljZSI6MTIzLjAsInBpY25hbWUiOiIxNTA0ODI1NjkxLjgxMTM0ODQuanBnIiwibnVtIjoxfSwiNDYiOnsiaWQiOjQ2LCJnb29kcyI6Ilx1NTM0ZVx1NGUzYSIsInByaWNlIjoxMjMuMCwicGljbmFtZSI6IjE1MDQ4MzU5NTEuODkwNTAxMy5wbmciLCJudW0iOjN9fSwibXl3ZWJsb2dpbiI6eyJpZCI6MjIsInVzZXJuYW1lIjoidGsxMjMiLCJuYW1lIjoidGsxMjMiLCJwYXNzd29yZCI6ImUxMGFkYzM5NDliYTU5YWJiZTU2ZTA1N2YyMGY4ODNlIiwic2V4IjoxLCJhZGRyZXNzIjoxLCJjb2RlIjoiIiwicGhvbmUiOiIxIiwiZW1haWwiOiIxIiwic3RhdGUiOjEsImFkZHRpbWUiOjF9fQ==','2017-09-24 04:45:59.066583'),('fav7zz3po27ppyfdl56142u13ux0kd53','NGJhMDZkN2MxNjExMGM3MWQzOWVjM2IxOWQxYzllYWY3ZmZhNGFhNDp7InZlcmlmeWNvZGUiOiJOVDNBIiwiYWRtaW51c2VyIjoiXHU2ZTM4XHU1M2VmXHU2YjIzIiwic2hvcGxpc3QiOnsiNDgiOnsiaWQiOiI0OCIsImdvb2RzIjoiMTIiLCJwcmljZSI6IjIxMy4wIiwicGljbmFtZSI6IjE1MDQ4MzY0MDguNjM2MDQ0NS5wbmciLCJudW0iOjF9LCI0MiI6eyJpZCI6IjQyIiwiZ29vZHMiOiJPUFBPXHU4MzYzXHU4MDAwXHU5ZWQxIiwicHJpY2UiOiIxMjMuMCIsInBpY25hbWUiOiIxNTA0ODI1NjkxLjgxMTM0ODQuanBnIn19fQ==','2017-09-23 09:59:14.975055'),('ibyk0vh0ofji01n5klu4rngn6zti5pz3','ZGQ5NzBkZjZmN2M2YmNmNTg3MjAxOWExNjE5ZDE0MTliMDFlMzliZDp7InNob3BsaXN0Ijp7fSwib3JkZXJsaXN0Ijp7IjU1Ijp7ImlkIjo1NSwiZ29vZHMiOiJcdTVjMGZcdTdjNzNcdTdlYTIiLCJwcmljZSI6MTIzNC4wLCJwaWNuYW1lIjoiMTUwNjc0MTY4OC4wODAyNzM2LnBuZyIsIm51bSI6NX19LCJteXdlYmxvZ2luIjp7ImlkIjoyMiwidXNlcm5hbWUiOiJ0azEyMyIsIm5hbWUiOiJ0azEyMyIsInBhc3N3b3JkIjoiZTEwYWRjMzk0OWJhNTlhYmJlNTZlMDU3ZjIwZjg4M2UiLCJzZXgiOjEsImFkZHJlc3MiOiIxIiwiY29kZSI6IiIsInBob25lIjoiMSIsImVtYWlsIjoiMSIsInN0YXRlIjoxLCJhZGR0aW1lIjoxfX0=','2017-10-14 07:33:59.225503'),('zzipffbqez8uoba0ikl6rc5tk024dfnb','NWViNWQ2NzllNDY2YmI4ZWViZjU4NmM4NWIzYzRjNzBjNzhjZGRkMTp7InNob3BsaXN0Ijp7fSwib3JkZXJsaXN0Ijp7IjQyIjp7ImlkIjo0MiwiZ29vZHMiOiJPUFBPXHU4MzYzXHU4MDAwXHU5ZWQxIiwicHJpY2UiOjEyMy4wLCJwaWNuYW1lIjoiMTUwNDgyNTY5MS44MTEzNDg0LmpwZyIsIm51bSI6M319LCJ2ZXJpZnljb2RlIjoiQUNBWCIsIm15d2VibG9naW4iOnsiaWQiOjIyLCJ1c2VybmFtZSI6InRrMTIzIiwibmFtZSI6InRrMTIzIiwicGFzc3dvcmQiOiJlMTBhZGMzOTQ5YmE1OWFiYmU1NmUwNTdmMjBmODgzZSIsInNleCI6MSwiYWRkcmVzcyI6IjEiLCJjb2RlIjoiIiwicGhvbmUiOiIxIiwiZW1haWwiOiIxIiwic3RhdGUiOjEsImFkZHRpbWUiOjF9LCJhZG1pbnVzZXIiOiJcdTZlZDVcdTU3NjQifQ==','2017-10-14 07:35:25.501074');

/*Table structure for table `goods` */

DROP TABLE IF EXISTS `goods`;

CREATE TABLE `goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `typeid` int(11) DEFAULT NULL,
  `goods` varchar(32) DEFAULT NULL,
  `company` varchar(50) DEFAULT NULL,
  `descr` text,
  `price` double(6,2) DEFAULT NULL,
  `picname` varchar(255) DEFAULT NULL,
  `state` tinyint(1) DEFAULT '1',
  `store` int(11) DEFAULT '0',
  `num` int(11) DEFAULT '0',
  `clicknum` int(11) DEFAULT '0',
  `addtime` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8;

/*Data for the table `goods` */

insert  into `goods`(`id`,`typeid`,`goods`,`company`,`descr`,`price`,`picname`,`state`,`store`,`num`,`clicknum`,`addtime`) values (54,20,'黑金小米','俺家滴','123',1234.00,'1506741659.1357563.jpg',1,1233,1,3,1234),(55,20,'小米红','俺家滴','123',1234.00,'1506741688.0802736.png',1,1229,5,3,1234),(56,20,'小米粉红','俺家滴','123',1234.00,'1506741716.2831056.png',1,1234,0,1,1234),(57,20,'小米黄','俺家滴','123',1234.00,'1506741752.9859958.png',1,1223,1,2,1234),(58,20,'小米白银','俺家滴','123',1234.00,'1506741784.141372.png',1,1234,0,0,1234),(59,20,'小米','俺家滴','123',1234.00,'1506741817.8919673.png',1,1230,4,1,1234),(60,21,'好辣','俺家滴','123',1234.00,'1506741885.8725455.jpg',1,1233,1,2,1234),(61,21,'牛肉干','俺家滴','123',1234.00,'1506741912.0526972.jpg',1,1234,0,0,1234),(62,21,'干果','俺家滴','123',1234.00,'1506741937.9611516.jpg',1,1234,0,0,1234),(63,21,'特辣','俺家滴','123',1234.00,'1506741968.1449275.jpg',1,1234,0,0,1234),(64,21,'好吃','俺家滴','123',1234.00,'1506742703.313411.jpg',1,1234,0,0,1234),(65,21,'好吃','俺家滴','a234',13.00,'1506756925.4619522.jpg',1,13,0,0,134);

/*Table structure for table `orders` */

DROP TABLE IF EXISTS `orders`;

CREATE TABLE `orders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `linkman` varchar(32) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `code` char(6) DEFAULT NULL,
  `phone` varchar(16) DEFAULT NULL,
  `addtime` int(11) DEFAULT NULL,
  `total` double(8,2) DEFAULT NULL,
  `status` tinyint(4) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8;

/*Data for the table `orders` */

insert  into `orders`(`id`,`uid`,`linkman`,`address`,`code`,`phone`,`addtime`,`total`,`status`) values (31,22,'tk123','1','','1',1506743547,4936.00,0),(32,22,'tk123','1','','1',1506747367,12340.00,1),(33,22,'tk123','1','','1',1506747552,4936.00,2),(34,22,'哈哈','1','','1',1506755224,1234.00,0),(35,22,'tk123','1','','1',1506755540,1234.00,3),(36,22,'tk123','激发','','1',1506755600,1234.00,0),(37,22,'tk123','1','2112','1',1506756839,6170.00,0);

/*Table structure for table `recommend` */

DROP TABLE IF EXISTS `recommend`;

CREATE TABLE `recommend` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `typeid` int(11) DEFAULT NULL,
  `goods` varchar(32) DEFAULT NULL,
  `company` varchar(50) DEFAULT NULL,
  `descr` text,
  `price` double(6,2) DEFAULT NULL,
  `picname` varchar(255) DEFAULT NULL,
  `state` tinyint(1) DEFAULT '1',
  `store` int(11) DEFAULT '0',
  `num` int(11) DEFAULT '0',
  `clicknum` int(11) DEFAULT '0',
  `addtime` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;

/*Data for the table `recommend` */

insert  into `recommend`(`id`,`typeid`,`goods`,`company`,`descr`,`price`,`picname`,`state`,`store`,`num`,`clicknum`,`addtime`) values (54,NULL,'黑金小米','','',1234.00,'1506741659.1357563.jpg',1,0,0,0,NULL),(61,NULL,'牛肉干','','',1234.00,'1506741912.0526972.jpg',1,0,0,0,NULL);

/*Table structure for table `type` */

DROP TABLE IF EXISTS `type`;

CREATE TABLE `type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `pid` int(11) DEFAULT '0',
  `path` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

/*Data for the table `type` */

insert  into `type`(`id`,`name`,`pid`,`path`) values (3,'食品',0,'0,'),(15,'手机',0,'0,'),(20,'安卓',15,'0,15,'),(21,'辣条',3,'0,3,');

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `name` varchar(16) DEFAULT NULL,
  `password` char(32) NOT NULL,
  `sex` tinyint(1) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `code` char(6) DEFAULT NULL,
  `phone` varchar(16) DEFAULT NULL,
  `email` varchar(50) NOT NULL,
  `state` tinyint(1) DEFAULT '1',
  `addtime` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

/*Data for the table `users` */

insert  into `users`(`id`,`username`,`name`,`password`,`sex`,`address`,`code`,`phone`,`email`,`state`,`addtime`) values (1,'12','滕坤','202cb962ac59075b964b07152d234b70',1,'0','123','123','123',1,1234),(2,'123456','白立鹏','d9b1d7db4cd6e70935368a1efb10e377',1,'123','123','12345','123',0,1504640020),(3,'aa','游可欣','202cb962ac59075b964b07152d234b70',0,'123','123','123','123',0,1123),(4,'haha','江志学','202cb962ac59075b964b07152d234b70',1,'12','12','12','12',1,12),(5,'zzl','赵泽林','289dff07669d7a23de0ef88d2f7129e7',1,'123','123','1234','123',1,123),(7,'lz','刘柱','202cb962ac59075b964b07152d234b70',1,'123','123','123','123',1,NULL),(9,'ty','田宇','202cb962ac59075b964b07152d234b70',1,'123','123','123','123',1,NULL),(11,'1','1','e10adc3949ba59abbe56e057f20f883e',1,'1','','123456','1',1,1),(12,'tk1234','tk','e10adc3949ba59abbe56e057f20f883e',1,'北京育荣教育园区','09912','1234567','123@qq.com',1,1),(13,'tk12','tk1','e10adc3949ba59abbe56e057f20f883e',1,'北京育荣教育园区','12341','0902834','123',1,1),(14,'tk12345','tk2','e10adc3949ba59abbe56e057f20f883e',1,'1','','123','123',1,1),(22,'tk123','tk123','e10adc3949ba59abbe56e057f20f883e',1,'1','','1','1',1,1),(23,'tk1','嗯嗯','e10adc3949ba59abbe56e057f20f883e',1,'1','','1','1',1,1),(24,'滕坤哈哈','滕坤','e10adc3949ba59abbe56e057f20f883e',1,'1','','1','1',1,1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
