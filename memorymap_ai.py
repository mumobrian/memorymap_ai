"""
🚀 MemoryMapAI – A Beginner’s Guide to Conversational Memory & Task Tracking
Using OpenAI for responses
"""

import os
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime
import json

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MEMORY_FILE = "manual_memory.json"

def load_manual_memory():
    """Load memory and tasks from JSON file."""
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"conversation": [], "tasks": []}


def save_manual_memory(memory):
    """Save memory and tasks to JSON file."""
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)


# ====== Stateless Mode ======
def stateless_chat(user_input):
    """Chat with OpenAI without memory."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_input}]
    )
    return response.choices[0].message.content


# ====== Manual Memory Mode ======
def manual_memory_chat(user_input, memory):
    """Chat with manual memory (conversation + tasks)."""
    # Save conversation
    memory["conversation"].append({"role": "user", "content": user_input})

    # Handle task commands
    if user_input.lower().startswith("add task"):
        task_name = user_input.replace("add task", "").strip()
        deadline = input("Enter deadline (YYYY-MM-DD HH:MM) or press Enter to skip: ")
        task = {
            "task": task_name,
            "deadline": deadline if deadline else "No deadline",
            "added": datetime.now().strftime("%Y-%m-%d %H:%M"),
        }
        memory["tasks"].append(task)
        save_manual_memory(memory)
        return f"✅ Task added: {task_name}"

    elif user_input.lower().startswith("view tasks"):
        if not memory["tasks"]:
            return "⚠️ No tasks available."
        task_list = "\n".join(
            [f"- {t['task']} (Deadline: {t['deadline']}, Added: {t['added']})"
             for t in memory["tasks"]]
        )
        return f"📝 Your tasks:\n{task_list}"

    elif user_input.lower().startswith("delete task"):
        if not memory["tasks"]:
            return "⚠️ No tasks to delete."
        for i, t in enumerate(memory["tasks"], start=1):
            print(f"{i}. {t['task']}")
        choice = int(input("Enter task number to delete: "))
        if 1 <= choice <= len(memory["tasks"]):
            removed = memory["tasks"].pop(choice - 1)
            save_manual_memory(memory)
            return f"🗑️ Task deleted: {removed['task']}"
        else:
            return "⚠️ Invalid task number."

    # Normal chat with history
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=memory["conversation"]
    )
    ai_reply = response.choices[0].message.content
    memory["conversation"].append({"role": "assistant", "content": ai_reply})
    save_manual_memory(memory)
    return ai_reply


# ====== Framework Memory Mode (LangChain Integration Placeholder) ======
def langchain_memory_chat(user_input):
    """
    Placeholder for LangChain integration.
    Here you’d use LangChain's ConversationBufferMemory or ConversationSummaryMemory.
    For now, we'll just simulate extended memory.
    """
    return f"[LangChain Mode Simulated] You said: {user_input}"


# ====== Main App ======
def main():
    print("👋 Welcome to MemoryMapAI – Explore conversational memory with OpenAI")
    print("Modes: \n1. Stateless \n2. Manual Memory \n3. LangChain Memory (simulated)\n")

    while True:
        mode = input("Choose mode (1-3) or 'exit' to quit: ")

        if mode == "exit":
            print("👋 Goodbye! Memory saved.")
            break

        user_input = input("You: ")

        if mode == "1":
            reply = stateless_chat(user_input)
        elif mode == "2":
            memory = load_manual_memory()
            reply = manual_memory_chat(user_input, memory)
        elif mode == "3":
            reply = langchain_memory_chat(user_input)
        else:
            reply = "⚠️ Invalid mode. Choose 1, 2, or 3."

        print(f"AI: {reply}")


if __name__ == "__main__":
    main()
