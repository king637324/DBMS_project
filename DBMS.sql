CREATE DATABASE  IF NOT EXISTS `database` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `database`;
-- MySQL dump 10.13  Distrib 8.0.24, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: database
-- ------------------------------------------------------
-- Server version	8.0.24

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `check_list`
--

DROP TABLE IF EXISTS `check_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `check_list` (
  `id` int NOT NULL,
  `ESSN` varchar(3) NOT NULL,
  `M_id` int NOT NULL,
  `checktime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `check_list`
--

LOCK TABLES `check_list` WRITE;
/*!40000 ALTER TABLE `check_list` DISABLE KEYS */;
INSERT INTO `check_list` VALUES (1,'001',12,'2021-12-01 22:12:13'),(2,'003',4,'2021-12-01 22:12:13'),(3,'004',2,'2021-12-02 22:12:13'),(4,'004',5,'2021-12-02 22:12:13'),(5,'005',9,'2021-12-02 22:12:13'),(6,'006',6,'2021-12-03 22:12:13'),(7,'007',5,'2021-12-03 22:12:13'),(8,'008',3,'2021-12-04 22:12:13'),(9,'008',10,'2021-12-04 22:12:13'),(10,'009',4,'2021-12-05 22:12:13'),(11,'010',8,'2021-12-05 22:12:13'),(12,'011',10,'2021-12-06 20:12:13'),(13,'012',14,'2021-12-06 21:12:13'),(14,'020',7,'2021-12-06 22:12:13');
/*!40000 ALTER TABLE `check_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `C_id` int NOT NULL AUTO_INCREMENT,
  `Cname` varchar(45) NOT NULL,
  `Cphone` varchar(45) NOT NULL,
  PRIMARY KEY (`C_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'丹尼','0939923454'),(2,'理德','0931341106'),(3,'蓋拉','0935372327'),(4,'詹恩','0936842358'),(5,'克萊夫','0968975744'),(6,'路易','0956588373'),(7,'奇恩','0989689847'),(8,'龍尼','0988402440'),(9,'蓋拉','0932087164'),(10,'諾蘭','0934941872'),(11,'瓦爾多','0922993688'),(12,'奎音','0987456781'),(13,'特薇拉','0960015634'),(14,'布琳','0919113455'),(15,'伊蒂絲','0931614885');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `D_id` int NOT NULL AUTO_INCREMENT,
  `Dname` varchar(45) DEFAULT NULL,
  `Dlocation` varchar(45) DEFAULT NULL,
  `MgrSSN` varchar(3) DEFAULT NULL,
  `StartDate` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`D_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES (1,'台南分店','台南','001','2021-12-06 23:58:55'),(2,'嘉義分店','嘉義','002','2021-12-06 23:58:55'),(3,'勝利分店','台南','003','2021-12-06 23:58:55'),(4,'楠梓分店','高雄','004','2021-12-06 23:58:55'),(5,'仁德分店','台南','005','2021-12-06 23:58:55'),(6,'建工分店','高雄','006','2021-12-06 23:58:55'),(7,'裕農分店','台南','007','2021-12-06 23:58:55'),(8,'彌陀分店','嘉義','008','2021-12-06 23:58:55'),(9,'嘉工分店','嘉義','009','2021-12-06 23:58:55'),(10,'潮州分店','屏東','010','2021-12-06 23:58:55'),(11,'旗津分店','高雄','011','2021-12-06 23:58:55');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `SSN` varchar(3) NOT NULL,
  `Ename` varchar(45) NOT NULL,
  `Sex` varchar(45) NOT NULL,
  `Ephone` varchar(45) NOT NULL,
  `Bithday` varchar(45) NOT NULL,
  `D_id` int NOT NULL,
  PRIMARY KEY (`SSN`),
  KEY `D_id_idx` (`D_id`),
  CONSTRAINT `D_id` FOREIGN KEY (`D_id`) REFERENCES `department` (`D_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('001','安妮雅','女','0914048009','1995-04-24',1),('002','謝麗','女','0925264071','1995-07-19',2),('003','瑞克','男','0968244348','1993-04-26',3),('004','卡倫','女','0913132488','1997-02-04',4),('005','拉理','男','0937463983','1989-12-26',5),('006','韋斯','男','0961405915','1999-10-27',6),('007','梅爾巴','女','0987361035','1994-10-17',7),('008','尼克','男','0927442841','1991-01-25',8),('009','斯科特','男','0963272982','1983-10-19',9),('010','佩吉','女','0954609018','1988-08-15',10),('011','蘿茜','女','0935895155','1991-02-25',11),('012','珍妮','女','0956067411','1980-07-31',5),('013','卡森','男','0988257695','1983-10-25',6),('014','德雅娜','女','0936673224','1980-08-07',4),('015','羅伯','男','0972799363','1998-10-04',8),('016','詹恩','女','0915804579','1997-11-15',9),('017','沃利','男','0926297263','1987-11-25',10),('018','珍妮','女','0913065302','1985-05-08',1),('019','拉爾夫','男','0970496365','1995-02-13',2),('020','艾麗思','女','0952434033','1998-12-23',11),('021','巴理','男','0972118519','1982-04-22',3),('022','雪兒','女','0970942688','1992-06-02',7),('023','測試','女','0982501524','1998-09-08',10);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `meal`
--

DROP TABLE IF EXISTS `meal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `meal` (
  `M_id` int NOT NULL AUTO_INCREMENT,
  `Mname` varchar(45) NOT NULL,
  `Mprice` varchar(45) NOT NULL,
  PRIMARY KEY (`M_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meal`
--

LOCK TABLES `meal` WRITE;
/*!40000 ALTER TABLE `meal` DISABLE KEYS */;
INSERT INTO `meal` VALUES (1,'原味蛋餅','20'),(2,'熱狗蛋餅','25'),(3,'卡拉雞蛋餅','50'),(4,'蛋堡','25'),(5,'起司豬排漢堡','40'),(6,'卡拉雞漢堡','60'),(7,'起司蛋餅','30'),(8,'鍋燒意麵','70'),(9,'炒泡麵','60'),(10,'鐵板麵','35'),(11,'薯條','30'),(12,'熱狗蛋','25'),(13,'紅茶','20'),(14,'豆漿','20'),(15,'奶茶','30');
/*!40000 ALTER TABLE `meal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_list`
--

DROP TABLE IF EXISTS `order_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_list` (
  `O_id` int NOT NULL AUTO_INCREMENT,
  `Oprice` int NOT NULL,
  `amount` int NOT NULL,
  `M_id` int NOT NULL,
  `C_id` int NOT NULL,
  `ESSN` varchar(3) NOT NULL,
  `dealtime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`O_id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_list`
--

LOCK TABLES `order_list` WRITE;
/*!40000 ALTER TABLE `order_list` DISABLE KEYS */;
INSERT INTO `order_list` VALUES (1,40,2,1,5,'011','2021-12-01 22:27:00'),(2,70,1,8,5,'011','2021-12-01 22:27:00'),(3,30,1,15,5,'011','2021-12-01 22:27:00'),(4,180,3,9,9,'003','2021-12-02 22:27:00'),(5,40,2,14,9,'003','2021-12-02 22:27:00'),(6,30,1,15,9,'003','2021-12-02 22:27:00'),(7,70,2,10,10,'020','2021-12-02 22:27:00'),(8,25,1,2,10,'020','2021-12-02 22:27:00'),(9,25,1,4,10,'020','2021-12-02 22:27:00'),(10,30,1,7,10,'020','2021-12-02 22:27:00'),(11,90,3,11,2,'015','2021-12-06 22:28:48'),(12,40,2,12,2,'015','2021-12-06 22:28:48'),(13,40,1,5,15,'018','2021-12-06 22:28:48'),(14,30,1,15,15,'018','2021-12-06 22:28:48'),(15,80,2,5,12,'006','2021-12-07 14:46:46'),(16,20,1,13,12,'006','2021-12-07 14:46:46'),(17,20,1,14,12,'006','2021-12-07 14:46:46'),(18,300,6,3,3,'009','2021-12-07 14:46:46'),(19,240,4,9,3,'009','2021-12-07 14:46:46'),(20,70,2,10,3,'009','2021-12-07 14:46:46'),(21,150,5,15,3,'009','2021-12-07 14:46:46'),(22,60,3,14,3,'009','2021-12-07 14:46:46');
/*!40000 ALTER TABLE `order_list` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-07 16:40:44
