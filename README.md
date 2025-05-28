# Freelancer Earnings Analysis Tool

![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)
![LangChain Version](https://img.shields.io/badge/LangChain-0.1%2B-orange)

A comprehensive Python tool for analyzing freelancer earnings data with natural language processing capabilities powered by LangChain and Ollama.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Available Predefined Queries](#available-predefined-queries)
- [Example Queries](#example-queries)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)

## Features

- **Data Analysis**: Comprehensive statistical analysis of freelancer earnings
- **Natural Language Queries**: Ask questions in plain English
- **LLM Integration**: Powered by DeepSeek model via Ollama
- **CLI Interface**: Easy-to-use command line interface
- **Predefined Queries**: Common analytical queries ready to use

## Installation

### Prerequisites

- **Python 3.9 or later**
- **Ollama installed and running**
- **DeepSeek model downloaded**

### Setup Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/test-task/freelancer-analysis.git
   cd test-task
   ```
   
## Project Structure

```
test/
├── data_analysis/
│   ├── analyzer.py         # Core data analysis functions
│   └── queries.py          # Predefined query templates
├── llm_integration/
│   └── llm_handler.py      # LangChain/Ollama integration
├── cli/
│   └── interface.py        # Command line interface
├── utils/
│   └── helpers.py          # Utility functions
├── main.py                 # Entry point
├── requirements.txt        # Dependencies
└── README.md   
```

## Usage
1. **List available queries:**
```
python main.py data/freelancer_earnings_bd.csv list
```

2. **Execute a predefined query:**
```
python main.py data/freelancer_earnings_bd.csv query payment_method_earnings
**or**
python main.py data/freelancer_earnings_bd.csv query "payment_method_earnings"
```

3. **Ask a natural language question:**
```
python main.py data/freelancer_earnings_bd.csv query "Find which payment method yields the highest earnings"
```
## Available Predefined Queries

- **payment_method_comparison**	- Compare earnings between payment methods
- **earnings_by_region** - Analyze earnings by client region
- **expert_performance**	- Analyze expert freelancer metrics
- **earnings_by_experience**	- Analyze earnings by experience level
- **top_platforms**	- Show top platforms by earnings
- **success_rate_analysis**	- Analyze job success rate statistics

## Example Queries
**Try these natural language questions:**
### data_analysis/queries.py
- "Find which payment method yields the highest earnings"
- "Percentage of experts with fewer than 100 jobs"
- "Show the top 3 platforms by average earnings"
- "Analyze earnings distribution by client region"
- "Analyze expert freelancer performance metrics"
- etc.

## Configuration

**Customize LLM behavior in llm_integration/llm_handler.py:**

```
self.llm = ChatOllama(
    model="deepseek-r1:14b",
    temperature=0.7,  # Controls randomness (0-1)
    top_p=0.9,        # Controls diversity
    repeat_penalty=1.1
)
```

## Troubleshooting
**Issue: "Cannot find reference 'Ollama'"**

```
pip install --upgrade langchain-community
```
**Issue: Model not found**

```
ollama serve
ollama pull deepseek-r1:14b
```
