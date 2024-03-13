# Commands for project run

## DB commands
- `sudo -i -u postgres` - Switch to the postgres user account.
- `psql` - Enter the PostgreSQL console.
- `create database restful;` - Create a database named "restful".
- `create role restful_user with password 'restful_pass';` - Create a user with the password.
- `alter role "store_username" with login;` - Grant login permission to the user.
- `grant all privileges on database "store_db" to store_username;` - Grant all privileges on the database to the user.
- `psql -hlocalhost -U restful_user -W restful` - Check the login by connecting to the "restful" database with the "restful_user" user account.
