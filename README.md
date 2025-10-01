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

### Prompt 1: Designing a Beginner-Friendly Chatbot with Memory

**Prompt:**
I want to build a simple Python chatbot for my capstone project that starts in a stateless mode but then evolves to show memory management step by step.

**AI Response Summary:**

* Start with a stateless chat loop.
* Add JSON-based persistence as a separate function.
* Use descriptive function names like `chat_stateless` and `chat_with_manual_memory`.
* Layer complexity gradually to help beginners.

**Helpfulness:**  – The roadmap made it much easier to teach and document. I now have a clear beginner-to-intermediate learning ladder for my chatbot project. 

---

### Prompt 2: Debugging Setup & Running the Code in VS Code

**Prompt:**
I installed Python and copied the chatbot code, but I’m running into issues like `ModuleNotFoundError: No module named 'openai'` and missing API keys.

**AI Response Summary:**

* Create a virtual environment (`python -m venv venv`).
* Activate inside VS Code.
* Install dependencies (`pip install -r requirements.txt`).
* Add `.env` with `OPENAI_API_KEY=...`.
* Run with `python memorymap_ai.py`.

**Helpfulness:** (9/10) Felt like a step-by-step troubleshooting guide. Very helpful, though I still had to figure out Windows vs. Linux activation on my own.

---

### Prompt 3: Understanding a Java Project Structure

**Prompt:**
As a beginner Java developer, I see folders like `src/main/java`, `src/test/java`, and a `pom.xml` file.

**AI Response Summary:**

* `src/main/java` → Application logic
* `src/test/java` → Tests
* `pom.xml` → Dependencies & build configuration
* Entry point → `public static void main(String[] args)`
* Maven automates dependency management.

**Helpfulness:**  (9/10) Cleared up the Maven mystery and explained the folder structure well. Made me confident about where to place my main Java class.

---

## 7. Common Issues & Fixes

Like most real-world projects, my chatbot didn’t work flawlessly the first time. Here are common issues I faced and how I fixed them:

### Issue 1: `ModuleNotFoundError: No module named 'openai'`

* **Why:** Dependencies not installed in virtual environment.
* **Fix:**

  ```bash
  venv\Scripts\activate   # Windows
  source venv/bin/activate   # Mac/Linux
  pip install -r requirements.txt
  ```

### Issue 2: `ValueError: OPENAI_API_KEY not found`

* **Why:** `.env` file missing or misformatted.
* **Fix:**

  ```
  OPENAI_API_KEY=sk-your-real-key-here
  ```

  (No spaces, no quotes)

### Issue 3: `FileNotFoundError: memory.json not found`

* **Why:** File doesn’t exist yet.
* **Fix:** Create an empty file:

  ```json
  []
  ```

### Issue 4: `json.decoder.JSONDecodeError`

* **Why:** `memory.json` got corrupted.
* **Fix:** Delete or fix formatting, then restart program.

---

## 8. References

* [OpenAI Python Docs](https://platform.openai.com/docs/libraries/python)
* [LangChain Official Docs](https://python.langchain.com/)
* [Python Dotenv](https://pypi.org/project/python-dotenv/)
* [Real Python – Working with JSON](https://realpython.com/python-json/)
