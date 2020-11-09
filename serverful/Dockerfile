FROM python:3-alpine

ENV http_proxy ""
ENV https_proxy ""

WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

EXPOSE 5000

CMD [ "python", "main.py" ]