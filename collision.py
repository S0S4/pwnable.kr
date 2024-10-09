#/usr/bin/python3

import paramiko


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('pwnable.kr', username='col', password='guest', port=2222)

string = r'\xc8\xce\xc5\x06' * 4 + r'\xcc\xce\xc5\x06'


command = f'./col "$(python -c \'print("{string}")\')"'
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
print(ssh_stdout.read().decode('utf-8'))

ssh.close()
