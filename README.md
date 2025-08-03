# 🧠 YOLOv5 Object Detection in Kubernetes 🚀

This project shows how to run a YOLOv5-based object detection app inside a **Kubernetes cluster**.  
It uses:
- **Helm** for easy deployment,
- **Amazon S3** to store input and output files,
- **Zabbix** for monitoring system health.

The app listens for files, runs object detection on them, and uploads the results to S3.


## 📦 What’s Inside

Object-detection-in-kubernetes/
├── helm/ → Helm charts for YOLOv5 and Zabbix
│ ├── yolvo/ → Helm chart for YOLOv5 deployment
│ ├── helmfile.yaml → Deploys YOLOv5 and Zabbix together
├── upload_to_s3.py → Upload result files to S3
├── download_from_s3.py → Download input files from S3
├── watch_and_detect.py → Runs YOLOv5 detection inside container
├── Dockerfile → Builds the Docker image for YOLOv5 app



## 🎯 Main Features

✅ Deploy YOLOv5 with a single Helm command  
✅ Detect objects in files (images or videos)  
✅ Automatically upload results to Amazon S3  
✅ Zabbix monitors your app's health and logs  
✅ Persistent storage for input/output  
✅ Easy scaling and Kubernetes-native
