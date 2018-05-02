import subprocess


def start_client():
    subprocess.run(['insmod','LiME/src/lime-4.15.0-kali2-amd64.ko',"path=$HOME/ram.raw format=lime"])


if __name__ == '__main__':
    start_client()
