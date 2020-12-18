# backend

## 启动

### 建立数据库表

如果你本地装了 mssql，那只需要配置好数据库密码，然后填入 `app/constants.py` 中的 `db_uri` 对应的属性中。

```python
db_uri = URL(
    ...,
    password=密码填在这里
)
```

如果你没装 mssql，但装了 docker，可以很方便的启动和删除一个数据库，可以看这个文档：docs/启动 docker 测试数据库.md：

### 数据准备

执行 `init_db.py` 即可初始化程序需要的数据库：

```bash
python init_db.py
```

即可创建好数据库。

想初始化数据，直接执行：

```bash
python init_data/init_data.py
```

### 启动 APP

我是使用的 poetry 这个工具管理依赖，你可以安装完所有的依赖，然后直接启动即可。


```bash
python manage.py
```

依赖在：`pyproject.toml` 这个文件 `[tool.poetry.dependencies]` 的字段下面。

然后打开后端页面： http://localhost:5000/ 即可。
