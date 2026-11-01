# Sprint 3 Project - CNN for pills classification

Environment setup with **uv** and **Python 3.10**.

This project uses [uv](https://docs.astral.sh/uv/) as the Python
package/environment manager and targets Python 3.10.

---

## 1. Install uv

If you don't have uv installed yet, install it with one of these:

```bash
# Linux / macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

```

Verify the installation:

```bash
uv --version
```

---

## 2. Create the virtual environment (Python 3.10)

The project pins Python 3.10 via the `.python-version` file, so uv will
pick it up automatically. Create the environment from scratch:

```bash
uv venv --python 3.10
```

This creates a `.venv` folder in the project root.

uv can also download Python 3.10 for you if it is not installed:

```bash
uv python install 3.10
uv venv --python 3.10
```

---

## 3. Install the dependencies

Install all required packages listed in `requirements_sprint2_project.txt`:

```bash
uv pip install -r requirements_sprint2_project.txt
```

Alternatively, install directly from `pyproject.toml` (synchronizes the
environment exactly to the project spec):

```bash
uv sync
```

---

## 4. Activate the environment (optional)

```bash
# Linux / macOS
source .venv/bin/activate
```

Most uv commands (`uv run ...`) work without manual activation.

---

## 5. Common commands

```bash
# Run a specific Python script
uv run python your_script.py

# Re-sync environment to match pyproject.toml / uv.lock
uv sync

# Remove the environment
rm -rf .venv      # Linux/macOS
rmdir /s .venv    # Windows cmd
```

---

## Content of `requirements_sprint2_project.txt`

```text
torch>=2.0.0
numpy>=1.24.0
pandas>=2.0.0
matplotlib>=3.7.0
datasets>=2.14.0
transformers>=4.30.0
tokenizers>=0.13.0
tqdm>=4.65.0
jupyter>=1.0.0
ipywidgets>=8.0.0
```

## 6. Настройка переменных окружения

Подговьте `.env` файл:

```env
OGYEIV2_DATASET_SRC_DIR=<директория_загрузки_датасета_из_Kaggle>
OGYEIV2_DATASET_DEST_DIR="data/dataset/ogyeiv2/parsed"
```