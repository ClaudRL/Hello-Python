是的，Python 有多个库可以让你直接在代码中调用 SQL 语句与数据库交互。以下是几个常用的库：

### 1. **SQLite (`sqlite3` 库)**
- Python 自带的 `sqlite3` 模块允许你创建、查询、修改 SQLite 数据库。
- **示例：**
    ```python
    import sqlite3

    # 连接到数据库（如果不存在则创建）
    conn = sqlite3.connect('example.db')

    # 创建游标对象
    c = conn.cursor()

    # 执行SQL语句
    c.execute('''CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
    c.execute("INSERT INTO students (name, age) VALUES ('John', 25)")

    # 提交事务
    conn.commit()

    # 查询数据
    c.execute("SELECT * FROM students")
    rows = c.fetchall()
    for row in rows:
        print(row)

    # 关闭连接
    conn.close()
    ```

### 2. **MySQL (`mysql-connector-python` 或 `PyMySQL` 库)**
- 用于与 MySQL 数据库通信，可以使用 `mysql-connector-python` 或 `PyMySQL` 等库。
- **安装：**
    ```bash
    pip install mysql-connector-python
    ```
- **示例：**
    ```python
    import mysql.connector

    # 连接到 MySQL 数据库
    conn = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="yourdatabase"
    )

    cursor = conn.cursor()

    # 执行SQL查询
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    for row in results:
        print(row)

    # 关闭连接
    conn.close()
    ```

### 3. **PostgreSQL (`psycopg2` 库)**
- 用于与 PostgreSQL 数据库进行交互的库。
- **安装：**
    ```bash
    pip install psycopg2
    ```
- **示例：**
    ```python
    import psycopg2

    # 连接到 PostgreSQL 数据库
    conn = psycopg2.connect(
        dbname="yourdbname",
        user="yourusername",
        password="yourpassword",
        host="localhost"
    )

    cursor = conn.cursor()

    # 执行SQL查询
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    for row in results:
        print(row)

    # 关闭连接
    conn.close()
    ```

### 4. **SQLAlchemy**
- `SQLAlchemy` 是一个非常流行的 ORM（对象关系映射）工具，允许你使用 SQL 查询，也允许将数据库表映射为 Python 类对象。
- **安装：**
    ```bash
    pip install SQLAlchemy
    ```
- **示例：**
    ```python
    from sqlalchemy import create_engine, Table, MetaData

    # 创建引擎并连接到数据库
    engine = create_engine('sqlite:///example.db')

    # 创建连接
    conn = engine.connect()

    # 执行SQL查询
    result = conn.execute("SELECT * FROM students")
    for row in result:
        print(row)

    # 关闭连接
    conn.close()
    ```

这些库让你能够灵活地在 Python 中使用 SQL 查询，并与不同类型的数据库进行交互。