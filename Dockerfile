FROM python:3.9-slim
WORKDIR /app
COPY validador_cpf.py .
COPY test_validador_cpf.py .
CMD ["python", "validador_cpf.py"]
