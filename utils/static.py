# sent = '赛前，中国女足就意识到这是一场“攻坚战”。在去年的雅加达亚运会女足半决赛中，中国女足发动了134次危险进攻，但30次射门仅4次射正，12次角球无一次转化为进球，最终同样仅以1比0小胜。'
# print(list(SentenceSplitter.split(sent)))
# ex = list('oiooiugd')
# ex[0]=chr(ord(ex[0])-32)
# print(ex[0]>'A')
# print(ex)

# s = '黎巴嫩 阿拉伯语 塞浦路斯 希腊语、土耳其语 沙特阿拉伯 阿拉伯语 土耳其 土耳其语 叙利亚 阿拉伯语 亚美尼亚 亚美尼亚语 也门 阿拉伯语 伊拉克 阿拉伯语 伊朗 波斯语 以色列 希伯来语、阿拉伯语 约旦 阿拉伯语 阿尔巴尼亚 阿尔巴尼亚语 爱沙尼亚 爱沙尼亚语 保加利亚 保加利亚语 波兰 波兰语 波斯尼亚和黑 塞哥维那 波斯尼亚语、克罗地亚语、 塞尔维亚语 黑山 黑山语 捷克 捷克语 克罗地亚 克罗地亚语 拉脱维亚 拉脱维亚语 立陶宛 立陶宛语 罗马尼亚 罗马尼亚语 马其顿 马其顿语 塞尔维亚 塞尔维亚语 斯洛伐克 斯洛伐克语 斯洛文尼亚 斯洛文尼亚语 匈牙利 匈牙利语 白俄罗斯 白俄罗斯语、俄语 俄罗斯 俄语 摩尔多瓦 罗马尼亚语 乌克兰 乌克兰语'
# ss = s.split(' ')
# s0=[]
# s1=[]
# for i in range(len(ss)):
#     if i%2==0:
#         s0.append(ss[i])
#     else:
#         s1.append(ss[i])
# print('\n'.join(s0))
# print('===========')
# print('\n'.join(s1))
_dict = {}
coun_dict = {}
cover_dict = {}
lan = '德顿语、葡萄牙语 菲律宾语、英语 柬埔寨语 老挝语 马来语、英语 缅甸语 泰语 马来语、英语 马来语、华语、泰米尔语、英语 印尼语 越南语 蒙古语 乌尔都语、英语 宗卡语、英语 迪维希语、英语 孟加拉语、英语 尼泊尔语、英语 僧伽罗语、泰米尔语、英语 印地语、英语 哈萨克语、俄语 吉尔吉斯语、俄语 塔吉克语、俄语 土库曼语、俄语 乌兹别克语、俄语 波斯语、普什图语 阿拉伯语 阿拉伯语 阿塞拜疆语、俄语 阿拉伯语 阿拉伯语 格鲁吉亚语、俄语 阿拉伯语 阿拉伯语 阿拉伯语 希腊语、土耳其语、英语 阿拉伯语 土耳其语 阿拉伯语 亚美尼亚语、俄语 阿拉伯语 阿拉伯语 波斯语 希伯来语、阿拉伯语 阿拉伯语 阿尔巴尼亚语 爱沙尼亚语、英语、俄语 保加利亚语 波兰语 波斯尼亚语、克罗地亚语、塞尔维亚语 黑山语 捷克语 克罗地亚语 拉脱维亚语、俄语 立陶宛语、俄语 罗马尼亚语 马其顿语 塞尔维亚语 斯洛伐克语 斯洛文尼亚语 匈牙利语 白俄罗斯语、俄语 俄语 罗马尼亚语、俄语 乌克兰语、俄语 阿拉伯语 法语 法语 西班牙语、法语、葡萄牙语 西班牙语 科摩罗语、法语、阿拉伯语 英语、塞苏陀语 法语、班巴拉语 英语、皮金语 英语 英语 法语、德语、卢森堡语 意大利语 西班牙语 英语 葡萄牙语 英语、斐济语、印地语 英语 马耳他语、英语 西班牙语 西班牙语 西班牙语 荷兰语 萨摩亚语、英语 英语 英语、法语、比斯拉马语 汤加语、英语 库克群岛毛利语、英语 西班牙语 西班牙语 法语 英语 英语、斯瓦希里语 基隆迪语、法语 英语、绍纳语、恩德贝莱语 法语、阿拉伯语 斯瓦希里语、英语 英语 葡萄牙语 英语 英语、阿拉伯语 英语 阿拉伯语、法语 阿拉伯语、法语 法语 希腊语 葡萄牙语、克里奥尔语 斯瓦希里语、英语 法语 英语 葡萄牙语 法语、芳语、米耶内语、巴太凯语 英语 克里奥尔语、英语、法语 法语、英语 法语 西班牙语 法语、哈桑语、布拉尔语、索宁克语、沃洛夫语 索马里语、阿拉伯语、英语、意大利语 西班牙语 纽埃语、英语 英语、克里奥尔语、乌尔都语、印第安语、印地语 法语、沃洛夫语 阿拉伯语 西班牙语、克丘亚语、阿依马拉语 英语 法语、马达加斯加语 阿拉伯语、法语 阿拉伯语、英语 英语 卢旺达语、英语、法语、斯瓦希里语 阿拉伯语 英语 英语 德语 西班牙语 阿姆哈拉语、英语 英语、毛利语 马其顿语'
for i,item in enumerate(lan.split(' ')):
    for it in item.split('、'):
        if it in _dict:
            _dict[it] += 1
        else:
            _dict[it] = 1
    coun_dict[i] = item.split('、')
