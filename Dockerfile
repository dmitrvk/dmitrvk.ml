FROM node:18

ARG API_URL

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

ENV REACT_APP_API_URL $API_URL

CMD [ "npm", "start" ]
