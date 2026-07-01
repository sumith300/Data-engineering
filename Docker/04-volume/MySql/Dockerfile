FROM mysql:8.0

ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=flask_db

COPY ./init.sql /docker-entrypoint-initdb.d/


EXPOSE 3307

# docker run -dp 3307:3306 --name mysql-container -v sumith-volume:/var/lib/mysql mysql-image
# docker run -dp 3307:3306 --name mysql-container mysql-image  