s = sorted(_dict.items(), key=lambda d: d[1], reverse=True)
# keys = []
# for i in s:
#     (l,n) = i
#     # print(l)
#     keys.append(l)
#
# keys = list(_dict.keys())
# dic1 = []
# dic2 = []
# other = []
# num = len(keys)
# print(keys)
# print(coun_dict)
# for i in range(num):
#     mx = []
#     ind = ''
#     for j in range(num):
#         lan = keys[j]
#         if lan in dic1:
#             continue
#         temp = []
#         for coun in coun_dict:
#             if lan in coun_dict[coun]:
#                 if coun not in dic2:
#                     temp.append(coun)
#         if len(temp)==0:
#             continue
#         if len(temp)>len(mx):
#             mx = temp.copy()
#             ind = lan
#         if len(temp)==len(mx):
#             try:
#                 if _dict[lan]>_dict[ind]:
#                     mx = temp.copy()
#                     ind = lan
#             except:
#                 print(temp)
#                 print(mx)
#     if len(mx)==0:
#         break
#     dic2+=mx
#     dic1.append(ind)
#     cover_dict[ind] = float(len(dic2))/float(len(coun_dict))
#     print('================')
#     print(dic1)
#     print(dic2)
# for i in range(num):
#     lan = keys[i]
#     if lan not in dic1:
#         other.append(lan)
# for item in dic1:
#     print(str(item))
#
# for item in other:
#     print(str(item))
#
# for item in dic1:
#     print(str(_dict[item]))
# for item in other:
#     print(str(_dict[item]))
#
# for item in dic1:
#     print(str(round(cover_dict[item],4)))
# print(other)
# s = sorted(_dict.items(), key=lambda d: d[1], reverse=True)
keys = []
for i in s:
    (l,n) = i
    # print(l)
    keys.append(l)
print(keys)
for i in s:
    (l,n) = i
    print(n)

# 德顿语、葡萄牙语 菲律宾语、英语 柬埔寨语 老挝语 马来语、英语 缅甸语 泰语 马来语、英语 马来语、华语、泰米尔语、 英语 印尼语 越南语 蒙古语 乌尔都语、英语 宗卡语、英语 迪维希语、英语 孟加拉语、英语 尼泊尔语、英语 僧伽罗语、泰米尔语、英语 印地语、英语 哈萨克语、俄语 吉尔吉斯语、俄语 塔吉克语、俄语 土库曼语、俄语 乌兹别克语、俄语 波斯语、普什图语 阿拉伯语 阿拉伯语 阿塞拜疆语、俄语 阿拉伯语 阿拉伯语 格鲁吉亚语、俄语 阿拉伯语 阿拉伯语 阿拉伯语 希腊语、土耳其语、英语 阿拉伯语 土耳其语 阿拉伯语 亚美尼亚语、俄语 阿拉伯语 阿拉伯语 波斯语 希伯来语、阿拉伯语 阿拉伯语 阿尔巴尼亚语 爱沙尼亚语、英语、俄语 保加利亚语 波兰语 波斯尼亚语、克罗地亚语、塞尔维亚语 黑山语 捷克语 克罗地亚语 拉脱维亚语、俄语 立陶宛语、俄语 罗马尼亚语 马其顿语 塞尔维亚语 斯洛伐克语 斯洛文尼亚语 匈牙利语 白俄罗斯语、俄语 俄语 罗马尼亚语、俄语 乌克兰语、俄语 阿拉伯语 法语 法语 西班牙语、法语、葡萄牙语 西班牙语 科摩罗语、法语、阿拉伯语 英语、塞苏陀语 法语、班巴拉语 英语、皮金语 英语 英语 法语、德语、卢森堡语 意大利语 西班牙语 英语 葡萄牙语 英语、斐济语、印地语 英语 马耳他语、英语 西班牙语 西班牙语 西班牙语 荷兰语 萨摩亚语、英语 英语 英语、法语、比斯拉马语 汤加语、英语 库克群岛毛利语、英语 西班牙语 西班牙语 法语 英语 英语、斯瓦希里语 基隆迪语、法语 英语、绍纳语、恩德贝莱语 法语、阿拉伯语 斯瓦希里语、英语 英语 葡萄牙语 英语 英语、阿拉伯语 英语 阿拉伯语、法语 阿拉伯语、法语 法语 希腊语 葡萄牙语、克里奥尔语 斯瓦希里语、英语 法语 英语 葡萄牙语 法语、芳语、米耶内语、巴太凯语 英语 克里奥尔语、英语、法语 法语、英语 法语 西班牙语 法语、哈桑语、布拉尔语、索宁克语、沃洛夫语 索马里语、阿拉伯语、英语、意大利语 西班牙语 纽埃语、英语 英语、克里奥尔语、乌尔都语、印第安语、印地语 法语、沃洛夫语 阿拉伯语 西班牙语、克丘亚语、阿依马拉语 英语 法语、马达加斯加语 阿拉伯语、法语 阿拉伯语、英语 英语 卢旺达语、英语、法语、斯瓦希里语 阿拉伯语 英语 英语 德语 西班牙语 阿姆哈拉语、英语 英语、毛利语 马其顿语