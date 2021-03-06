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
1，把calls当中所有播出的号码，加入到set当中，去重
和calls当中接受电话对比，如果不存在，则认定为推销电话
2，再和texts当中的发送方和接受方对比，如果都不存在其中，则认为是推销号码
"""
"""主叫号码"""
caller1 = set()
"""被叫号码"""
caller2 = set()
"""短信发送"""
texter1 = set()
"""短信接收"""
texter2 = set()

"""嫌疑号码"""
suspect_caller = set()
real_suspect_caller = set()

for call_elements in calls:
    caller1.add(call_elements[0])
    caller2.add(call_elements[1])

for call_elements in texts:
    caller2.add(call_elements[0])
    caller2.add(call_elements[1])


"""caller1 减去 callere2 当中的集合，剩下的未接收电话，发送短信，接受短信的号码"""
caller1 -= caller2

print("These numbers could be telemarketers: \n"+"\n".join(sorted(caller1)))
"""
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

