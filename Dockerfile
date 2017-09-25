FROM node
WORKDIR /appl
COPY package.json /appl
RUN npm install
COPY . /appl
CMD node index.js
EXPOSE 8081
