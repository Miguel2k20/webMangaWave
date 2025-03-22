FROM node:16
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 80
RUN npm cache clean --force && npm install
CMD ["npm", "run", "serve"]