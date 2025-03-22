FROM node:16
WORKDIR /app
COPY package*.json ./
RUN mkdir -p /app/node_modules/.cache && chmod -R 777 /app/node_modules/.cache
RUN npm install
COPY . .
EXPOSE 80
CMD ["npm", "run", "serve"]