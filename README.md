## Stato della documentazione

- **Ultima versione utilizzata:** 14/07/2026
- **Link build testata:** <https://github.com/Fil0807/BDAP_Automation-Public->


<br><br>

# BDAP-Automation-Deployment

Questa repository documenta i processi utilizzati per distribuire **BDAP Automation** come applicazione Windows.

L'obiettivo è consentire l'esecuzione del software senza richiedere all'utente finale l'installazione di Python o delle dipendenze del progetto.

## Metodi di distribuzione

- [Metodo 1 - Generazione dell'eseguibile con PyInstaller](#metodo-1---generazione-delleseguibile-con-pyinstaller): generazione di un eseguibile tramite PyInstaller.
- [Metodo 2 - Distribuzione tramite installer Windows (Inno Setup)](#metodo-2---distribuzione-tramite-installer-windows-inno-setup): creazione di un installer Windows che automatizzi completamente l'installazione dell'applicazione.
- [Metodo 3 - Distribuzione per macOS (PyInstaller)](#metodo-3---distribuzione-per-macos-PyInstaller): creazione di un file dmg per la condivisione installazione facilitata dell'app anche su MacOS.
<br><br><br>

# BDAP-Automation-Deployment

Questa repository documenta i processi utilizzati per distribuire **BDAP Automation** come applicazione Windows e macOS.
In tutti i passa è consigliata la creazione di un ambiente di sviluppo tramite i seguenti comandi:


Creazione ambiente virtuale:
```bash
python -m venv .venv
```

Attivazione ambiente virtule:
```bash
source .venv/bin/activate
```

Installazione/Aggiornaento dei requisiti:
```bash
pip install -r requirements.txt
```


<br>
<br>
<br>
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

Il secondo approccio prevede la distribuzione dell'applicazione tramite un installer Windows generato con **Inno Setup 7.0**.

Il file ```BDAPAutomation.iss``` comprende tutti i dati necessari ed un esempio del percorso per indicare i file corretti

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

<br><br><br>












# Metodo 3 - Distribuzione per macOS (PyInstaller)

La distribuzione per macOS avviene tramite la creazione di un'applicazione autonoma (`.app`) e della successiva conversione in un pacchetto di installazione (`.dmg`).

Per questo processo vengono utilizzati i seguenti strumenti:

- **PyInstaller**: converte il progetto Python in una normale applicazione macOS.
- **create-dmg**: genera il file `.dmg` utilizzato per distribuire l'applicazione.

<br>

## Requisiti

Per garantire la compatibilità con le librerie del progetto e con gli strumenti di conversione è necessario utilizzare una versione di **Python compresa tra la 3.11 e la 3.12**.

La procedura descritta di seguito utilizza **Python 3.12**.

<br>

## Processo di generazione

### 1. Verifica di Homebrew

Aprire il Terminale ed eseguire:

```bash
brew --version
```

Se il comando restituisce un errore o Homebrew non è installato, procedere con l'installazione:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

<br>

### 2. Installazione di create-dmg

Installare il tool necessario alla creazione del file `.dmg`:

```bash
brew install create-dmg
```

<br>

### 3. Posizionarsi nella cartella del progetto

Dal Terminale spostarsi nella cartella principale del progetto e aggiungere il file `BDAP Automation.spec`.

<br>


### 4. Installazione delle dipendenze

Installare tutte le dipendenze del progetto:

```bash
pip install -r requirements.txt
```

Installare successivamente `PyInstaller`:

```bash
pip install pyinstaller
```

<br>


### 5. Creazione file .app
Creare il file *.app* con il seguente comando:
```bash
pyinstaller --clean "BDAP Automation.spec
```

<br>

### 6. Creazione file .dmg
Da terminale attivo nella cartella del progetto:
```bash
create-dmg \
  --volname "BDAP Automation" \
  --window-size 800 400 \
  --icon-size 100 \
  --icon "BDAP Automation.app" 220 180 \
  --hide-extension "BDAP Automation.app" \
  --app-drop-link 580 180 \
  "BDAP_Automation.dmg" \
  "dist/"
```

<br>

## Performance e Test
Nel caso si volesse avere una versione più rapida da provare è possibile sostituire il file *BDAP Automation.spec* con il file *BDAP Automation-OneDir.spec*
!Rinominare il file o aggiornare i comandi!

Questa versione evita passaggi di compressione non necessarie nella fase di test, ma potrebbe causa problemi di compatibilità con alcune librerie.

<br>

## Compatibilità

La procedura è stata testata su sistemi macOS con processore **Intel**.

Per ottenere una build nativa compatibile con processori **Apple Silicon (M1, M2, M3, ...)** è necessario eseguire l'intera procedura di compilazione direttamente su un Mac dotato di tale architettura.

Questo è dovuto al fatto che alcune librerie Python contenenti componenti nativi (ad esempio **Pillow**) vengono compilate e scaricate automaticamente per l'architettura della macchina utilizzata durante la build.



