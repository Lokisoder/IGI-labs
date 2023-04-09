FROM python

WORKDIR /home/ruslan/PycharmProjects/pythonProject1

COPY . .

CMD ["python", "tas1.py", "tas2.py", "tas3.py"]