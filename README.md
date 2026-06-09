#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

print("🔍 Bug Monthly Tracker - Kali Linux Edition")
print(f"📅 Current Date: {datetime.now().strftime('%B %Y')}\n")

def create_readme():
    readme_content = """# Bug Monthly Tracker

![Kali Linux](https://img.shields.io/badge/Kali%20Linux-000000?style=for-the-badge&logo=kali-linux&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

**Kali Linux tool jo ongoing Bug Bounties aur Monthly Challenges track karta hai.**

Ek simple aur fast CLI tool specially Indian Bug Bounty Hunters ke liye.

## ✨ Features

- Major platforms ke active programs
- Monthly challenges awareness (Bug Bytes, etc.)
- Direct official links
- Lightweight CLI tool

## 👨‍💻 Author

**Made with ❤️ by Vimal Bijalwan**

For the Indian Bug Bounty Community.

## 🛠️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/bug-monthly-tracker.git
cd bug-monthly-tracker
pip3 install requests beautifulsoup4
python3 bug_monthly_tracker.py
