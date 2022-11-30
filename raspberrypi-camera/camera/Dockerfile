FROM navikey/raspbian-bullseye:latest
WORKDIR /app


RUN apt update && apt-get -y upgrade
RUN apt-get install -y python3 python3-pip vim
RUN pip install --upgrade pip
RUN apt install -y python3-picamera2 --no-install-recommends
RUN pip install requests
ADD ./ /app/
CMD [ "python3", "main.py" ]