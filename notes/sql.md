# SQL

```sql
CREATE DATABASE userdb;
CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON userdb.* TO 'user'@'localhost';
FLUSH PRIVILEGES;
```
