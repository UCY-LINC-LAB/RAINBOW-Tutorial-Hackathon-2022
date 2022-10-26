# Pull base image of latest Python 3.7.x
FROM python:3.6

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

# Add and install requirements
ADD requirements.txt /code/
RUN pip install -r requirements.txt

# pass code to the image
ADD ./code/ /code/

# execute entrypoint
RUN chmod +x /code/entrypoint.sh
CMD ["/bin/bash", "/code/entrypoint.sh"]