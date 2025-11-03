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

- Python 3.9+
- Docker Desktop (for n8n workflow automation)
- Ollama (for local LLM) or OpenAI API key
- PowerShell (Windows) or Bash (Linux/Mac)

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd job_agent

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys and configuration
```

### Quick Start

**Option 1: Using n8n Workflows (Recommended)**

n8n provides a visual workflow automation interface with built-in LangChain and LLM support.

```bash
# 1. Open Docker Desktop

# 2. Start n8n container in Docker Desktop

# 3. Access n8n UI at http://localhost:5678

# 4. Import workflows from workflow/workflow.json
```

**Option 2: Using Jupyter Notebook**

```bash
# Initialize local LLM (if using Ollama)
./ollama_warmup.ps1

# Run the notebook to test the workflow
jupyter notebook notebook.ipynb
```

