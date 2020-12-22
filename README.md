# backend

## 启动

### 建立数据库表

如果你本地装好了数据库，那只需要配置好数据库密码，然后填入 `app/constants.py` 中的对应的变量中。

项目需要 mysql 和 mssql，mssql 是做数据采集服务器。嵌入式设备采集数据后存入已有的 mssql 数据库。
本项目通过 Mysql 来维护项目本身的数据。

测试开发时可以使用 docker，可以很方便的启动和删除一个数据库，可以看 docs 下的文档。

### 数据准备

注意，因为为了防止误修改了 mssql 数据库，如果想初始化 mssql 数据库，需要设置一个环境变量才行，放在 `.env` 或者环境变量中都可以：

为了防止误修改了 mssql 数据库！
为了防止误修改了 mssql 数据库！
为了防止误修改了 mssql 数据库！

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

我是使用的 poetry 这个工具管理依赖，你需要安装完所有的依赖，使用 poetry 或者 pip 都可，参考 `docs/依赖管理.md`。

安装好之后需要配置环境变量，创建 .env 文件，填入：

```dotenv
SECRET_KEY="自己设置一个"
PLC_PASSWORD=My.Password
MES_PASSWORD=My.Password
MYSQL_ROOT_PASSWORD=root
```

`PLC_PASSWORD` 和 `MES_PASSWORD` 是实时采集数据库的密码。
最后一个是 mysql 的数据库密码。

数据库的地址什么的可以直接先改 `app/constants.py` 里面的信息

还有一些配置在 `__init__.py` 中的 `init_config` 中。

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

    然后执行 `flask run` 就可以启动了，如果运行在生产环境，请把 `FLASK_ENV` 设置为 `production`

然后打开后端页面： <http://localhost:5000> 即可。
