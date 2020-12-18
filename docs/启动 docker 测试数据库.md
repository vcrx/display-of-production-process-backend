# 启动 docker 测试数据库

## 使用 docker

创建 `.env` 文件，里面填入：

```dotenv
mssql_ROOT_PASSWORD=root
```

首先启动数据库，设置好账户密码。

```bash
docker-compose up -d
```

## 删除数据库

```bash
docker-compose down -v
```
