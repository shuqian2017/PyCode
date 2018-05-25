# -*-coding:utf-8 -*-

import re
import sys


def remove_space(data_list):
    '''去除列表中的空格元素'''
    for i in data_list:
        if type(i) is not int:
            if len(i.strip()) == 0:
                data_list.remove(i)
    return data_list

def fetch_data_from_bracket(data_list, first_right_bracket_pos):
    '''用递归的形式取出每一对括号里的数据并进行运算且得出结果'''
    print('data_list:', data_list)

    left_bracket_pos, right_bracket_pos = data_list.index('('), data_list.index(')') + 1
    print('\033[31;1mleft bracket pos:%s right_bracket_pos: %s\033[0m' % (left_bracket_pos, first_right_bracket_pos))
    data_after_strip = data_list[left_bracket_pos: right_bracket_pos]

    if data_after_strip.count("(") > 1:
        print('fetch_data_from_bracket:%s \033[31;1m%s\033[0m left pos:%s' % (data_after_strip, data_after_strip[1:], left_bracket_pos))
        return fetch_data_from_bracket(data_after_strip[1:], first_right_bracket_pos)

    else:
        print('last:', len(data_after_strip), data_after_strip)
        bracket_start_pos = first_right_bracket_pos - len(data_after_strip) + 1
        calc_res = parse_operator(data_after_strip)
        return calc_res, bracket_start_pos, first_right_bracket_pos + 1

def parse_bracket(formula):  # 解析空格中的公式
    '''解析空格中的公式，并运算出结果'''
    pattern = r"\(.+\)"
    m = re.search(pattern, formula)   # 匹配出所有的括号
    print(m)
    if m:
        data_with_brackets = m.group()
        data_with_brackets = remove_space(list(data_with_brackets))
        calc_res = fetch_data_from_bracket(data_with_brackets, data_with_brackets.index(')'))
        print('\033[33;1mResult:\033[0m', calc_res)
        print(calc_res[1], calc_res[2])
        print(data_with_brackets[calc_res[1]:calc_res[2]])
        del data_with_brackets[calc_res[1]:calc_res[2]]
        data_with_brackets.insert(calc_res[1], str(calc_res[0]))
        return parse_bracket(''.join(data_with_brackets))   # 继续处理其他的括号
    else:
        print('\033[30;1mCaculation result:\033[0m', formula)

def caculate_1(formula):
    result = int(formula[0])
    last_operator = None
    formula = list(formula)
    nagative_mark = False
    for index, i in enumerate(formula[1:]):
        if i.isdigit():
            if nagative_mark:
                i = int('-'+i)
                nagative_mark = False
            else:
                i = int(i)
            if last_operator == '*':
                result *= i
            elif last_operator == '/':
                try:
                    result /= i
                except ZeroDivisionError as e:
                    print('\033[31;1mError:%s\033[0m' % e)
                    sys.exit()
        elif i == '-':
            nagative_mark = True
        else:
            last_operator = i

    print('乘法运算结果:', result)
    return result

def caculate_2(data_list, operator_list):
    '''eg.data_list:['4',3,1372,'1'] operator_list:['-', '+', '-']'''
    data_list = remove_space(data_list)
    print('caculater_2:', data_list, operator_list)
    result = int(data_list[0])
    for i in data_list[1:]:
        if operator_list[0] == '+':
            result += int(i)
        elif operator_list[0] == '-':
            result -= int(i)
        del operator_list[0]
    print('caculate_2 result:', result)
    return result

def parse_operator(formula):
    print('开始运算公式:', formula)
    formula = formula[1:-1]
    low_priorities = re.findall('[+,-]', ''.join(formula))
    data_after_remove_low_priorities = re.split('[+,-]', ''.join(formula))
    print('去掉加减后的公式列表，先算乘除:', data_after_remove_low_priorities)

    # enumerate()函数用于将一个可遍历的数据对象，组合成一个索引序列，同时列出下标，一般用作for循环中
    for index, i in enumerate(data_after_remove_low_priorities):
        if i.endswith("*") or i.endswith("/"):
            data_after_remove_low_priorities[index] += '-' + data_after_remove_low_priorities[index+1]
            del data_after_remove_low_priorities[index+1]
    print('------------>handle nagative num:', data_after_remove_low_priorities)
    # 计算乘除运算
    nagative_mark = False

    for index, i in enumerate(data_after_remove_low_priorities):
        if not i.isdigit():
            if len(i.strip()) == 0:
                nagative_mark = True
            else:
                string_to_list = []
                if nagative_mark:
                    prior_1 = '-' + i[0]
                    nagative_mark = False
                else:
                    prior_1 = i[0]
                for l in i[1:]:
                    if l.isdigit():
                        if prior_1.isdigit() or len(prior_1) > 1:
                            prior_1 += 1
                        else:
                            prior_1 = 1
                    else:
                        string_to_list.append(prior_1)
                        string_to_list.append(l)
                        prior_1 = 1
                else:
                    string_to_list.append(prior_1)

                print('------>::', string_to_list)
                calc_res = caculate_1(string_to_list)   # 乘除运算结果
                data_after_remove_low_priorities[index] = calc_res
                '''operators = re.findall('[*,/]', i)
                data = re.split('[*,/]', i)
                combine_to_one_list = map(None, data, operators)
                combine_to_one_list = re.split("[\[,\],\(,), '', None]", str(combine_to_one_list))
                combine_to_one_list = ''.join(combine_to_one_list).split()
                print('--->', combine_to_one_list)'''

        else:
            if nagative_mark:
                data_after_remove_low_priorities[index] = '-' + i
    print('去掉* 和 / 后开始运算加减：', data_after_remove_low_priorities, low_priorities)
    # 计算加减运算
    return caculate_2(data_after_remove_low_priorities, low_priorities)

def main():
    while True:
        user_input = input(">>>:").strip()
        if len(user_input) == 0:
            continue
        user_input = '(' + user_input + ')'
        parse_bracket(user_input)

        print('\033[44;1mpython计算器运算结果：\033[0m', eval(user_input))

if __name__ == "__main__":
    main()
