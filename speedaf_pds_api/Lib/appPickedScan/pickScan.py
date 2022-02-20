from config import test_config
import requests
from Common.login import login


# 揽件扫描接口
class pickScan:
    def pickScan(self,token,waybillCode):
        url = test_config + "/manager/pda/pickedScan/add"
        headers = {'content-type': 'application/json',
                   'Authorization':token}

        data = {"waybillCode":waybillCode,"weight":"3"}

        re = requests.post(url,json=data,headers=headers)
        return re.text


if __name__ == "__main__":
    token = login("234210027","test123456")
    res = pickScan().pickScan(token,"NGL202100000157")
    print(res)