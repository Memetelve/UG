#!/bin/bash

CONTAINER_NAME="nginx-container"
NGINX_HTML_DIR="./nginx-html"

mkdir -p $NGINX_HTML_DIR

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

docker run -d -p 80:80 --name $CONTAINER_NAME -v $(pwd)/$NGINX_HTML_DIR:/usr/share/nginx/html nginx

container_ip=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $CONTAINER_NAME)
echo "$container_ip"
