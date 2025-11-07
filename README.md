# Job-Hunting AI Agent

> An autonomous agentic-AI system to streamline and optimize the job application process for engineers

## 🎯 Overview

The Job-Hunting AI Agent is an intelligent automation system designed to revolutionize the way engineers search for and apply to job opportunities. By leveraging advanced AI capabilities, this agent automates the tedious aspects of job hunting while personalizing applications to maximize success rates.

**Core Use Case:** Automated job search and application preparation for engineering positions

**Target Users:** Engineers actively searching for new job opportunities

**Success Metric:** Increase the conversion rate from job applications to first-round interviews

## 🔍 Problem Statement

### Current Challenges

The traditional job search process is inefficient and time-consuming:

- **Manual Job Discovery:** Constantly checking multiple job websites or relying on generic daily emails from platforms like Indeed
- **Static Application Materials:** CVs remain unchanged regardless of specific job requirements
- **Labor-Intensive Personalization:** Manually using tools like Notebook LLM to craft motivation letters for each application
- **Low Signal-to-Noise Ratio:** Sifting through irrelevant job postings to find suitable opportunities

### The Solution

The Job-Hunting AI Agent addresses these pain points through intelligent automation:

- **Job Search & Aggregation:** Integrate with multiple job portals (Indeed, LinkedIn, company career pages) to collect and normalize job postings automatically
- **Job Description Analysis:** Use NLP to classify and rank jobs based on relevance to the user's skills, preferences, and location
- **CV & Motivation Letter Automation:** Automatically tailor the CV and motivation letter to each job description, with a user interface for review and approval before submission
- **Application Tracking:** Track submitted applications, interviews, and outcomes to provide feedback and improve future recommendations

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- [Poetry](https://python-poetry.org/docs/#installation) (recommended) or pip
- Docker Desktop (for n8n workflow automation)
- Ollama (for local LLM) or OpenAI API key
- PowerShell (Windows) or Bash (Linux/Mac)

### Installation with Poetry (Recommended)

#### 1. Install Poetry

If you don't have Poetry installed:

**Windows (PowerShell):**
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

**Linux/Mac:**
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

#### 2. Clone and Install

```bash
# Clone the repository
git clone <repository-url>
cd job_agent

# Install dependencies (Poetry automatically creates and manages venv)
poetry install

# This installs all dependencies including dev tools:
# pytest, black, ruff, mypy, jupyter, ipykernel
```

#### 3. Activate Poetry Shell (Optional)

```bash
poetry shell
```

Or run commands directly with `poetry run`:
```bash
poetry run pytest
poetry run jupyter notebook
```

#### 4. Set Up Environment Variables (Optional)

```bash
cp .env.example .env
# Edit .env with your API keys and configuration
```

### Alternative: Installation with pip

If you prefer traditional pip:

```bash
# Clone the repository
git clone <repository-url>
cd job_agent

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or: .\venv\Scripts\Activate.ps1  # Windows

# Install in editable mode with dev dependencies
pip install -e ".[dev]"
```

## 🏃 Quick Start

### 1. Using n8n Workflows

n8n provides a visual workflow automation interface with built-in LangChain and LLM support.

```bash
# 1. Open Docker Desktop

# 2. Start n8n container in Docker Desktop

# 3. Access n8n UI at http://localhost:5678

# 4. Import workflows from workflow/workflow.json
```

When self-hosting n8n on Windows, mount `C:\Users\yanyi\Documents\AI_project\job_agent\` into /data folder in n8n containern, which enable reading prompts and persist generated files from within the container.

### 2. Using Ollama (Local LLM)

Start the local LLM (qwen3:0.6b) that supports HTTP requests:

```bash
ollama run qwen3:0.6b
```

Warm up Ollama using PowerShell:

```powershell
./ollama_warmup.ps1
```

To stop the LLM, simply close the terminal window running the command.

### 3. Using Jupyter Notebooks

With Poetry:
```bash
poetry run jupyter notebook
# or if in poetry shell:
jupyter notebook
```

Navigate to `notebooks/` and open `notebook.ipynb`.

## 💻 Usage

### Working with Poetry

**Add a new dependency:**
```bash
poetry add requests
poetry add openai
```

**Add a dev dependency:**
```bash
poetry add --group dev pytest-mock
```

**Run commands in Poetry environment:**
```bash
poetry run python script.py
poetry run pytest
poetry run jupyter notebook
```

**Activate Poetry shell:**
```bash
poetry shell  # Now you can run commands directly
python script.py
pytest
jupyter notebook
```

**Update dependencies:**
```bash
poetry update
```

**Show installed packages:**
```bash
poetry show
poetry show --tree  # Shows dependency tree
```

### In Python Scripts

After installation, you can import from `job_agent`:

```python
from job_agent import load_prompt_file

# Load a prompt file
prompt = load_prompt_file("prompts/ai_agent.prompt")
print(prompt)
```

### In Jupyter Notebooks

#### Setup Jupyter Kernel (One-time Setup)

For the best experience, create a dedicated Jupyter kernel for this project:

```bash
poetry run python -m ipykernel install --user --name=job_agent --display-name="Python (job_agent)"
```

Then in Jupyter:
1. Open your notebook
2. Click **Kernel** → **Change Kernel** → **Python (job_agent)**

Or in VS Code:
- Click **Select Kernel** → Choose **Python (job_agent)**

#### Using the Kernel

With the kernel selected, imports work seamlessly:

```python
from job_agent import load_prompt_file

prompt = load_prompt_file("../prompts/ai_agent.prompt")
```

#### Adding New Packages

**Good news!** You don't need to reinstall the kernel when adding new packages:

```bash
# Add a new package
poetry add requests

# The package is automatically available!
# Just restart the kernel in Jupyter:
# Kernel → Restart
```

The kernel points to your Poetry environment, so any new packages installed with `poetry add` are immediately available after a kernel restart.

### Available Utilities

Currently available in the `job_agent` package:

- **`load_prompt_file(file_path, ignore_comments=True)`** - Load prompt files and filter out comment lines

## 🛠️ Development

### Development Workflow with Poetry

1. **Make code changes** in `src/job_agent/`
2. **Add tests** in `tests/`
3. **Run tests:**
   ```bash
   poetry run pytest
   # or with coverage:
   poetry run pytest --cov=job_agent
   ```
4. **Format code:**
   ```bash
   poetry run black .
   # or:
   poetry run ruff format .
   ```
5. **Check for issues:**
   ```bash
   poetry run ruff check .
   ```

### Adding New Dependencies with Poetry

**Add runtime dependency:**
```bash
poetry add package-name
```

**Add with version constraint:**
```bash
poetry add "package-name>=1.0.0"
poetry add "package-name^1.0.0"  # Compatible with 1.x.x
```

**Add development dependency:**
```bash
poetry add --group dev package-name
```

Poetry automatically updates `pyproject.toml` and `poetry.lock`.

### Code Formatting

```bash
poetry run black .
# or
poetry run ruff format .
```

### Linting

```bash
poetry run ruff check .
```

## 🧪 Testing

### Run All Tests

```bash
poetry run pytest
```

### Run with Coverage

```bash
poetry run pytest --cov=job_agent
```

### Run Specific Test File

```bash
poetry run pytest tests/test_file_utils.py
```

### Run Tests with Verbose Output

```bash
poetry run pytest -v
```

## 🔧 Troubleshooting

### Poetry-specific Issues

**Poetry not found after installation:**

Add Poetry to your PATH. Restart your terminal or:

**Windows:**
```powershell
$env:Path += ";$env:APPDATA\Python\Scripts"
```

**Linux/Mac:**
```bash
export PATH="$HOME/.local/bin:$PATH"
```

**Virtual environment location:**

Poetry creates venvs in a cache directory by default. To create it in the project:
```bash
poetry config virtualenvs.in-project true
poetry install
```

**Lock file issues:**

If you get lock file errors:
```bash
poetry lock --no-update  # Regenerate lock file
poetry install
```

**Clear Poetry cache:**
```bash
poetry cache clear . --all
```

### Import errors in notebooks

If you get import errors in Jupyter:

**1. Check you're using the correct kernel:**
   - Look at top-right corner of notebook
   - Should show **"Python (job_agent)"** or **"job_agent"**
   - If not, click **Kernel** → **Change Kernel** → **Python (job_agent)**

**2. Install the kernel if missing:**
   ```bash
   poetry run python -m ipykernel install --user --name=job_agent --display-name="Python (job_agent)"
   ```

**3. Restart the kernel:**
   - In Jupyter: **Kernel** → **Restart**

**4. Verify installation:**
   ```bash
   poetry run python -c "from job_agent import load_prompt_file; print('✅ Import successful!')"
   ```

**5. After adding new packages:**
   - You don't need to reinstall the kernel
   - Just restart it: **Kernel** → **Restart**

### Tests not found

Make sure you're running pytest from the project root with Poetry:
```bash
poetry run pytest
```

### Dependency conflicts

If Poetry can't resolve dependencies:
```bash
poetry update  # Update to latest compatible versions
# or
poetry add package-name --dry-run  # Check before adding
```

## 📚 Poetry Quick Reference

| Task | Poetry Command | pip Equivalent |
|------|----------------|----------------|
| Install project | `poetry install` | `pip install -e ".[dev]"` |
| Add dependency | `poetry add requests` | `pip install requests` (+ edit pyproject.toml) |
| Add dev dependency | `poetry add --group dev pytest` | `pip install pytest` (+ edit pyproject.toml) |
| Update deps | `poetry update` | `pip install --upgrade ...` |
| Run command | `poetry run pytest` | `pytest` (after venv activation) |
| Activate shell | `poetry shell` | `source venv/bin/activate` |
| Show deps | `poetry show` | `pip list` |
| Remove dep | `poetry remove package` | `pip uninstall package` |
| Setup Jupyter kernel | `poetry run python -m ipykernel install --user --name=job_agent` | Manual venv + ipykernel |
| Start Jupyter | `poetry run jupyter notebook` | `jupyter notebook` (after venv activation) |

## 📝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

[Add your license here]

## 🙏 Acknowledgments

- n8n for workflow automation
- Ollama for local LLM capabilities
- Poetry for dependency management

---

**Note:** This project uses Poetry for dependency management. See the [Poetry documentation](https://python-poetry.org/docs/) for more information.
