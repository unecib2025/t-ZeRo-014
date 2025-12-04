# Задача 1
ips = ["10.0.0.1", "10.0.0.2", "10.0.0.1", "192.168.1.10"]
print(set(ips))

# Задача 2
blocked = {"root", "admin", "test"}
blocked.add("hacker")
blocked.remove("test")
print(blocked)

# Задача 3
forbidden = {21, 22, 23, 25}
port = 22
if port in forbidden:
    print("Порт запрещён")
else:
    print("Порт разрешён")

# Задача 4
known = {"mal.com", "bad.net"}
new = {"bad.net", "xevil.org"}
print(new - known)

# Задача 5
white = {"alice", "bob", "root"}
black = {"root", "admin"}
print(white & black)

# Задача 6
A = {"CVE-1", "CVE-2"}
B = {"CVE-2", "CVE-3"}
print(A | B)

# Задача 7
admin = {"read", "write", "delete"}
user = {"read", "download"}
print(admin ^ user)

# Задача 8
all_pw = ["123", "qwerty", "test", "123", "qwerty", "admin"]
blocked_pw = {"test"}
print(set(all_pw) - blocked_pw)

# Задача 9
global_ips = {10.0.0.1, 10.0.0.2, 192.168.1.1}
local_ips = {10.0.0.2, 10.0.0.3}
local_ips.intersection_update(global_ips)
print(local_ips)

# Задача 10
logs = ["scan", "debug_mode", "scan", "connect", "debug_info"]
print({x for x in logs if "debug" not in x})