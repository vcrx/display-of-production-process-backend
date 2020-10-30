/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50621
Source Host           : localhost:3306
Source Database       : sssf

Target Server Type    : MYSQL
Target Server Version : 50621
File Encoding         : 65001

Date: 2020-10-22 13:50:48
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `pwd` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` int(11) DEFAULT NULL,
  `is_super` smallint(6) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone` (`phone`),
  KEY `role_id` (`role_id`),
  KEY `ix_admin_addtime` (`addtime`),
  CONSTRAINT `admin_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES ('3', 'admin', 'pbkdf2:sha256:50000$mz5n1Rsm$8ea24b516ae181669c2db4cd3450907f2459eca2a3cd0c9dc5be0436994cc050', '', null, '1', '2020-07-15 09:42:11', '4');
INSERT INTO `admin` VALUES ('5', 'puke', 'pbkdf2:sha256:50000$pgBnXrLf$9fcbc6fedc8409cebc33dcbb41b62fabc07e99f4cbce85f52646571e8b1711ee', null, null, '1', '2020-07-21 13:33:45', '4');
INSERT INTO `admin` VALUES ('6', 'zk', 'pbkdf2:sha256:50000$km0DijDZ$c5b01dd1ee50d44da31897a534700b710a66cde3544218b7a32c9b26e15903ff', null, null, '0', '2020-07-21 13:34:40', '3');

-- ----------------------------
-- Table structure for adminlog
-- ----------------------------
DROP TABLE IF EXISTS `adminlog`;
CREATE TABLE `adminlog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(100) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  `admin_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `admin_id` (`admin_id`),
  KEY `ix_adminlog_addtime` (`addtime`),
  CONSTRAINT `adminlog_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of adminlog
-- ----------------------------
INSERT INTO `adminlog` VALUES ('1', '127.0.0.1', '2020-07-20 20:36:18', '3');
INSERT INTO `adminlog` VALUES ('2', '127.0.0.1', '2020-07-21 13:14:02', '3');
INSERT INTO `adminlog` VALUES ('3', '127.0.0.1', '2020-07-21 13:26:22', '3');
INSERT INTO `adminlog` VALUES ('4', '127.0.0.1', '2020-07-21 13:27:00', '3');
INSERT INTO `adminlog` VALUES ('5', '127.0.0.1', '2020-07-21 13:32:21', '3');
INSERT INTO `adminlog` VALUES ('6', '127.0.0.1', '2020-07-21 13:33:16', '3');
INSERT INTO `adminlog` VALUES ('7', '127.0.0.1', '2020-07-21 13:35:39', '5');
INSERT INTO `adminlog` VALUES ('8', '127.0.0.1', '2020-07-21 13:37:11', '5');
INSERT INTO `adminlog` VALUES ('9', '127.0.0.1', '2020-07-21 13:38:56', '5');
INSERT INTO `adminlog` VALUES ('10', '127.0.0.1', '2020-07-21 13:46:28', '6');
INSERT INTO `adminlog` VALUES ('11', '127.0.0.1', '2020-07-21 14:06:03', '3');
INSERT INTO `adminlog` VALUES ('12', '127.0.0.1', '2020-08-21 13:36:19', '3');
INSERT INTO `adminlog` VALUES ('13', '127.0.0.1', '2020-08-21 14:54:53', '3');
INSERT INTO `adminlog` VALUES ('14', '127.0.0.1', '2020-08-21 15:34:34', '3');
INSERT INTO `adminlog` VALUES ('15', '127.0.0.1', '2020-08-21 15:43:09', '3');
INSERT INTO `adminlog` VALUES ('16', '127.0.0.1', '2020-08-21 15:44:11', '3');
INSERT INTO `adminlog` VALUES ('17', '127.0.0.1', '2020-08-21 15:44:21', '3');
INSERT INTO `adminlog` VALUES ('18', '127.0.0.1', '2020-08-21 15:45:23', '3');
INSERT INTO `adminlog` VALUES ('19', '127.0.0.1', '2020-08-21 15:56:10', '3');
INSERT INTO `adminlog` VALUES ('20', '127.0.0.1', '2020-08-21 22:33:10', '3');
INSERT INTO `adminlog` VALUES ('21', '127.0.0.1', '2020-08-21 22:33:22', '3');
INSERT INTO `adminlog` VALUES ('22', '127.0.0.1', '2020-10-19 09:17:36', '3');
INSERT INTO `adminlog` VALUES ('23', '127.0.0.1', '2020-10-19 09:35:26', '3');
INSERT INTO `adminlog` VALUES ('24', '127.0.0.1', '2020-10-19 23:22:46', '3');
INSERT INTO `adminlog` VALUES ('25', '127.0.0.1', '2020-10-21 08:35:30', '3');
INSERT INTO `adminlog` VALUES ('26', '127.0.0.1', '2020-10-21 08:40:01', '3');
INSERT INTO `adminlog` VALUES ('27', '127.0.0.1', '2020-10-21 08:41:01', '3');
INSERT INTO `adminlog` VALUES ('28', '127.0.0.1', '2020-10-21 08:41:26', '3');
INSERT INTO `adminlog` VALUES ('29', '127.0.0.1', '2020-10-21 08:42:47', '3');
INSERT INTO `adminlog` VALUES ('30', '127.0.0.1', '2020-10-21 08:45:14', '3');
INSERT INTO `adminlog` VALUES ('31', '127.0.0.1', '2020-10-21 08:46:57', '3');
INSERT INTO `adminlog` VALUES ('32', '127.0.0.1', '2020-10-21 08:48:44', '3');
INSERT INTO `adminlog` VALUES ('33', '127.0.0.1', '2020-10-21 08:49:53', '3');
INSERT INTO `adminlog` VALUES ('34', '127.0.0.1', '2020-10-21 08:52:38', '3');
INSERT INTO `adminlog` VALUES ('35', '127.0.0.1', '2020-10-21 08:57:17', '3');
INSERT INTO `adminlog` VALUES ('36', '127.0.0.1', '2020-10-21 08:57:30', '5');
INSERT INTO `adminlog` VALUES ('37', '127.0.0.1', '2020-10-21 08:58:32', '6');
INSERT INTO `adminlog` VALUES ('38', '127.0.0.1', '2020-10-21 09:01:03', '3');
INSERT INTO `adminlog` VALUES ('39', '127.0.0.1', '2020-10-21 09:19:13', '3');
INSERT INTO `adminlog` VALUES ('40', '127.0.0.1', '2020-10-21 09:19:25', '3');
INSERT INTO `adminlog` VALUES ('41', '127.0.0.1', '2020-10-21 09:19:47', '3');
INSERT INTO `adminlog` VALUES ('42', '127.0.0.1', '2020-10-21 09:27:55', '3');
INSERT INTO `adminlog` VALUES ('43', '127.0.0.1', '2020-10-21 09:32:18', '3');
INSERT INTO `adminlog` VALUES ('44', '127.0.0.1', '2020-10-21 14:22:14', '3');
INSERT INTO `adminlog` VALUES ('45', '127.0.0.1', '2020-10-21 14:28:13', '3');
INSERT INTO `adminlog` VALUES ('46', '127.0.0.1', '2020-10-21 14:47:56', '3');
INSERT INTO `adminlog` VALUES ('47', '127.0.0.1', '2020-10-21 15:00:17', '3');
INSERT INTO `adminlog` VALUES ('48', '127.0.0.1', '2020-10-21 15:01:12', '3');
INSERT INTO `adminlog` VALUES ('49', '127.0.0.1', '2020-10-21 15:16:06', '3');
INSERT INTO `adminlog` VALUES ('50', '127.0.0.1', '2020-10-21 17:34:09', '3');
INSERT INTO `adminlog` VALUES ('51', '127.0.0.1', '2020-10-21 18:46:17', '3');
INSERT INTO `adminlog` VALUES ('52', '127.0.0.1', '2020-10-21 19:28:52', '3');
INSERT INTO `adminlog` VALUES ('53', '127.0.0.1', '2020-10-21 22:28:35', '3');
INSERT INTO `adminlog` VALUES ('54', '127.0.0.1', '2020-10-21 23:01:36', '3');
INSERT INTO `adminlog` VALUES ('55', '127.0.0.1', '2020-10-21 23:12:47', '3');

