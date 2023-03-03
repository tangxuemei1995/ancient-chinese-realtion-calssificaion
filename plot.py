from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from pylab import *
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

plt.rcParams['axes.unicode_minus'] = False
from matplotlib.font_manager import FontManager
 
mpl_fonts = set(f.name for f in FontManager().ttflist)
 
for f in sorted(mpl_fonts):
     print('\t' + f)

exit()
f = open('./tmp/cclue/our_bert/use_entity_type_pe_cnn/cclue_test_true_pred.txt', 'r', encoding='utf-8')
text = f.read().strip().split('\n')

y_pred, y_true = [], [] 
for x in text:
    x = x.split('\t')
    y_true.append(x[1])
    y_pred.append(x[2])
labels = ['子(e2,e1)','子(e1,e2)','隶属于(e1,e2)', '隶属于(e2,e1)','任职(e1,e2)','任职(e2,e1)','同名于(e1,e2)', '同名于(e2,e1)','号(e1,e2)', '号(e2,e1)','作战(e1,e2)', '作战(e2,e1)','位于(e1,e2)', '位于(e2,e1)','名(e1,e2)', '名(e2,e1)','讨伐(e1,e2)', '讨伐(e2,e1)','去往(e1,e2)', '去往(e2,e1','杀(e1,e2)', '杀(e2,e1)','管理(e1,e2)', '管理(e2,e1)','属于(e1,e2)', '属于(e2,e1)','作(e1,e2)', '作(e2,e1)','兄(e1,e2)', '兄(e2,e1)','弟(e1,e2)', '弟(e2,e1)']
# y_pred =  ['2','2','3','1','4'] # 类似的格式
# y_true =  ['0','1','2','3','4'] # 类似的格式
# # 对上面进行赋值

C = confusion_matrix(y_true, y_pred, labels=labels) # 可将'1'等替换成自己的类别，如'cat'。

plt.matshow(C, cmap=plt.cm.YlGn) # 根据最下面的图按自己需求更改颜色
# plt.colorbar()

for i in range(len(C)):
    for j in range(len(C)):
        plt.annotate(C[j, i], xy=(i, j), horizontalalignment='center', verticalalignment='center')

# plt.tick_params(labelsize=15) # 设置左边和上面的label类别如0,1,2,3,4的字体大小。

plt.ylabel('True label')
plt.xlabel('Predicted label')
# plt.ylabel('True label', fontdict={'family': 'Times New Roman', 'size': 20}) # 设置字体大小。
# plt.xlabel('Predicted label', fontdict={'family': 'Times New Roman', 'size': 20})
plt.yticks(range(len(labels)), labels) 
plt.xticks(range(len(labels)), labels) 
# plt.xticks(range(0,5), labels=['a','b','c','d','e']) # 将x轴或y轴坐标，刻度 替换为文字/字符
# plt.yticks(range(0,5), labels=['a','b','c','d','e'])
# plt.ylim(bottom=100,top=100)
plt.savefig('混淆.png',dpi=300,figsize=(16, 16), bbox_inches='tight')
# plt.show()
