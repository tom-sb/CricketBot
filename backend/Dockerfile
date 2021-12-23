FROM python:3.9.6-alpine

RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN pip --no-cache-dir install -r requirements.txt
RUN pip --no-cache-dir install torch==1.10.1+cpu torchvision==0.11.2+cpu torchaudio==0.10.1+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html

COPY . /app

WORKDIR /app

EXPOSE 80

ENTRYPOINT ["sh", "/entrypoint.sh"]

#ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:80"]

