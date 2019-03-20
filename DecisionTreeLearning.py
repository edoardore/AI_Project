import DecisionTree
import math

def DecisionTreeLearner(dataset):

    def decisionTreeLearning(examples, attributes, parents_examples=()):
        if len(examples) == 0:
            return pluralityValue(parents_examples) #ritorna la piu frequente classificazione tra gli examples
        elif allSameClass(examples):
            return DecisionTree.Leaf(examples[0][dataset.target]) #se tutti hanno la stessa classe ritorna la classe del primo esempio
        elif len(attributes) == 0:
            return pluralityValue(examples) #ritorna la piu frequente classificazione tra gli esempi
        else:
            mostImpAtt, threshold = chooseAttribute(attributes, examples)
            tree = DecisionTree.DecisionTree(mostImpAtt, threshold, dataset.attrnames[mostImpAtt])
            ExampleMinor, ExampleMajor = splittingOnThreshold(mostImpAtt, threshold, examples)#separazione basata sulla soglia
            #fa la ricorsione ed aggiunge all albero
            branchesLeft = decisionTreeLearning(ExampleMinor, removeAttr(mostImpAtt, attributes), examples)#ricorsione
            branchesRight = decisionTreeLearning(ExampleMajor, removeAttr(mostImpAtt, attributes), examples)#ricorsione
            tree.addLeft(threshold, branchesLeft)
            tree.addRight(threshold, branchesRight)
            return tree

    def chooseAttribute(attributes, examples): #trova il piu importante attributo e relativa soglia in accordo all information gain
        maxgainAttr = 0
        thresholdAttr = 0
        listValuesForAttribute = getListValuesForAttribute(dataset.examples, dataset.target)  # prepara una lista di valori per ogni attributo per trovare il piu importante
        global mostImportanceA
        for attr in attributes:
            maxgainValue = 0
            threshValue = 0
            for i in listValuesForAttribute[attr]:
                gain = float(informationGain(attr, float(i), examples))     # calcola il suo gain
                if gain > maxgainValue :                                          #scelgo sempre quello maggiore
                    maxgainValue = gain
                    threshValue = float(i)
            if maxgainValue  >= maxgainAttr:
                maxgainAttr = maxgainValue
                mostImportanceA = attr
                thresholdAttr = threshValue
        return mostImportanceA, thresholdAttr

    def pluralityValue(examples):
        i = 0
        global popular
        for v in dataset.values: #per ogni classificazione conta le occorrenze, poi scegli la piu popular
            count = counting(dataset.target, v, examples)
            if  count > i:
                i = count
                popular = v
        return DecisionTree.Leaf(popular)

    def allSameClass(examples): #ritorna True se tutti gli esempi hanno stessa classe
        sameClass = examples[0][dataset.target] #prendo quella del primo esempio come riferimento
        for e in examples:
            if e[dataset.target] != sameClass:
                return False
        return True

    def informationGain(attribute, threshold, examples):
        def entropy(examples): #definisco la funzione entropia
            entr = 0
            if len(examples) != 0:
                for v in dataset.values:
                    p = float(counting(dataset.target, v, examples)) / len(examples)
                    if p != 0:
                        entr += (-p) * math.log(p, 2.0)
            return float(entr)
        def remainder(examples):
            N = float(len(examples))
            ExampleMinor, ExampleMajor = splittingOnThreshold(attribute, threshold, examples)
            remainderExampleMinor = (float((len(ExampleMinor))) / N) * entropy(ExampleMinor)
            remainderExampleMajor = (float((len(ExampleMajor))) / N) * entropy(ExampleMajor)
            return (remainderExampleMinor + remainderExampleMajor)

        #formula che calcola l' information gain
        return entropy(examples) - remainder(examples)

    def counting(attribute, value, example): #conta il numero di example che hanno attributo uguale a value
        return sum(e[attribute] == value for e in example)

    def removeAttr(delAttr, attributes): #delAttr e l'attributo da rimuovere
        result=list(attributes)
        result.remove(delAttr)
        return result

    def splittingOnThreshold(attribute, threshold, examples):
        ExampleMinor, ExampleMajor = [], []
        for e in examples:
            if float(e[attribute]) <= threshold: #divide gli esempi basandosi sulla threshold dell'attributo dato
                ExampleMinor.append(e)
            else:
                ExampleMajor.append(e)
        return ExampleMinor, ExampleMajor


    return decisionTreeLearning(dataset.examples, dataset.inputs)

def getListValuesForAttribute(exemples, nA): #crea una lista di liste con singoli valori degli attributi
    valuesList = []
    for n in range(nA):
        l = []
        for i in range(0,len(exemples)):
            l.append(exemples[i][n])#valori per ogni attributo
        l = list(set(l))#rimuove i duplicati
        valuesList.append(l)  #attributi senza duplicati
    return valuesList