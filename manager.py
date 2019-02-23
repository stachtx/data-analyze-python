#-------------------------------------------------------------------------------
# Name:        IAD zadanie 1
# Purpose:
#
# Author:      Tomasz Stachura
#
# Created:     15.03.2017
# Copyright:   (c) Tomasz Stachura 203996 2017
# Licence:     freeware
#-------------------------------------------------------------------------------
import linecache
import math
import matplotlib.pyplot as plt

class Flower:
    def __init__ (self,sepalL,sepalW,petalL,petalW,kind):
        self.sepalLength=sepalL
        self.sepalWidth=sepalW
        self.petalLength=petalL
        self.petalWidth=petalW
        self.Kind=kind

flowers=[]
kinds=['','Iris-setosa','Iris-versicolor','Iris-virginica']
features=['sepalLength','sepalWidth','petalLength','petalWidth']

def load():
    file = open('iris.txt', 'r').read()
    lines = file.split('\n')

    for line in lines:
        dane= line.split(',')
        flowers.append(Flower(dane[0],dane[1],dane[2],dane[3],dane[4]))

def draw(list):

    ax=chartData(list, 'sepal','Iris-setosa','x')
    ay=chartData(list, 'sepal','Iris-setosa','y')
    bx=chartData(list, 'sepal','Iris-versicolor','x')
    by=chartData(list, 'sepal','Iris-versicolor','y')
    cx=chartData(list, 'sepal','Iris-virginica','x')
    cy=chartData(list, 'sepal','Iris-virginica','y')

    pax=chartData(list, 'petal','Iris-setosa','x')
    pay=chartData(list, 'petal','Iris-setosa','y')
    pbx=chartData(list, 'petal','Iris-versicolor','x')
    pby=chartData(list, 'petal','Iris-versicolor','y')
    pcx=chartData(list, 'petal','Iris-virginica','x')
    pcy=chartData(list, 'petal','Iris-virginica','y')

    plt.figure(1)
    plt.xlabel('length')
    plt.ylabel('Width')
    plt.title('Sepal')
    plt.plot(ax,ay, 'rs', bx, by, 'bs', cx, cy, 'gs')

    plt.figure(2)
    plt.xlabel('length')
    plt.ylabel('Width')
    plt.title('Petal')
    plt.plot(pax,pay, 'rs', pbx, pby, 'bs', pcx, pcy, 'gs')
    plt.show()

def chartData(container, feature, kind,axis):
    list = []
    for flower in container:
        if flower.Kind == kind:
            if feature == 'sepal':
                if axis=='x':
                    list.append(getattr(flower, 'sepalLength'))
                elif axis=='y':
                    list.append(getattr(flower, 'sepalWidth'))
            elif feature == 'petal':
                if axis=='x':
                    list.append(getattr(flower, 'petalLength'))
                elif axis=='y':
                    list.append(getattr(flower, 'petalWidth'))
    return list

def getSpecifiedIrisData(container, feature, kind):
    list = []
    if not kind:
        for flower in container:
            list.append(float(getattr(flower, feature)))
    else:
        for flower in container:
            if flower.Kind == kind:
                list.append(float(getattr(flower, feature)))
    return list

def distance(lista):
    return max(lista)-min(lista)

def median(list):
    length=len(list)
    list.sort()
    if 0 ==( length % 2):
        return ((list[length/2])+list[length/2+1])/2
    else:
        return list[(length+1)/2]

def quartileFirst(list):
    length=len(list)
    list.sort()
    if 0 ==( length % 2):
        return (list[length/4]+list[length/4+1])/2
    else:
        return list[(length+1)/4]

def quartileThird(list):
    length=len(list)
    list.sort()
    if 0 ==( length % 2):
        return (list[length*3/4]+list[length*3/4+1])/2
    else:
        return list[(length+1)*3/4]

def harmonicMean(list):
    length=len(list)
    sum=0
    for i in list:
        sum=sum+1/i
    return length/sum

def geometricMean(list):
    length=len(list)
    sum=0
    for i in list:
        sum+=math.log(i)
    return math.exp(sum/length)

def arithmeticMean(list):
    length=len(list)
    sum=0
    for i in list:
        sum+=i
    return sum/length

def powerMeanRowTwo(list):
    length=len(list)
    sum=0
    for i in list:
        sum+=math.pow(i,2)
    return math.sqrt(sum/length)

def powerMeanRowThree(list):
    length=len(list)
    sum=0
    for i in list:
        sum+=math.pow(i,3)
    return math.pow(sum/length,1.0/3.0)

def variation(list):
    length=len(list)
    sum=0
    for i in list:
        sum+=math.pow(i-arithmeticMean(list),2)
    return sum/length

def standardDeviation(list):
    return math.pow(variation(list),2)

def kurtosis(list):
    length=len(list)
    sum=0
    for i in list:
        sum+=math.pow(i-arithmeticMean(list),4)
    return sum/length/math.pow(standardDeviation(list),2)

def main():
    pass
if __name__ == '__main__':
    main()

    load()

    for i in kinds:
        for j in features:
            print("Minimum  "+j+"   "+i+" = "+ str(min(getSpecifiedIrisData(flowers,j,i))))
        for j in features:
            print("Maximum  "+j+"   "+i+" = "+ str(max(getSpecifiedIrisData(flowers,j,i))))
        for j in features:
            print("Distance  "+j+"   "+i+" = "+ str(distance(getSpecifiedIrisData(flowers,j,i))))
        for j in features:
            print("Median  "+j+"   "+i+" = "+ str(median(getSpecifiedIrisData(flowers,j,i))))
        for j in features:
            print("First quartile  "+j+"   "+i+" = "+ str(quartileFirst(getSpecifiedIrisData(flowers,j,i))))
        for j in features:
            print("Third quartile  "+j+"   "+i+" = "+ str(quartileThird(getSpecifiedIrisData(flowers,j,i))))
        for j in features:
            print("Harmonic mean "+j+"   "+i+" = "+ str(harmonicMean(getSpecifiedIrisData(flowers,j,i))))
        for j in features:
            print("Geometric mean "+j+"   "+i+" = "+ str(geometricMean(getSpecifiedIrisData(flowers,j,i))))
        for j in features:
            print("Arithmetic mean "+j+"   "+i+" = "+ str(arithmeticMean(getSpecifiedIrisData(flowers,j,i))))
        for j in features:
            print("Power mean row 2 "+j+"   "+i+" = "+ str(powerMeanRowTwo(getSpecifiedIrisData(flowers,j,i))))
        for j in features:
            print("Power mean row 3 "+j+"   "+i+" = "+ str(powerMeanRowThree(getSpecifiedIrisData(flowers,j,i))))
        for j in features:
            print("Variation "+j+"   "+i+" = "+ str(variation(getSpecifiedIrisData(flowers,j,i))))
        for j in features:
            print("Standard deviation "+j+"   "+i+" = "+ str(standardDeviation(getSpecifiedIrisData(flowers,j,i))))
        for j in features:
            print("Kurtosis "+j+"   "+i+" = "+ str(kurtosis(getSpecifiedIrisData(flowers,j,i))))

draw(flowers)
