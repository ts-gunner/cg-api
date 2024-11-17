DROP TABLE IF EXISTS `user_profile`;
CREATE TABLE IF NOT EXISTS `user_profile` (
    `id` int not null PRIMARY KEY AUTO_INCREMENT,
    openid VARCHAR(100) NOT NULL COMMENT '微信提供当前小程序的openid，标识个人id',
    unionid VARCHAR(100) NULL COMMENT '微信提供多平台的openid，标识个人id',
    nickname VARCHAR(100)  COMMENT '用户昵称',
    phone_number VARCHAR(50)  COMMENT '手机号码',
    avatar_url TEXT COMMENT '头像地址',
    remark TEXT COMMENT '备注',
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE (openid)
) default charset=utf8mb4 COMMENT '用户信息';

DROP TABLE IF EXISTS `user_role`;
CREATE TABLE IF NOT EXISTS `user_role` (
    role_id VARCHAR(100) PRIMARY KEY NOT NULL,
    role_name VARCHAR(50) NOT NULL
) default charset=utf8mb4 COMMENT '用户角色';
INSERT INTO `user_role`(`role_id`, `role_name`) VALUES ("admin", "超级管理员");
INSERT INTO `user_role`(`role_id`, `role_name`) VALUES ("monitor", "监督员");
INSERT INTO `user_role`(`role_id`, `role_name`) VALUES ("monkey", "小牛马");

DROP TABLE IF EXISTS `user_role_map`;
CREATE TABLE IF NOT EXISTS `user_role_map` (
    `id` int not null PRIMARY KEY AUTO_INCREMENT,
    role_id VARCHAR(100) NOT NULL,
    user_id VARCHAR(100) NOT NULL,
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) default charset=utf8mb4 COMMENT '用户-角色-映射表';



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
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) default charset=utf8mb4 COMMENT '用户-组-映射表';

DROP TABLE IF EXISTS `task_info`;
CREATE TABLE IF NOT EXISTS `task_info` (
    task_id VARCHAR(100) PRIMARY KEY,
    user_id VARCHAR(100),
    category VARCHAR(30) NOT NULL,
    point DECIMAL(10, 2),
    status VARCHAR(30) NOT NULL,
    content VARCHAR(255) NOT NULL,
    `attach_list` TEXT,
    `body` TEXT,
    remark VARCHAR(255),
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) default charset=utf8mb4 COMMENT '任务表';



DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
    permission_id VARCHAR(50) PRIMARY KEY NOT NULL,
    permission_name VARCHAR(50) NOT NULL,
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) default charset=utf8mb4 COMMENT '权限信息';
INSERT INTO `auth_permission`(`permission_id`, `permission_name`) VALUES ("*:*", "所有权限");
INSERT INTO `auth_permission`(`permission_id`, `permission_name`) VALUES ("task:add", "添加任务");
INSERT INTO `auth_permission`(`permission_id`, `permission_name`) VALUES ("task:audit", "审核任务");
INSERT INTO `auth_permission`(`permission_id`, `permission_name`) VALUES ("task:check", "查看workers任务");


DROP TABLE IF EXISTS `user_permission`;
CREATE TABLE IF NOT EXISTS `user_permission` (
    `id` int not null PRIMARY KEY AUTO_INCREMENT,
    permission_id VARCHAR(50) NOT NULL,
    user_id VARCHAR(100) NOT NULL,
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) default charset=utf8mb4 COMMENT '用户权限';

DROP TABLE IF EXISTS `role_permission`;
CREATE TABLE IF NOT EXISTS `role_permission` (
    `id` int not null PRIMARY KEY AUTO_INCREMENT,
    permission_id VARCHAR(50) NOT NULL,
    role_id VARCHAR(100) NOT NULL,
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) default charset=utf8mb4 COMMENT '角色权限';
INSERT INTO `role_permission`(`permission_id`, `role_id`) VALUES ("*:*", "admin");
INSERT INTO `role_permission`(`permission_id`, `role_id`) VALUES ("task:check", "monitor");
INSERT INTO `role_permission`(`permission_id`, `role_id`) VALUES ("task:add", "monkey");



DROP TABLE IF EXISTS `rewards_balance`;
CREATE TABLE IF NOT EXISTS `rewards_balance` (
    `id` int not null PRIMARY KEY AUTO_INCREMENT,
    user_id VARCHAR(100) NOT NULL,
    total_points DECIMAL(10, 2) DEFAULT 0 NOT NULL,
    used_points DECIMAL(10, 2) DEFAULT 0 NOT NULL,
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) default charset=utf8mb4 COMMENT '积分表';

DROP TABLE IF EXISTS `market_goods`;
CREATE TABLE IF NOT EXISTS `market_goods` (
    `id` int not null PRIMARY KEY AUTO_INCREMENT,
    good_id VARCHAR(100) NOT NULL,
    good_name VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    point DECIMAL(10, 2),
    display_img_path TEXT,
    remark VARCHAR(255),
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) default charset=utf8mb4 COMMENT '商品表';

DROP TABLE IF EXISTS `notification`;
CREATE TABLE IF NOT EXISTS `notification` (
    no_id VARCHAR(100) NOT NULL PRIMARY KEY,
    no_name VARCHAR(50) NOT NULL,
    notify_context TEXT,
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) default charset=utf8mb4 COMMENT '公告表';