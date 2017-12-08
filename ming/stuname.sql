/*
SQLyog 企业版 - MySQL GUI v7.14 
MySQL - 5.6.38-log : Database - stuname
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`stuname` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `stuname`;

/*Data for the table `auth_group` */

/*Data for the table `auth_group_permissions` */

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add user',2,'add_user'),(5,'Can change user',2,'change_user'),(6,'Can delete user',2,'delete_user'),(7,'Can add permission',3,'add_permission'),(8,'Can change permission',3,'change_permission'),(9,'Can delete permission',3,'delete_permission'),(10,'Can add group',4,'add_group'),(11,'Can change group',4,'change_group'),(12,'Can delete group',4,'delete_group'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session');

/*Data for the table `auth_user` */

/*Data for the table `auth_user_groups` */

/*Data for the table `auth_user_user_permissions` */

/*Data for the table `django_admin_log` */

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(4,'auth','group'),(3,'auth','permission'),(2,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2017-12-06 02:25:33.000857'),(2,'auth','0001_initial','2017-12-06 02:25:40.674296'),(3,'admin','0001_initial','2017-12-06 02:25:42.463398'),(4,'admin','0002_logentry_remove_auto_add','2017-12-06 02:25:42.537402'),(5,'contenttypes','0002_remove_content_type_name','2017-12-06 02:25:43.585462'),(6,'auth','0002_alter_permission_name_max_length','2017-12-06 02:25:44.422510'),(7,'auth','0003_alter_user_email_max_length','2017-12-06 02:25:45.100549'),(8,'auth','0004_alter_user_username_opts','2017-12-06 02:25:45.153552'),(9,'auth','0005_alter_user_last_login_null','2017-12-06 02:25:45.613578'),(10,'auth','0006_require_contenttypes_0002','2017-12-06 02:25:45.654580'),(11,'auth','0007_alter_validators_add_error_messages','2017-12-06 02:25:45.721584'),(12,'auth','0008_alter_user_username_max_length','2017-12-06 02:25:47.200669'),(13,'auth','0009_alter_user_last_name_max_length','2017-12-06 02:25:47.898709'),(14,'sessions','0001_initial','2017-12-06 02:25:48.377736');

/*Data for the table `django_session` */

/*Data for the table `name` */

insert  into `name`(`id`,`name`) values (1,'钟宝'),(2,'陈晓晖'),(3,'张胜扬'),(4,'高越'),(5,'赵美新'),(6,'张亮'),(7,'骆铜磊'),(8,'蔡欣欣'),(9,'陈行'),(10,'郭磊'),(11,'徐广文'),(12,'王子明'),(13,'刘壮'),(14,'邓玉洁'),(15,'付彬'),(16,'张建宇'),(17,'关靖霖'),(18,'张艺潇'),(19,'傅元超'),(20,'张鸿喜'),(21,'杨坤'),(22,'崔耀辉'),(23,'徐达'),(24,'张蒙恩'),(25,'邢天宇'),(26,'朱明元'),(27,'荣建凯'),(28,'李艳玲'),(29,'张家铭'),(30,'刘慧然'),(31,'徐颖'),(32,'王凯'),(33,'王娇娇'),(34,'兰婉婷'),(35,'蒋志学'),(36,'万凌云'),(37,'游可欣'),(38,'白立鹏'),(39,'滕坤'),(40,'曹祖亚'),(41,'杨帅'),(42,'高茂盛'),(43,'王广胜'),(44,'赵泽林'),(45,'杨晓亮'),(46,'王忠正'),(47,'刘笑国'),(48,'卜令涛'),(49,'李亚'),(50,'周光丽'),(51,'刘明宇'),(52,'王晓雨'),(53,'张蓓'),(54,'李丛从'),(55,'牛少鹏'),(56,'吕欣'),(57,'任泽权'),(58,'吴升宇'),(59,'王永君'),(60,'牛广林'),(61,'韩培南'),(62,'张鹏程');

/*Data for the table `stuname` */

insert  into `stuname`(`id`,`name`,`status`,`date`) values (9,'白立鹏',1,'2017-12-08 21:17:36');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
