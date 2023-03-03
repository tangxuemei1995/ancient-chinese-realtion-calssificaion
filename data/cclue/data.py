import json 
'''将cclue转化'''
import random
text = {}

for line in open('./train.tsv'):
    l = line.strip().split('\t')
    if l[1] not in text.keys():
        text[l[1]] = []
        text[l[1]].append(line)
    else:
         text[l[1]].append(line)
for line in open('./dev.tsv'):
     l = line.strip().split('\t')
     if l[1] not in text.keys():
         text[l[1]] = []
         text[l[1]].append(line)
     else:
         text[l[1]].append(line)
new_train = []
for key in text:
    if key == '0':
        new_train += text[key][0:201]
    elif key == '2':
        new_train += text[key][0:201]
    else:
        new_train  += text[key] 
random.shuffle(new_train)
f = open( './train_new.tsv','w',encoding='utf-8')
for x in new_train:
    f.write(x)
#
# res = {}
# count = 0
# re2id = {}
# for line in open('./relation2id.tsv','r',encoding='utf-8'):
#     re2id[line.strip()] = count
#     count +=1

# count = 0
# f = open('./dev.tsv','w',encoding='utf-8')
# for line in open('./dev_data.json'):
#     line = line.strip().split(' "spo_list": ')
#     text = line[0][10:-2]
#     spo = line[1].split(',')
#     re = spo[0].split('"predicate": "')[-1][0:-1]
#     entity2_type = spo[1].split('"object_type": "')[-1][0:-1]
#     entity1_type = spo[2].split('"subject_type": "')[-1][0:-1]
#     entity2 = spo[3].split('"object": "')[-1][0:-1]
#     entity1 = spo[4].split('"subject": "')[-1][0:-3]
#     first,end = 0,0 #用于判断在一句话中，首尾实体是否出现了多次
#     new_text = ''
#     if entity1 == entity2:
#         print('首位实体一致',entity1,entity2 )
#     entity_order = 0 #用于判断是否尾实体先出现
#     j = 0
#     for i in range(len(text)):
#
#
#         if text[i:i+len(entity1)] == entity1:
#             if first == 0:
#                 if end == 0:#用于判断关系是否已经加上实体顺序
#                    re += '(e1,e2)'
#                    entity_order = 1
#                 else:
#                     re += '(e2,e1)'
#                     entity_order = 1
#                 new_text += 'b' + ' '
#                 for x in text[i:i+len(entity1)]:
#                     new_text += x+' '
#                 new_text += 'e' + ' '
#                 first = 1
#                 j = i + len(entity1)
#             else:
#                 if end == 0:
#                     #这时候还没有尾实体，因此将首实体位置更新
#                     new_text = new_text.replace('b ','').replace('e ','')
#                     new_text += 'b' + ' '
#                     for x in text[i:i+len(entity1)]:
#                         new_text += x+' '
#                     new_text += 'e' + ' '
#                     first = 1
#                     j  = i + len(entity1)
#                 # print('首实体在句子中出现两次！',text,entity1,entity2,re)
#                 # print(new_text)
#
#   #               print(text)
#   #               exit()
#
#
#         elif text[i:i+len(entity2)] == entity2:
#             if end == 0:
#
#                     new_text = new_text.replace('m ','').replace('n ','')
#                     new_text += 'm' + ' '
#                     for x in text[i:i+len(entity2)]:
#                         new_text += x+' '
#                     new_text += 'n' + ' '
#                     end = 1
#                     j  = i+len(entity2)
#
#             else:
#                 if first == 0:
#
#                     #首实体一直没出现就一直更新尾实体的位置，直到最后的尾实体
#
#                     new_text = new_text.replace('m ','').replace('n ','')
#                     new_text += 'm' + ' '
#                     for x in text[i:i+len(entity2)]:
#                         new_text += x+' '
#                         new_text += 'n' + ' '
#                     end = 1
#                     j  = i+len(entity2) #当前的文本已经到了这个位置
#                 else:
#                     #首实体已出现就不再更新尾实体的位置
#                     pass
#                 # print('尾实体在句子中出现两次！',text, entity1,entity2,re)
#                 # print(new_text)
#                 # print(text)
#       #           exit()
#         else:
#             # if j == 0:
# #                 new_text += text[i] + ' '
#             if i < j :
#                 continue
#             else:
#                 new_text += text[i] + ' '
#     new_text = new_text.strip()
#     # if re not in res.keys():
#     #     re2id[re] = count
#     #     count += 1
#     #     res[re] = 0
#     #     res[re] +=1
#     # else:
#     #     res[re] +=1
#     if entity_order == 0:
#         new_text += '\t' + str(re2id[re]) + '\t' + entity1_type + '\t'+ entity2_type + '\t' + '1' +'\n'
#         f.write(new_text)
#     else:
#         new_text += '\t' + str(re2id[re]) + '\t' + entity2_type + '\t'+ entity1_type + '\t' + '1' +'\n'
#         f.write(new_text)
# f1 = open('./relation2id.tsv','w',encoding='utf-8')
# print(res)
# for key in re2id.keys():
#     f1.write(key+'\n')
#  
#{'任职(e2,e1)': 458, '隶属于(e1,e2)': 63, '任职(e1,e2)': 604, '子(e2,e1)': 51, '同名于(e1,e2)': 128, '隶属于(e2,e1)': 124, '号(e1,e2)': 120, '作战(e2,e1)': 15, '位于(e1,e2)': 61, '依附(e1,e2)': 31, '名(e1,e2)': 107, '讨伐(e1,e2)': 37, '子(e1,e2)': 194, '去往(e1,e2)': 171, '升迁(e1,e2)': 31, '杀(e1,e2)': 77, '管理(e2,e1)': 37, '同名于(e2,e1)': 111, '弟(e1,e2)': 57, '出生地(e1,e2)': 67, '出生地(e2,e1)': 12, '葬于(e1,e2)': 30, '管理(e1,e2)': 33, '属于(e1,e2)': 14, '归属(e2,e1)': 31, '父(e1,e2)': 39, '依附(e2,e1)': 18, '属于(e2,e1)': 72, '朋友(e1,e2)': 13, '杀(e2,e1)': 29, '朋友(e2,e1)': 13, '位于(e2,e1)': 42, '作战(e1,e2)': 22, '兄(e1,e2)': 16, '字(e1,e2)': 32, '作(e1,e2)': 29, '弟(e2,e1)': 13, '姓(e2,e1)': 5, '姓(e1,e2)': 17, '兄(e2,e1)': 50, '去往(e2,e1)': 8, '讨伐(e2,e1)': 7, '名(e2,e1)': 6, '号(e2,e1)': 10, '作(e2,e1)': 2, '葬于(e2,e1)': 1, '父(e2,e1)': 2, '归属(e1,e2)': 3}

