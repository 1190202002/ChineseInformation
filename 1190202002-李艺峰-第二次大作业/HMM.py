from numpy import *
import numpy
import numpy as np
from func import *


class HMM():
    '''
    param trainWordLists:观测序列，指每一个字本身。
    param trainTagLists:隐状态，每一个字背后的标注信息。
    param self.initProb:初始概率（隐状态），每一个标注的初始化概率。
                                    self.initProb[tag] += 1
    param self.transitionProb:转移概率（隐状态），某一个标注转移到下一个标注的概率。
                                  self.emitProb[tag][word] += 1
    param self.emitProb: 发射概率 （隐状态表现为显状态的概率），指在某个标注下，生成某个字的概率。
                                  self.transitionProb[tag][nextTag] += 1
    生成隐马尔可夫模型。
    '''
    def __init__(self, wordDictSize, tagDictSize):
        self.wordDictSize = wordDictSize
        self.tagDictSize = tagDictSize

        #初始化转移概率矩阵、发射概率矩阵、初始概率矩阵
        self.transitionProb = np.random.rand(self.tagDictSize, self.tagDictSize)
        for index in range(self.tagDictSize):
            self.transitionProb[index] = self.transitionProb[index] / np.sum(self.transitionProb[index])

        self.initProb = numpy.random.rand(self.tagDictSize)
        self.initProb = self.initProb / np.sum(self.initProb)

        self.emitProb = numpy.random.rand(self.tagDictSize, self.wordDictSize)
        for index in range(self.tagDictSize):
            self.emitProb[index] = self.emitProb[index] / np.sum(self.emitProb[index])


    
    def trainhmm(self, trainWordLists, trainTagLists):
        '''
        极大似然估计隐马尔可夫模型参数
        '''
        self.transitionProb = numpy.zeros((self.tagDictSize, self.tagDictSize))
        self.initProb = numpy.zeros(self.tagDictSize) 
        self.emitProb = numpy.zeros((self.tagDictSize, self.wordDictSize))

        for i in range(len(trainWordLists)):
            for j in range(len(trainWordLists[i])):
                word, tag = trainWordLists[i][j], trainTagLists[i][j]
                self.initProb[tag] += 1
                self.emitProb[tag][word] += 1
                if j < len(trainWordLists[i])-1:
                    nextTag = trainTagLists[i][j+1]
                    self.transitionProb[tag][nextTag] += 1
        self.initProb = self.initProb / (self.initProb.sum())
        for index, value in enumerate(self.emitProb.sum(axis=1)):
            if value == 0: continue
            self.emitProb[index, :] = self.emitProb[index, :] / value

        for index, value in enumerate(self.transitionProb.sum(axis=1)):
            if value == 0: continue
            self.transitionProb[index, :] = self.transitionProb[index, :] / value

        self.initProb[self.initProb == 0] = 1e-10
        self.transitionProb[self.transitionProb == 0] = 1e-10
        self.emitProb[self.emitProb == 0] = 1e-10


    def viterbi(self, sentence):
        '''
        维特比算法，估计隐状态最大可能序列
        '''
        sentenceSize = len(sentence)
        score = numpy.zeros((sentenceSize, self.tagDictSize))
        path = numpy.zeros((sentenceSize, self.tagDictSize))

        score[0] = self.initProb + self.emitProb[:,sentence[0]]

        state = numpy.zeros(sentenceSize)

        for index, word in enumerate(sentence):
            if index == 0: continue
            temp = score[index-1] + self.transitionProb.T
            path[index] = numpy.argmax(temp, axis=1)
            score[index] = [element[int(path[index,i])] for i, element in enumerate(temp)] + self.emitProb[:,word]

        state[-1] = numpy.argmax(score[-1])
        
        for i in reversed(range(sentenceSize)):
            if i == sentenceSize -1: continue
            state[i] = path[i+1][int(state[i+1])]
        return state

    def test(self, testWordLists):
        self.transitionProb = numpy.log10(self.transitionProb)
        self.emitProb = numpy.log10(self.emitProb)
        self.initProb = numpy.log10(self.initProb)
        tagPall = []
        for sentence in testWordLists:
            tagPre = self.viterbi(sentence)
            tagPall.append(tagPre)
        return tagPall



   

