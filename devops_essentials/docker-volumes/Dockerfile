FROM ubuntu:latest

RUN apt-get update && apt-get install -y nginx

EXPOSE 80

VOLUME /data

CMD ["nginx", "-g", "daemon off;"]
