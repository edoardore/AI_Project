class DataSet:
    def __init__(self, examples=None, inputs=None, attributes=None, target=None, attrnames=None, values=None):
        self.examples = examples
        self.target = target
        self.values = values
        self.inputs = inputs
        self.attributes = attributes
        self.attrnames = attrnames or attributes


# examples       : is the list of all examples of the dataset
# target         : is the position of the attribute that indicates the classification of the example
# values         : contains the values of the classification
# inputs         : attributes except the classification
# attributes     : all the attributes
# attrnames      : name of the attributes in the dataset


#parsing del file .txt e ritorna un DataSet
def setDataSet(file, attrnames, target, values):
    examples = []
    for line in open(file).readlines():
        content = line.split(',')
        content = [c.rstrip() for c in content]
        example = []
        for j in range(0, len(content)):
            example.append(content[j])
        if '?' not in example:  # non considero le righe del dataset con attributi mancanti (in MammographicMasses)
            examples.append(example)
    attributes = []
    for i in range(0, len(example)):
        attributes.append(i)
    inputs = list(attributes)
    inputs.pop(inputs.index(target))
    return DataSet(examples, inputs, attributes, target, attrnames, values)
