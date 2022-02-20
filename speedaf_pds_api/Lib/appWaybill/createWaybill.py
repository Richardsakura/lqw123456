from config import test_config
import requests,json
from Common.login import login


# 快递录单接口
class createWaybill:
    def createWaybill(self,inData,token):
        url = test_config + "/manager/pda/waybill/create"
        headers = {'content-type': 'application/json',
                   'Authorization':token}

        data = inData

        re = requests.post(url,json=data,headers=headers)
        waybillCode = json.loads(re.text)['data']
        return re.text,waybillCode



if __name__ == "__main__":
    token = login("234210027","test123456")
    indata = {
        "billingType": "2",
        "codFee": "3",
        "code": "",
        "customerCode": "",
        "forecastWeight": "2.0",
        "freightFee": "",
        "goodsName": "苹果",
        "insuranceAmount": "",
        "insuranceFee": "",
        "orderCode": "",
        "orderType": 1,
        "packageNumber": 1,
        "receiver": {
            "address": "dfasfdsa",
            "areaCode": "A02834",
            "areaName": "Surulere",
            "cityCode": "C00757",
            "cityName": "Oyo state",
            "countryCode": "",
            "countryName": "",
            "email": "",
            "provinceCode": "R01660",
            "provinceName": "SOUTH-WEST",
            "receiver": "yuanyuan",
            "receiverAddress": "SOUTH-WEST Oyo state Suruleredfasfdsa",
            "receiverInfo": "yuanyuan,54543543",
            "telephone": "54543543"
        },
        "remark": "",
        "seller": "",
        "sender": {
            "address": "432432432",
            "areaCode": "A02834",
            "areaName": "Surulere",
            "cityCode": "C00757",
            "cityName": "Oyo state",
            "countryCode": "",
            "countryName": "",
            "customerCode": "",
            "email": "",
            "provinceCode": "R01660",
            "provinceName": "SOUTH-WEST",
            "seller": "",
            "sender": "weiwei",
            "senderAddress": "SOUTH-WEST Oyo state Surulere432432432",
            "senderInfo": "weiwei,34324324",
            "telephone": "34324324"
        },
        "waybillType": "2"
    }
    a = createWaybill().createWaybill(indata,token)
    print(a[1])  # <class 'tuple'>

