# This Dockerfile is for the hosting of the static HTML site within
# a Pod on a kubernetes cluster.

FROM node:14.7.0-stretch

COPY apps/web-build/server.js /web/
COPY apps/web-build/package.json /web/
COPY build/html/ /web/public/

WORKDIR /web/

RUN npm install

CMD ["node", "server.js"]