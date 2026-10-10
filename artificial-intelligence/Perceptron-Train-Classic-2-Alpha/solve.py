import urllib.request
import json
import re

BASE = "http://chatelaine.cylabacademy.net:23404"

def cfg():
    return json.loads(urllib.request.urlopen(BASE + "/config.json", timeout=10).read().decode())

def train(lr):
    data = json.dumps({"learningRate": lr}).encode()
    req = urllib.request.Request(BASE + "/train", data=data,
                                 headers={"Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req, timeout=15).read().decode())

def main():
    c = cfg()
    print("[*] target:", c.get("successTarget"), "current:", c.get("successCount"))

    # Need 5 distinct successful (100% accuracy) learning rates.
    # Rate sweeps that converge in this instance:
    candidates = [0.8, 1.0, 1.5, 2.0, 3.0, 1.2, 2.5, 0.9, 1.8, 4.0]
    for lr in candidates:
        res = train(lr)
        print(f"[*] lr={lr} acc={res.get('accuracy')} success={res.get('success')}")
        flag = res.get("flag") or ""
        if not flag:
            m = re.search(r"academy\{[^}]+\}", json.dumps(res))
            flag = m.group(0) if m else ""
        if flag:
            print("[+] FLAG:", flag)
            return
    print("[-] finished sweep, final:", cfg().get("successCount"))

if __name__ == "__main__":
    main()
