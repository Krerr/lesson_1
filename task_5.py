import subprocess

ya =["ping", "yandex.ru"]


sub_proc = subprocess.Popen(ya, stdout=subprocess.PIPE)
for line in sub_proc.stdout:
    print(line.decode("utf-8"))


yu =["ping", "youtube.com"]


sub_proc = subprocess.Popen(yu, stdout=subprocess.PIPE)
for line in sub_proc.stdout:
    print(line.decode('utf-8'))