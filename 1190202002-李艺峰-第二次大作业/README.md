# 基于隐马尔可夫模型（hmm）的人名识别
## 训练模型
根据训练数据集（train.txt)用极大似然估计法计算隐马尔可夫模型中5个基本元素：
param trainWordLists:观测序列，指每一个字本身。
param trainTagLists:隐状态，每一个字背后的标注信息。
param self.initProb:初始概率（隐状态），每一个标注的初始化概率。
                                    self.initProb[tag] += 1
param self.transitionProb:转移概率（隐状态），某一个标注转移到下一个标注的概率。
                                  self.emitProb[tag][word] += 1
param self.emitProb: 发射概率 （隐状态表现为显状态的概率），指在某个标注下，生成某个字的概率。
                                  self.transitionProb[tag][nextTag] += 1
生成隐马尔可夫模型。

## 预测状态序列
采用维特比算法对每个观测序列的隐状态序列进行估计，得出最大概率的隐状态序列

## 识别人名
在隐状态序列中查找，如果有3个相连的状态为'B-NAME': 0, 'M-NAME': 1, 'E-NAME': 2，那么则判断为3字人名。若有2个相连状态为'B-NAME': 0,'E-NAME': 2,那么则判断为2字人名。其他不常见字数人名不计入考虑。