#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
My First Python Script! 🐍
Written by: Berdi Nazarov
Purpose: Welcome to programming, kanka!
"""

def greet_user(name):
    """Greet the user with style!"""
    print(f"🚀 Merhaba {name}! Welcome to my coding journey!")
    print("=" * 50)

def show_info():
    """Display system info about me"""
    info = {
        "Name": "Berdi Nazarov",
        "Age": 17,
        "Location": "Turkmenistan 🇹🇲",
        "OS": "Linux Mint XFCE",
        "Laptop": "Intel Celeron N3550 (Low-end but powerful! 💪)",
        "RAM": "6GB",
        "Dream": "Data Analyst → University → Tech Career",
    }
    
    print("\n📊 My Profile:")
    for key, value in info.items():
        print(f"  {key}: {value}")

def main():
    """Main function"""
    greet_user("Berdi")
    show_info()
    
    print("\n" + "=" * 50)
    print("✨ This is just the beginning, kanka!")
    print("🔥 Let's code and change the world!")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    main()
