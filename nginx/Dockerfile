FROM nginx:latest

COPY backend.conf /etc/nginx/conf.d

COPY ./collected_static ./static

#RUN mkdir -p /web/media
#
## Установите права доступа
#RUN chmod -R 777 /web/media # Папка с правами на запись для media