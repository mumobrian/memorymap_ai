# 📘 MemoryMapAI Toolkit

A Friendly Guide to Building Conversational AI with Memory in Python

---

## 1. Title & Objective

**Title:** MemoryMapAI – A Beginner’s Guide to Conversational AI with Memory using OpenAI

**Objective:**
This project introduces beginners to conversational AI by showing how memory works in chatbots. We explore:

* Stateless conversations (no memory).
* Manual memory storage using a JSON file.
* A foundation for future expansion with frameworks like LangChain.

The end goal is to help beginners build a chatbot that remembers context, saves tasks, and persists conversations across sessions — something you don’t usually see in “Hello World” examples.

---

## 2. Quick Summary of the Technology

**What is it?**
MemoryMapAI is a Python-based project that demonstrates how to create conversational AI applications using the OpenAI API. It introduces memory management concepts step by step, starting from no memory → manual JSON memory → framework-ready.

**Where is it used?**

* Chatbots and customer support assistants
* Task managers or productivity apps
* Interactive AI tutors

**One real-world example:**
Think of ChatGPT itself. Unlike stateless bots, it remembers your previous messages, which makes conversations natural and continuous. MemoryMapAI shows how to implement this behavior.

---

## 3. System Requirements

* **Operating System:** Works on Windows, macOS, or Linux
* **Editor:** Visual Studio Code (VS Code) recommended
* **Python Version:** Python 3.8 or above
* **Required Packages (via requirements.txt):**

  * `openai>=1.0.0`
  * `python-dotenv>=1.0.0`
  * `orjson>=3.9.0`

---

## 4. Installation & Setup Instructions

Clone or create project folder:

```bash
mkdir memorymap_ai
cd memorymap_ai
```

Create virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Set up OpenAI API key:

1. Create a `.env` file in your project folder.
2. Add your API key:

   ```
   OPENAI_API_KEY=your_api_key_here
   ```

Run the chatbot:

```bash
python memorymap_ai.py
```

Choose a mode when prompted:

* `stateless` → No memory
* `manual` → Saves chat + tasks in `manual_memory.json`
* `exit` → Quit

---

## 5. Minimal Working Example

**What it does:**
A simple chatbot session that remembers tasks and conversation history in manual mode.

**Example code snippet:**

```python
# Start the chatbot in manual memory mode
mode = "manual"
print("Switched to manual memory mode with JSON persistence")

# User adds a task
user_input = "add task Buy milk"
# Bot response (asks for deadline)
"Got it! When should this task be completed?"

# User provides deadline
"Tomorrow 5PM"

# Bot saves it
"Task added: 'Buy milk' with deadline: Tomorrow 5PM"
```

**Expected output:**

```
[INFO] Switched to Manual Memory Mode
You: add task Buy milk
Bot: Got it! When should this task be completed?
You: Tomorrow 5PM
Bot: Task added: 'Buy milk' with deadline: Tomorrow 5PM
```

---

## 6. AI Prompt Journal

# 📝 AI Prompt Journal

---

## Prompt 1: Designing a Beginner-Friendly Chatbot with Memory

**Prompt:**
I want to build a simple Python chatbot for my capstone project that starts in a stateless mode but then evolves to show memory management step by step. I’m unsure how to structure my code in a way that beginners can understand while also leaving room to extend it.

**My approach so far:**

* Looked at basic chatbot tutorials using while True loops.
* Noticed examples often skip over persistence or memory.
* Identified JSON as a possible way to store conversation state.

**Project structure (so far):**

```
memorymap_ai/
├── memorymap_ai.py
├── memory.json   (if used for storing memory)
├── requirements.txt
└── .env
```

**Questions I asked myself:**

* Should I keep stateless and memory-based versions in the same script or split them into modules?
* How do I name functions so they clearly reflect what they do?
* What’s the best way for beginners to see the “before and after” of adding memory?

**AI Response Summary:**
The AI suggested starting with a very basic stateless chat loop, then adding JSON-based persistence as a separate function. It recommended descriptive function names like `chat_stateless` and `chat_with_manual_memory`. It emphasized that layering complexity helps beginners understand memory without being overwhelmed.

**Helpfulness:**
⭐ 10/10 – The roadmap made it much easier to teach and document. I now have a clear beginner-to-intermediate learning ladder for my chatbot project.

---

## Prompt 2: Debugging Setup & Running the Code in VS Code

**Prompt:**
I installed Python and copied the chatbot code, but I’m running into issues like `ModuleNotFoundError: No module named 'openai'` and missing API keys. I need a beginner-friendly checklist to run this project smoothly in VS Code.

**My approach so far:**

* Installed Python from the official site.
* Opened the project folder in VS Code.
* Tried running the script directly with `python memorymap_ai.py`.
* Saw multiple errors related to dependencies and `.env` configuration.

