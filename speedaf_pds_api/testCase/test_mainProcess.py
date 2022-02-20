#-*- coding: utf-8 -*-p

import pytest
# 导入库函数
from Lib.appWaybill.createWaybill import createWaybill
from Lib.appPickedScan.pickScan import pickScan
from Common.login import login
# 导入请求体和期望值的数据源
from Common.get_ExcelData import get_excelData
import allure,os
import json


@allure.description('收发到派签-主流程')
@allure.feature('收发到派签-主流程')
class TestMainProcess:
    def setup_class(self):
        """录单模块-登录初始化"""
        self.token = login("234210027","test123456")

    @allure.story('快递录单接口')
    @allure.title('快递录单接口')
    @allure.severity('critical')  # 测试用例的重要级别
    @allure.description('快递录单接口')
    @pytest.mark.createWaybill  # 标签---
    @pytest.mark.parametrize('inData,exp_value', get_excelData('主流程',2,2, 5,7))
    def test_create_waybill(self,inData,exp_value):
        res = createWaybill().createWaybill(json.loads(inData),self.token)
        # 运单号打印
        waybill_code = res[1]
        print(waybill_code)
        # 断言
        assert json.loads(res[0])["success"] == True

    @allure.story('揽件扫描接口')
    @allure.title('揽件扫描接口')
    @allure.severity('critical')  # 测试用例的重要级别
    @allure.description('揽件扫描接口')
    @pytest.mark.pickScan  # 标签---
    @pytest.mark.parametrize('inData,exp_value', get_excelData('主流程',2,2, 5,7))
    def test_pick_scan(self,inData,exp_value):
        waybillCode = createWaybill().createWaybill(json.loads(inData),self.token)[1]
        # 揽件扫描接口
        res = pickScan().pickScan(self.token,waybillCode)
        assert  json.loads(res)["success"] == True







if __name__ == '__main__':
    # 执行用例，生成tmp
    pytest.main(['test_mainProcess.py', '-s', '--alluredir', '../report/tmp'])
    # 复制环境变量文件
    os.system('copy environment.properties report/tmp/environment.properties')
    # # 生成报告
    os.system('allure generate ../report/tmp -o ../report/report  --clean')
