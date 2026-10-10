import urllib.request
import json
import re

BASE = "http://xebec.cylabacademy.net:29078"

def cfg():
    return json.loads(urllib.request.urlopen(BASE + "/config.json", timeout=10).read().decode())

def train(lr):
    data = json.dumps({"learningRate": lr}).encode()
    req = urllib.request.Request(BASE + "/train", data=data,
                                 headers={"Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req, timeout=15).read().decode())

def main():
    c = cfg()
    print("[*] config:", json.dumps(c))

    # 3-bit parity, not linearly separable -> 75% is the max (6/8).
    for lr in [0.1, 0.2, 0.3, 0.5, 1.0, 2.0]:
        res = train(lr)
        print(f"[*] lr={lr} acc={res.get('accuracy')} success={res.get('success')}")
        flag = res.get("flag") or ""
        if not flag:
            m = re.search(r"academy\{[^}]+\}", json.dumps(res))
            flag = m.group(0) if m else ""
        if flag:
            print("[+] FLAG:", flag)
            return

if __name__ == "__main__":
    main()