-- ----------------------------
-- Table structure for auth
-- ----------------------------
DROP TABLE IF EXISTS `auth`;
CREATE TABLE `auth` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `url` (`url`),
  KEY `ix_auth_addtime` (`addtime`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth
-- ----------------------------
INSERT INTO `auth` VALUES ('12', '主路由', '/', '2020-07-21 13:17:09');
INSERT INTO `auth` VALUES ('13', '首页', '/index/', '2020-07-21 13:17:37');
INSERT INTO `auth` VALUES ('14', '生丝水分控制-影响因素', '/influence/', '2020-07-21 13:18:33');
INSERT INTO `auth` VALUES ('15', '生丝水分控制-报警控制', '/police/', '2020-07-21 13:18:55');
INSERT INTO `auth` VALUES ('16', '生丝水分控制-人工干预', '/people/', '2020-07-21 13:19:20');
INSERT INTO `auth` VALUES ('17', '可视化分析-温度可视化', '/temp_visual/', '2020-07-21 13:19:40');
INSERT INTO `auth` VALUES ('18', '可视化分析-湿度可视化', '/humidity_visual/', '2020-07-21 13:19:55');
INSERT INTO `auth` VALUES ('19', '统计查询-查询', '/select/', '2020-07-21 13:20:11');
INSERT INTO `auth` VALUES ('20', '统计查询-统计', '/statistics/', '2020-07-21 13:20:26');
INSERT INTO `auth` VALUES ('21', '用户管理-添加管理员', '/admin/add/', '2020-07-21 13:20:57');
INSERT INTO `auth` VALUES ('22', '用户管理-管理员列表', '/admin/list/<int:page>/', '2020-07-21 13:21:15');
INSERT INTO `auth` VALUES ('23', '修改密码', '/pwd/', '2020-07-21 13:21:28');
INSERT INTO `auth` VALUES ('24', '权限管理-添加权限', '/auth/add/', '2020-07-21 13:21:56');
INSERT INTO `auth` VALUES ('25', '权限管理-权限列表', '/auth/list/<int:page>/', '2020-07-21 13:22:14');
INSERT INTO `auth` VALUES ('26', '权限管理-删除权限', '/auth/del/<int:id>/', '2020-07-21 13:22:35');
INSERT INTO `auth` VALUES ('27', '权限管理-编辑权限', '/auth/edit/<int:id>/', '2020-07-21 13:22:51');
INSERT INTO `auth` VALUES ('28', '角色管理-添加角色', '/role/add/', '2020-07-21 13:23:10');
INSERT INTO `auth` VALUES ('29', '角色管理-角色列表', '/role/list/<int:page>/', '2020-07-21 13:23:30');
INSERT INTO `auth` VALUES ('30', '角色管理-删除角色', '/role/del/<int:id>/', '2020-07-21 13:23:51');
INSERT INTO `auth` VALUES ('31', '角色管理-编辑角色', '/role/edit/<int:id>/', '2020-07-21 13:24:09');
INSERT INTO `auth` VALUES ('32', '维护管理-操作日志列表', '/oplog/list/<int:page>/', '2020-07-21 13:24:30');
INSERT INTO `auth` VALUES ('33', '维护管理-登录日志列表', '/adminloginlog/list/<int:page>/', '2020-07-21 13:24:45');

-- ----------------------------
-- Table structure for bj_control
-- ----------------------------
DROP TABLE IF EXISTS `bj_control`;
CREATE TABLE `bj_control` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sshc_cksfup` int(11) DEFAULT NULL,
  `sshc_cksfdown` int(11) DEFAULT NULL,
  `yjl_rksfup` int(11) DEFAULT NULL,
  `yjl_rksfdown` int(11) DEFAULT NULL,
  `yjl_cljzlup` int(11) DEFAULT NULL,
  `yjl_cljzldown` int(11) DEFAULT NULL,
  `yjl_cssllup` int(11) DEFAULT NULL,
  `yjl_csslldown` int(11) DEFAULT NULL,
  `yjl_lywdup` int(11) DEFAULT NULL,
  `yjl_lywddown` int(11) DEFAULT NULL,
  `yjl_ljjslup` int(11) DEFAULT NULL,
  `yjl_ljjsldown` int(11) DEFAULT NULL,
  `yjl_ssjslup` int(11) DEFAULT NULL,
  `yjl_ssjsldown` int(11) DEFAULT NULL,
  `yjl_wdup` int(11) DEFAULT NULL,
  `yjl_wddown` int(11) DEFAULT NULL,
  `yjl_sdup` int(11) DEFAULT NULL,
  `yjl_sddown` int(11) DEFAULT NULL,
  `yjl_ckwdup` int(11) DEFAULT NULL,
  `yjl_ckwddown` int(11) DEFAULT NULL,
  `yjl_cksfup` int(11) DEFAULT NULL,
  `yjl_cksfdown` int(11) DEFAULT NULL,
  `cy_wdup` int(11) DEFAULT NULL,
  `cy_wddown` int(11) DEFAULT NULL,
  `cy_sdup` int(11) DEFAULT NULL,
  `cy_sddown` int(11) DEFAULT NULL,
  `qs_wdup` int(11) DEFAULT NULL,
  `qs_wddown` int(11) DEFAULT NULL,
  `qs_sdup` int(11) DEFAULT NULL,
  `qs_sddown` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of bj_control
-- ----------------------------

-- ----------------------------
-- Table structure for cy
-- ----------------------------
DROP TABLE IF EXISTS `cy`;
CREATE TABLE `cy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `wd` int(11) DEFAULT NULL,
  `sd` int(11) DEFAULT NULL,
  `cysc` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of cy
-- ----------------------------

-- ----------------------------
-- Table structure for cy_info
-- ----------------------------
DROP TABLE IF EXISTS `cy_info`;
CREATE TABLE `cy_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cy_bch` int(11) DEFAULT NULL,
  `cy_pch` int(11) DEFAULT NULL,
  `cy_pph` int(11) DEFAULT NULL,
  `cy_czh` int(11) DEFAULT NULL,
  `cy_pfh` int(11) DEFAULT NULL,
  `cy_mkh` int(11) DEFAULT NULL,
  `cy_product_start_time` datetime DEFAULT NULL,
  `cy_product_end_time` datetime DEFAULT NULL,
  `cysc` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_cy_info_cy_product_start_time` (`cy_product_start_time`),
  KEY `ix_cy_info_cy_product_end_time` (`cy_product_end_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of cy_info
-- ----------------------------

-- ----------------------------
-- Table structure for ksh
-- ----------------------------
DROP TABLE IF EXISTS `ksh`;
CREATE TABLE `ksh` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `yjl_id` int(11) DEFAULT NULL,
  `cy_id` int(11) DEFAULT NULL,
  `qs_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `yjl_id` (`yjl_id`),
  KEY `cy_id` (`cy_id`),
  KEY `qs_id` (`qs_id`),
  CONSTRAINT `ksh_ibfk_1` FOREIGN KEY (`yjl_id`) REFERENCES `yjl` (`id`),
  CONSTRAINT `ksh_ibfk_2` FOREIGN KEY (`cy_id`) REFERENCES `cy` (`id`),
  CONSTRAINT `ksh_ibfk_3` FOREIGN KEY (`qs_id`) REFERENCES `qs` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ksh
-- ----------------------------

-- ----------------------------
-- Table structure for oplog
-- ----------------------------
DROP TABLE IF EXISTS `oplog`;
CREATE TABLE `oplog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(100) DEFAULT NULL,
  `reason` varchar(600) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  `admin_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `admin_id` (`admin_id`),
  KEY `ix_oplog_addtime` (`addtime`),
  CONSTRAINT `oplog_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=508 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of oplog
-- ----------------------------
INSERT INTO `oplog` VALUES ('1', '127.0.0.1', '查看主页', '2020-07-21 13:14:02', '3');
INSERT INTO `oplog` VALUES ('2', '127.0.0.1', '查看主页', '2020-07-21 13:14:05', '3');
INSERT INTO `oplog` VALUES ('3', '127.0.0.1', '查看影响因素', '2020-07-21 13:14:07', '3');
INSERT INTO `oplog` VALUES ('4', '127.0.0.1', '进行报警控制', '2020-07-21 13:14:08', '3');
INSERT INTO `oplog` VALUES ('5', '127.0.0.1', '进行人工干预', '2020-07-21 13:14:09', '3');
INSERT INTO `oplog` VALUES ('6', '127.0.0.1', '温度可视化', '2020-07-21 13:14:10', '3');
INSERT INTO `oplog` VALUES ('7', '127.0.0.1', '湿度可视化', '2020-07-21 13:14:12', '3');
INSERT INTO `oplog` VALUES ('8', '127.0.0.1', '查询数据情况', '2020-07-21 13:14:13', '3');
INSERT INTO `oplog` VALUES ('9', '127.0.0.1', '查看统计情况', '2020-07-21 13:14:15', '3');
INSERT INTO `oplog` VALUES ('10', '127.0.0.1', '查看管理员列表', '2020-07-21 13:14:18', '3');
INSERT INTO `oplog` VALUES ('11', '127.0.0.1', '查看管理员列表', '2020-07-21 13:14:51', '3');
INSERT INTO `oplog` VALUES ('12', '127.0.0.1', '查看权限列表', '2020-07-21 13:15:17', '3');
INSERT INTO `oplog` VALUES ('13', '127.0.0.1', '查看角色列表', '2020-07-21 13:15:26', '3');
INSERT INTO `oplog` VALUES ('14', '127.0.0.1', '查看角色列表', '2020-07-21 13:15:28', '3');
INSERT INTO `oplog` VALUES ('15', '127.0.0.1', '查看权限列表', '2020-07-21 13:15:42', '3');
INSERT INTO `oplog` VALUES ('16', '127.0.0.1', '删除权限', '2020-07-21 13:15:43', '3');
INSERT INTO `oplog` VALUES ('17', '127.0.0.1', '查看权限列表', '2020-07-21 13:15:43', '3');
INSERT INTO `oplog` VALUES ('18', '127.0.0.1', '删除权限', '2020-07-21 13:15:44', '3');
INSERT INTO `oplog` VALUES ('19', '127.0.0.1', '查看权限列表', '2020-07-21 13:15:44', '3');
INSERT INTO `oplog` VALUES ('20', '127.0.0.1', '删除权限', '2020-07-21 13:15:44', '3');
INSERT INTO `oplog` VALUES ('21', '127.0.0.1', '查看权限列表', '2020-07-21 13:15:44', '3');
INSERT INTO `oplog` VALUES ('22', '127.0.0.1', '删除权限', '2020-07-21 13:15:45', '3');
INSERT INTO `oplog` VALUES ('23', '127.0.0.1', '查看权限列表', '2020-07-21 13:15:45', '3');
INSERT INTO `oplog` VALUES ('24', '127.0.0.1', '删除权限', '2020-07-21 13:15:45', '3');
INSERT INTO `oplog` VALUES ('25', '127.0.0.1', '查看权限列表', '2020-07-21 13:15:45', '3');
INSERT INTO `oplog` VALUES ('26', '127.0.0.1', '删除权限', '2020-07-21 13:15:46', '3');
INSERT INTO `oplog` VALUES ('27', '127.0.0.1', '查看权限列表', '2020-07-21 13:15:46', '3');
INSERT INTO `oplog` VALUES ('28', '127.0.0.1', '删除权限', '2020-07-21 13:15:46', '3');
INSERT INTO `oplog` VALUES ('29', '127.0.0.1', '查看权限列表', '2020-07-21 13:15:46', '3');
INSERT INTO `oplog` VALUES ('30', '127.0.0.1', '删除权限', '2020-07-21 13:15:46', '3');
INSERT INTO `oplog` VALUES ('31', '127.0.0.1', '查看权限列表', '2020-07-21 13:15:46', '3');
INSERT INTO `oplog` VALUES ('32', '127.0.0.1', '删除权限', '2020-07-21 13:15:46', '3');
INSERT INTO `oplog` VALUES ('33', '127.0.0.1', '查看权限列表', '2020-07-21 13:15:46', '3');
INSERT INTO `oplog` VALUES ('34', '127.0.0.1', '删除权限', '2020-07-21 13:15:46', '3');
INSERT INTO `oplog` VALUES ('35', '127.0.0.1', '查看权限列表', '2020-07-21 13:15:46', '3');
INSERT INTO `oplog` VALUES ('36', '127.0.0.1', '删除权限', '2020-07-21 13:15:47', '3');
INSERT INTO `oplog` VALUES ('37', '127.0.0.1', '查看权限列表', '2020-07-21 13:15:47', '3');
INSERT INTO `oplog` VALUES ('38', '127.0.0.1', '查看权限列表', '2020-07-21 13:16:46', '3');
INSERT INTO `oplog` VALUES ('39', '127.0.0.1', '添加权限主路由', '2020-07-21 13:17:09', '3');
INSERT INTO `oplog` VALUES ('40', '127.0.0.1', '添加权限首页', '2020-07-21 13:17:37', '3');
INSERT INTO `oplog` VALUES ('41', '127.0.0.1', '添加权限生丝水分控制-影响因素', '2020-07-21 13:18:33', '3');
INSERT INTO `oplog` VALUES ('42', '127.0.0.1', '添加权限生丝水分控制-报警控制', '2020-07-21 13:18:55', '3');
INSERT INTO `oplog` VALUES ('43', '127.0.0.1', '添加权限生丝水分控制-人工干预', '2020-07-21 13:19:20', '3');
INSERT INTO `oplog` VALUES ('44', '127.0.0.1', '添加权限可视化分析-温度可视化', '2020-07-21 13:19:40', '3');
INSERT INTO `oplog` VALUES ('45', '127.0.0.1', '添加权限可视化分析-湿度可视化', '2020-07-21 13:19:55', '3');
INSERT INTO `oplog` VALUES ('46', '127.0.0.1', '添加权限统计查询-查询', '2020-07-21 13:20:11', '3');
INSERT INTO `oplog` VALUES ('47', '127.0.0.1', '添加权限统计查询-统计', '2020-07-21 13:20:26', '3');
INSERT INTO `oplog` VALUES ('48', '127.0.0.1', '添加权限用户管理-添加管理员', '2020-07-21 13:20:57', '3');
INSERT INTO `oplog` VALUES ('49', '127.0.0.1', '添加权限用户管理-管理员列表', '2020-07-21 13:21:15', '3');
INSERT INTO `oplog` VALUES ('50', '127.0.0.1', '添加权限修改密码', '2020-07-21 13:21:28', '3');
INSERT INTO `oplog` VALUES ('51', '127.0.0.1', '添加权限权限管理-添加权限', '2020-07-21 13:21:56', '3');
INSERT INTO `oplog` VALUES ('52', '127.0.0.1', '添加权限权限管理-权限列表', '2020-07-21 13:22:14', '3');
INSERT INTO `oplog` VALUES ('53', '127.0.0.1', '添加权限权限管理-删除权限', '2020-07-21 13:22:35', '3');
INSERT INTO `oplog` VALUES ('54', '127.0.0.1', '添加权限权限管理-编辑权限', '2020-07-21 13:22:51', '3');
INSERT INTO `oplog` VALUES ('55', '127.0.0.1', '添加权限角色管理-添加角色', '2020-07-21 13:23:10', '3');
INSERT INTO `oplog` VALUES ('56', '127.0.0.1', '添加权限角色管理-角色列表', '2020-07-21 13:23:30', '3');
INSERT INTO `oplog` VALUES ('57', '127.0.0.1', '添加权限角色管理-删除角色', '2020-07-21 13:23:51', '3');
INSERT INTO `oplog` VALUES ('58', '127.0.0.1', '添加权限角色管理-编辑角色', '2020-07-21 13:24:09', '3');
INSERT INTO `oplog` VALUES ('59', '127.0.0.1', '添加权限维护管理-操作日志列表', '2020-07-21 13:24:30', '3');
INSERT INTO `oplog` VALUES ('60', '127.0.0.1', '添加权限维护管理-登录日志列表', '2020-07-21 13:24:45', '3');
INSERT INTO `oplog` VALUES ('61', '127.0.0.1', '查看权限列表', '2020-07-21 13:24:50', '3');
INSERT INTO `oplog` VALUES ('62', '127.0.0.1', '查看权限列表', '2020-07-21 13:25:02', '3');
INSERT INTO `oplog` VALUES ('63', '127.0.0.1', '查看权限列表', '2020-07-21 13:25:05', '3');
INSERT INTO `oplog` VALUES ('64', '127.0.0.1', '查看权限列表', '2020-07-21 13:25:07', '3');
INSERT INTO `oplog` VALUES ('65', '127.0.0.1', '查看权限列表', '2020-07-21 13:25:10', '3');
INSERT INTO `oplog` VALUES ('66', '127.0.0.1', '查看主页', '2020-07-21 13:26:22', '3');
INSERT INTO `oplog` VALUES ('67', '127.0.0.1', '查看角色列表', '2020-07-21 13:26:28', '3');
INSERT INTO `oplog` VALUES ('68', '127.0.0.1', '查看主页', '2020-07-21 13:27:00', '3');
INSERT INTO `oplog` VALUES ('69', '127.0.0.1', '添加角色普通管理员', '2020-07-21 13:29:33', '3');
INSERT INTO `oplog` VALUES ('70', '127.0.0.1', '添加角色超级管理员', '2020-07-21 13:30:51', '3');
INSERT INTO `oplog` VALUES ('71', '127.0.0.1', '查看角色列表', '2020-07-21 13:31:00', '3');
INSERT INTO `oplog` VALUES ('72', '127.0.0.1', '删除角色', '2020-07-21 13:31:05', '3');
INSERT INTO `oplog` VALUES ('73', '127.0.0.1', '查看角色列表', '2020-07-21 13:31:05', '3');
INSERT INTO `oplog` VALUES ('74', '127.0.0.1', '查看主页', '2020-07-21 13:32:21', '3');
INSERT INTO `oplog` VALUES ('75', '127.0.0.1', '查看主页', '2020-07-21 13:33:16', '3');
INSERT INTO `oplog` VALUES ('76', '127.0.0.1', '添加管理员puke', '2020-07-21 13:33:45', '3');
INSERT INTO `oplog` VALUES ('77', '127.0.0.1', '添加管理员zk', '2020-07-21 13:34:40', '3');
INSERT INTO `oplog` VALUES ('78', '127.0.0.1', '查看管理员列表', '2020-07-21 13:35:03', '3');
INSERT INTO `oplog` VALUES ('79', '127.0.0.1', '查看管理员列表', '2020-07-21 13:35:10', '3');
INSERT INTO `oplog` VALUES ('80', '127.0.0.1', '查看管理员列表', '2020-07-21 13:35:11', '3');
INSERT INTO `oplog` VALUES ('81', '127.0.0.1', '查看主页', '2020-07-21 13:35:39', '5');
INSERT INTO `oplog` VALUES ('82', '127.0.0.1', '查看管理员列表', '2020-07-21 13:35:44', '5');
INSERT INTO `oplog` VALUES ('83', '127.0.0.1', '查看管理员列表', '2020-07-21 13:35:49', '5');
INSERT INTO `oplog` VALUES ('84', '127.0.0.1', '查看管理员列表', '2020-07-21 13:35:50', '5');
INSERT INTO `oplog` VALUES ('85', '127.0.0.1', '查看主页', '2020-07-21 13:37:11', '5');
INSERT INTO `oplog` VALUES ('86', '127.0.0.1', '查看管理员列表', '2020-07-21 13:37:19', '5');
INSERT INTO `oplog` VALUES ('87', '127.0.0.1', '查看管理员列表', '2020-07-21 13:37:23', '5');
INSERT INTO `oplog` VALUES ('88', '127.0.0.1', '查看主页', '2020-07-21 13:38:56', '5');
INSERT INTO `oplog` VALUES ('89', '127.0.0.1', '查看管理员列表', '2020-07-21 13:39:04', '5');
INSERT INTO `oplog` VALUES ('90', '127.0.0.1', '查看管理员列表', '2020-07-21 13:39:10', '5');
INSERT INTO `oplog` VALUES ('91', '127.0.0.1', '查看主页', '2020-07-21 13:46:28', '6');
INSERT INTO `oplog` VALUES ('92', '127.0.0.1', '查看主页', '2020-07-21 14:06:03', '3');
INSERT INTO `oplog` VALUES ('93', '127.0.0.1', '查看管理员列表', '2020-07-21 14:06:26', '3');
INSERT INTO `oplog` VALUES ('94', '127.0.0.1', '查看主页', '2020-08-21 13:36:19', '3');
INSERT INTO `oplog` VALUES ('95', '127.0.0.1', '查看主页', '2020-08-21 14:54:53', '3');
INSERT INTO `oplog` VALUES ('96', '127.0.0.1', '查看主页', '2020-08-21 15:34:34', '3');
INSERT INTO `oplog` VALUES ('97', '127.0.0.1', '查看主页', '2020-08-21 15:43:09', '3');
INSERT INTO `oplog` VALUES ('98', '127.0.0.1', '查看主页', '2020-08-21 15:44:11', '3');
INSERT INTO `oplog` VALUES ('99', '127.0.0.1', '查看主页', '2020-08-21 15:44:21', '3');
INSERT INTO `oplog` VALUES ('100', '127.0.0.1', '查看主页', '2020-08-21 15:45:23', '3');
INSERT INTO `oplog` VALUES ('101', '127.0.0.1', '查看主页', '2020-08-21 15:56:10', '3');
INSERT INTO `oplog` VALUES ('102', '127.0.0.1', '查看主页', '2020-08-21 15:56:27', '3');
INSERT INTO `oplog` VALUES ('103', '127.0.0.1', '查看主页', '2020-08-21 22:33:10', '3');
INSERT INTO `oplog` VALUES ('104', '127.0.0.1', '查看主页', '2020-08-21 22:33:22', '3');
INSERT INTO `oplog` VALUES ('105', '127.0.0.1', '查看主页', '2020-10-19 09:17:36', '3');
INSERT INTO `oplog` VALUES ('106', '127.0.0.1', '查看影响因素', '2020-10-19 09:18:31', '3');
INSERT INTO `oplog` VALUES ('107', '127.0.0.1', '进行人工干预', '2020-10-19 09:18:32', '3');
INSERT INTO `oplog` VALUES ('108', '127.0.0.1', '进行报警控制', '2020-10-19 09:18:34', '3');
INSERT INTO `oplog` VALUES ('109', '127.0.0.1', '进行人工干预', '2020-10-19 09:18:38', '3');
INSERT INTO `oplog` VALUES ('110', '127.0.0.1', '进行报警控制', '2020-10-19 09:18:39', '3');
INSERT INTO `oplog` VALUES ('111', '127.0.0.1', '进行人工干预', '2020-10-19 09:18:42', '3');
INSERT INTO `oplog` VALUES ('112', '127.0.0.1', '查看影响因素', '2020-10-19 09:18:44', '3');
INSERT INTO `oplog` VALUES ('113', '127.0.0.1', '温度可视化', '2020-10-19 09:18:45', '3');
INSERT INTO `oplog` VALUES ('114', '127.0.0.1', '湿度可视化', '2020-10-19 09:18:47', '3');
INSERT INTO `oplog` VALUES ('115', '127.0.0.1', '查询数据情况', '2020-10-19 09:18:49', '3');
INSERT INTO `oplog` VALUES ('116', '127.0.0.1', '查看统计情况', '2020-10-19 09:18:51', '3');
INSERT INTO `oplog` VALUES ('117', '127.0.0.1', '查看管理员列表', '2020-10-19 09:18:55', '3');
INSERT INTO `oplog` VALUES ('118', '127.0.0.1', '查看角色列表', '2020-10-19 09:19:04', '3');
INSERT INTO `oplog` VALUES ('119', '127.0.0.1', '查看主页', '2020-10-19 09:20:10', '3');
INSERT INTO `oplog` VALUES ('120', '127.0.0.1', '查看主页', '2020-10-19 09:35:26', '3');
INSERT INTO `oplog` VALUES ('121', '127.0.0.1', '进行报警控制', '2020-10-19 09:41:20', '3');
INSERT INTO `oplog` VALUES ('122', '127.0.0.1', '进行人工干预', '2020-10-19 09:41:37', '3');
INSERT INTO `oplog` VALUES ('123', '127.0.0.1', '查看影响因素', '2020-10-19 09:41:39', '3');
INSERT INTO `oplog` VALUES ('124', '127.0.0.1', '进行报警控制', '2020-10-19 09:41:41', '3');
INSERT INTO `oplog` VALUES ('125', '127.0.0.1', '进行报警控制', '2020-10-19 09:41:48', '3');
INSERT INTO `oplog` VALUES ('126', '127.0.0.1', '查看影响因素', '2020-10-19 09:41:55', '3');
INSERT INTO `oplog` VALUES ('127', '127.0.0.1', '进行人工干预', '2020-10-19 09:41:57', '3');
INSERT INTO `oplog` VALUES ('128', '127.0.0.1', '查看主页', '2020-10-19 23:22:46', '3');
INSERT INTO `oplog` VALUES ('129', '127.0.0.1', '查看主页', '2020-10-19 23:23:01', '3');
INSERT INTO `oplog` VALUES ('130', '127.0.0.1', '查看影响因素', '2020-10-19 23:23:10', '3');
INSERT INTO `oplog` VALUES ('131', '127.0.0.1', '进行报警控制', '2020-10-19 23:23:16', '3');
INSERT INTO `oplog` VALUES ('132', '127.0.0.1', '进行人工干预', '2020-10-19 23:23:20', '3');
INSERT INTO `oplog` VALUES ('133', '127.0.0.1', '温度可视化', '2020-10-19 23:23:24', '3');
INSERT INTO `oplog` VALUES ('134', '127.0.0.1', '湿度可视化', '2020-10-19 23:23:27', '3');
INSERT INTO `oplog` VALUES ('135', '127.0.0.1', '查询数据情况', '2020-10-19 23:23:31', '3');
INSERT INTO `oplog` VALUES ('136', '127.0.0.1', '查看统计情况', '2020-10-19 23:23:34', '3');
INSERT INTO `oplog` VALUES ('137', '127.0.0.1', '查看管理员列表', '2020-10-19 23:23:40', '3');
INSERT INTO `oplog` VALUES ('138', '127.0.0.1', '查看权限列表', '2020-10-19 23:24:56', '3');
INSERT INTO `oplog` VALUES ('139', '127.0.0.1', '查看角色列表', '2020-10-19 23:25:10', '3');
INSERT INTO `oplog` VALUES ('140', '127.0.0.1', '查看角色列表', '2020-10-19 23:25:32', '3');
INSERT INTO `oplog` VALUES ('141', '127.0.0.1', '查看主页', '2020-10-19 23:26:29', '3');
INSERT INTO `oplog` VALUES ('142', '127.0.0.1', '查看主页', '2020-10-21 07:42:49', '3');
INSERT INTO `oplog` VALUES ('143', '127.0.0.1', '查看主页', '2020-10-21 08:48:44', '3');
INSERT INTO `oplog` VALUES ('144', '127.0.0.1', '查看主页', '2020-10-21 08:49:00', '3');
INSERT INTO `oplog` VALUES ('145', '127.0.0.1', '查看主页', '2020-10-21 08:50:14', '3');
INSERT INTO `oplog` VALUES ('146', '127.0.0.1', '查看主页', '2020-10-21 08:50:22', '3');
INSERT INTO `oplog` VALUES ('147', '127.0.0.1', '查看主页', '2020-10-21 08:50:34', '3');
INSERT INTO `oplog` VALUES ('148', '127.0.0.1', '查看主页', '2020-10-21 08:52:25', '3');
INSERT INTO `oplog` VALUES ('149', '127.0.0.1', '查看主页', '2020-10-21 08:52:38', '3');
INSERT INTO `oplog` VALUES ('150', '127.0.0.1', '查看主页', '2020-10-21 08:52:44', '3');
INSERT INTO `oplog` VALUES ('151', '127.0.0.1', '查看主页', '2020-10-21 08:52:46', '3');
INSERT INTO `oplog` VALUES ('152', '127.0.0.1', '查看影响因素', '2020-10-21 08:52:47', '3');
INSERT INTO `oplog` VALUES ('153', '127.0.0.1', '进行报警控制', '2020-10-21 08:52:49', '3');
INSERT INTO `oplog` VALUES ('154', '127.0.0.1', '进行人工干预', '2020-10-21 08:52:51', '3');
INSERT INTO `oplog` VALUES ('155', '127.0.0.1', '温度可视化', '2020-10-21 08:52:52', '3');
INSERT INTO `oplog` VALUES ('156', '127.0.0.1', '湿度可视化', '2020-10-21 08:52:53', '3');
INSERT INTO `oplog` VALUES ('157', '127.0.0.1', '查询数据情况', '2020-10-21 08:52:55', '3');
INSERT INTO `oplog` VALUES ('158', '127.0.0.1', '查看统计情况', '2020-10-21 08:52:56', '3');
INSERT INTO `oplog` VALUES ('159', '127.0.0.1', '查看管理员列表', '2020-10-21 08:52:59', '3');
INSERT INTO `oplog` VALUES ('160', '127.0.0.1', '查看权限列表', '2020-10-21 08:53:04', '3');
INSERT INTO `oplog` VALUES ('161', '127.0.0.1', '查看角色列表', '2020-10-21 08:53:25', '3');
INSERT INTO `oplog` VALUES ('162', '127.0.0.1', '查看权限列表', '2020-10-21 08:53:36', '3');
INSERT INTO `oplog` VALUES ('163', '127.0.0.1', '编辑权限', '2020-10-21 08:53:45', '3');
INSERT INTO `oplog` VALUES ('164', '127.0.0.1', '编辑权限', '2020-10-21 08:53:54', '3');
INSERT INTO `oplog` VALUES ('165', '127.0.0.1', '查看权限列表', '2020-10-21 08:54:01', '3');
INSERT INTO `oplog` VALUES ('166', '127.0.0.1', '编辑权限', '2020-10-21 08:54:13', '3');
INSERT INTO `oplog` VALUES ('167', '127.0.0.1', '查看权限列表', '2020-10-21 08:54:26', '3');
INSERT INTO `oplog` VALUES ('168', '127.0.0.1', '编辑权限', '2020-10-21 08:54:38', '3');
INSERT INTO `oplog` VALUES ('169', '127.0.0.1', '查看权限列表', '2020-10-21 08:54:41', '3');
INSERT INTO `oplog` VALUES ('170', '127.0.0.1', '编辑权限', '2020-10-21 08:54:49', '3');
INSERT INTO `oplog` VALUES ('171', '127.0.0.1', '查看权限列表', '2020-10-21 08:54:52', '3');
INSERT INTO `oplog` VALUES ('172', '127.0.0.1', '编辑权限', '2020-10-21 08:55:06', '3');
INSERT INTO `oplog` VALUES ('173', '127.0.0.1', '查看权限列表', '2020-10-21 08:55:09', '3');
INSERT INTO `oplog` VALUES ('174', '127.0.0.1', '编辑权限', '2020-10-21 08:55:28', '3');
INSERT INTO `oplog` VALUES ('175', '127.0.0.1', '查看权限列表', '2020-10-21 08:56:23', '3');
INSERT INTO `oplog` VALUES ('176', '127.0.0.1', '查看权限列表', '2020-10-21 08:56:37', '3');
INSERT INTO `oplog` VALUES ('177', '127.0.0.1', '查看权限列表', '2020-10-21 08:56:38', '3');
INSERT INTO `oplog` VALUES ('178', '127.0.0.1', '查看权限列表', '2020-10-21 08:56:43', '3');
INSERT INTO `oplog` VALUES ('179', '127.0.0.1', '查看角色列表', '2020-10-21 08:56:46', '3');
INSERT INTO `oplog` VALUES ('180', '127.0.0.1', '查看主页', '2020-10-21 08:57:17', '3');
INSERT INTO `oplog` VALUES ('181', '127.0.0.1', '查看主页', '2020-10-21 08:57:30', '5');
INSERT INTO `oplog` VALUES ('182', '127.0.0.1', '查看角色列表', '2020-10-21 08:57:39', '5');
INSERT INTO `oplog` VALUES ('183', '127.0.0.1', '查看管理员列表', '2020-10-21 08:57:44', '5');
INSERT INTO `oplog` VALUES ('184', '127.0.0.1', '查看主页', '2020-10-21 08:58:32', '6');
INSERT INTO `oplog` VALUES ('185', '127.0.0.1', '查看影响因素', '2020-10-21 08:58:38', '6');
INSERT INTO `oplog` VALUES ('186', '127.0.0.1', '查询数据情况', '2020-10-21 08:58:40', '6');
INSERT INTO `oplog` VALUES ('187', '127.0.0.1', '查看管理员列表', '2020-10-21 08:58:45', '6');
INSERT INTO `oplog` VALUES ('188', '127.0.0.1', '查看主页', '2020-10-21 09:01:03', '3');
INSERT INTO `oplog` VALUES ('189', '127.0.0.1', '查看权限列表', '2020-10-21 09:01:06', '3');
INSERT INTO `oplog` VALUES ('190', '127.0.0.1', '编辑权限', '2020-10-21 09:01:20', '3');
INSERT INTO `oplog` VALUES ('191', '127.0.0.1', '查看权限列表', '2020-10-21 09:01:24', '3');
INSERT INTO `oplog` VALUES ('192', '127.0.0.1', '编辑权限', '2020-10-21 09:01:37', '3');
INSERT INTO `oplog` VALUES ('193', '127.0.0.1', '查看权限列表', '2020-10-21 09:01:39', '3');
INSERT INTO `oplog` VALUES ('194', '127.0.0.1', '编辑权限', '2020-10-21 09:01:47', '3');
INSERT INTO `oplog` VALUES ('195', '127.0.0.1', '查看权限列表', '2020-10-21 09:01:49', '3');
INSERT INTO `oplog` VALUES ('196', '127.0.0.1', '编辑权限', '2020-10-21 09:01:56', '3');
INSERT INTO `oplog` VALUES ('197', '127.0.0.1', '查看权限列表', '2020-10-21 09:01:58', '3');
INSERT INTO `oplog` VALUES ('198', '127.0.0.1', '查看权限列表', '2020-10-21 09:02:01', '3');
INSERT INTO `oplog` VALUES ('199', '127.0.0.1', '编辑权限', '2020-10-21 09:02:09', '3');
INSERT INTO `oplog` VALUES ('200', '127.0.0.1', '查看权限列表', '2020-10-21 09:02:11', '3');
INSERT INTO `oplog` VALUES ('201', '127.0.0.1', '查看权限列表', '2020-10-21 09:02:13', '3');
INSERT INTO `oplog` VALUES ('202', '127.0.0.1', '编辑权限', '2020-10-21 09:02:24', '3');
INSERT INTO `oplog` VALUES ('203', '127.0.0.1', '查看权限列表', '2020-10-21 09:03:03', '3');
INSERT INTO `oplog` VALUES ('204', '127.0.0.1', '查看权限列表', '2020-10-21 09:03:17', '3');
INSERT INTO `oplog` VALUES ('205', '127.0.0.1', '编辑权限', '2020-10-21 09:03:27', '3');
INSERT INTO `oplog` VALUES ('206', '127.0.0.1', '查看权限列表', '2020-10-21 09:03:31', '3');
INSERT INTO `oplog` VALUES ('207', '127.0.0.1', '编辑权限', '2020-10-21 09:03:41', '3');
INSERT INTO `oplog` VALUES ('208', '127.0.0.1', '查看权限列表', '2020-10-21 09:03:44', '3');
INSERT INTO `oplog` VALUES ('209', '127.0.0.1', '编辑权限', '2020-10-21 09:03:52', '3');
INSERT INTO `oplog` VALUES ('210', '127.0.0.1', '查看权限列表', '2020-10-21 09:03:53', '3');
INSERT INTO `oplog` VALUES ('211', '127.0.0.1', '编辑权限', '2020-10-21 09:04:02', '3');
INSERT INTO `oplog` VALUES ('212', '127.0.0.1', '查看权限列表', '2020-10-21 09:04:04', '3');
INSERT INTO `oplog` VALUES ('213', '127.0.0.1', '编辑权限', '2020-10-21 09:04:15', '3');
INSERT INTO `oplog` VALUES ('214', '127.0.0.1', '查看权限列表', '2020-10-21 09:04:18', '3');
INSERT INTO `oplog` VALUES ('215', '127.0.0.1', '编辑权限', '2020-10-21 09:04:24', '3');
INSERT INTO `oplog` VALUES ('216', '127.0.0.1', '查看权限列表', '2020-10-21 09:04:26', '3');
INSERT INTO `oplog` VALUES ('217', '127.0.0.1', '编辑权限', '2020-10-21 09:04:32', '3');
INSERT INTO `oplog` VALUES ('218', '127.0.0.1', '查看权限列表', '2020-10-21 09:04:34', '3');
INSERT INTO `oplog` VALUES ('219', '127.0.0.1', '编辑权限', '2020-10-21 09:04:40', '3');
INSERT INTO `oplog` VALUES ('220', '127.0.0.1', '查看权限列表', '2020-10-21 09:04:42', '3');
INSERT INTO `oplog` VALUES ('221', '127.0.0.1', '查看权限列表', '2020-10-21 09:04:45', '3');
INSERT INTO `oplog` VALUES ('222', '127.0.0.1', '编辑权限', '2020-10-21 09:04:54', '3');
INSERT INTO `oplog` VALUES ('223', '127.0.0.1', '查看权限列表', '2020-10-21 09:04:57', '3');
INSERT INTO `oplog` VALUES ('224', '127.0.0.1', '编辑权限', '2020-10-21 09:05:04', '3');
INSERT INTO `oplog` VALUES ('225', '127.0.0.1', '查看权限列表', '2020-10-21 09:05:06', '3');
INSERT INTO `oplog` VALUES ('226', '127.0.0.1', '查看管理员列表', '2020-10-21 09:05:21', '3');
INSERT INTO `oplog` VALUES ('227', '127.0.0.1', '查看主页', '2020-10-21 09:05:32', '3');
INSERT INTO `oplog` VALUES ('228', '127.0.0.1', '进行报警控制', '2020-10-21 09:05:34', '3');
INSERT INTO `oplog` VALUES ('229', '127.0.0.1', '进行人工干预', '2020-10-21 09:05:35', '3');
INSERT INTO `oplog` VALUES ('230', '127.0.0.1', '温度可视化', '2020-10-21 09:05:37', '3');
INSERT INTO `oplog` VALUES ('231', '127.0.0.1', '湿度可视化', '2020-10-21 09:05:38', '3');
INSERT INTO `oplog` VALUES ('232', '127.0.0.1', '查询数据情况', '2020-10-21 09:05:39', '3');
INSERT INTO `oplog` VALUES ('233', '127.0.0.1', '查看统计情况', '2020-10-21 09:05:40', '3');
INSERT INTO `oplog` VALUES ('234', '127.0.0.1', '查看管理员列表', '2020-10-21 09:05:42', '3');
INSERT INTO `oplog` VALUES ('235', '127.0.0.1', '查看权限列表', '2020-10-21 09:05:52', '3');
INSERT INTO `oplog` VALUES ('236', '127.0.0.1', '查看角色列表', '2020-10-21 09:05:57', '3');
INSERT INTO `oplog` VALUES ('237', '127.0.0.1', '查看权限列表', '2020-10-21 09:13:25', '3');
INSERT INTO `oplog` VALUES ('238', '127.0.0.1', '查看权限列表', '2020-10-21 09:15:06', '3');
INSERT INTO `oplog` VALUES ('239', '127.0.0.1', '查看角色列表', '2020-10-21 09:15:19', '3');
INSERT INTO `oplog` VALUES ('240', '127.0.0.1', '查看权限列表', '2020-10-21 09:15:21', '3');
INSERT INTO `oplog` VALUES ('241', '127.0.0.1', '查看权限列表', '2020-10-21 09:15:28', '3');
INSERT INTO `oplog` VALUES ('242', '127.0.0.1', '查看权限列表', '2020-10-21 09:15:33', '3');
INSERT INTO `oplog` VALUES ('243', '127.0.0.1', '查看权限列表', '2020-10-21 09:15:36', '3');
INSERT INTO `oplog` VALUES ('244', '127.0.0.1', '查看管理员列表', '2020-10-21 09:15:41', '3');
INSERT INTO `oplog` VALUES ('245', '127.0.0.1', '查看角色列表', '2020-10-21 09:16:56', '3');
INSERT INTO `oplog` VALUES ('246', '127.0.0.1', '查看主页', '2020-10-21 09:18:46', '3');
INSERT INTO `oplog` VALUES ('247', '127.0.0.1', '进行密码修改', '2020-10-21 09:19:03', '3');
INSERT INTO `oplog` VALUES ('248', '127.0.0.1', '查看主页', '2020-10-21 09:19:13', '3');
INSERT INTO `oplog` VALUES ('249', '127.0.0.1', '查看主页', '2020-10-21 09:19:25', '3');
INSERT INTO `oplog` VALUES ('250', '127.0.0.1', '进行密码修改', '2020-10-21 09:19:44', '3');
INSERT INTO `oplog` VALUES ('251', '127.0.0.1', '查看主页', '2020-10-21 09:19:47', '3');
INSERT INTO `oplog` VALUES ('252', '127.0.0.1', '查看主页', '2020-10-21 09:27:55', '3');
INSERT INTO `oplog` VALUES ('253', '127.0.0.1', '查看影响因素', '2020-10-21 09:27:58', '3');
INSERT INTO `oplog` VALUES ('254', '127.0.0.1', '进行报警控制', '2020-10-21 09:27:59', '3');
INSERT INTO `oplog` VALUES ('255', '127.0.0.1', '进行人工干预', '2020-10-21 09:28:00', '3');
INSERT INTO `oplog` VALUES ('256', '127.0.0.1', '温度可视化', '2020-10-21 09:28:01', '3');
INSERT INTO `oplog` VALUES ('257', '127.0.0.1', '湿度可视化', '2020-10-21 09:28:03', '3');
INSERT INTO `oplog` VALUES ('258', '127.0.0.1', '查询数据情况', '2020-10-21 09:28:04', '3');
INSERT INTO `oplog` VALUES ('259', '127.0.0.1', '查看统计情况', '2020-10-21 09:28:05', '3');
INSERT INTO `oplog` VALUES ('260', '127.0.0.1', '查看管理员列表', '2020-10-21 09:28:07', '3');
INSERT INTO `oplog` VALUES ('261', '127.0.0.1', '查看权限列表', '2020-10-21 09:28:10', '3');
INSERT INTO `oplog` VALUES ('262', '127.0.0.1', '查看角色列表', '2020-10-21 09:28:12', '3');
INSERT INTO `oplog` VALUES ('263', '127.0.0.1', '查看主页', '2020-10-21 09:32:18', '3');
INSERT INTO `oplog` VALUES ('264', '127.0.0.1', '查看主页', '2020-10-21 11:05:20', '3');
INSERT INTO `oplog` VALUES ('265', '127.0.0.1', '查看主页', '2020-10-21 14:07:45', '3');
INSERT INTO `oplog` VALUES ('266', '127.0.0.1', '查看主页', '2020-10-21 14:21:51', '3');
INSERT INTO `oplog` VALUES ('267', '127.0.0.1', '查看主页', '2020-10-21 14:22:14', '3');
INSERT INTO `oplog` VALUES ('268', '127.0.0.1', '查看主页', '2020-10-21 14:28:13', '3');
INSERT INTO `oplog` VALUES ('269', '127.0.0.1', '查看主页', '2020-10-21 14:47:56', '3');
INSERT INTO `oplog` VALUES ('270', '127.0.0.1', '查看主页', '2020-10-21 14:54:09', '3');
INSERT INTO `oplog` VALUES ('271', '127.0.0.1', '查看权限列表', '2020-10-21 14:54:15', '3');
INSERT INTO `oplog` VALUES ('272', '127.0.0.1', '编辑权限', '2020-10-21 14:54:27', '3');
INSERT INTO `oplog` VALUES ('273', '127.0.0.1', '查看主页', '2020-10-21 14:54:31', '3');
INSERT INTO `oplog` VALUES ('274', '127.0.0.1', '查看权限列表', '2020-10-21 14:54:34', '3');
INSERT INTO `oplog` VALUES ('275', '127.0.0.1', '编辑权限', '2020-10-21 14:54:41', '3');
INSERT INTO `oplog` VALUES ('276', '127.0.0.1', '查看权限列表', '2020-10-21 14:54:44', '3');
INSERT INTO `oplog` VALUES ('277', '127.0.0.1', '编辑权限', '2020-10-21 14:54:50', '3');
INSERT INTO `oplog` VALUES ('278', '127.0.0.1', '查看权限列表', '2020-10-21 14:54:52', '3');
INSERT INTO `oplog` VALUES ('279', '127.0.0.1', '编辑权限', '2020-10-21 14:54:57', '3');
INSERT INTO `oplog` VALUES ('280', '127.0.0.1', '查看权限列表', '2020-10-21 14:54:59', '3');
INSERT INTO `oplog` VALUES ('281', '127.0.0.1', '编辑权限', '2020-10-21 14:55:06', '3');
INSERT INTO `oplog` VALUES ('282', '127.0.0.1', '查看权限列表', '2020-10-21 14:55:08', '3');
INSERT INTO `oplog` VALUES ('283', '127.0.0.1', '编辑权限', '2020-10-21 14:55:15', '3');
INSERT INTO `oplog` VALUES ('284', '127.0.0.1', '查看权限列表', '2020-10-21 14:55:19', '3');
INSERT INTO `oplog` VALUES ('285', '127.0.0.1', '编辑权限', '2020-10-21 14:55:24', '3');
INSERT INTO `oplog` VALUES ('286', '127.0.0.1', '查看权限列表', '2020-10-21 14:55:26', '3');
INSERT INTO `oplog` VALUES ('287', '127.0.0.1', '编辑权限', '2020-10-21 14:55:30', '3');
INSERT INTO `oplog` VALUES ('288', '127.0.0.1', '查看权限列表', '2020-10-21 14:55:32', '3');
INSERT INTO `oplog` VALUES ('289', '127.0.0.1', '编辑权限', '2020-10-21 14:55:37', '3');
INSERT INTO `oplog` VALUES ('290', '127.0.0.1', '查看权限列表', '2020-10-21 14:55:39', '3');
INSERT INTO `oplog` VALUES ('291', '127.0.0.1', '编辑权限', '2020-10-21 14:55:44', '3');
INSERT INTO `oplog` VALUES ('292', '127.0.0.1', '查看权限列表', '2020-10-21 14:55:46', '3');
INSERT INTO `oplog` VALUES ('293', '127.0.0.1', '查看权限列表', '2020-10-21 14:55:50', '3');
INSERT INTO `oplog` VALUES ('294', '127.0.0.1', '编辑权限', '2020-10-21 14:55:55', '3');
INSERT INTO `oplog` VALUES ('295', '127.0.0.1', '查看权限列表', '2020-10-21 14:55:57', '3');
INSERT INTO `oplog` VALUES ('296', '127.0.0.1', '编辑权限', '2020-10-21 14:56:02', '3');
INSERT INTO `oplog` VALUES ('297', '127.0.0.1', '查看权限列表', '2020-10-21 14:56:05', '3');
INSERT INTO `oplog` VALUES ('298', '127.0.0.1', '编辑权限', '2020-10-21 14:56:10', '3');
INSERT INTO `oplog` VALUES ('299', '127.0.0.1', '查看权限列表', '2020-10-21 14:56:12', '3');
INSERT INTO `oplog` VALUES ('300', '127.0.0.1', '编辑权限', '2020-10-21 14:56:33', '3');
INSERT INTO `oplog` VALUES ('301', '127.0.0.1', '查看权限列表', '2020-10-21 14:56:35', '3');
INSERT INTO `oplog` VALUES ('302', '127.0.0.1', '编辑权限', '2020-10-21 14:56:40', '3');
INSERT INTO `oplog` VALUES ('303', '127.0.0.1', '查看权限列表', '2020-10-21 14:56:43', '3');
INSERT INTO `oplog` VALUES ('304', '127.0.0.1', '编辑权限', '2020-10-21 14:56:47', '3');
INSERT INTO `oplog` VALUES ('305', '127.0.0.1', '查看权限列表', '2020-10-21 14:56:49', '3');
INSERT INTO `oplog` VALUES ('306', '127.0.0.1', '编辑权限', '2020-10-21 14:56:55', '3');
INSERT INTO `oplog` VALUES ('307', '127.0.0.1', '查看权限列表', '2020-10-21 14:56:57', '3');
INSERT INTO `oplog` VALUES ('308', '127.0.0.1', '编辑权限', '2020-10-21 14:57:06', '3');
INSERT INTO `oplog` VALUES ('309', '127.0.0.1', '查看权限列表', '2020-10-21 14:57:11', '3');
INSERT INTO `oplog` VALUES ('310', '127.0.0.1', '编辑权限', '2020-10-21 14:57:26', '3');
INSERT INTO `oplog` VALUES ('311', '127.0.0.1', '查看权限列表', '2020-10-21 14:57:28', '3');
INSERT INTO `oplog` VALUES ('312', '127.0.0.1', '编辑权限', '2020-10-21 14:57:32', '3');
INSERT INTO `oplog` VALUES ('313', '127.0.0.1', '查看权限列表', '2020-10-21 14:57:33', '3');
INSERT INTO `oplog` VALUES ('314', '127.0.0.1', '查看权限列表', '2020-10-21 14:57:38', '3');
INSERT INTO `oplog` VALUES ('315', '127.0.0.1', '编辑权限', '2020-10-21 14:57:42', '3');
INSERT INTO `oplog` VALUES ('316', '127.0.0.1', '查看权限列表', '2020-10-21 14:57:45', '3');
INSERT INTO `oplog` VALUES ('317', '127.0.0.1', '编辑权限', '2020-10-21 14:57:53', '3');
INSERT INTO `oplog` VALUES ('318', '127.0.0.1', '查看权限列表', '2020-10-21 14:57:57', '3');
INSERT INTO `oplog` VALUES ('319', '127.0.0.1', '查看权限列表', '2020-10-21 14:57:59', '3');
INSERT INTO `oplog` VALUES ('320', '127.0.0.1', '查看权限列表', '2020-10-21 14:58:03', '3');
INSERT INTO `oplog` VALUES ('321', '127.0.0.1', '查看权限列表', '2020-10-21 14:58:06', '3');
INSERT INTO `oplog` VALUES ('322', '127.0.0.1', '查看权限列表', '2020-10-21 14:58:07', '3');
INSERT INTO `oplog` VALUES ('323', '127.0.0.1', '查看主页', '2020-10-21 14:58:09', '3');
INSERT INTO `oplog` VALUES ('324', '127.0.0.1', '查看主页', '2020-10-21 14:58:11', '3');
INSERT INTO `oplog` VALUES ('325', '127.0.0.1', '查看主页', '2020-10-21 14:58:16', '3');
INSERT INTO `oplog` VALUES ('326', '127.0.0.1', '查看主页', '2020-10-21 14:58:19', '3');
INSERT INTO `oplog` VALUES ('327', '127.0.0.1', '查看影响因素', '2020-10-21 14:58:21', '3');
INSERT INTO `oplog` VALUES ('328', '127.0.0.1', '查看主页', '2020-10-21 14:58:27', '3');
INSERT INTO `oplog` VALUES ('329', '127.0.0.1', '查看主页', '2020-10-21 14:58:28', '3');
INSERT INTO `oplog` VALUES ('330', '127.0.0.1', '查看主页', '2020-10-21 14:58:30', '3');
INSERT INTO `oplog` VALUES ('331', '127.0.0.1', '查看影响因素', '2020-10-21 14:58:33', '3');
INSERT INTO `oplog` VALUES ('332', '127.0.0.1', '温度可视化', '2020-10-21 14:58:35', '3');
INSERT INTO `oplog` VALUES ('333', '127.0.0.1', '温度可视化', '2020-10-21 15:00:06', '3');
INSERT INTO `oplog` VALUES ('334', '127.0.0.1', '温度可视化', '2020-10-21 15:00:07', '3');
INSERT INTO `oplog` VALUES ('335', '127.0.0.1', '温度可视化', '2020-10-21 15:00:08', '3');
INSERT INTO `oplog` VALUES ('336', '127.0.0.1', '查看主页', '2020-10-21 15:00:17', '3');
INSERT INTO `oplog` VALUES ('337', '127.0.0.1', '查看主页', '2020-10-21 15:00:30', '3');
INSERT INTO `oplog` VALUES ('338', '127.0.0.1', '查看影响因素', '2020-10-21 15:00:31', '3');
INSERT INTO `oplog` VALUES ('339', '127.0.0.1', '进行报警控制', '2020-10-21 15:00:32', '3');
INSERT INTO `oplog` VALUES ('340', '127.0.0.1', '进行人工干预', '2020-10-21 15:00:34', '3');
INSERT INTO `oplog` VALUES ('341', '127.0.0.1', '温度可视化', '2020-10-21 15:00:37', '3');
INSERT INTO `oplog` VALUES ('342', '127.0.0.1', '湿度可视化', '2020-10-21 15:00:38', '3');
INSERT INTO `oplog` VALUES ('343', '127.0.0.1', '查询数据情况', '2020-10-21 15:00:39', '3');
INSERT INTO `oplog` VALUES ('344', '127.0.0.1', '查看统计情况', '2020-10-21 15:00:40', '3');
INSERT INTO `oplog` VALUES ('345', '127.0.0.1', '查看管理员列表', '2020-10-21 15:00:43', '3');
INSERT INTO `oplog` VALUES ('346', '127.0.0.1', '查看权限列表', '2020-10-21 15:00:45', '3');
INSERT INTO `oplog` VALUES ('347', '127.0.0.1', '查看角色列表', '2020-10-21 15:00:48', '3');
INSERT INTO `oplog` VALUES ('348', '127.0.0.1', '查看主页', '2020-10-21 15:00:54', '3');
INSERT INTO `oplog` VALUES ('349', '127.0.0.1', '查看主页', '2020-10-21 15:01:12', '3');
INSERT INTO `oplog` VALUES ('350', '127.0.0.1', '查看主页', '2020-10-21 15:03:39', '3');
INSERT INTO `oplog` VALUES ('351', '127.0.0.1', '查看主页', '2020-10-21 15:03:50', '3');
INSERT INTO `oplog` VALUES ('352', '127.0.0.1', '查看影响因素', '2020-10-21 15:03:52', '3');
INSERT INTO `oplog` VALUES ('353', '127.0.0.1', '查看影响因素', '2020-10-21 15:12:20', '3');
INSERT INTO `oplog` VALUES ('354', '127.0.0.1', '查看影响因素', '2020-10-21 15:12:21', '3');
INSERT INTO `oplog` VALUES ('355', '127.0.0.1', '查看主页', '2020-10-21 15:12:23', '3');
INSERT INTO `oplog` VALUES ('356', '127.0.0.1', '查看主页', '2020-10-21 15:12:27', '3');
INSERT INTO `oplog` VALUES ('357', '127.0.0.1', '查看主页', '2020-10-21 15:12:29', '3');
INSERT INTO `oplog` VALUES ('358', '127.0.0.1', '查看主页', '2020-10-21 15:12:30', '3');
INSERT INTO `oplog` VALUES ('359', '127.0.0.1', '查看影响因素', '2020-10-21 15:13:00', '3');
INSERT INTO `oplog` VALUES ('360', '127.0.0.1', '进行报警控制', '2020-10-21 15:13:02', '3');
INSERT INTO `oplog` VALUES ('361', '127.0.0.1', '进行人工干预', '2020-10-21 15:13:05', '3');
INSERT INTO `oplog` VALUES ('362', '127.0.0.1', '查询数据情况', '2020-10-21 15:13:07', '3');
INSERT INTO `oplog` VALUES ('363', '127.0.0.1', '查看统计情况', '2020-10-21 15:13:11', '3');
INSERT INTO `oplog` VALUES ('364', '127.0.0.1', '查看管理员列表', '2020-10-21 15:13:17', '3');
INSERT INTO `oplog` VALUES ('365', '127.0.0.1', '温度可视化', '2020-10-21 15:13:19', '3');
INSERT INTO `oplog` VALUES ('366', '127.0.0.1', '湿度可视化', '2020-10-21 15:13:22', '3');
INSERT INTO `oplog` VALUES ('367', '127.0.0.1', '查看影响因素', '2020-10-21 15:13:23', '3');
INSERT INTO `oplog` VALUES ('368', '127.0.0.1', '进行人工干预', '2020-10-21 15:13:25', '3');
INSERT INTO `oplog` VALUES ('369', '127.0.0.1', '查看权限列表', '2020-10-21 15:13:28', '3');
INSERT INTO `oplog` VALUES ('370', '127.0.0.1', '查看角色列表', '2020-10-21 15:13:31', '3');
INSERT INTO `oplog` VALUES ('371', '127.0.0.1', '查看角色列表', '2020-10-21 15:13:44', '3');
INSERT INTO `oplog` VALUES ('372', '127.0.0.1', '查看权限列表', '2020-10-21 15:13:47', '3');
INSERT INTO `oplog` VALUES ('373', '127.0.0.1', '查看管理员列表', '2020-10-21 15:13:51', '3');
INSERT INTO `oplog` VALUES ('374', '127.0.0.1', '查询数据情况', '2020-10-21 15:13:53', '3');
INSERT INTO `oplog` VALUES ('375', '127.0.0.1', '查看统计情况', '2020-10-21 15:13:55', '3');
INSERT INTO `oplog` VALUES ('376', '127.0.0.1', '温度可视化', '2020-10-21 15:13:58', '3');
INSERT INTO `oplog` VALUES ('377', '127.0.0.1', '湿度可视化', '2020-10-21 15:14:02', '3');
INSERT INTO `oplog` VALUES ('378', '127.0.0.1', '查看影响因素', '2020-10-21 15:14:05', '3');
INSERT INTO `oplog` VALUES ('379', '127.0.0.1', '进行报警控制', '2020-10-21 15:14:07', '3');
INSERT INTO `oplog` VALUES ('380', '127.0.0.1', '进行人工干预', '2020-10-21 15:14:13', '3');
INSERT INTO `oplog` VALUES ('381', '127.0.0.1', '查看主页', '2020-10-21 15:14:14', '3');
INSERT INTO `oplog` VALUES ('382', '127.0.0.1', '查看主页', '2020-10-21 15:14:52', '3');
INSERT INTO `oplog` VALUES ('383', '127.0.0.1', '查看主页', '2020-10-21 15:14:53', '3');
INSERT INTO `oplog` VALUES ('384', '127.0.0.1', '查看主页', '2020-10-21 15:14:53', '3');
INSERT INTO `oplog` VALUES ('385', '127.0.0.1', '查看主页', '2020-10-21 15:14:54', '3');
INSERT INTO `oplog` VALUES ('386', '127.0.0.1', '查看主页', '2020-10-21 15:14:54', '3');
INSERT INTO `oplog` VALUES ('387', '127.0.0.1', '查看主页', '2020-10-21 15:14:54', '3');
INSERT INTO `oplog` VALUES ('388', '127.0.0.1', '查看主页', '2020-10-21 15:14:54', '3');
INSERT INTO `oplog` VALUES ('389', '127.0.0.1', '查看主页', '2020-10-21 15:14:54', '3');
INSERT INTO `oplog` VALUES ('390', '127.0.0.1', '查看主页', '2020-10-21 15:14:55', '3');
INSERT INTO `oplog` VALUES ('391', '127.0.0.1', '查看主页', '2020-10-21 15:14:55', '3');
INSERT INTO `oplog` VALUES ('392', '127.0.0.1', '查看主页', '2020-10-21 15:14:55', '3');
INSERT INTO `oplog` VALUES ('393', '127.0.0.1', '查看主页', '2020-10-21 15:16:06', '3');
INSERT INTO `oplog` VALUES ('394', '127.0.0.1', '查看主页', '2020-10-21 15:16:57', '3');
INSERT INTO `oplog` VALUES ('395', '127.0.0.1', '查看主页', '2020-10-21 15:16:58', '3');
INSERT INTO `oplog` VALUES ('396', '127.0.0.1', '查看影响因素', '2020-10-21 15:16:59', '3');
INSERT INTO `oplog` VALUES ('397', '127.0.0.1', '进行报警控制', '2020-10-21 15:17:01', '3');
INSERT INTO `oplog` VALUES ('398', '127.0.0.1', '进行人工干预', '2020-10-21 15:17:03', '3');
INSERT INTO `oplog` VALUES ('399', '127.0.0.1', '温度可视化', '2020-10-21 15:17:04', '3');
INSERT INTO `oplog` VALUES ('400', '127.0.0.1', '湿度可视化', '2020-10-21 15:17:05', '3');
INSERT INTO `oplog` VALUES ('401', '127.0.0.1', '查询数据情况', '2020-10-21 15:17:06', '3');
INSERT INTO `oplog` VALUES ('402', '127.0.0.1', '查看统计情况', '2020-10-21 15:17:07', '3');
INSERT INTO `oplog` VALUES ('403', '127.0.0.1', '查看管理员列表', '2020-10-21 15:17:09', '3');
INSERT INTO `oplog` VALUES ('404', '127.0.0.1', '查看主页', '2020-10-21 17:34:09', '3');
INSERT INTO `oplog` VALUES ('405', '127.0.0.1', '查看主页', '2020-10-21 18:46:17', '3');
INSERT INTO `oplog` VALUES ('406', '127.0.0.1', '查看主页', '2020-10-21 19:28:52', '3');
INSERT INTO `oplog` VALUES ('407', '127.0.0.1', '查看主页', '2020-10-21 21:23:04', '3');
INSERT INTO `oplog` VALUES ('408', '127.0.0.1', '查看主页', '2020-10-21 21:23:06', '3');
INSERT INTO `oplog` VALUES ('409', '127.0.0.1', '查看影响因素', '2020-10-21 21:23:08', '3');
INSERT INTO `oplog` VALUES ('410', '127.0.0.1', '进行报警控制', '2020-10-21 21:23:09', '3');
INSERT INTO `oplog` VALUES ('411', '127.0.0.1', '进行人工干预', '2020-10-21 21:23:10', '3');
INSERT INTO `oplog` VALUES ('412', '127.0.0.1', '温度可视化', '2020-10-21 21:23:12', '3');
INSERT INTO `oplog` VALUES ('413', '127.0.0.1', '湿度可视化', '2020-10-21 21:23:13', '3');
INSERT INTO `oplog` VALUES ('414', '127.0.0.1', '查询数据情况', '2020-10-21 21:23:19', '3');
INSERT INTO `oplog` VALUES ('415', '127.0.0.1', '查看统计情况', '2020-10-21 21:23:20', '3');
INSERT INTO `oplog` VALUES ('416', '127.0.0.1', '查看主页', '2020-10-21 21:27:30', '3');
INSERT INTO `oplog` VALUES ('417', '127.0.0.1', '温度可视化', '2020-10-21 21:27:33', '3');
INSERT INTO `oplog` VALUES ('418', '127.0.0.1', '查看权限列表', '2020-10-21 21:27:48', '3');
INSERT INTO `oplog` VALUES ('419', '127.0.0.1', '查看权限列表', '2020-10-21 21:29:07', '3');
INSERT INTO `oplog` VALUES ('420', '127.0.0.1', '查看权限列表', '2020-10-21 21:29:26', '3');
INSERT INTO `oplog` VALUES ('421', '127.0.0.1', '查看权限列表', '2020-10-21 21:29:27', '3');
INSERT INTO `oplog` VALUES ('422', '127.0.0.1', '查看权限列表', '2020-10-21 22:27:28', '3');
INSERT INTO `oplog` VALUES ('423', '127.0.0.1', '查看主页', '2020-10-21 22:28:35', '3');
INSERT INTO `oplog` VALUES ('424', '127.0.0.1', '查看主页', '2020-10-21 22:28:46', '3');
INSERT INTO `oplog` VALUES ('425', '127.0.0.1', '查看影响因素', '2020-10-21 22:28:47', '3');
INSERT INTO `oplog` VALUES ('426', '127.0.0.1', '进行报警控制', '2020-10-21 22:28:49', '3');
INSERT INTO `oplog` VALUES ('427', '127.0.0.1', '进行人工干预', '2020-10-21 22:28:51', '3');
INSERT INTO `oplog` VALUES ('428', '127.0.0.1', '温度可视化', '2020-10-21 22:28:52', '3');
INSERT INTO `oplog` VALUES ('429', '127.0.0.1', '湿度可视化', '2020-10-21 22:28:53', '3');
INSERT INTO `oplog` VALUES ('430', '127.0.0.1', '查询数据情况', '2020-10-21 22:28:54', '3');
INSERT INTO `oplog` VALUES ('431', '127.0.0.1', '查看统计情况', '2020-10-21 22:28:56', '3');
INSERT INTO `oplog` VALUES ('432', '127.0.0.1', '进行人工干预', '2020-10-21 22:53:56', '3');
INSERT INTO `oplog` VALUES ('433', '127.0.0.1', '进行人工干预', '2020-10-21 22:54:09', '3');
INSERT INTO `oplog` VALUES ('434', '127.0.0.1', '查看角色列表', '2020-10-21 22:56:07', '3');
INSERT INTO `oplog` VALUES ('435', '127.0.0.1', '查看影响因素', '2020-10-21 22:57:42', '3');
INSERT INTO `oplog` VALUES ('436', '127.0.0.1', '查看影响因素', '2020-10-21 22:58:10', '3');
INSERT INTO `oplog` VALUES ('437', '127.0.0.1', '查看影响因素', '2020-10-21 22:58:59', '3');
INSERT INTO `oplog` VALUES ('438', '127.0.0.1', '查看影响因素', '2020-10-21 22:59:01', '3');
INSERT INTO `oplog` VALUES ('439', '127.0.0.1', '查看影响因素', '2020-10-21 22:59:41', '3');
INSERT INTO `oplog` VALUES ('440', '127.0.0.1', '查看影响因素', '2020-10-21 22:59:41', '3');
INSERT INTO `oplog` VALUES ('441', '127.0.0.1', '查看影响因素', '2020-10-21 22:59:42', '3');
INSERT INTO `oplog` VALUES ('442', '127.0.0.1', '查看影响因素', '2020-10-21 22:59:42', '3');
INSERT INTO `oplog` VALUES ('443', '127.0.0.1', '查看影响因素', '2020-10-21 23:00:36', '3');
INSERT INTO `oplog` VALUES ('444', '127.0.0.1', '查看影响因素', '2020-10-21 23:00:36', '3');
INSERT INTO `oplog` VALUES ('445', '127.0.0.1', '查看影响因素', '2020-10-21 23:01:15', '3');
INSERT INTO `oplog` VALUES ('446', '127.0.0.1', '查看影响因素', '2020-10-21 23:01:16', '3');
INSERT INTO `oplog` VALUES ('447', '127.0.0.1', '查看影响因素', '2020-10-21 23:01:29', '3');
INSERT INTO `oplog` VALUES ('448', '127.0.0.1', '查看影响因素', '2020-10-21 23:01:29', '3');
INSERT INTO `oplog` VALUES ('449', '127.0.0.1', '查看影响因素', '2020-10-21 23:01:30', '3');
INSERT INTO `oplog` VALUES ('450', '127.0.0.1', '查看影响因素', '2020-10-21 23:01:30', '3');
INSERT INTO `oplog` VALUES ('451', '127.0.0.1', '查看影响因素', '2020-10-21 23:01:30', '3');
INSERT INTO `oplog` VALUES ('452', '127.0.0.1', '查看影响因素', '2020-10-21 23:01:31', '3');
INSERT INTO `oplog` VALUES ('453', '127.0.0.1', '查看影响因素', '2020-10-21 23:01:31', '3');
INSERT INTO `oplog` VALUES ('454', '127.0.0.1', '查看主页', '2020-10-21 23:01:36', '3');
INSERT INTO `oplog` VALUES ('455', '127.0.0.1', '查看影响因素', '2020-10-21 23:01:39', '3');
INSERT INTO `oplog` VALUES ('456', '127.0.0.1', '查看角色列表', '2020-10-21 23:03:58', '3');
INSERT INTO `oplog` VALUES ('457', '127.0.0.1', '查看角色列表', '2020-10-21 23:09:26', '3');
INSERT INTO `oplog` VALUES ('458', '127.0.0.1', '查看影响因素', '2020-10-21 23:09:31', '3');
INSERT INTO `oplog` VALUES ('459', '127.0.0.1', '查看影响因素', '2020-10-21 23:09:33', '3');
INSERT INTO `oplog` VALUES ('460', '127.0.0.1', '查看影响因素', '2020-10-21 23:10:23', '3');
INSERT INTO `oplog` VALUES ('461', '127.0.0.1', '查看影响因素', '2020-10-21 23:11:19', '3');
INSERT INTO `oplog` VALUES ('462', '127.0.0.1', '查看影响因素', '2020-10-21 23:11:44', '3');
INSERT INTO `oplog` VALUES ('463', '127.0.0.1', '查看影响因素', '2020-10-21 23:11:46', '3');
INSERT INTO `oplog` VALUES ('464', '127.0.0.1', '查看影响因素', '2020-10-21 23:11:46', '3');
INSERT INTO `oplog` VALUES ('465', '127.0.0.1', '查看影响因素', '2020-10-21 23:11:47', '3');
INSERT INTO `oplog` VALUES ('466', '127.0.0.1', '查看影响因素', '2020-10-21 23:11:47', '3');
INSERT INTO `oplog` VALUES ('467', '127.0.0.1', '查看影响因素', '2020-10-21 23:11:47', '3');
INSERT INTO `oplog` VALUES ('468', '127.0.0.1', '查看影响因素', '2020-10-21 23:11:47', '3');
INSERT INTO `oplog` VALUES ('469', '127.0.0.1', '查看影响因素', '2020-10-21 23:11:47', '3');
INSERT INTO `oplog` VALUES ('470', '127.0.0.1', '查看影响因素', '2020-10-21 23:12:00', '3');
INSERT INTO `oplog` VALUES ('471', '127.0.0.1', '查看影响因素', '2020-10-21 23:12:00', '3');
INSERT INTO `oplog` VALUES ('472', '127.0.0.1', '查看影响因素', '2020-10-21 23:12:01', '3');
INSERT INTO `oplog` VALUES ('473', '127.0.0.1', '查看影响因素', '2020-10-21 23:12:01', '3');
INSERT INTO `oplog` VALUES ('474', '127.0.0.1', '查看影响因素', '2020-10-21 23:12:01', '3');
INSERT INTO `oplog` VALUES ('475', '127.0.0.1', '查看影响因素', '2020-10-21 23:12:01', '3');
INSERT INTO `oplog` VALUES ('476', '127.0.0.1', '查看影响因素', '2020-10-21 23:12:02', '3');
INSERT INTO `oplog` VALUES ('477', '127.0.0.1', '查看影响因素', '2020-10-21 23:12:02', '3');
INSERT INTO `oplog` VALUES ('478', '127.0.0.1', '查看影响因素', '2020-10-21 23:12:22', '3');
INSERT INTO `oplog` VALUES ('479', '127.0.0.1', '查看影响因素', '2020-10-21 23:12:22', '3');
INSERT INTO `oplog` VALUES ('480', '127.0.0.1', '查看影响因素', '2020-10-21 23:12:22', '3');
INSERT INTO `oplog` VALUES ('481', '127.0.0.1', '查看影响因素', '2020-10-21 23:12:23', '3');
INSERT INTO `oplog` VALUES ('482', '127.0.0.1', '查看影响因素', '2020-10-21 23:12:31', '3');
INSERT INTO `oplog` VALUES ('483', '127.0.0.1', '查看影响因素', '2020-10-21 23:12:32', '3');
INSERT INTO `oplog` VALUES ('484', '127.0.0.1', '查看影响因素', '2020-10-21 23:12:32', '3');
INSERT INTO `oplog` VALUES ('485', '127.0.0.1', '查看影响因素', '2020-10-21 23:12:32', '3');
INSERT INTO `oplog` VALUES ('486', '127.0.0.1', '查看影响因素', '2020-10-21 23:12:32', '3');
INSERT INTO `oplog` VALUES ('487', '127.0.0.1', '查看影响因素', '2020-10-21 23:12:32', '3');
INSERT INTO `oplog` VALUES ('488', '127.0.0.1', '查看影响因素', '2020-10-21 23:12:33', '3');
INSERT INTO `oplog` VALUES ('489', '127.0.0.1', '查看影响因素', '2020-10-21 23:12:33', '3');
INSERT INTO `oplog` VALUES ('490', '127.0.0.1', '查看影响因素', '2020-10-21 23:12:33', '3');
INSERT INTO `oplog` VALUES ('491', '127.0.0.1', '查看影响因素', '2020-10-21 23:12:34', '3');
INSERT INTO `oplog` VALUES ('492', '127.0.0.1', '查看影响因素', '2020-10-21 23:12:34', '3');
INSERT INTO `oplog` VALUES ('493', '127.0.0.1', '查看影响因素', '2020-10-21 23:12:47', '3');
INSERT INTO `oplog` VALUES ('494', '127.0.0.1', '查看影响因素', '2020-10-21 23:13:02', '3');
INSERT INTO `oplog` VALUES ('495', '127.0.0.1', '查看影响因素', '2020-10-21 23:13:02', '3');
INSERT INTO `oplog` VALUES ('496', '127.0.0.1', '查看影响因素', '2020-10-21 23:13:03', '3');
INSERT INTO `oplog` VALUES ('497', '127.0.0.1', '查看影响因素', '2020-10-21 23:13:03', '3');
INSERT INTO `oplog` VALUES ('498', '127.0.0.1', '查看影响因素', '2020-10-21 23:13:03', '3');
INSERT INTO `oplog` VALUES ('499', '127.0.0.1', '查看影响因素', '2020-10-21 23:13:04', '3');
INSERT INTO `oplog` VALUES ('500', '127.0.0.1', '查看影响因素', '2020-10-21 23:13:04', '3');
INSERT INTO `oplog` VALUES ('501', '127.0.0.1', '查看影响因素', '2020-10-21 23:13:04', '3');
INSERT INTO `oplog` VALUES ('502', '127.0.0.1', '查看影响因素', '2020-10-21 23:13:05', '3');
INSERT INTO `oplog` VALUES ('503', '127.0.0.1', '查看影响因素', '2020-10-21 23:13:05', '3');
INSERT INTO `oplog` VALUES ('504', '127.0.0.1', '查看影响因素', '2020-10-21 23:13:05', '3');
INSERT INTO `oplog` VALUES ('505', '127.0.0.1', '查看权限列表', '2020-10-21 23:14:55', '3');
INSERT INTO `oplog` VALUES ('506', '127.0.0.1', '查看角色列表', '2020-10-21 23:15:03', '3');
INSERT INTO `oplog` VALUES ('507', '127.0.0.1', '查看影响因素', '2020-10-21 23:15:16', '3');

-- ----------------------------
-- Table structure for qs
-- ----------------------------
DROP TABLE IF EXISTS `qs`;
CREATE TABLE `qs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `wd` int(11) DEFAULT NULL,
  `sd` int(11) DEFAULT NULL,
  `qssc` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of qs
-- ----------------------------

-- ----------------------------
-- Table structure for qs_info
-- ----------------------------
DROP TABLE IF EXISTS `qs_info`;
CREATE TABLE `qs_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `qs_bch` int(11) DEFAULT NULL,
  `qs_pch` int(11) DEFAULT NULL,
  `qs_pph` int(11) DEFAULT NULL,
  `qs_czh` int(11) DEFAULT NULL,
  `qs_pfh` int(11) DEFAULT NULL,
  `qs_mkh` int(11) DEFAULT NULL,
  `qs_product_start_time` datetime DEFAULT NULL,
  `qs_product_end_time` datetime DEFAULT NULL,
  `qs_zqyl` int(11) DEFAULT NULL,
  `qs_yskqyl` int(11) DEFAULT NULL,
  `qs_syl` int(11) DEFAULT NULL,
  `qs_rfwd` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_qs_info_qs_product_end_time` (`qs_product_end_time`),
  KEY `ix_qs_info_qs_product_start_time` (`qs_product_start_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of qs_info
-- ----------------------------

-- ----------------------------
-- Table structure for rg_control
-- ----------------------------
DROP TABLE IF EXISTS `rg_control`;
CREATE TABLE `rg_control` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rg_ljjsl` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of rg_control
-- ----------------------------

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  `auths` varchar(600) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `ix_role_addtime` (`addtime`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of role
-- ----------------------------
INSERT INTO `role` VALUES ('3', '普通管理员', '2020-07-21 13:29:33', '12,13,14,15,16,17,18,19,20,23');
INSERT INTO `role` VALUES ('4', '超级管理员', '2020-07-21 13:30:51', '12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33');

-- ----------------------------
-- Table structure for sshc
-- ----------------------------
DROP TABLE IF EXISTS `sshc`;
CREATE TABLE `sshc` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rksf` int(11) DEFAULT NULL,
  `wd` int(11) DEFAULT NULL,
  `sd` int(11) DEFAULT NULL,
  `cksf` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sshc
-- ----------------------------

-- ----------------------------
-- Table structure for sshc_info
-- ----------------------------
DROP TABLE IF EXISTS `sshc_info`;
CREATE TABLE `sshc_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sshc_rksf` int(11) DEFAULT NULL,
  `sshc_wd` int(11) DEFAULT NULL,
  `sshc_sd` int(11) DEFAULT NULL,
  `sshc_ljjsl` int(11) DEFAULT NULL,
  `sshc_cksf` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sshc_info
-- ----------------------------

-- ----------------------------
-- Table structure for sssf
-- ----------------------------
DROP TABLE IF EXISTS `sssf`;
CREATE TABLE `sssf` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mean` int(11) DEFAULT NULL,
  `bp` int(11) DEFAULT NULL,
  `hgl` int(11) DEFAULT NULL,
  `cpk` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sssf
-- ----------------------------

-- ----------------------------
-- Table structure for sssf_control
-- ----------------------------
DROP TABLE IF EXISTS `sssf_control`;
CREATE TABLE `sssf_control` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ycy_time` int(11) DEFAULT NULL,
  `sshc_id` int(11) DEFAULT NULL,
  `yjl_id` int(11) DEFAULT NULL,
  `cy_id` int(11) DEFAULT NULL,
  `qs_id` int(11) DEFAULT NULL,
  `sssf_id` int(11) DEFAULT NULL,
  `bj_control_id` int(11) DEFAULT NULL,
  `rg_control_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `sshc_id` (`sshc_id`),
  KEY `yjl_id` (`yjl_id`),
  KEY `cy_id` (`cy_id`),
  KEY `qs_id` (`qs_id`),
  KEY `sssf_id` (`sssf_id`),
  KEY `bj_control_id` (`bj_control_id`),
  KEY `rg_control_id` (`rg_control_id`),
  CONSTRAINT `sssf_control_ibfk_1` FOREIGN KEY (`sshc_id`) REFERENCES `sshc` (`id`),
  CONSTRAINT `sssf_control_ibfk_2` FOREIGN KEY (`yjl_id`) REFERENCES `yjl` (`id`),
  CONSTRAINT `sssf_control_ibfk_3` FOREIGN KEY (`cy_id`) REFERENCES `cy` (`id`),
  CONSTRAINT `sssf_control_ibfk_4` FOREIGN KEY (`qs_id`) REFERENCES `qs` (`id`),
  CONSTRAINT `sssf_control_ibfk_5` FOREIGN KEY (`sssf_id`) REFERENCES `sssf` (`id`),
  CONSTRAINT `sssf_control_ibfk_6` FOREIGN KEY (`bj_control_id`) REFERENCES `bj_control` (`id`),
  CONSTRAINT `sssf_control_ibfk_7` FOREIGN KEY (`rg_control_id`) REFERENCES `rg_control` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sssf_control
-- ----------------------------

-- ----------------------------
-- Table structure for tjcx
-- ----------------------------
DROP TABLE IF EXISTS `tjcx`;
CREATE TABLE `tjcx` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sshc_info_id` int(11) DEFAULT NULL,
  `yjl_info_id` int(11) DEFAULT NULL,
  `cy_info_id` int(11) DEFAULT NULL,
  `qs_info_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `sshc_info_id` (`sshc_info_id`),
  KEY `yjl_info_id` (`yjl_info_id`),
  KEY `cy_info_id` (`cy_info_id`),
  KEY `qs_info_id` (`qs_info_id`),
  CONSTRAINT `tjcx_ibfk_1` FOREIGN KEY (`sshc_info_id`) REFERENCES `sshc_info` (`id`),
  CONSTRAINT `tjcx_ibfk_2` FOREIGN KEY (`yjl_info_id`) REFERENCES `yjl_info` (`id`),
  CONSTRAINT `tjcx_ibfk_3` FOREIGN KEY (`cy_info_id`) REFERENCES `cy_info` (`id`),
  CONSTRAINT `tjcx_ibfk_4` FOREIGN KEY (`qs_info_id`) REFERENCES `qs_info` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tjcx
-- ----------------------------

-- ----------------------------
-- Table structure for yc
-- ----------------------------
DROP TABLE IF EXISTS `yc`;
CREATE TABLE `yc` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `yc_ljjsl` int(11) DEFAULT NULL,
  `yc_sssfup` int(11) DEFAULT NULL,
  `yc_sssfdown` int(11) DEFAULT NULL,
  `yjl_id` int(11) DEFAULT NULL,
  `cy_id` int(11) DEFAULT NULL,
  `qs_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `yjl_id` (`yjl_id`),
  KEY `cy_id` (`cy_id`),
  KEY `qs_id` (`qs_id`),
  CONSTRAINT `yc_ibfk_1` FOREIGN KEY (`yjl_id`) REFERENCES `yjl` (`id`),
  CONSTRAINT `yc_ibfk_2` FOREIGN KEY (`cy_id`) REFERENCES `cy` (`id`),
  CONSTRAINT `yc_ibfk_3` FOREIGN KEY (`qs_id`) REFERENCES `qs` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of yc
-- ----------------------------

-- ----------------------------
-- Table structure for yjl
-- ----------------------------
DROP TABLE IF EXISTS `yjl`;
CREATE TABLE `yjl` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rksf` int(11) DEFAULT NULL,
  `cljzl` int(11) DEFAULT NULL,
  `cssll` int(11) DEFAULT NULL,
  `lywd` int(11) DEFAULT NULL,
  `ljjsl` int(11) DEFAULT NULL,
  `ssjsl` int(11) DEFAULT NULL,
  `wd` int(11) DEFAULT NULL,
  `sd` int(11) DEFAULT NULL,
  `ckwd` int(11) DEFAULT NULL,
  `cksf` int(11) DEFAULT NULL,
  `glsc` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of yjl
-- ----------------------------

-- ----------------------------
-- Table structure for yjl_info
-- ----------------------------
DROP TABLE IF EXISTS `yjl_info`;
CREATE TABLE `yjl_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ykl_bch` int(11) DEFAULT NULL,
  `ykl_pch` int(11) DEFAULT NULL,
  `ykl_pph` int(11) DEFAULT NULL,
  `ykl_czh` int(11) DEFAULT NULL,
  `ykl_pfh` int(11) DEFAULT NULL,
  `ykl_mkh` int(11) DEFAULT NULL,
  `ykl_product_start_time` datetime DEFAULT NULL,
  `ykl_product_end_time` datetime DEFAULT NULL,
  `ykl_zqyl` int(11) DEFAULT NULL,
  `ykl_yskqyl` int(11) DEFAULT NULL,
  `ykl_syl` int(11) DEFAULT NULL,
  `ykl_rksf` int(11) DEFAULT NULL,
  `ykl_pckd` int(11) DEFAULT NULL,
  `ykl_pcfl` int(11) DEFAULT NULL,
  `ykl_rffl` int(11) DEFAULT NULL,
  `ykl_bczqfmkd` int(11) DEFAULT NULL,
  `ykl_jyfhzqyl` int(11) DEFAULT NULL,
  `ykl_lywd` int(11) DEFAULT NULL,
  `ykl_jlbsssd` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_yjl_info_ykl_product_end_time` (`ykl_product_end_time`),
  KEY `ix_yjl_info_ykl_product_start_time` (`ykl_product_start_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of yjl_info
-- ----------------------------
