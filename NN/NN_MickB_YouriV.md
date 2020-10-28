# Neural Network
### Mick Bos en Youri de Vor  
## Uitleg Code  
### Call Tree  
main  
- randomWeights
- updatevalue  
- update  
    - receiveWeightedError  
    - updateInputs  
        - getOutput  
    - inK
    - delta  
        - getOutput
            - sigmoid  
        - derivedSigmoid

### Totaal-Uitleg
De Dataset wordt met numpy gegenereerd. Er wordt vervolgens een selectie gemaakt om als validatieset te gebruiken. De rest van de data wordt trainingsdata. De bloemen namen worden gecodeerd als arrays van drie bits. 1,0,0, 0,1,0 en 0,0,1 zijn de opties. Dit wordt door middel van een lambda gedaan. Om dit te laten werken is met CTRL + H de originele dataset aangepast door de bloemennamen te vervangen voor getallen 1, 2 of 3. Numpy's **genfromtxt** werkt namelijk niet met strings of arrays.

Door middel van **sigmoidneuron** (constructor) worden er neuronen aangemaakt in lijsten. Deze lijsten fungeren als layers. Als input lijst krijgt een **sigmoidneuron** de vorige layer mee. 

Vervolgens wordt er 1000 keer over de trainingsdata geloopt. Voor ieder datapunt wordt **update** gecalld. Update zorgt ervoor dat de gewichten van de output layer neuronen worden aangepast en callt vervolgens **update** voor alle voorgaande neuronen na hen de benodigde weighted errors gegeven te hebben voor backpropagation. 

> Door middel van de **progressbar** library wordt progressie geprint.

Na 1000 iteraties wordt door middel van **getOutput** voor alle drie de neuronen een prediction gevraagd voor de gegeven validatie data. Deze worden achter elkaar in een array gezet om te vergelijken met de correcte labels.
Correcte antwoorden worden genoteerd en aan het einde worden alle vergelijkingen geprint met onderaan een accuraatheidspercentage.



## Resultaten
Op een validatieset van 24 entries maakt het netwerk slechts twee fouten. Dit komt neer op een accuraatheid van 91,7%
|prediction|correct answer|correct?
|---|---|---|
| [0 1 0] | [0 1 0]|v
| [1 0 0] | [1 0 0]|v
| [0 0 1] | [0 0 1]|v
| [0 1 0] | [0 1 0]|v
| [1 0 0] | [1 0 0]|v
| [1 0 0] | [1 0 0]|v
| [1 0 0] | [1 0 0]|v
| [0 1 0] | [0 1 0]|v
| [1 0 0] | [1 0 0]|v
| [0 1 0] | [0 1 0]|v
| [1 0 0] | [1 0 0]|v
| [0 1 0] | [0 1 0]|v
| [1 0 0] | [1 0 0]|v
| [0 0 1] | [0 0 1]|v
| [1 0 0] | [0 1 0]|x
| [0 0 1] | [0 0 1]|v
| [0 0 1] | [0 0 1]|v
| [0 1 0] | [0 1 0]|v
| [1 0 0] | [1 0 0]|v
| [0 0 1] | [0 0 1]|v
| [0 1 0] | [0 1 0]|v
| [0 0 1] | [0 0 1]|v
| [0 0 1] | [0 0 1]|v
| [1 0 0] | [0 1 0]|x

|Accuracy: |91.66666666666666 %|
|---|---|
