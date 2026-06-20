# BDAP-Automation-Deployment

Questa repository documenta i processi utilizzati per distribuire **BDAP Automation** come applicazione Windows.

L'obiettivo è consentire l'esecuzione del software senza richiedere all'utente finale l'installazione di Python o delle dipendenze del progetto.

## Metodi di distribuzione

Attualmente sono in valutazione due differenti approcci di distribuzione:

- **Metodo 1:** generazione di un eseguibile tramite PyInstaller.
- **Metodo 2:** creazione di un installer Windows che automatizzi completamente l'installazione dell'applicazione.

<br>

# Metodo 1 - Generazione dell'eseguibile con PyInstaller

Il primo metodo utilizzato per distribuire **BDAP Automation** consiste nella creazione di un eseguibile tramite **PyInstaller**.

La build viene generata in modalità **OneDir**, producendo una cartella contenente l'eseguibile e tutte le dipendenze necessarie al funzionamento dell'applicazione.

<br>

## Configurazione del progetto

Nel file `requirements.txt` è stata aggiunta la dipendenza:

```txt
PyInstaller>=6.0
```

È stato inoltre creato il file `setup.py`, utilizzato per automatizzare la generazione dell'eseguibile.

Il file `setup.py` centralizza la configurazione della build e consente di avviare il processo di generazione tramite un unico comando.

Eseguendo:

```bash
python setup.py build_exe
```

viene avviato automaticamente **PyInstaller** con tutti i parametri necessari alla creazione della versione distribuibile dell'applicazione.

<br>

## Processo di generazione

### 1. Installazione delle dipendenze

```bash
pip install -r requirements.txt
```

### 2. Avvio della build

```bash
python setup.py build_exe
```

### 3. Generazione dell'output

Al termine del processo viene creata una cartella contenente l'eseguibile e tutte le librerie necessarie al funzionamento dell'applicazione.

<br>

## Output generato

```text
BDAP_Automation/
│
├── BDAP_Automation.exe
├── librerie Python
├── file runtime
├── DLL necessarie
└── altre dipendenze
```

La cartella generata può essere distribuita direttamente all'utente finale senza ulteriori configurazioni.

<br>

## Librerie utilizzate

### PyInstaller

**PyInstaller** è lo strumento responsabile della conversione dell'applicazione Python in un programma eseguibile per Windows.

Durante la build analizza automaticamente le dipendenze del progetto e le include all'interno della distribuzione finale.

Documentazione ufficiale: <https://pyinstaller.org/>

### tkinterdnd2

Libreria che fornisce il supporto alle funzionalità di **Drag & Drop** dell'interfaccia grafica.

Repository: <https://github.com/pmgagne/tkinterdnd2>

### openpyxl

Utilizzata per la lettura e la scrittura dei file Excel gestiti dall'applicazione.

Documentazione ufficiale: <https://openpyxl.readthedocs.io/>

### matplotlib

Libreria utilizzata per la generazione di grafici e visualizzazioni dati.

Documentazione ufficiale: <https://matplotlib.org/>

### Flask

Framework Python utilizzato per la realizzazione di applicazioni e servizi web.

Documentazione ufficiale: <https://flask.palletsprojects.com/>

<br>

## Considerazioni

### Vantaggi

- Nessuna installazione di Python richiesta.
- Distribuzione semplice e immediata.
- Compatibilità con sistemi Windows privi di ambiente di sviluppo.
- Procedura di build facilmente integrabile in pipeline automatiche.

### Limiti

- Distribuzione tramite una cartella contenente numerosi file.
- Dimensioni maggiori rispetto al solo codice sorgente.
- Possibili falsi positivi da alcuni antivirus.
- Necessità di rigenerare la build dopo ogni modifica dell'applicazione.

<br>

# Metodo 2 - Distribuzione tramite installer Windows

## Obiettivo

Il secondo approccio prevede la distribuzione dell'applicazione tramite un installer dedicato.

L'obiettivo è fornire all'utente finale un'esperienza di installazione simile a quella delle comuni applicazioni Windows, riducendo al minimo le operazioni manuali.

<br>

## Funzionalità previste

L'installer dovrà occuparsi automaticamente di:

- Creazione della cartella di installazione.
- Copia dell'eseguibile e delle dipendenze necessarie.
- Creazione dei collegamenti nel menu Start e sul Desktop.
- Configurazione delle risorse richieste dall'applicazione.
- Registrazione dell'applicazione tra i programmi installati di Windows.
- Generazione di una procedura di disinstallazione dedicata.

<br>

