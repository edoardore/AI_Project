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

## Esempio di output del file ```Main.py```
```
Selezionare il dataset che si vuole testare:
1) Blood Transfusion
2) Iris
3) Haberman
4) Mammographic Masses
Digitare il numero qui --->1
***************************************************************************
Visita per livelli albero di decisione sul dataset per intero:
Recency 6.0
Monetary 1000.0 Time 79.0
Time 17.0 Time 49.0 Monetary 250.0 0
Frequency 1.0 Frequency 2.0 Frequency 14.0 Frequency 10.0 Frequency 0 Frequency 17.0
0 0 0 0 1 1 0 0 0 0 0 0
***************************************************************************
Test su dataset con nessun valore mancante:
Risultati Ten Fold Cross Validation:
Testing set numero 1 58 % classificate correttamente, ovvero 30 classificazioni corrette su 51
Testing set numero 2 72 % classificate correttamente, ovvero 37 classificazioni corrette su 51
Testing set numero 3 72 % classificate correttamente, ovvero 37 classificazioni corrette su 51
Testing set numero 4 64 % classificate correttamente, ovvero 33 classificazioni corrette su 51
Testing set numero 5 82 % classificate correttamente, ovvero 42 classificazioni corrette su 51
Testing set numero 6 66 % classificate correttamente, ovvero 34 classificazioni corrette su 51
Testing set numero 7 74 % classificate correttamente, ovvero 38 classificazioni corrette su 51
Testing set numero 8 76 % classificate correttamente, ovvero 39 classificazioni corrette su 51
Testing set numero 9 78 % classificate correttamente, ovvero 40 classificazioni corrette su 51
Testing set numero 10 76 % classificate correttamente, ovvero 39 classificazioni corrette su 51
71 % classificate correttamente in media, ovvero 369 classificazioni corrette su 510
***************************************************************************
Test su dataset con elementi rimossi casualmente con probabilita uniforme 0.1
Risultati Ten Fold Cross Validation:
Testing set numero 1 68 % classificate correttamente, ovvero 35 classificazioni corrette su 51
Testing set numero 2 68 % classificate correttamente, ovvero 35 classificazioni corrette su 51
Testing set numero 3 72 % classificate correttamente, ovvero 37 classificazioni corrette su 51
Testing set numero 4 72 % classificate correttamente, ovvero 37 classificazioni corrette su 51
Testing set numero 5 66 % classificate correttamente, ovvero 34 classificazioni corrette su 51
Testing set numero 6 82 % classificate correttamente, ovvero 42 classificazioni corrette su 51
Testing set numero 7 78 % classificate correttamente, ovvero 40 classificazioni corrette su 51
Testing set numero 8 70 % classificate correttamente, ovvero 36 classificazioni corrette su 51
Testing set numero 9 78 % classificate correttamente, ovvero 40 classificazioni corrette su 51
Testing set numero 10 72 % classificate correttamente, ovvero 37 classificazioni corrette su 51
72 % classificate correttamente in media, ovvero 373 classificazioni corrette su 510
***************************************************************************
Test su dataset con elementi rimossi casualmente con probabilita uniforme 0.2
Risultati Ten Fold Cross Validation:
Testing set numero 1 66 % classificate correttamente, ovvero 34 classificazioni corrette su 51
Testing set numero 2 82 % classificate correttamente, ovvero 42 classificazioni corrette su 51
Testing set numero 3 68 % classificate correttamente, ovvero 35 classificazioni corrette su 51
Testing set numero 4 84 % classificate correttamente, ovvero 43 classificazioni corrette su 51
Testing set numero 5 80 % classificate correttamente, ovvero 41 classificazioni corrette su 51
Testing set numero 6 80 % classificate correttamente, ovvero 41 classificazioni corrette su 51
Testing set numero 7 78 % classificate correttamente, ovvero 40 classificazioni corrette su 51
Testing set numero 8 70 % classificate correttamente, ovvero 36 classificazioni corrette su 51
Testing set numero 9 86 % classificate correttamente, ovvero 44 classificazioni corrette su 51
Testing set numero 10 84 % classificate correttamente, ovvero 43 classificazioni corrette su 51
77 % classificate correttamente in media, ovvero 399 classificazioni corrette su 510
***************************************************************************
Test su dataset con elementi rimossi casualmente con probabilita uniforme 0.5
Risultati Ten Fold Cross Validation:
Testing set numero 1 88 % classificate correttamente, ovvero 45 classificazioni corrette su 51
Testing set numero 2 84 % classificate correttamente, ovvero 43 classificazioni corrette su 51
Testing set numero 3 94 % classificate correttamente, ovvero 48 classificazioni corrette su 51
Testing set numero 4 88 % classificate correttamente, ovvero 45 classificazioni corrette su 51
Testing set numero 5 92 % classificate correttamente, ovvero 47 classificazioni corrette su 51
Testing set numero 6 80 % classificate correttamente, ovvero 41 classificazioni corrette su 51
Testing set numero 7 92 % classificate correttamente, ovvero 47 classificazioni corrette su 51
Testing set numero 8 86 % classificate correttamente, ovvero 44 classificazioni corrette su 51
Testing set numero 9 90 % classificate correttamente, ovvero 46 classificazioni corrette su 51
Testing set numero 10 88 % classificate correttamente, ovvero 45 classificazioni corrette su 51
88 % classificate correttamente in media, ovvero 451 classificazioni corrette su 510
```

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
