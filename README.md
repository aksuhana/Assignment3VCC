# Assignment3VCC
# 🌥️ Local to GCP Auto-Scaler Based on CPU Usage

This project demonstrates a hybrid cloud setup that auto-scales from a local Ubuntu VM to Google Cloud Platform (GCP) based on real-time resource usage (CPU & Memory).

## 🧠 Overview

- Monitor CPU & memory on a local VirtualBox VM
- If usage > 75%, auto-scale to GCP by adding VM instances
- If usage < 50%, scale back down to save cost
- Sample Flask app deployed on GCP VMs

---

## 🛠️ Tech Stack

- Python (`psutil`, `subprocess`)
- Google Cloud SDK (`gcloud`)
- VirtualBox (local VM)
- GCP Compute Engine
- Flask (demo app)
- Optional: systemd or nohup for background task

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/aksuhana/Assignment3VCC.git.git

