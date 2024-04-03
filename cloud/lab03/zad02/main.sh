#!/bin/bash

CONTAINER_NAME="lab3ex2"
NGINX_HTML_DIR="./nginx-html"
NGINX_CONF_DIR="./nginx-conf"
NGINX_PORT=12344

mkdir -p $NGINX_HTML_DIR
mkdir -p $NGINX_CONF_DIR

cat <<EOF > $NGINX_HTML_DIR/index.html
<!DOCTYPE html>
<html>
<head>
    <title>Whot?</title>
</head>
<body>
    <h1>.</h1>
</body>
</html>
EOF

cat <<EOF > $NGINX_CONF_DIR/nginx.conf
server {
    listen $NGINX_PORT;
    server_name localhost;

    location / {
        root /usr/share/nginx/html;
        index index.html;
    }
}
EOF

docker rm -f $CONTAINER_NAME

docker run -d -p 80:$NGINX_PORT --name $CONTAINER_NAME -v $(pwd)/$NGINX_HTML_DIR:/usr/share/nginx/html -v $(pwd)/$NGINX_CONF_DIR:/etc/nginx/conf.d nginx
