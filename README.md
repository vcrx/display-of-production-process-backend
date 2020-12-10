# backend

## 启动
### 建立数据库表

如果你本地装了 mysql，那只需要配置好数据库密码，然后填入 `app/__init__.py` 中的 `app.config["SQLALCHEMY_DATABASE_URI"]` 中。

如果你没装 mysql，但装了 docker，可以很方便的启动和删除数据库：
#### 使用 docker
创建 `.env` 文件，里面填入：

```dotenv
MYSQL_ROOT_PASSWORD=root
```

首先启动数据库，设置好账户密码。

```bash
docker-compose up -d
```
##### 删除数据库

```bash
docker-compose down -v
```

### 数据准备

执行 `app/init_db.py` 和 `app/init_data.py` 两个文件即可初始化数据库：

```bash
python app/init_db.py
python app/init_data.py
```

即可创建好数据库。

### 启动 APP

我是使用的 poetry 这个工具管理依赖，你可以安装完所有的依赖，然后直接启动即可。


```bash
python manage.py
```

依赖在：`pyproject.toml` 这个文件 `[tool.poetry.dependencies]` 的字段下面。

然后打开后端页面： http://localhost:5000/ 即可。


## 其他信息
