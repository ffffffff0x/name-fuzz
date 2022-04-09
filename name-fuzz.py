#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import readline
from pypinyin import pinyin, lazy_pinyin, Style

# suffix 字典
filename="suffix.txt"

# 检验名称输入是否全是中文字符
def is_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True

# 拼音分词
class PyTrieNode(object):
    def __init__(self, key="", seq=[]):
        self.key = key
        self.end = len(seq) == 0
        self.children = {}
        if len(seq) > 0:
            self.children[seq[0]] = PyTrieNode(seq[0], seq[1:])

    def add(self, seq):
        if len(seq) == 0:
            self.end = True
        else:
            key = seq[0]
            value = seq[1:]
            if key in self.children:
                self.children[key].add(value)
            else:
                self.children[key] = PyTrieNode(key, value)

    def find(self, sent):
        for i in range(len(sent)):
            i = len(sent) - i
            if len(sent) >= i:
                key = sent[:i]
                if key in self.children:
                    buf, succ = self.children[key].find(sent[i:])
                    if succ:
                        return key + buf, True
        return "", self.end

class PyTrie(object):
    def __init__(self):
        self.root = PyTrieNode()
        self.root.end = False

    def setup(self):
        self.add(["a"])
        self.add(["ai"])
        self.add(["an"])
        self.add(["ang"])
        self.add(["ao"])
        self.add(["e"])
        self.add(["ei"])
        self.add(["en"])
        self.add(["er"])
        self.add(["o"])
        self.add(["ou"])
        self.add(["b", "a"])
        self.add(["b", "ai"])
        self.add(["b", "an"])
        self.add(["b", "ang"])
        self.add(["b", "ao"])
        self.add(["b", "ei"])
        self.add(["b", "en"])
        self.add(["b", "eng"])
        self.add(["b", "i"])
        self.add(["b", "ian"])
        self.add(["b", "iao"])
        self.add(["b", "ie"])
        self.add(["b", "in"])
        self.add(["b", "ing"])
        self.add(["b", "o"])
        self.add(["b", "u"])
        self.add(["c", "a"])
        self.add(["c", "ai"])
        self.add(["c", "an"])
        self.add(["c", "ang"])
        self.add(["c", "ao"])
        self.add(["c", "e"])
        self.add(["c", "en"])
        self.add(["c", "eng"])
        self.add(["c", "i"])
        self.add(["c", "ong"])
        self.add(["c", "ou"])
        self.add(["c", "u"])
        self.add(["c", "uan"])
        self.add(["c", "ui"])
        self.add(["c", "un"])
        self.add(["c", "uo"])
        self.add(["ch", "a"])
        self.add(["ch", "ai"])
        self.add(["ch", "an"])
        self.add(["ch", "ang"])
        self.add(["ch", "ao"])
        self.add(["ch", "e"])
        self.add(["ch", "en"])
        self.add(["ch", "eng"])
        self.add(["ch", "i"])
        self.add(["ch", "ong"])
        self.add(["ch", "ou"])
        self.add(["ch", "u"])
        self.add(["ch", "uai"])
        self.add(["ch", "uan"])
        self.add(["ch", "uang"])
        self.add(["ch", "ui"])
        self.add(["ch", "un"])
        self.add(["ch", "uo"])
        self.add(["d", "a"])
        self.add(["d", "ai"])
        self.add(["d", "an"])
        self.add(["d", "ang"])
        self.add(["d", "ao"])
        self.add(["d", "e"])
        self.add(["d", "eng"])
        self.add(["d", "i"])
        self.add(["d", "ia"])
        self.add(["d", "ian"])
        self.add(["d", "iao"])
        self.add(["d", "ie"])
        self.add(["d", "ing"])
        self.add(["d", "iu"])
        self.add(["d", "ong"])
        self.add(["d", "ou"])
        self.add(["d", "u"])
        self.add(["d", "uan"])
        self.add(["d", "ui"])
        self.add(["d", "un"])
        self.add(["d", "uo"])
        self.add(["f", "a"])
        self.add(["f", "an"])
        self.add(["f", "ang"])
        self.add(["f", "ei"])
        self.add(["f", "en"])
        self.add(["f", "eng"])
        self.add(["f", "o"])
        self.add(["f", "ou"])
        self.add(["f", "u"])
        self.add(["g", "a"])
        self.add(["g", "ai"])
        self.add(["g", "an"])
        self.add(["g", "ang"])
        self.add(["g", "ao"])
        self.add(["g", "e"])
        self.add(["g", "ei"])
        self.add(["g", "en"])
        self.add(["g", "eng"])
        self.add(["g", "ong"])
        self.add(["g", "ou"])
        self.add(["g", "u"])
        self.add(["g", "ua"])
        self.add(["g", "uai"])
        self.add(["g", "uan"])
        self.add(["g", "uang"])
        self.add(["g", "ui"])
        self.add(["g", "un"])
        self.add(["g", "uo"])
        self.add(["h", "a"])
        self.add(["h", "ai"])
        self.add(["h", "an"])
        self.add(["h", "ang"])
        self.add(["h", "ao"])
        self.add(["h", "e"])
        self.add(["h", "ei"])
        self.add(["h", "en"])
        self.add(["h", "eng"])
        self.add(["h", "ong"])
        self.add(["h", "ou"])
        self.add(["h", "u"])
        self.add(["h", "ua"])
        self.add(["h", "uai"])
        self.add(["h", "uan"])
        self.add(["h", "uang"])
        self.add(["h", "ui"])
        self.add(["h", "un"])
        self.add(["h", "uo"])
        self.add(["j", "i"])
        self.add(["j", "ia"])
        self.add(["j", "ian"])
        self.add(["j", "iang"])
        self.add(["j", "iao"])
        self.add(["j", "ie"])
        self.add(["j", "in"])
        self.add(["j", "ing"])
        self.add(["j", "iong"])
        self.add(["j", "iu"])
        self.add(["j", "u"])
        self.add(["j", "uan"])
        self.add(["j", "ue"])
        self.add(["j", "un"])
        self.add(["k", "a"])
        self.add(["k", "ai"])
        self.add(["k", "an"])
        self.add(["k", "ang"])
        self.add(["k", "ao"])
        self.add(["k", "e"])
        self.add(["k", "en"])
        self.add(["k", "eng"])
        self.add(["k", "ong"])
        self.add(["k", "ou"])
        self.add(["k", "u"])
        self.add(["k", "ua"])
        self.add(["k", "uai"])
        self.add(["k", "uan"])
        self.add(["k", "uang"])
        self.add(["k", "ui"])
        self.add(["k", "un"])
        self.add(["k", "uo"])
        self.add(["l", "a"])
        self.add(["l", "ai"])
        self.add(["l", "an"])
        self.add(["l", "ang"])
        self.add(["l", "ao"])
        self.add(["l", "e"])
        self.add(["l", "ei"])
        self.add(["l", "eng"])
        self.add(["l", "i"])
        self.add(["l", "ia"])
        self.add(["l", "ian"])
        self.add(["l", "iang"])
        self.add(["l", "iao"])
        self.add(["l", "ie"])
        self.add(["l", "in"])
        self.add(["l", "ing"])
        self.add(["l", "iu"])
        self.add(["l", "ong"])
        self.add(["l", "ou"])
        self.add(["l", "u"])
        self.add(["l", "u:"])
        self.add(["l", "u:e"])
        self.add(["l", "uan"])
        self.add(["l", "un"])
        self.add(["l", "uo"])
        self.add(["m", ""])
        self.add(["m", "a"])
        self.add(["m", "ai"])
        self.add(["m", "an"])
        self.add(["m", "ang"])
        self.add(["m", "ao"])
        self.add(["m", "e"])
        self.add(["m", "ei"])
        self.add(["m", "en"])
        self.add(["m", "eng"])
        self.add(["m", "i"])
        self.add(["m", "ian"])
        self.add(["m", "iao"])
        self.add(["m", "ie"])
        self.add(["m", "in"])
        self.add(["m", "ing"])
        self.add(["m", "iu"])
        self.add(["m", "o"])
        self.add(["m", "ou"])
        self.add(["m", "u"])
        self.add(["n", "a"])
        self.add(["n", "ai"])
        self.add(["n", "an"])
        self.add(["n", "ang"])
        self.add(["n", "ao"])
        self.add(["n", "e"])
        self.add(["n", "ei"])
        self.add(["n", "en"])
        self.add(["n", "eng"])
        self.add(["n", "g"])
        self.add(["n", "i"])
        self.add(["n", "ian"])
        self.add(["n", "iang"])
        self.add(["n", "iao"])
        self.add(["n", "ie"])
        self.add(["n", "in"])
        self.add(["n", "ing"])
        self.add(["n", "iu"])
        self.add(["n", "ong"])
        self.add(["n", "ou"])
        self.add(["n", "u"])
        self.add(["n", "u:"])
        self.add(["n", "u:e"])
        self.add(["n", "uan"])
        self.add(["n", "uo"])
        self.add(["p", "a"])
        self.add(["p", "ai"])
        self.add(["p", "an"])
        self.add(["p", "ang"])
        self.add(["p", "ao"])
        self.add(["p", "ei"])
        self.add(["p", "en"])
        self.add(["p", "eng"])
        self.add(["p", "i"])
        self.add(["p", "ian"])
        self.add(["p", "iao"])
        self.add(["p", "ie"])
        self.add(["p", "in"])
        self.add(["p", "ing"])
        self.add(["p", "o"])
        self.add(["p", "ou"])
        self.add(["p", "u"])
        self.add(["q", "i"])
        self.add(["q", "ia"])
        self.add(["q", "ian"])
        self.add(["q", "iang"])
        self.add(["q", "iao"])
        self.add(["q", "ie"])
        self.add(["q", "in"])
        self.add(["q", "ing"])
        self.add(["q", "iong"])
        self.add(["q", "iu"])
        self.add(["q", "u"])
        self.add(["q", "uan"])
        self.add(["q", "ue"])
        self.add(["q", "un"])
        self.add(["r", "an"])
        self.add(["r", "ang"])
        self.add(["r", "ao"])
        self.add(["r", "e"])
        self.add(["r", "en"])
        self.add(["r", "eng"])
        self.add(["r", "i"])
        self.add(["r", "ong"])
        self.add(["r", "ou"])
        self.add(["r", "u"])
        self.add(["r", "uan"])
        self.add(["r", "ui"])
        self.add(["r", "un"])
        self.add(["r", "uo"])
        self.add(["s", "a"])
        self.add(["s", "ai"])
        self.add(["s", "an"])
        self.add(["s", "ang"])
        self.add(["s", "ao"])
        self.add(["s", "e"])
        self.add(["s", "en"])
        self.add(["s", "eng"])
        self.add(["s", "i"])
        self.add(["s", "ong"])
        self.add(["s", "ou"])
        self.add(["s", "u"])
        self.add(["s", "uan"])
        self.add(["s", "ui"])
        self.add(["s", "un"])
        self.add(["s", "uo"])
        self.add(["sh", "a"])
        self.add(["sh", "ai"])
        self.add(["sh", "an"])
        self.add(["sh", "ang"])
        self.add(["sh", "ao"])
        self.add(["sh", "e"])
        self.add(["sh", "ei"])
        self.add(["sh", "en"])
        self.add(["sh", "eng"])
        self.add(["sh", "i"])
        self.add(["sh", "ou"])
        self.add(["sh", "u"])
        self.add(["sh", "ua"])
        self.add(["sh", "uai"])
        self.add(["sh", "uan"])
        self.add(["sh", "uang"])
        self.add(["sh", "ui"])
        self.add(["sh", "un"])
        self.add(["sh", "uo"])
        self.add(["t", "a"])
        self.add(["t", "ai"])
        self.add(["t", "an"])
        self.add(["t", "ang"])
        self.add(["t", "ao"])
        self.add(["t", "e"])
        self.add(["t", "eng"])
        self.add(["t", "i"])
        self.add(["t", "ian"])
        self.add(["t", "iao"])
        self.add(["t", "ie"])
        self.add(["t", "ing"])
        self.add(["t", "ong"])
        self.add(["t", "ou"])
        self.add(["t", "u"])
        self.add(["t", "uan"])
        self.add(["t", "ui"])
        self.add(["t", "un"])
        self.add(["t", "uo"])
        self.add(["w", "a"])
        self.add(["w", "ai"])
        self.add(["w", "an"])
        self.add(["w", "ang"])
        self.add(["w", "ei"])
        self.add(["w", "en"])
        self.add(["w", "eng"])
        self.add(["w", "o"])
        self.add(["w", "u"])
        self.add(["x", "i"])
        self.add(["x", "ia"])
        self.add(["x", "ian"])
        self.add(["x", "iang"])
        self.add(["x", "iao"])
        self.add(["x", "ie"])
        self.add(["x", "in"])
        self.add(["x", "ing"])
        self.add(["x", "iong"])
        self.add(["x", "iu"])
        self.add(["x", "u"])
        self.add(["x", "uan"])
        self.add(["x", "ue"])
        self.add(["x", "un"])
        self.add(["y", "a"])
        self.add(["y", "an"])
        self.add(["y", "ang"])
        self.add(["y", "ao"])
        self.add(["y", "e"])
        self.add(["y", "i"])
        self.add(["y", "iao"])
        self.add(["y", "in"])
        self.add(["y", "ing"])
        self.add(["y", "o"])
        self.add(["y", "ong"])
        self.add(["y", "ou"])
        self.add(["y", "u"])
        self.add(["y", "uan"])
        self.add(["y", "ue"])
        self.add(["y", "un"])
        self.add(["z", "a"])
        self.add(["z", "ai"])
        self.add(["z", "an"])
        self.add(["z", "ang"])
        self.add(["z", "ao"])
        self.add(["z", "e"])
        self.add(["z", "ei"])
        self.add(["z", "en"])
        self.add(["z", "eng"])
        self.add(["z", "i"])
        self.add(["z", "ong"])
        self.add(["z", "ou"])
        self.add(["z", "u"])
        self.add(["z", "uan"])
        self.add(["z", "ui"])
        self.add(["z", "un"])
        self.add(["z", "uo"])
        self.add(["zh", "a"])
        self.add(["zh", "ai"])
        self.add(["zh", "an"])
        self.add(["zh", "ang"])
        self.add(["zh", "ao"])
        self.add(["zh", "e"])
        self.add(["zh", "en"])
        self.add(["zh", "eng"])
        self.add(["zh", "i"])
        self.add(["zh", "ong"])
        self.add(["zh", "ou"])
        self.add(["zh", "u"])
        self.add(["zh", "ua"])
        self.add(["zh", "uai"])
        self.add(["zh", "uan"])
        self.add(["zh", "uang"])
        self.add(["zh", "ui"])
        self.add(["zh", "un"])
        self.add(["zh", "uo"])

    def add(self, seq):
        self.root.add(seq)

    def scan(self, sent):
        words = []
        while len(sent) > 0:
            buf, succ = self.root.find(sent)
            # print("buf: {}, succ: {}".format(buf, succ))
            if succ:
                words.append(buf)
                sent = sent[len(buf):]
            else:
                words.append('invalid:' + sent[0])
                sent = sent[1:]
        return words

