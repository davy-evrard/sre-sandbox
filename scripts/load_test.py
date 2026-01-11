import requests
import time

url = "http://localhost:8000/risky"

print("🔥 Starting Load Test on The Unstable API... Press Ctrl+C to stop.")

while True:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("✅ Success")
        else:
            print(f"❌ Error: {response.status_code}")
    except Exception as e:
        print(f"💀 Connection Failed: {e}")
    
    # Fast traffic: 5 requests per second
    time.sleep(0.2)
