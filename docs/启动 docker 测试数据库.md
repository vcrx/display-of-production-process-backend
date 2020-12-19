# 启动 docker 测试数据库

创建一个 docker 的 mysql 服务器

## 使用 docker

再根目录下创建 `.env` 文件，里面填入：

```dotenv
MYSQL_ROOT_PASSWORD=root
```

首先启动数据库，设置好账户密码。

```bash
docker-compose up -d
```

想初始化 mysql 的数据，直接执行：

```bash
python init_data/init_data.py
```

## 删除数据库

```bash
docker-compose down -v
```
