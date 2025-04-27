import time
import sys

def slow_print(text, delay=0.03):
    
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def banner():
    """
    Prints a nice welcome banner for the tool.
    """
    print("="*50)
    print("🛡️  WiFi Security Analyzer")
    print("📶  Scan | Analyze | Protect")
    print("="*50)
