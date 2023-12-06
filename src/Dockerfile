FROM python:3.12
WORKDIR /src
COPY . ./
RUN pip install flask requests python-dotenv
EXPOSE 5001
CMD [ "python3","app.py" ]