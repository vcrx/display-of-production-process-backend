# 启动 docker 测试数据库

在 docker 中启动数据库。

以下命令都在项目根目录下执行。

## 使用 docker

再根目录下创建 `.env` 文件，里面填入：

```dotenv
MYSQL_ROOT_PASSWORD="想设置的 mysql 数据库密码"
PLC_PASSWORD="plc密码"
MES_PASSWORD="mes密码"
```

首先启动数据库，设置好账户密码。

```bash
docker-compose up -d
```

## 填充 mysql 测试数据库

想初始化 mysql 的数据，直接执行：

```bash
python init_data/init_data.py
```

## 填充 mssql 测试数据库

如果你想填充 mssql 数据库，那就要设置 `NEED_INIT_MSSQL` 环境变量。

## 删除数据库

停止数据库并删除内部数据，不想删除数据不要加 `-v`：

```bash
docker-compose down -v
```
