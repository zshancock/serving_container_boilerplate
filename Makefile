APP_NAME := starter


clean:
	docker stop $(APP_NAME)

serving.build:
	docker build -f ./Dockerfile -t $(APP_NAME):serving .

serving.run: serving.build
	docker run -p 8000:8000 --name $(APP_NAME) $(APP_NAME):serving