**Project structure (at this point):**

```
memorymap_ai/
├── memorymap_ai.py
├── requirements.txt
├── venv/  (virtual environment, after setup)
└── .env
```

**Key problem areas I identified:**

* Missing modules like `openai`.
* Unsure how to activate the virtual environment in VS Code.
* `.env` file not being recognized properly.

**AI Response Summary:**
The AI walked me through:

* Creating a virtual environment (`python -m venv venv`).
* Activating it inside VS Code.
* Installing dependencies (`pip install -r requirements.txt`).
* Adding a `.env` file with `OPENAI_API_KEY=....`.
* Running the app with `python memorymap_ai.py`.

It also explained how to delete and regenerate broken JSON files if persistence fails.

**Helpfulness:**
⭐ 9/10 – Felt like a step-by-step troubleshooting guide. Very helpful, though I still had to figure out Windows vs. Linux activation on my own.

---

## Prompt 3: Understanding a Java Project Structure

**Prompt:**
As a beginner Java developer, I see folders like `src/main/java`, `src/test/java`, and a `pom.xml` file, but I’m not sure where my code should go or how Maven fits into the build process.

**My approach so far:**

* Compared the folder structure to Python projects.
* Looked inside `src/main/java` and saw empty packages.
* Opened `pom.xml` but couldn’t make sense of all the XML tags.

**Project structure (simplified):**

```
my_java_project/
├── src/
│   ├── main/java/   (application code)
│   └── test/java/   (test cases)
├── pom.xml
└── target/          (auto-generated after build)
```

**Questions I asked myself:**

* Should the entry point always go in `src/main/java`?
* Does Maven automatically handle dependencies, or do I need to download JARs?
* What role do plugins in `pom.xml` play?

**AI Response Summary:**
The AI explained that:

* `src/main/java` is for application logic.
* `src/test/java` is for tests.
* `pom.xml` manages dependencies and build configuration.
* The entry point is typically a class with `public static void main(String[] args)`.
* It highlighted that Maven automates dependency management, so I don’t need to manually download JARs.

**Helpfulness:**
⭐ 9/10 – Cleared up the Maven mystery and explained the folder structure well. Made me confident about where to place my main Java class.

## 7. Common Issues & Fixes

Like most real-world projects, my chatbot didn’t work flawlessly the first time. Here are common issues I faced and how I fixed them:

# 🛠 Common Issues & Fixes

---

## Issue 1: `ModuleNotFoundError: No module named 'openai'`

**What happened:**
When I first ran the program, Python complained that the `openai` module was missing.

**Why:**
Dependencies were not installed inside the virtual environment.

**Fix:**
Activate the virtual environment:

* Windows:

  ```bash
  venv\Scripts\activate
  ```
* Mac/Linux:

  ```bash
  source venv/bin/activate
  ```

Reinstall dependencies:

```bash
pip install -r requirements.txt
```

---

## Issue 2: `FileNotFoundError: memory.json not found`

**What happened:**
The memory feature broke because the JSON file didn’t exist yet.

**Why:**
The program assumes `memory.json` is already there.

**Fix:**
Create an empty JSON file before first run:

```json
[]
```

Save it as `memory.json` in the project folder. From then on, the chatbot will update it automatically.

---

## Issue 3: `ValueError: OPENAI_API_KEY not found`

**What happened:**
The chatbot immediately failed with an API key error.

**Why:**
I had created a `.env` file, but the formatting was wrong (extra spaces, quotes, or missing altogether).

**Fix:**
Create a `.env` file in the root directory:

```
OPENAI_API_KEY=sk-your-real-key-here
```

Make sure there are **no spaces or quotes**.
Restart the terminal so the environment variables reload.

---

## Issue 4: `json.decoder.JSONDecodeError`

**What happened:**
At some point, the chatbot crashed in the middle of saving, leaving `memory.json` corrupted.

**Why:**
The file contained half-written data or invalid JSON which is soo common in early development.

**Fix:**

* Open `memory.json` and check for missing brackets/commas.
* If it’s beyond saving, delete it and let the program regenerate a fresh file.

---

## Issue 5: Bot Always Responds the Same Way

**What happened:**
No matter what I typed, the bot repeated the same answer.

**Why:**
I had accidentally hardcoded `"Hello"` instead of passing `user_input` into the API call.

**Fix:**
Check that you’re using:

```python
messages=[{"role": "user", "content": user_input}]
```

instead of any fixed text.


## 8. References

* [OpenAI Python Docs](https://platform.openai.com/docs/libraries/python)
* [LangChain Official Docs](https://python.langchain.com/)
* [Python Dotenv](https://pypi.org/project/python-dotenv/)
* [Real Python – Working with JSON](https://realpython.com/python-json/)
