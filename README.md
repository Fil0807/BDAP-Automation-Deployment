## Stato della documentazione

- **Ultima versione utilizzata:** 18 giugno 2026
- **Link build testata:** <https://github.com/Elisabetta-43/Stage_Locatelli>


<br><br>

# BDAP-Automation-Deployment

Questa repository documenta i processi utilizzati per distribuire **BDAP Automation** come applicazione Windows.

L'obiettivo è consentire l'esecuzione del software senza richiedere all'utente finale l'installazione di Python o delle dipendenze del progetto.

## Metodi di distribuzione

- **Metodo 1:** generazione di un eseguibile tramite PyInstaller.
- **Metodo 2:** creazione di un installer Windows che automatizzi completamente l'installazione dell'applicazione.

<br><br><br>

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
ROOT
│
├── ...
└── BDAP_Automation/
      │
      ├── BDAP_Automation.exe
      └── _internal/
              │
              └── Dipendenze del programma
```

La cartella generata può essere distribuita direttamente all'utente finale senza ulteriori configurazioni.

<br>

## Librerie utilizzate

### PyInstaller

**PyInstaller** è lo strumento responsabile della conversione dell'applicazione Python in un programma eseguibile per Windows.

Durante la build analizza automaticamente le dipendenze del progetto e le include all'interno della distribuzione finale.

Documentazione ufficiale: <https://pyinstaller.org/>

<br>

## Considerazioni

### Vantaggi

- Nessuna installazione di Python richiesta.
- Distribuzione semplice e immediata.
- Compatibilità con sistemi Windows privi di ambiente di sviluppo.

### Limiti

- Distribuzione tramite una cartella contenente numerosi file.

<br><br><br>

# Metodo 2 - Distribuzione tramite installer Windows (Inno Setup)

## Obiettivo

Il secondo approccio prevede la distribuzione dell'applicazione tramite un installer Windows generato con **Inno Setup 7.0**.

L'obiettivo è fornire all'utente finale un'esperienza di installazione simile a quella delle comuni applicazioni Windows, riducendo al minimo le operazioni manuali e semplificando la gestione degli aggiornamenti e della disinstallazione.

<br>

## Strumento utilizzato

Download ufficiale:

<https://jrsoftware.org/isdl.php#v7>

Documentazione ufficiale:

<https://jrsoftware.org/isinfo.php>

<br>

## Funzionalità implementate

L'installer si occupa automaticamente di:

- Creazione della cartella di installazione.
- Copia dell'eseguibile e delle relative dipendenze.
- Creazione del collegamento sul Desktop.
- Creazione del gruppo applicazione nel menu Start.
- Registrazione dell'applicazione tra i programmi installati di Windows.
- Generazione automatica dell'uninstaller.
- Rimozione dei file installati durante la procedura di disinstallazione.

<br>

## Processo di distribuzione

1. Generazione della build tramite PyInstaller.
2. Raccolta dei file prodotti nella cartella di distribuzione.
3. Compilazione dello script `.iss` tramite Inno Setup.
4. Generazione del pacchetto di installazione finale (`BDAP Automation Installer.exe`).

<br>

## Output generato

L'output finale consiste in un singolo file eseguibile di installazione:

```text
BDAP Automation Installer.exe
```

L'utente finale può avviare il file e completare l'installazione tramite una procedura guidata standard di Windows.

<br>

## Vantaggi rispetto alla distribuzione diretta

- Distribuzione tramite un unico file.
- Installazione guidata.
- Presenza di una procedura di disinstallazione.

<br>
