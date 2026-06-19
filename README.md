# BDAP-Automation-Deployment
Documentazione del processo di conversione di BDAP Automation da applicazione Python a eseguibile Windows.
L



# Metodo 1 : Generazione dell'eseguibile con PyInstaller
Il primo metodo utilizzato per distribuire BDAP Automation consiste nella creazione di un eseguibili tramite PyInstaller

L'output consiste in una cartella contenente tutte le dipendenze del programma e l'eseguibile.
Non richiede di installere python o librerie da parte dell'utente

<br><br>

# Modifiche effettuate
Nel file `requirements.txt` è stata aggiunta la dipendenza:

```PyInstaller>=6.0```

<br>

È stato creato il file `setup.py`, per la generazione dell'eseguibile.
Eseguendo il comando:
```python setup.py build_exe```
si esegue automaticamente PyInstaller con tutti i parametri necessari alla creazione della versione distribuibile dell'applicazione.

<br><br>

# Processo di Generazione
1. Installazione delle dipendenze

```pip install -r requirements.txt```

2. Avvio della build

```python setup.py build_exe```

3. Generazione dell'output
Al termine del processo viene creata una cartella contenente l'eseguibile e tutte le librerie necessarie al funzionamento dell'applicazione


```text
BDAP_Automation/
│
├── BDAP_Automation.exe
├── librerie Python
├── file runtime
├── DLL necessarie
└── altre dipendenze
```

<br><br>


# Librerie Utilizzate
*PyInstaller*

PyInstaller è lo strumento responsabile della conversione dell'applicazione Python in un programma eseguibile per Windows.

Durante la build analizza automaticamente le dipendenze del progetto e le include all'interno della cartella finale.

*tkinterdnd2*
Librerie che fornisce il supporto alle funzionalità di Drag&Drop dell'interfaccia grafica


*openpyxl*
Utilizzata per la lettura e la scrittura dei file Excel gestiti dall'applicazione.


*matplotlib e Flask*
Presenti tra le dipendenze del progetto e incluse automaticamente nella distribuzione quando necessarie.

