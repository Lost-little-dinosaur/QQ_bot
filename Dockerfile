FROM python:3.9.7



# 设置工作目录（Docker虚拟机上的虚拟工作目录）
WORKDIR ./QQ机器_Docker
#代码添加到code文件夹
ADD . .

## 安装Chorme以及模拟浏览器的依赖包

# env
RUN apt-get update \
&& apt-get -y install wget

# package build
RUN mkdir /packages

# chrome
RUN cd /packages \
&& wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
&& apt-get -y install fonts-liberation \
libasound2 \
libatk-bridge2.0-0 \
libatk1.0-0 \
libatspi2.0-0 \
libcups2 \
libdbus-1-3 \
libdrm2 \
libgbm1 \
libgtk-3-0 \
libnspr4 \
libnss3 \
libxcomposite1 \
libxdamage1 \
libxfixes3 \
libxkbcommon0 \
libxrandr2 \
libxshmfence1 \
xdg-utils \
&& dpkg -i google-chrome-stable_current_amd64.deb

# chrome driver
RUN cd /packages \
&& wget https://chromedriver.storage.googleapis.com/103.0.5060.53/chromedriver_linux64.zip \
&& unzip chromedriver_linux64.zip \
&& mv chromedriver /usr/bin/ \
&& chmod +x /usr/bin/chromedriver

# package delete
RUN rm -rf /packages

# 安装支持
RUN pip install -r requirements.txt

RUN apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends ca-certificates curl

#CMD ["python3","wait.py"]
CMD ["python3","bot.py"]
#暴露端口
EXPOSE 8082

#shm_size=1g

