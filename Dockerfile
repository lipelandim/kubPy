FROM python:3
COPY . /app
RUN pip install uvicorn && pip install fastapi 
WORKDIR /app
CMD python main.py
