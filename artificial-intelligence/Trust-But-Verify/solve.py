import socket, time, re
HOST = "xebec.cylabacademy.net"
PORT = 47103

def main():
    s = socket.create_connection((HOST, PORT), timeout=15)
    s.settimeout(4)
    full = b""
    def send(b):
        s.sendall(b)
    start = time.time()
    while time.time() - start < 240:
        try:
            d = s.recv(8192)
            if not d:
                break
            full += d
            low = d.decode(errors="ignore").lower()
            if "[a/b/c/d]" in low:
                time.sleep(0.4); send(b"d\n"); continue
            if "[a/b/c]" in low:
                time.sleep(0.4); send(b"c\n"); continue
            if "[a/b]" in low:
                time.sleep(0.4); send(b"b\n"); continue
            if "[y/n]" in low or "(y/n)" in low:
                time.sleep(0.3); send(b"y\n"); continue
            if "press enter" in low:
                time.sleep(0.3); send(b"\n"); continue
            time.sleep(0.3)
        except socket.timeout:
            try: send(b"\n")
            except: break
            continue
    s.close()
    t = full.decode(errors="ignore")
    m = re.search(r"academy\{[^}]+\}", t)
    if m:
        print("FLAG:", m.group(0))
    else:
        print("flag not found, tail:")
        print(t[-2000:])

if __name__ == "__main__":
    main()
