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
