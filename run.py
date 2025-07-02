import subprocess

def run_api():
    subprocess.run(["fastapi", "dev", "src/main.py", "--port", "4000"])

if __name__ == "__main__":
    run_api()
