FROM nginx 

COPY nginx.conf /etc/nginx/conf.d/default.conf

RUN mkdir /etc/nginx/ssl
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl/key.key -out /etc/nginx/ssl/key.crt -subj "/CN=/O=/"

EXPOSE 80
EXPOSE 443
