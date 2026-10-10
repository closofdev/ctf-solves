import socket
import time
import re

HOST = "chatelaine.cylabacademy.net"
PORT = 37297

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
    # points: class 0 at lower-left, class 1 at upper-right
    # -> linear boundary like y = -x (w1=1, w2=1, b=0)
    send("SET 1 1 0")
    out = send("CHECK")
    text = out.decode(errors="replace")
    print(text)
    m = re.search(r"academy\{[^}]+\}", buf.decode(errors="replace"))
    if m:
        print("[+] FLAG:", m.group(0))
    s.close()

if __name__ == "__main__":
    main()
