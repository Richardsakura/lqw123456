#-*- coding: utf-8 -*-

import xlrd


def get_excelData(sheetName,startCol,endCol,resValueCol,expValueCol):
    '''

    :param sheetName: sheet名
    :param startCol: 开始行，从1开始数
    :param endCol: 结束行
    :param resValueCol: 请求体，列从0开始数
    :param expValueCol: 预期响应，列从0开始数
    :return:
    '''
    excelDir = '../Data/运单相关接口.xls'
    workBook = xlrd.open_workbook(excelDir,formatting_info=True)
    workSheet = workBook.sheet_by_name(sheetName)
    res_list  = []
    for cnt in range(startCol-1,endCol):
        res_value = workSheet.cell_value(cnt,resValueCol)
        exp_value = workSheet.cell_value(cnt,expValueCol)
        res_list.append((res_value,exp_value))
    return res_list


if __name__ == "__main__":
    value = get_excelData('快递录单',2,2, 5,7)
    print(value)


