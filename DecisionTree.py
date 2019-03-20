from graphviz import Digraph


class DecisionTree:

    def __init__(self, attribute, threshold, attrname=None, default_child=None, branches=None):
        self.attr = attribute
        self.threshold = threshold
        self.attrname = attrname or attribute
        self.default_child = default_child
        self.branches = branches or {}
        self.Left = 0  # valore <= della threshold
        self.Right = 1  # valore > della threshold

    def __call__(self, example):
        attrvalue = example[self.attr]
        if float(attrvalue) > self.threshold:
            return self.branches[(self.threshold, self.Right)](example)
        else:
            return self.branches[(self.threshold, self.Left)](example)

    def addLeft(self, value, subtree):
        self.branches[(value, self.Left)] = subtree

    def addRight(self, value, subtree):
        self.branches[(value, self.Right)] = subtree

    def getLeft(self):
        tree = self.branches.get((self.threshold, self.Left))
        return tree

    def getRight(self):
        tree = self.branches.get((self.threshold, self.Right))
        return tree


    #Esegue la visita per livelli dell albero e stampa attrname e threshold, apre un pdf con rappresentazione grafica tramite libreria graphviz
    def GraphViz(rootnode):
        print '***************************************************************************'
        print 'Visita per livelli albero di decisione sul dataset per intero:'
        u = Digraph('DecisionTree', filename='DecisionTree.gv')
        u.attr(size='30,30')
        u.node_attr.update(color='lightblue1', style='filled')
        thislevel = [rootnode]
        i = ' '
        j = ''
        while thislevel:
            nextlevel = list()
            for n in thislevel:
                if not isinstance(n, Leaf):
                    print n.attrname, n.threshold,
                    if not isinstance(n.getLeft(), Leaf):
                        u.edge(n.attrname + ' ' + str(n.threshold) + j,
                               n.getLeft().attrname + ' ' + str(n.getLeft().threshold) + i, label='<=')
                    else:
                        u.edge(n.attrname + ' ' + str(n.threshold) + j, n.getLeft().result, label='<=')
                    if not isinstance(n.getRight(), Leaf):
                        u.edge(n.attrname + ' ' + str(n.threshold) + j,
                               n.getRight().attrname + ' ' + str(n.getRight().threshold) + i, label='>')
                    else:
                        u.edge(n.attrname + ' ' + str(n.threshold) + j, n.getRight().result, label='>')
                    if n.getLeft(): nextlevel.append(n.getLeft())
                    if n.getRight(): nextlevel.append(n.getRight())
                else:
                    print n.result,
            print
            i = i + ' '
            j = j + ' '
            thislevel = nextlevel
        u.view()


class Leaf:
    def __init__(self, result):
        self.result = result

    def __call__(self, example):
        return self.result