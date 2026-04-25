
#!/usr/bin/env bash
set -euo pipefail

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

if [ ! -f .env ]; then
  cp .env.example .env
  echo "Created .env from .env.example. Edit .env and set OPENAI_API_KEY."
fi

echo "Setup complete."
echo "Activate with: source .venv/bin/activate"
echo "Run with: python -m agent_app.main"