# 生成相应规则(基于组织)
def results_list_A():

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

        CompanyName_str3 = CompanyName_str2[0].upper()+CompanyName_str2[1:]

        # jiangsuxxyouxiangongsi
        print("CompanyName_str1      : ",CompanyName_str1)
        # jsxxyxgs
        print("CompanyName_str2      : ",CompanyName_str2)
        # Jsxxyxgs
        print("CompanyName_str3      : ",CompanyName_str3)

        # jsxxyxgs + 后缀
        f1 = open(filename, "r")
        for line in f1:
            results_list_A.append(CompanyName_str2+line.replace('\n', '').replace('\r', ''))
        f1.close()

        f = open("output0.txt", "w")
        f.write(CompanyName_str1+"\n")
        f.write(CompanyName_str2+"\n")
        f.write(CompanyName_str3+"\n")
        f.close()

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

        ShortCompanyName_str3 = ShortCompanyName_str1[0].upper()+ShortCompanyName_str1[1:]

        ShortCompanyName_str4 = ShortCompanyName_str2[0].upper()+ShortCompanyName_str2[1:]

        ShortCompanyName_str5 = ShortCompanyName_str2.upper()

        # jiangsuxx
        print("ShortCompanyName_str1 : ",ShortCompanyName_str1)
        # jsxx
        print("ShortCompanyName_str2 : ",ShortCompanyName_str2)
        # Jiangsuxx
        print("ShortCompanyName_str3 : ",ShortCompanyName_str3)
        # Jsxx
        print("ShortCompanyName_str4 : ",ShortCompanyName_str4)
        # JSXX
        print("ShortCompanyName_str5 : ",ShortCompanyName_str5)

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

        # Jsxx + 后缀
        f1 = open(filename, "r")
        for line in f1:
            results_list_A.append(ShortCompanyName_str4+line.replace('\n', '').replace('\r', ''))
        f1.close()

        # JSXX + 后缀
        f1 = open(filename, "r")
        for line in f1:
            results_list_A.append(ShortCompanyName_str5+line.replace('\n', '').replace('\r', ''))
        f1.close()

        f = open("output0.txt", "a")
        f.write(ShortCompanyName_str1+"\n")
        f.write(ShortCompanyName_str2+"\n")
        f.write(ShortCompanyName_str3+"\n")
        f.write(ShortCompanyName_str4+"\n")
        f.write(ShortCompanyName_str5+"\n")
        f.close()

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

        f = open("output0.txt", "a")
        f.write(SystemName_str1+"\n")
        f.write(SystemName_str2+"\n")
        f.close()

    # 输出至 output1.txt
    if len(results_list_A) > 1:
        f = open("output1.txt", "w")
        for x in results_list_A:
            f.write(x+"\n")
        f.close()
        print("基于组织的简写内容已生成至 output0.txt")
        print("基于组织的字典内容已生成至 output1.txt")
        print("\n")

