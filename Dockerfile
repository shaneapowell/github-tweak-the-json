FROM alpine
RUN apk add --update nodejs
COPY main.js main.js
ENTRYPOINT ["/usr/bin/node"]

