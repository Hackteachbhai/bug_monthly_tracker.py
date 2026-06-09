#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sys

print("🔍 Bug Monthly Tracker - Kali Linux Edition")
print(f"📅 Current Date: {datetime.now().strftime('%B %Y')}\n")

def fetch_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) BugTracker/1.0'
        }
        r = requests.get(url, headers=headers, timeout=12)
        r.raise_for_status()
        return BeautifulSoup(r.text, 'html.parser')
    except Exception as e:
        return None

def show_active_programs():
    print("🌐 Major Platforms - Ongoing Bug Bounties & Monthly Challenges:")
    print("="*70)
    
    print("\n1. HackerOne")
    print("   Status: Thousands of ongoing programs")
    print("   Link: https://www.hackerone.com/opportunities/all")
    
    print("\n2. Bugcrowd")
    print("   Status: Many public ongoing programs")
    print("   Link: https://www.bugcrowd.com/bug-bounty-programs/")
    
    print("\n3. Intigriti")
    print("   Status: Monthly Bug Bytes Challenges")
    print("   Link: https://www.intigriti.com/researchers/bug-bytes")
    
    print("\n4. YesWeHack")
    print("   Status: Monthly challenges + ongoing programs")
    print("   Link: https://www.yeswehack.com/")
    
    print("\n5. Wordfence")
    print("   Status: Monthly Bug Detector Streak Bonus (Ongoing)")
    print("   Link: https://www.wordfence.com/threat-intel/bug-bounty-program/")
    
    print("\n6. Immunefi (Crypto/Web3)")
    print("   Status: High reward ongoing bounties")
    print("   Link: https://immunefi.com/explore/")

def main():
    show_active_programs()
    
    print("\n" + "="*70)
    print("💡 Pro Tips:")
    print("• bbscope: go install github.com/sw33tLie/bbscope@latest")
    print("• Har mahine start mein new challenges check karo")
    print("• Official links se latest deadlines confirm karo")
    print("\nResponsible Bug Hunting! 🔥")
    
    print("\n" + "="*70)
    print("👨‍💻 Made by Vimal Bijalwan")
    print("   For Indian Bug Bounty Community")

if __name__ == "__main__":
    main()
