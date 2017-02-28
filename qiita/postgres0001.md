# Postgres使い（個人メモ）
* Start server

```Bash
pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start
```

* GUI tools
[Postgres.app](https://postgresapp.com/)


* ログインするには
    * はじめに, all usersを見る
    
    ```bash
    psql -U "admin name" -l
    ```
    
    * set user passwd
    
    _default user always be postgres_
    
    ```bash
    sudo -u postgres psql postgres
    ```
    
    _psqlの中では_
    
    ```
    \password postgres
    ```

* データベース削除
    * with login

    ```
    drop database <.name>;
    ```
    
    * without login
        
    ```bash
    dropdb -e <database.name>
    ```

