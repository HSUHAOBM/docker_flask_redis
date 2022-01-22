# 使用python3.8 alpine模板
FROM python:3.8.3-alpine3.12
# 将当前目录映射到容器内/app目录
ADD . /app
# 设置/app为工作目录
WORKDIR /app
# 安装python依赖包
RUN pip install -r requirements.txt
# 启动flask应用服务
CMD python main.py
