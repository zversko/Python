import pytest
from hw import find_text_in_command, getout
from sshhw import ssh_find_text_in_command, ssh_getout
import yaml
import random
import string
from datetime import datetime

with open('config.yaml') as file:
    data = yaml.safe_load(file)

@pytest.fixture()
def make_folders_local():
    return find_text_in_command(f'mkdir {data["folderoutlocal"]}', "")

@pytest.fixture()
def make_folders():
    return ssh_find_text_in_command(host=str(data["host"]),
                                    user=str(data["user"]),
                                    password=str(data["password"]),
                                    command=f'mkdir {data["folderin"]} {data["folderout"]}',
                                    text="")

@pytest.fixture()
def clear_folders():
    yield
    ssh_find_text_in_command(host=str(data["host"]),
                             user=str(data["user"]),
                             password=str(data["password"]),
                             command=f'rm -rf {data["folderin"]} {data["folderout"]}',
                             text="")

@pytest.fixture()
def clear_folders_local():
    yield
    find_text_in_command(f'rm -rf {data["folderoutlocal"]}', "")

@pytest.fixture()
def make_files():
    for i in range(data["count"]):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        ssh_find_text_in_command(host=str(data["host"]),
                                 user=str(data["user"]),
                                 password=str(data["password"]),
                                 command="cd {}; dd if=/dev/urandom of={} bs={} count=1 iflag=fullblock".format(data["folderin"], filename, data["bs"]),
                                 text="")

@pytest.fixture(autouse=True)
def print_time():
    print("Start: {}".format(datetime.now().strftime("%H:%M:%S.%f")))
    yield
    print("\nFinish: {}".format(datetime.now().strftime("%H:%M:%S.%f")))

@pytest.fixture(autouse=True)
def stat():
    yield
    stat = ssh_getout(host=str(data["host"]),
                      user=str(data["user"]),
                      password=str(data["password"]),
                      command="cat /proc/loadavg")
    find_text_in_command("echo 'time: {} count:{} size: {} load: {}'>> stat.txt".format(datetime.now().strftime("%H:%M:%S.%f"), data["count"], data["bs"], stat), "")

