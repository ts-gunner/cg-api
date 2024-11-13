# 小程序 - 成果集市后台

## 快速开始

1. 创建虚拟环境： python -m venv .venv
2. 安装依赖包： pip install -r requirements.txt
3. 配置`.env`: 根据`.env.template`配置相关环境变量



## 项目介绍

小程序： cg-market

云服务： 腾讯云centos服务器，腾讯云对象储存

python依赖包可参考哦requirements.txt

角色管理： RBAC, 一个人有多个角色，一个角色有多个权限， 一个人可以直接授权
鉴权: jwt


# 项目进度

## 2024/11/07
1. 管理员可以审核worker提交的task
2. bug: 角色只要不是monkey都是可以审核，应该只有审核权限的人才可以审核。

## 2024/11/08
1. 添加角色权限判断，utils/auth