#test
# {'隶属于(e2,e1)': 18, '任职(e1,e2)': 86, '位于(e1,e2)': 13, '任职(e2,e1)': 76, '号(e1,e2)': 19, '子(e1,e2)': 23, '杀(e1,e2)': 10, '弟(e1,e2)': 8, '去往(e1,e2)': 24, '属于(e2,e1)': 14, '名(e1,e2)': 18, '同名于(e2,e1)': 14, '讨伐(e2,e1)': 3, '兄(e2,e1)': 12, '位于(e2,e1)': 4, '子(e2,e1)': 2, '属于(e1,e2)': 2, '隶属于(e1,e2)': 11, '同名于(e1,e2)': 14, '作(e1,e2)': 7, '作战(e1,e2)': 5, '杀(e2,e1)': 8, '管理(e2,e1)': 6, '作战(e2,e1)': 7, '管理(e1,e2)': 6, '号(e2,e1)': 1, '讨伐(e1,e2)': 6, '弟(e2,e1)': 1}
#dev
#{'子(e1,e2)': 49, '任职(e1,e2)': 177, '弟(e1,e2)': 20, '任职(e2,e1)': 130, '杀(e1,e2)': 25, '葬于(e1,e2)': 9, '名(e1,e2)': 35, '弟(e2,e1)': 3, '杀(e2,e1)': 19, '隶属于(e2,e1)': 41, '位于(e2,e1)': 11, '升迁(e1,e2)': 12, '依附(e2,e1)': 5, '去往(e1,e2)': 43, '父(e1,e2)': 10, '兄(e2,e1)': 22, '子(e2,e1)': 16, '同名于(e2,e1)': 40, '隶属于(e1,e2)': 9, '作(e1,e2)': 10, '号(e1,e2)': 24, '作战(e2,e1)': 10, '管理(e2,e1)': 11, '讨伐(e2,e1)': 4, '依附(e1,e2)': 8, '出生地(e1,e2)': 19, '位于(e1,e2)': 22, '父(e2,e1)': 3, '同名于(e1,e2)': 25, '朋友(e1,e2)': 4, '管理(e1,e2)': 9, '属于(e2,e1)': 17, '作战(e1,e2)': 5, '归属(e2,e1)': 7, '姓(e1,e2)': 2, '去往(e2,e1)': 4, '讨伐(e1,e2)': 6, '名(e2,e1)': 3, '字(e1,e2)': 4, '朋友(e2,e1)': 4, '兄(e1,e2)': 1, '出生地(e2,e1)': 1, '号(e2,e1)': 2, '属于(e1,e2)': 1}