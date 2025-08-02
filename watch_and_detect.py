import time
import os
import subprocess
import shutil

input_dir = "/app/input"
processed_dir = "/app/processed"
output_dir = "/app/output"

os.makedirs(processed_dir, exist_ok=True)

def get_unprocessed_images():
    return [
        f for f in os.listdir(input_dir)
        if f.lower().endswith(('.jpg', '.jpeg', '.png')) and
        not os.path.exists(os.path.join(processed_dir, f))
    ]

def run_once():
    images = get_unprocessed_images()
    if images:
        print(f"Detected {len(images)} new image(s). Running detection...")
        for img in images:
            img_path = os.path.join(input_dir, img)
            subprocess.run([
                "python3", "detect.py",
                "--weights", "yolov5s.pt",
                "--source", img_path,
                "--project", output_dir,
                "--name", "results",
                "--exist-ok"
            ])
            shutil.move(img_path, os.path.join(processed_dir, img))
        print("Processing complete.")
    else:
        print("No new images found.")

if __name__ == "__main__":
    run_once()
