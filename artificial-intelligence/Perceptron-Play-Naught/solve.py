import socket
import time
import re

HOST = "chatelaine.cylabacademy.net"
PORT = 20759

def main():
    s = socket.create_connection((HOST, PORT), timeout=15)
    s.settimeout(3)
    buf = b""

    def rd():
        nonlocal buf
        out = b""
        try:
            while True:
                d = s.recv(8192)
                if not d:
                    break
                out += d
                if len(d) < 8192:
                    break
        except socket.timeout:
            pass
        buf += out
        return out

    def send(cmd):
        s.sendall((cmd + "\n").encode())
        time.sleep(0.4)
        return rd()

    rd()  # banner
    # class 0 all at y=-1, class 1 all at y>=1 -> horizontal boundary y=0
    # activation = w1*x + w2*y + b ; set w1=0, w2=1, b=0
    send("SET 0 1 0")
    out = send("CHECK")
    text = out.decode(errors="replace")
    print(text)
    m = re.search(r"academy\{[^}]+\}", text)
    if not m:
        m = re.search(r"academy\{[^}]+\}", buf.decode(errors="replace"))
    if m:
        print("[+] FLAG:", m.group(0))
    s.close()

if __name__ == "__main__":
    main()
