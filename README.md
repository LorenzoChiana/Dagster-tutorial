# Dagster-tutorial

Questo repository fornisce un tutorial per configurare e utilizzare Dagster, un orchestratore di dati per machine learning, analisi ed ETL. Segui le istruzioni qui sotto per iniziare.

## Introduzione

### Prerequisiti

Assicurati di avere Python 3 installato sul tuo computer. Puoi controllare la versione di Python con:
```bash
python3 --version
```

### Configurazione

1. **Crea un ambiente virtuale:**

   ```bash
   python3 -m venv .pyenv
   ```

2. **Attiva l'ambiente virtuale:**

   - Su Unix o MacOS, esegui:
     ```bash
     source .pyenv/bin/activate
     ```
   - Su Windows, esegui:
     ```bash
     .pyenv\Scripts\activate
     ```

3. **Installa Dagster e Dagster Webserver:**

   ```bash
   pip install dagster dagster-webserver
   ```

### Esecuzione del Server di Sviluppo di Dagster

1. **Avvia il server di sviluppo di Dagster:**

   ```bash
   dagster dev -f hello-dagster.py
   ```

   Questo avvierà il server web di Dagster, che puoi accedere nel tuo browser web all'indirizzo `http://localhost:3000`.

### Struttura dei File

- `hello-dagster.py`: Questo file contiene la definizione della pipeline di Dagster.

### Risorse Aggiuntive

Per maggiori informazioni su come utilizzare Dagster, visita la [documentazione ufficiale](https://docs.dagster.io/).

## Licenza

Questo progetto è licenziato sotto la Licenza MIT. Consulta il file [LICENSE](LICENSE) per i dettagli.
