# Issues

* **ImportError: No module named MySQLdb**
>engine = create_engine("mysql://root:shenjing@127.0.0.1:3306/test?charset=utf8", echo=True)

   I got the `ImportError: No module named MySQLdb` error when the above command was executed.To fix it, I installed the `mysql-python` module and the issue was fixed.
  > pip install mysql-python