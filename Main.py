import DataSet
import DecisionTreeLearning
import random
import itertools
import operator
import matplotlib.pyplot as plt

#permetto all'utente di selezionare il dataset da usare
index = input('Selezionare il dataset che si vuole testare:\n'
              '1) Blood Transfusion\n'
              '2) Iris\n'
              '3) Haberman\n'
              '4) Mammographic Masses\n'
              'Digitare il numero qui --->')

if index == 1:
    filesource = 'BloodTransfusion.txt'
    fileAttr = ['Recency', 'Frequency', 'Monetary', 'Time', 'Donate']
    posClassification = 4
    fileClass = ['0', '1']

elif index == 2:
    filesource = 'Iris.txt'
    fileAttr = ['Sepal-length', 'Sepal-width', 'Petal-length', 'Petal-width', 'Class']
    posClassification = 4
    fileClass = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

elif index == 3:
    filesource = 'Haberman.txt'
    fileAttr = ['Age', 'Patient year of operation', 'Number of positive axillary nodes detected', ' Survival status']
    posClassification = 3
    fileClass = ['1', '2']

elif index == 4:
    filesource = 'MammographicMasses.txt'
    fileAttr = ['BI-RADS', 'Age', 'Shape', 'Margin', 'Density', ' Severity']
    posClassification = 5
    fileClass = ['0', '1']

#chiamo il metodo che fa il parsing del file .txt del dataset scelto
fileDataset = DataSet.setDataSet(filesource, fileAttr, posClassification, fileClass)

#rimuove valori nel dataset con probabilita uniforme (funziona bene con i valori di p 0.1, 0.2, 0.5)
def removeValAttrWithProb(dataset, p):
    a = 1 / p
    for n in range(len(dataset.examples)):
        for j in range(len(dataset.examples[n])):
            i = random.randint(1, a)
            if i == 1:
                dataset.examples[n][j] = None
    return dataset

#creo il validation set per il 10 fold cross validation
def testing(fileDataset, number):
    length = len(fileDataset.examples) / 10
    k = number * length
    validation = []
    i = 0
    while i < length:
        validation.append(fileDataset.examples[i + k])
        i = i + 1
    return DataSet.DataSet(validation, fileDataset.inputs, fileDataset.attributes, fileDataset.target,
                           fileDataset.attrnames, fileDataset.values)

#creo il training set per il 10 fold cross validation
def training(fileDataset, number):
    totalLength = len(fileDataset.examples)
    length = len(fileDataset.examples) / 10
    k = number * length
    training = []
    i = 0
    while i < k:
        training.append(fileDataset.examples[i])
        i = i + 1
    j = k + length
    while j < totalLength:
        training.append(fileDataset.examples[j])
        j = j + 1
    return DataSet.DataSet(training, fileDataset.inputs, fileDataset.attributes, fileDataset.target,
                           fileDataset.attrnames, fileDataset.values)

#ritorna la media di una lista
def avg(list):
    length = len(list)
    count = 0
    for i in list:
        count = count + i
    return count / length


def tenFoldCrossValidation(fileDataset):
    print 'Risultati Ten Fold Cross Validation:'
    i = 0
    percents = []
    corrects = []
    random.shuffle(fileDataset.examples)
    while i < 10:
        train = training(fileDataset, i)
        val = testing(fileDataset, i)
        tree = DecisionTreeLearning.DecisionTreeLearner(train)
        correctV = 0
        for example in val.examples:
            if tree.__call__(example) == example[len(example) - 1]:
                correctV = correctV + 1
        percent = (correctV * 100) / len(val.examples)
        print 'Validation set numero', i + 1, percent, '% classificate correttamente, ovvero', correctV, \
            'classificazioni corrette su', len(val.examples)
        i = i + 1
        percents.append(percent)
        corrects.append(correctV)
    print avg(percents), '% classificate correttamente in media, ovvero', sum(corrects), \
        'classificazioni corrette su', len(val.examples) * 10
    return avg(percents)

#cerca il valore piu diffuso (e lo ritorna) per un determinato attribute nel dataset evitando i valori mancanti
def mostCommonValueOfAttrInDataSet(Dataset, attribute):
    L = []
    for element in Dataset.examples:
        if element[attribute] != None:
            L.append(element[attribute])
    SL = sorted((x, i) for i, x in enumerate(L))
    groups = itertools.groupby(SL, key=operator.itemgetter(0))

    def _auxfun(g):
        item, iterable = g
        count = 0
        min_index = len(L)
        for _, where in iterable:
            count += 1
            min_index = min(min_index, where)
        return count, -min_index

    return max(groups, key=_auxfun)[0]

#per ogni valore mancante rimpiazza il valore con il metodo descritto nella sezione 3.7.4 Mitchell
def replaceMissingValue(fileDataset):
    i = 0
    for elements in fileDataset.examples:
        j = 0
        for element in elements:
            if element == None:
                fileDataset.examples[i][j] = mostCommonValueOfAttrInDataSet(fileDataset, j)
            j = j + 1
        i = i + 1
    return fileDataset


# test del metodo descritto nella sezione 3.7.4 Mitchell
def test(fileDataset):
    print '***************************************************************************'
    print'Test su dataset con nessun valore mancante:'
    percents = []
    percents.append(tenFoldCrossValidation(fileDataset))
    prob = [0.1, 0.2, 0.5]
    for p in prob:
        print '***************************************************************************'
        print 'Test su dataset con elementi rimossi casualmente con probabilita uniforme', p
        removeValAttrWithProb(fileDataset, p)
        filledFileDataset = replaceMissingValue(fileDataset)
        percents.append(tenFoldCrossValidation(filledFileDataset))
    prob.insert(0, 0)
    plt.plot(prob, percents, 'ro', label="Media Percentuali 10FoldCrossValidation")
    plt.plot(prob, percents, 'b--')
    plt.legend()
    plt.xlabel("Probabilita' Elemento Mancante Nel Dataset")
    plt.ylabel("Percentuale Classificazioni Corrette")
    plt.show()

#creazione dell albero di decisione con dataset completo
tree = DecisionTreeLearning.DecisionTreeLearner(fileDataset)
#visita per livelli dell albero con dataset completo e visualizzazione grafica
tree.GraphViz()
test(fileDataset)