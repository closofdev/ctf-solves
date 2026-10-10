import urllib.request
import json
import re

BASE = "http://chatelaine.cylabacademy.net:45644"

def main():
    cfg = json.loads(urllib.request.urlopen(BASE + "/config.json", timeout=10).read().decode())
    print("[*] config:", cfg)
    lr = 0.5
    data = json.dumps({"learningRate": lr}).encode()
    req = urllib.request.Request(BASE + "/train", data=data,
                                 headers={"Content-Type": "application/json"})
    res = json.loads(urllib.request.urlopen(req, timeout=15).read().decode())
    print("[*] accuracy:", res.get("accuracy"), "success:", res.get("success"))
    print("[*] message:", res.get("message"))
    flag = res.get("flag") or ""
    if not flag:
        m = re.search(r"academy\{[^}]+\}", json.dumps(res))
        flag = m.group(0) if m else ""
    print("[+] FLAG:", flag)

if __name__ == "__main__":
    main()
