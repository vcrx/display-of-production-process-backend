# 测试采集SQLServer中的数据

像 README 说的那样安装好 python 包环境（依赖在：`pyproject.toml` 这个文件 `[tool.poetry.dependencies]` 的字段下面。）：

1. 设置 sqlserver 数据库地址
  修改 app/constants,py 里 原始采集数据库的地址

2. 运行 test_getsqlserver.py 这个文件，有输出就表示能获取 sqlserver 里的数据。

如果你想测试一下完整的从 采集数据库 取回来放到 程序数据库中的 demo，你需要设置好程序数据库。

执行完 init_db.py 之后，直接执行 test_migrate.py ，就会发现数据已经读取成功并保存到 mysql 的实时数据表。

定时读取并转换的 demo:

test_apscheduler.py 里是一个每3秒执行一次转换的 demo，执行查看效果即可。
