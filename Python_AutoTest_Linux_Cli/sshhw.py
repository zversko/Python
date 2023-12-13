import paramiko
import yaml

with open('config.yaml') as file:
    data = yaml.safe_load(file)

def ssh_checkout(host, user, passwd, cmd, text, port=22):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=passwd, port=port)
    stdin, stdout, stderr = client.exec_command(cmd)
    exit_code = stdout.channel.recv_exit_status()
    out = (stdout.read() + stderr.read()).decode("utf-8")
    client.close()
    if text in out and exit_code == 0:
        return True
    else:
        return False
def ssh_find_text_in_command(host, user, password, command, text, port=22):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=password, port=port)
    stdin, stdout, stderr = client.exec_command(command)
    exit_code = stdout.channel.recv_exit_status()
    out = (stdout.read() + stderr.read()).decode('utf-8')
    client.close()
    if text in out and exit_code == 0:
        return True
    else:
        return False

def ssh_getout(host, user, password, command, port=22):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=password, port=port)
    stdin, stdout, stderr = client.exec_command(command)
    out = (stdout.read() + stderr.read()).decode("utf-8")
    client.close()
    return out

def ssh_upload_files(host, user, password, local_path, remote_path, port=22):
    print(f'\nЗагружаем файл {local_path} в каталог {remote_path}')
    transport = paramiko.Transport(host, port)
    transport.connect(None, user, password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(local_path, remote_path)
    if sftp:
        sftp.close()
    if transport:
        transport.close()

def ssh_download_files(host, user, password, remote_path, local_path, port=22):
    print(f"\nСкачиваем файл {remote_path} в каталог {local_path}")
    transport = paramiko.Transport((host, port))
    transport.connect(None, username=user, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.get(remote_path, local_path)
    if sftp:
        sftp.close()
    if transport:
        transport.close()

def ssh_find_text_Negative(host, user, password, command, text, port=22):
   client = paramiko.SSHClient()
   client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
   client.connect(hostname=host, username=user, password=password, port=port)
   stdin, stdout, stderr = client.exec_command(command)
   exit_code = stdout.channel.recv_exit_status()
   out = (stdout.read() + stderr.read()).decode("utf-8")
   client.close()
   if text not in out or exit_code != 0:
       return True
   else:
       return False
