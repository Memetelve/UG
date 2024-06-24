FROM node:latest

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

# Build the app then run

RUN npm run build

CMD ["npm", "start"]
