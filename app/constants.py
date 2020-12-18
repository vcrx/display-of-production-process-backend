db_uri_pymssql = "mssql+pymssql://sa:My.Password@127.0.0.1:1433/{db_name}"
db_uri_pyodbc = "mssql+pyodbc://sa:My.Password@127.0.0.1:1433/{db_name}?driver=SQL+Server+Native+Client+10.0&charset=utf8"
db_uri = db_uri_pyodbc
yancao_db_uri = db_uri.format(db_name="yancao")
origin_db_uri = db_uri.format(db_name="test")
