# backend

## 建立数据库表

创建 `.env` 文件，里面填入：

```dotenv
MYSQL_ROOT_PASSWORD=root
```

首先启动数据库，设置好账户密码。

```bash
docker-compose up -d
```

将 `app/__init__.py` 中的 `register_blueprint` 注释掉，执行 `app/init_db.py` 和 `app/init_data.py` 两个文件。
即可创建好数据库。

## 删除数据库

```bash
docker-compose down -v
```
