# Flask portability test

A minimal Flask app that displays a text message plus details of the environment
serving it (Python version, Flask version, OS). Used to check that a project built
in one environment runs unchanged in another.

Requires Python 3.9+.

## Run

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000

## Endpoints

| Path      | Returns                                |
|-----------|----------------------------------------|
| `/`       | The message and environment details    |
| `/health` | `{"status": "ok"}` for a quick check   |

## Optional settings (environment variables)

| Variable      | Default                                | Purpose                                   |
|---------------|----------------------------------------|-------------------------------------------|
| `APP_MESSAGE` | `Hello from the portability test app!` | Text shown on the page                    |
| `HOST`        | `127.0.0.1`                            | Use `0.0.0.0` to reach it from other hosts |
| `PORT`        | `5000`                                 | Listening port                            |

## Moving it to another environment

Copy `app.py`, `requirements.txt` and this README (not `.venv`), then repeat the
Run steps there. The page shows the Python version, OS and interpreter path, so
you can confirm which environment is serving it.
