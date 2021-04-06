# Pull base image.
FROM nvidia/cuda:10.1-cudnn7-runtime

RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install setuptools
WORKDIR /production
# Install dependencies.
COPY . .
RUN pip3 install -r requirements.txt

# Start application.
EXPOSE 8000
CMD ["sh", "./boot.sh"]
