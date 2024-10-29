# Welcome to the Repository

This is a simple Text Summarization Tool. You can either provide a text to summarize or provide a link to the target article.

## Table of Contents

- [Installation](#installation)
- [Launch](#launch)
- [Implementation Details](#implementation-etails)
- [Result Evaluation](#result-evaluation)
- [Future Improvements](#future-mprovements)

## Installation

### Ollama
1. macOS: Download [here](https://ollama.com/download/Ollama-darwin.zip)
2. Windows: Download [here](https://ollama.com/download/OllamaSetup.exe)
3. Linux: `curl -fsSL https://ollama.com/install.sh | sh`

Then, run `ollama pull llama3.2:1b` to pull the model

For more information, visit https://github.com/ollama/ollama/tree/main

### Backend
```bash
cd backend
pip install -r requirements.txt
```

### Frontend
```bash
cd frontend
npm install
```

## Launch
### Ollama
```bash
ollama run llama3.2:1b
```

### Backend
```bash
cd backend
flask run
```

### Frontend
```bash
cd frontend
npm start
```

## Implementation Details

The project implemented a zero-shot prompting strategy in the core summarization agent. By prompting the system with a message and defining its role and responsibilities, this provides basic context to the LLM. The target text is subsequently fed into the model, and the generated response is returned as the result.

## Result Evaluation

To evaluate the results, we compared our generated output with the summary produced by [Resoomer](https://resoomer.com/en/), an online website summarizing tool. We utilized [this](https://edition.cnn.com/2024/10/28/politics/trump-extreme-closing-argument/index.html) CNN news article as the reference website and retrieved summaries from both platforms. While our tool successfully delivers a more concise output, Resoomer excelled in presenting the response with distinct paragraphs and subsections. Depending on users' requirements, each tool satisfies different expectations.

## Future Improvements

There are several planned improvements:

1. Refined prompts: By creating a more refined prompt or employing other methods such as the few-shot prompting strategy, we can enhance the results by offering a more structured summary in response.

2. Result Verification: By establishing additional agents like a VerificationAgent, we can assess the quality of the results and only accept responses of high quality.

3. Improved UI: By designing a better user interface, users can have an enhanced experience.