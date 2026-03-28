From python:latest


WORKDIR /app

#RUN mkdir -p /static_folder
#COPY ./static_html /static_folder

COPY ./src .

#RUN echo "Hello, World!" > index.html

#docker build -f Dockerfile -t pyapp .
#docker run -it pyapp
#but cannot push to docker hub

#docker build -f Dockerfile -t shioun/py-app:latest .
#docker push shioun/py-app:latest

#run python web server with "python -m http.server 8000" in the terminal
#docker run -it -p 8080:8000 pyapp
CMD ["python", "-m", "http.server", "8000"]