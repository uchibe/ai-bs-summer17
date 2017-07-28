import numpy as np
import memory
import random
from keras.models import Sequential, load_model
from keras.layers import Flatten, ZeroPadding2D
from keras.layers.convolutional import Conv2D
from keras.layers.core import Dense, Dropout, Activation
from keras.layers.pooling import MaxPooling2D
from keras.optimizers import SGD, Adam

class DeepQ:

    def __init__(self,outputs,memorySize,discountFactor,learningRate,learnStart,img_rows,img_cols,img_channels):
        self.output_size=outputs
        self.memory=memory.Memory(memorySize)
        self.discountFactor=discountFactor
        self.learnStart=learnStart
        self.learningRate=learningRate
        self.img_rows=img_rows
        self.img_cols=img_cols
        self.img_channels=img_channels

    def initNetworks(self):

        model=self.createModel()
        self.model=model
        self.saveModel('iniweights_smcv.h5')
        targetModel=self.createModel()
        self.targetModel=targetModel

        
        return self.model

    def createModel(self):

        model=Sequential()
        #print(img_rows)
        #print(img_cols)
        #print(img_channels)
        model.add(Conv2D(16,(3,3),strides=(2,2),input_shape=(self.img_rows,self.img_cols,self.img_channels)))
        model.add(Activation('relu'))
        model.add(ZeroPadding2D((1,1)))
        model.add(Conv2D(16,(3,3),strides=(2,2)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))
        model.add(Flatten())
        model.add(Dense(256))
        model.add(Activation('relu'))
        #model.add(Dropout(0.5))
        model.add(Dense(self.output_size))
        #model.add(Activation('softmax'))
        #model.compile(RMSprop(lr=self.learningRate),'MSE')
        #sgd=SGD(lr=self.learningRate)
        adam=Adam(lr=self.learningRate)
        model.compile(loss='mse',optimizer=adam)
        model.summary()

        return model

    def getMemorySize(self):

        return self.memory.getCurrentSize()

    def getMiniBatch(self):
        return self.memory.getMiniBatch(32)

    def getMemory(self):

        return self.memory.getAllMemory()

    def getModel(self):
        return self.model

    def trainModel(self,inputs,targets):
        return self.model.train_on_batch(inputs,targets)
        
    def getPredict(self,state):
        return self.model.predict(state)

    def getTargetPredict(self,state):
        return self.targetModel.predict(state)

    def getTargetQValues(self,state):

        predicted=self.targetModel.predict(state)
        return predicted[0]

    def getQValues(self,state):

        predicted=self.model.predict(state)
        return predicted[0]

    def getMaxIndex(self,qValues):

        return np.argmax(qValues)

    def selectAction(self,qValues,explorationRate):

        rand=random.random()
        if rand<explorationRate: #epsilon
            action=np.random.randint(0,self.output_size)
        else:
            action=self.getMaxIndex(qValues)

        return action

    def addMemory(self,state,action,reward,newState,isFinal):

        self.memory.addMemory(state,action,reward,newState,isFinal)

        return 

    def loadWeights(self,path):
            
        self.model.load_weights(path)

    def calculateTarget(self,qValuesNewState,reward,isFinal):

        if isFinal:
            return reward
        else:
            return reward+self.discountFactor*self.getMaxQ(qValuesNewState)

    def getMaxQ(self,qValues):

        return np.max(qValues)

    def printNetwork(self):
        i=0
        #print(self.model.layers)
        layer1=self.model.layers[0]
        print layer1.get_weights()[0][0,0,:]
        #for layer in self.model.layers:
        #    weights=layer.get_weights()
        #    print "layer ",i,": ",weights[0]
        #    i+=1

    def saveModel(self,path):
        self.model.save(path)

    def loadModel(self,path):
        self.model=load_model(path)

    def loadTargetModel(self,path):
        self.targetModel=load_model(path)
        
    def saveWeights(self):
        self.model.save_weights("newweights.h5",overwrite=True)

    def updateTargetNetwork(self):
        self.backupNetwork(self.model,self.targetModel)

    def backupNetwork(self,model,backup):
        weightMatrix=[]
        for layer in model.layers:
            weights=layer.get_weights()
            weightMatrix.append(weights)

            
        #np.save('weightMatrix.npy',weightMatrix)
        #print(weightMatrix.shape)
        i=0
        for layer in backup.layers:
            weights=weightMatrix[i]
            layer.set_weights(weights)
            i+=1
        
    #def loadWeights(self,path):
    #    self.model.set_weights(load_model(path).get_weights())

    def learnOnMini(self,useTarget=False):
        loss=0
        mini=self.getMiniBatch()
        inputs=np.zeros((32,32,32,1))
        targets=np.zeros((32,3))
        i=0
        for sample in mini:
            isFinal=sample['isFinal']
            s=sample['state']
            a=sample['action']
            r=sample['reward']
            newS=sample['newState']
            inputs[i:i+1]=s
            targets[i]=self.getPredict(s)
            if not useTarget:
                Q_sa=self.getPredict(newS)
            else:
                Q_sa=self.getTargetPredict(newS)
            if isFinal:
                targets[i,a]=r
            else:
                targets[i,a]=r+0.99*np.max(Q_sa)

            i+=1

        loss+=self.trainModel(inputs,targets)
        #self.printNetwork()
        
        return loss
