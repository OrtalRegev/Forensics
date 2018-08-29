import subprocess
import sys
import hashlib

if (len(sys.argv) != 3) or (len(sys.argv) != 2):
    print("Usage:"
          "Parameter #1: File path"
          "Parameter #2: Image info ( if pre-known ), this will make things a lot faster")


def get_os_type(file_name):
    return subprocess.check_output(["volatility", "-f", file_name, "imageinfo"]).split("Suggested Profile")[1].split(
        "\n")[0].split(" : ")[1].split(",")[0]


def get_process_pids(file_name, os_type):
    pids = []
    for line in subprocess.check_output(["volatility", "-f", file_name, "--profile={}".format(os_type), "psscan"]).split("\n"):
        for element in line.split(" "):
            if element.isdigit():
                pids.append(element)
                break
    return pids


def dump_process(file_name, os_type, pid, output_directory):
    subprocess.check_output(["volatility", "-f", file_name, "--profile={}".format(os_type),
                             "memdump", "-p", pid, "-D", output_directory])


def get_file_hash(file_name, hash_type):
    opened_file = open(file_name)
    read_file = opened_file.read()
    if hash_type == "md5":
        return hashlib.md5(read_file).hexdigest()
    elif hash_type == "sha1":
        return hashlib.sha1(read_file).hexdigest()