# 生成相应规则(基于人员)
def results_list_B():

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

# 生成相应规则(基于人员拼音)
def results_list_C():

    results_list_C = []

    if PersonName:
        pyt = PyTrie()
        pyt.setup()
        PersonName_array3 = pyt.scan(PersonName)
        PersonName_str4=""
        PersonName_str5=""
        PersonName_str6=""

        for tempvar in PersonName_array3:
            temp_str1 = "".join(tempvar)
            PersonName_str4 = PersonName_str4 + temp_str1

        for tempvar in PersonName_array3:
            temp_str2 = "".join(tempvar)[0]
            PersonName_str5 = PersonName_str5 + temp_str2

        PersonName_str6 = "".join(PersonName_array3[0])
        for tempvar in PersonName_array3[1:]:
            temp_str3 = "".join(tempvar)[0]
            PersonName_str6 = PersonName_str6 + temp_str3

        results_list_C.append(PersonName_str4)
        results_list_C.append(PersonName_str5)
        results_list_C.append(PersonName_str6)

        # zhangsan
        print("PersonName_str4       : ",PersonName_str4)
        # zs
        print("PersonName_str5       : ",PersonName_str5)
        # zhangs
        print("PersonName_str6       : ",PersonName_str6)

    # 输出至 output2.txt
    if len(results_list_C) > 1:
        f = open("output2.txt", "w")
        for x in results_list_C:
            f.write(x+"\n")
        f.close()
        print("基于组织的字典内容已生成至 output2.txt")
        print("\n")

# 生成相应规则(基于地点)
def results_list_D():

    results_list_D = []

    # print("省份名称: " + ProvinceName)
    # print("城市名称: " + CityName)
    # print("区县名称: " + DistrictName)

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
    ShortCompanyName = input("公司/单位/组织简称  (例如: 江苏XX):").lower()
    SystemName = input("系统/业务简称       (例如: 智慧交通):").lower()
    PersonName = input("人员名称            (例如: 申田由甲):").lower()

    #PhoneNumber = input("电话号码(例如:13333333333 可为空): ").lower()
    #Email = input("电子邮箱(例如:test@163.com 可为空): ").lower()
    #ProvinceName = input("省份名称(例如:江苏 ,可为空): ").lower()
    #CityName = input("城市名称(例如:南京 ,可为空): ").lower()
    #DistrictName = input("区县名称(例如:江宁 ,可为空): ").lower()

    print("\n")
    results_list_A()

    if is_all_chinese(PersonName):
        results_list_B()
    else:
        results_list_C()

if __name__ == '__main__':
    main()
