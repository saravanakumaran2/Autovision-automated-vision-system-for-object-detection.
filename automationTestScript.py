#!/usr/bin/env python3
import subprocess
import re
import datetime
import os
import sys

def strip_ansi_codes(text: str) -> str:
    """Remove ANSI escape sequences from terminal output."""
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)

def run_detection_script(script_path: str) -> str:
    """Runs the detection script and waits for completion, capturing full output."""
    proc = subprocess.run(
        [sys.executable, script_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    clean_output = strip_ansi_codes(proc.stdout)
    print(clean_output)
    return clean_output

def parse_detection_output(output: str):
    """
    Extract object detections from YOLO logs.
    Looks for lines like: "image 1/1 ...: 640x640 1 apple, 1 orange, ..."
    """
    detection_lines = re.findall(r'image\s+\d+/\d+.*?:.*?(\d+.*?)$', output, re.MULTILINE)
    if not detection_lines:
        return False, []
    objs = []
    for match in detection_lines:
        parts = [p.strip() for p in match.split(',') if p.strip()]
        objs.extend(parts)
    return bool(objs), objs

def write_test_report(output: str, detected_objects):
    """Write log, detection info, pass/fail into a timestamped report file."""
    ts = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    dirname = "test_reports"
    os.makedirs(dirname, exist_ok=True)
    path = os.path.join(dirname, f"test_results_{ts}.txt")
    with open(path, "w") as f:
        f.write(f"[{ts}] Drone Detection Log:\n\n")
        f.write(output + "\n\n")
        if detected_objects:
            f.write(f"Detected objects: {', '.join(detected_objects)}\n")
            f.write("Test case PASSED.\n")
        else:
            f.write("No objects detected. Test case FAILED.\n")
    print(f"\nTest report saved: {path}")

def main():
    script = "watch_and_detect.py"  # adjust if needed
    print(f"[{datetime.datetime.now()}] Running detection script...")
    output = run_detection_script(script)
    ok, objs = parse_detection_output(output)
    write_test_report(output, objs)

if __name__ == "__main__":
    main()
