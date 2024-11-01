DROP TABLE IF EXISTS `user_profile`;
CREATE TABLE IF NOT EXISTS `user_profile` (
    `id` int not null PRIMARY KEY AUTO_INCREMENT,
    openid VARCHAR(100) NOT NULL COMMENT '微信提供当前小程序的openid，标识个人id',
    unionid VARCHAR(100) NULL COMMENT '微信提供多平台的openid，标识个人id',
    nickname VARCHAR(100)  COMMENT '用户昵称',
    phone_number VARCHAR(50)  COMMENT '手机号码',
    avatar_url TEXT COMMENT '头像地址',
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (openid)
) default charset=utf8mb4 COMMENT '用户信息';

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
    permission_id VARCHAR(50) PRIMARY KEY NOT NULL,
    permission_name VARCHAR(50) NOT NULL,
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP
) default charset=utf8mb4 COMMENT '权限信息';

DROP TABLE IF EXISTS `user_permission`;
CREATE TABLE IF NOT EXISTS `user_permission` (
    `id` int not null PRIMARY KEY AUTO_INCREMENT,
    permission_id VARCHAR(50) NOT NULL,
    user_id VARCHAR(100) NOT NULL,
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP
) default charset=utf8mb4 COMMENT '用户权限';

DROP TABLE IF EXISTS `role_permission`;
CREATE TABLE IF NOT EXISTS `role_permission` (
    `id` int not null PRIMARY KEY AUTO_INCREMENT,
    permission_id VARCHAR(50) NOT NULL,
    role_id VARCHAR(100) NOT NULL,
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP
) default charset=utf8mb4 COMMENT '角色权限';

DROP TABLE IF EXISTS `user_role_map`;
CREATE TABLE IF NOT EXISTS `user_role_map` (
    `id` int not null PRIMARY KEY AUTO_INCREMENT,
    role_id VARCHAR(100) NOT NULL,
    user_id VARCHAR(100) NOT NULL,
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP
) default charset=utf8mb4 COMMENT '用户-角色-映射表';


DROP TABLE IF EXISTS `user_role`;
CREATE TABLE IF NOT EXISTS `user_role` (
    role_id VARCHAR(100) PRIMARY KEY NOT NULL,
    role_name VARCHAR(50) NOT NULL
) default charset=utf8mb4 COMMENT '用户角色';
INSERT INTO `user_role`(`role_id`, `role_name`) VALUES ("admin", "超级管理员");
INSERT INTO `user_role`(`role_id`, `role_name`) VALUES ("monitor", "监督员");
INSERT INTO `user_role`(`role_id`, `role_name`) VALUES ("monkey", "小牛马");

DROP TABLE IF EXISTS `user_group`;
CREATE TABLE IF NOT EXISTS `user_group` (
    group_id VARCHAR(100) NOT NULL,
    group_name VARCHAR(50) NOT NULL
) default charset=utf8mb4 COMMENT '用户组';

DROP TABLE IF EXISTS `user_group_map`;
CREATE TABLE IF NOT EXISTS `user_group_map` (
    `id` int not null PRIMARY KEY AUTO_INCREMENT,
    group_id VARCHAR(100) NOT NULL,
    user_id VARCHAR(100) NOT NULL,
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP
) default charset=utf8mb4 COMMENT '用户-组-映射表';