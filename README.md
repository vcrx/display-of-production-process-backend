# backend

## 启动

### 依赖

参考 `docs/依赖管理.md`。

### 配置

安装好依赖之后需要配置环境变量，创建 .env 文件，填入：

```dotenv
SECRET_KEY="自己设置一个"
PLC_PASSWORD="PLC 数据库密码"
MES_PASSWORD="MES 数据库密码"
MYSQL_PASSWORD="程序数据库密码"
```

提供了一个 `.env.example`，可以改名为 `.env` 后修改里面的内容。

`PLC_PASSWORD` 和 `MES_PASSWORD` 是实时采集数据库的密码。

`MYSQL_PASSWORD` 是程序使用的的数据库密码。

数据库地址什么的可以直接先改 `app/constants.py` 里面的信息

还有一些配置在 `app/__init__.py` 中的 `init_config` 中。如：

```python
def init_config(app: Flask):
    ...
    # 是否需要从头采集 SQLServer 数据库
    app.config["SCHEDULER_COLLECTION_FROM_SCRATCH"] = False
```

#### 安装 SQLServer ODBC Driver

会遇到一个报错： `[IM002] [Microsoft][ODBC 驱动程序管理器] 未发现数据源名称并且未指定默认驱动程序 (0) (SQLDriverConnect)`

这里在 `resources/SQLServerDriver` 里面提供有两个安装包，选择对应自己系统的版本就好了。

你也可以去下载 Microsoft 的驱动 <https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server>。
但是需要在 `app/constants.py` 中把驱动程序名字改成和你下载的对应的，比如：`ODBC Driver 17 for SQL Server`。

### 建立数据库表

如果你本地装好了数据库，那只需要配置好数据库密码，然后填入 `.env` 中的对应的变量中。

项目需要 MySQL 和 mssql，mssql 是做数据采集服务器。嵌入式设备采集数据后存入已有的 mssql 数据库。
本项目通过 MySQL 来维护项目本身的数据。

注意 MySQL 字符集记得要选 `utf8`。

测试开发时可以使用 docker，可以很方便的启动和删除一个数据库，可以看 docs 下的文档。

### 数据准备

注意，因为为了防止误修改了 mssql 数据库，如果想初始化 mssql 数据库，需要设置一个环境变量才行，放在 `.env` 或者环境变量中都可以：

防止误修改 mssql 数据库！
防止误修改 mssql 数据库！
防止误修改 mssql 数据库！

```dotenv
NEED_INIT_MSSQL=True
```

执行 `init_db.py` 即可初始化程序需要的数据库：

```bash
python init_db.py
```

即可创建好数据库。

想初始化的数据，直接执行：

```bash
python init_data/init_data.py
```

### 启动 APP

两种启动方式：

1. 直接执行文件

    ```bash
    python manage.py
    ```

2. flask run

    推荐使用这种方式，创建一个 `.env` 文件，填入：

    ```dotenv
    FLASK_ENV=development
    ```

    然后执行 `flask run` 就可以启动了，如果运行在生产环境，请在 `.env` 中把 `FLASK_ENV` 设置为 `production`

然后打开后端页面： <http://localhost:5000> 即可。
