FROM python:3.8
EXPOSE 8080
WORKDIR /endpoint
COPY . .
CMD ["uvicorn", "main:endpoint", "--host", "0.0.0.0", "--port", "8080"]