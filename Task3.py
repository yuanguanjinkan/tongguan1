"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    """
    循环遍历文件当中以（080）开头的拨出号码，将被拨打方的号码放入set当中去重
    """
    calledByBangalore = set()
for call_elements in calls:
    if call_elements[0].startswith('(080)'):
        if call_elements[1].startswith('('):
            calledByBangalore.add(call_elements[1][int(call_elements[1].find('(')): int(call_elements[1].find(')'))+1])
        elif call_elements[1].startswith('7') or call_elements[1].startswith('8') or call_elements[1].startswith('9'):
            calledByBangalore.add(call_elements[1][0: 4])


listcalledByBangalore = list(calledByBangalore)
listcalledByBangalore.sort()
for called_elements in listcalledByBangalore:
    print("The numbers called by people in Bangalore have codes:"+called_elements)

"""
由班加罗尔播王班加罗尔电话占比
"""

count_fromb_tob = 0
count_fromb = 0
for call_elements in calls:
    if call_elements[0].startswith('(080)'):
        count_fromb += 1
    if call_elements[0].startswith('(080)') and call_elements[1].startswith('(080)'):
        count_fromb_tob += 1

print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round(count_fromb_tob*100/count_fromb,2)))

"""
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""
