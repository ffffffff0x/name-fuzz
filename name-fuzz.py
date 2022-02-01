#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import readline
from pypinyin import pinyin, lazy_pinyin, Style

# suffix 字典
filename="suffix.txt"

def results_list_A():

    # 生成相应规则(基于组织)
    results_list_A = []

    # 例如: 江苏XX有限公司
    if CompanyName:
        CompanyName_array1=pinyin(CompanyName, style=Style.NORMAL, strict=False)
        CompanyName_array2=pinyin(CompanyName, style=Style.FIRST_LETTER, strict=False)
        CompanyName_str1 = ""
        CompanyName_str2 = ""

        for tempvar in CompanyName_array1:
            temp_str1 = "".join(tempvar)
            CompanyName_str1 = CompanyName_str1 + temp_str1

        for tempvar in CompanyName_array2:
            temp_str2 = "".join(tempvar)
            CompanyName_str2 = CompanyName_str2 + temp_str2

        # jiangsuxxyouxiangongsi
        print("CompanyName_str1      : ",CompanyName_str1)
        # jsxxyxgs
        print("CompanyName_str2      : ",CompanyName_str2)

        # jsxxyxgs + 后缀
        f1 = open(filename, "r")
        for line in f1:
            results_list_A.append(CompanyName_str2+line.replace('\n', '').replace('\r', ''))
        f1.close()

    # 例如: 江苏XX
    if ShortCompanyName:
        ShortCompanyName_array1=pinyin(ShortCompanyName, style=Style.NORMAL, strict=False)
        ShortCompanyName_array2=pinyin(ShortCompanyName, style=Style.FIRST_LETTER, strict=False)
        ShortCompanyName_str1 = ""
        ShortCompanyName_str2 = ""

        for tempvar in ShortCompanyName_array1:
            temp_str3 = "".join(tempvar)
            ShortCompanyName_str1 = ShortCompanyName_str1 + temp_str3

        for tempvar in ShortCompanyName_array2:
            temp_str4 = "".join(tempvar)
            ShortCompanyName_str2 = ShortCompanyName_str2 + temp_str4

        # jiangsuxx
        print("ShortCompanyName_str1 : ",ShortCompanyName_str1)
        # jsxx
        print("ShortCompanyName_str2 : ",ShortCompanyName_str2)

        # jiangsuxx + 后缀
        f1 = open(filename, "r")
        for line in f1:
            results_list_A.append(ShortCompanyName_str1+line.replace('\n', '').replace('\r', ''))
        f1.close()

        # jsxx + 后缀
        f1 = open(filename, "r")
        for line in f1:
            results_list_A.append(ShortCompanyName_str2+line.replace('\n', '').replace('\r', ''))
        f1.close()

    # 例如: 智慧交通
    if SystemName:
        SystemName_array1=pinyin(SystemName, style=Style.NORMAL, strict=False)
        SystemName_array2=pinyin(SystemName, style=Style.FIRST_LETTER, strict=False)
        SystemName_str1 = ""
        SystemName_str2 = ""

        for tempvar in SystemName_array1:
            temp_str5 = "".join(tempvar)
            SystemName_str1 = SystemName_str1 + temp_str5

        for tempvar in SystemName_array2:
            temp_str6 = "".join(tempvar)
            SystemName_str2 = SystemName_str2 + temp_str6

        # zhihuijiaotong
        print("SystemName_str1       : ",SystemName_str1)
        # zhjt
        print("SystemName_str2       : ",SystemName_str2)

        # zhjt + 后缀
        f1 = open(filename, "r")
        for line in f1:
            results_list_A.append(SystemName_str2+line.replace('\n', '').replace('\r', ''))
        f1.close()

    # 输出至 output1.txt
    if len(results_list_A) > 1:
        f = open("output1.txt", "w")
        for x in results_list_A:
            f.write(x+"\n")
        f.close()
        print("基于组织的字典内容已生成至 output1.txt")
        print("\n")

def results_list_B():

    # 生成相应规则(基于人员)
    results_list_B = []

    if PersonName:
        PersonName_array1=pinyin(PersonName, style=Style.NORMAL, strict=False)
        PersonName_array2=pinyin(PersonName, style=Style.FIRST_LETTER, strict=False)
        PersonName_str1 = ""
        PersonName_str2 = ""

        for tempvar in PersonName_array1:
            temp_str1 = "".join(tempvar)
            PersonName_str1 = PersonName_str1 + temp_str1

        for tempvar in PersonName_array2:
            temp_str2 = "".join(tempvar)
            PersonName_str2 = PersonName_str2 + temp_str2

        PersonName_str3 = "".join(PersonName_array1[0])
        for tempvar in PersonName_array2[1:]:
            temp_str2 = "".join(tempvar)
            PersonName_str3 = PersonName_str3 + temp_str2

        results_list_B.append(PersonName_str1)
        results_list_B.append(PersonName_str2)
        results_list_B.append(PersonName_str3)

        # zhangsan
        print("PersonName_str1       : ",PersonName_str1)
        # zs
        print("PersonName_str2       : ",PersonName_str2)
        # zhangs
        print("PersonName_str3       : ",PersonName_str3)

    # 输出至 output2.txt
    if len(results_list_B) > 1:
        f = open("output2.txt", "w")
        for x in results_list_B:
            f.write(x+"\n")
        f.close()
        print("基于组织的字典内容已生成至 output2.txt")
        print("\n")

def results_list_C():

    # 生成相应规则(基于地点)
    results_list_C = []

    print("省份名称: " + ProvinceName)
    print("城市名称: " + CityName)
    print("区县名称: " + DistrictName)

def main():

    global CompanyName
    global ShortCompanyName
    global SystemName
    global StreetName
    global PersonName
    global PersonPhoneNumber
    global PersonEmail
    #global ProvinceName
    #global CityName
    #global DistrictName

    CompanyName = input("公司/单位/组织全称  (例如: 江苏XX有限公司):").lower()
    ShortCompanyName = input("公司/单位/组织简称  (例如: XX公司):").lower()
    SystemName = input("系统/业务简称       (例如: 智慧交通):").lower()
    PersonName = input("人员名称            (例如: 申田由甲):").lower()
    #PhoneNumber = input("电话号码(例如:13333333333 可为空): ").lower()
    #Email = input("电子邮箱(例如:test@163.com 可为空): ").lower()

    #ProvinceName = input("省份名称(例如:江苏 ,可为空): ").lower()
    #CityName = input("城市名称(例如:南京 ,可为空): ").lower()
    #DistrictName = input("区县名称(例如:江宁 ,可为空): ").lower()
    print("\n")

    results_list_A()
    results_list_B()
    #results_list_C()

if __name__ == '__main__':
    main()
