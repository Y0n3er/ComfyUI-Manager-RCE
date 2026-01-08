import subprocess

if __name__ == "__main__":
    subprocess.run(["touch", "/tmp/success"], check=True)