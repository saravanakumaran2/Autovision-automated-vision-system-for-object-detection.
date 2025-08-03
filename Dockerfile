FROM saravana227/yolov5-detector
WORKDIR /app
COPY . /app
CMD ["python", "automationTestScript.py"]
