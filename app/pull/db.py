from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Query


class DatabaseManagement:
    def __init__(self):
        self.engine = create_engine(
            "mssql+pymssql://sa:My.Password@127.0.0.1:1433/test"
        )  # 初始化数据库连接
        DBsession = sessionmaker(bind=self.engine)  # 创建DBsession类
        self.session = DBsession()  # 创建对象

    def create_database(self, metadata):
        metadata.create_all(self.engine)

    def query(self, target_class) -> Query:
        return self.session.query(target_class)

    def close(self):  # 关闭session
        self.session.close()

    def execute_sql(self, sql_str):  # 执行sql语句
        return self.session.execute(sql_str)
