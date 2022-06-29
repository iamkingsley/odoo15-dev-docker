# Odoo 15

## This docker version shows you how to:

 - mount custom addons located in ./addons
 - use a custom configuration file located in .config/odoo.conf
 - use named volumes for the Odoo and postgres data dir

 ## To start your Odoo instance, go in the directory of the docker-compose.yml file and type:

 ```js
 docker-compose up -d
 ```
### NB

### If you are using the ```docker-compose up``` command to start your servers, then you need to add the following line to your ```docker-compose.yml``` file under the odoo service:
```js
command: odoo -u all -d odoo-prod
```
#### Where ```odoo-prod``` is the name of your database. This overwrites the default command (which is just odoo without update) and tells docker to update all modules when the container restarts.

### Alternatively, you can also run a separate container that performs the updates:
```js
docker run -v [your volumes] odoo:10.0 odoo -u all -d odoo-prod
```
## OR

### Start a PostgreSQL server and run it
```js
$ docker run -d -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo -e POSTGRES_DB=postgres --name db postgres:13
```
### Start an Odoo instance
```js
$ docker run -p 8069:8069 --name odoo --link db:db -t odoo -i base
```

#### The alias of the container running Postgres must be db for Odoo to be able to connect to the Postgres server.

### Stop and restart an Odoo instance
```js
$ docker stop odoo
$ docker start -a odoo
```