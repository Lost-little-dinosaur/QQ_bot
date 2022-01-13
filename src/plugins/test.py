# import time
#
# hour = 1
# min = 5
# second = 6
# hours = []
# mins = []
# seconds = []
# timestamps = []
# ids = []
#
# temp = time.strftime('%Y-%m-%d %H:%M:%S',
#                      time.localtime(time.time() + int(hour) * 3600 + int(min) * 60 + int(second)))
# s = '3144794112'
#
# with open('timing.txt', 'a') as f1:
#     f1.write('0:' + temp + str(hour) + str(min) + str(second) + "id:" + s + '\n')
# with open('timing.txt', 'r') as f2:  # 把历史文档中的时间读取出来，转化成时间戳，和当前时间对比后生成对应还剩多少小时、分钟和秒
#     for line in f2.readlines():
#         accurate_time = str(line[2:line.find('id:') - 3])
#         # print(accurate_time)
#         time_array = time.strptime(accurate_time, "%Y-%m-%d %H:%M:%S")
#         timestamps.append(int(time.mktime(time_array)))
#         deta_time = float(
#             str(int(time.mktime(time_array))) + '.' + line[line.find('id:') - 3:line.find('id:')]) - time.time()
#         hours.append(deta_time // 3600)
#         mins.append((deta_time - (deta_time // 3600) * 3600) // 60)
#         seconds.append(deta_time - (deta_time // 3600) * 3600 - ((deta_time - (deta_time // 3600) * 3600) // 60) * 60)
#
#         ids.append(line[line.find('id:') + 3:].strip('\n'))
#
# print(hours)
# print(mins)
# print(seconds)
# print(ids)
