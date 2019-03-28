# AI_Project
Progetto di Intelligenza artificiale sugli alberi di decisione con valori nel data set mancanti.

## Utilizzo
Eseguire il modulo Main.py, in automatico verranno eseguite le funzioni
```python
tree = DecisionTreeLearning.DecisionTreeLearner(fileDataset)
tree.GraphViz()
test(fileDataset)
```
Selezionare adesso uno dei quattro Data Sets mostrati e digitare il numero corrispondente a quello scelto.
```comment
1) Blood Transfusion
2) Iris
3) Haberman
4) Mammographic Masses
```
##

## Esecuzione
Il programma darà in ordine i seguenti output:
-Visita per livelli dell'albero di decisione creato sull'intero dataset selezionato.

-Visualizzazione grafica dell`albero di decisione tramite libreria grafica GraphViz

-Inizio dei test con tenFoldCrossValidation:
Si scompone il dataset in 10 sottoinsiemi di dimensione n/10, selezionato 1/10 del dataset per il testing si crea l'albero decisionale
sui rimanenti 9/10 del dataset. In ordine andiamo a 'spostare' il testing ed il training set ed eseguiamo in totale 10 test di classificazioni.
Calcolata la media delle classificazione corrette riportiamo i risultati. Questo processo viene inizialmente eseguito senza valori mancanti nel dataset.

-Si riportano i risultati del tenFoldCrossValidation senza rimozione di valori dal DataSet scelto

-Si riportano i risultati del tenFoldCrossValidation con rimozione dei valori con percentuale 0.1 dal DataSet scelto

-Si riportano i risultati del tenFoldCrossValidation con rimozione dei valori con percentuale 0.2 dal DataSet scelto

-Si riportano i risultati del tenFoldCrossValidation con rimozione dei valori con percentuale 0.5 dal DataSet scelto

-Si mostra su grafico le medie delle classificazioni corrette ottenute al variare di p=[0.0, 0.1, 0.2, 0.5].

## Librerie utilizzate
```python
random
itertools
operator
matplotlib.pyplot 
graphviz 
math
```
Attenzione: solitamente sugli IDE più comuni sono quasi tutte presenti tranne per [graphviz](https://graphviz.gitlab.io/download/).

## Riferimenti
Tutti i datasets forniti in questo progetto sono stati presi da [UCI](https://archive.ics.uci.edu/ml/index.php) Machine Learning.
L'implementazione di `DecisionTreeLearning.py` è stata ripresa e riadattata dalla seguente [reposirtory](https://github.com/aimacode/aima-python/blob/master/learning.py) pubblica, anche facendo riferimento a Russell & Norvig 18.3.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.


## License
[Edoardo Re](https://github.com/edoardore), 2019
