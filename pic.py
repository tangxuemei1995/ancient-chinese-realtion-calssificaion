import pandas as pd
import numpy as np
from sklearn import metrics
import itertools
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from matplotlib import font_manager

# df = pd.read_csv('xxx.csv')
# wrong_labels = df['wrong_labels'].tolist()
# right_labels = df['right_labels'].tolist()
fname = '/System/Library/Fonts/Supplemental/Songti.ttc'
font = font_manager.FontProperties(fname=fname,size=8)
f = open('./cclue_test_true_pred.txt', 'r', encoding='utf-8')
text = f.read().strip().split('\n')

y_pred, y_true = [], [] 
for x in text:
    x = x.split('\t')
    y_true.append(x[1])
    y_pred.append(x[2])
# 构造混淆矩阵
labels = ['子(e2,e1)','子(e1,e2)','隶属于(e1,e2)', '隶属于(e2,e1)','任职(e1,e2)','任职(e2,e1)','同名于(e1,e2)', '同名于(e2,e1)','号(e1,e2)', '号(e2,e1)','作战(e1,e2)', '作战(e2,e1)','位于(e1,e2)', '位于(e2,e1)','名(e1,e2)','讨伐(e1,e2)', '讨伐(e2,e1)','去往(e1,e2)','杀(e1,e2)', '杀(e2,e1)','管理(e1,e2)', '管理(e2,e1)','属于(e1,e2)', '属于(e2,e1)','作(e1,e2)', '兄(e2,e1)','弟(e1,e2)', '弟(e2,e1)']
my_confusion_matrix = confusion_matrix(y_true, y_pred, labels=labels) # np.array(right_labels), labels=None, sample_weight=None)

# 所有的分类 label


def plot_Matrix(cm, classes, title=None,  cmap=plt.cm.Blues):
    plt.rc('font',family='sans-serif',size='4.5')   # 设置字体样式、大小
    plt.rcParams['font.sans-serif'] = ['Tahoma', 'DejaVu Sans', 'SimHei', 'Lucida Grande', 'Verdana']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.figure(figsize=(200, 200))
    plt.rcParams['figure.dpi'] = 200 #分辨率

    
    # 按行进行归一化
    cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    # 占比1%以下的单元格，设为0，防止在最后的颜色中体现出来
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            if int(cm[i, j]*100 + 0.5) == 0:
                cm[i, j]=0

    fig, ax = plt.subplots()
    im = ax.matshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax) # 侧边的颜色条带
    
    plt.title('Confusion matrix')
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           xticklabels=list(range(len(classes))), yticklabels=list(range(len(classes))),
           title=title,
           ylabel='True label',
           xlabel='Predicted label')
           
   # 通过绘制格网，模拟每个单元格的边框
    ax.set_xticks(np.arange(cm.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(cm.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="gray", linestyle='-', linewidth=0.05)
    ax.tick_params(which="minor", bottom=False, left=False)

    # 将x轴上的lables旋转45度
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # 标注百分比信息
    fmt = 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            if int(cm[i, j]*100 + 0.5) > 0:
                ax.text(j, i, format(int(cm[i, j]*100 + 0.5) , fmt) + '%',
                        ha="center", va="center",
                        color="white"  if cm[i, j] > thresh else "black")
    fig.tight_layout()
    plt.yticks(range(len(labels)), labels,fontproperties=font) 
    plt.xticks(range(len(labels)), labels,fontproperties=font, rotation=-45)
    plt.savefig('混淆.png',dpi=300,figsize=(16, 16), bbox_inches='tight')

plot_Matrix(my_confusion_matrix, labels, title='')
