# GenAI

# 🎨 Stable Diffusion Prompt-to-Image Generator on AWS

![Powered by Hugging Face](https://img.shields.io/badge/HuggingFace-Diffusers-yellow)
![Flask API](https://img.shields.io/badge/Backend-Flask-blue)
![Runs on AWS EC2](https://img.shields.io/badge/Cloud-AWS-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A lightweight, GPU-ready Flask API for generating stunning images from text prompts using 🤗 **Stable Diffusion**. Designed for deployment on **AWS EC2** with NVIDIA GPUs.

---

## 🚀 Features

- 🔥 Powered by [Stable Diffusion v1.5](https://huggingface.co/runwayml/stable-diffusion-v1-5)
- ⚡ Runs on AWS EC2 with CUDA acceleration
- 🎯 Accepts prompt via REST API
- 🖼️ Saves and serves generated images dynamically

---

## 📦 Setup Instructions

### 1. 🔧 Create and Launch EC2 (GPU Enabled)
Choose one of:
- `g4dn.xlarge`
- `p3.2xlarge`
- `g5.xlarge`

> Use Deep Learning AMI (Ubuntu) or install manually.

---

### 2. 🐍 Python Environment

```bash
conda create -n sd_env python=3.10 -y
conda activate sd_env

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install diffusers transformers accelerate flask python-dotenv

---

## 🗂️ Project Structure

stable-diffusion-server/
├── app.py
├── image_utils.py
├── static/images/
├── .env
└── requirements.txt

---

## 📄 .env Configuration

HF_TOKEN=your_huggingface_access_token

---

## 🧠 Run Server

python app.py
# OR for production
gunicorn app:app --bind 0.0.0.0:5000

---

## 🔁 API Usage

### 1. Endpoint
POST /generate

### 2. Payload
{
  "prompt": "A surreal landscape with floating islands"
}

### 3. Response
{
  "image_url": "static/images/generated.png"
}

### 4. Image Access
GET /images/<filename>
