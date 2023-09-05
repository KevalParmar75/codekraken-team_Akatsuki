Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
import tkinter as tk
from tkinter import messagebox

import openai

# Initialize your OpenAI GPT-3 API key
openai.api_key = 'your api key'

# Create a chat function using GPT-3
def chat_with_gpt(input_text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=input_text,
        max_tokens=50
    )
    return response.choices[0].text.strip()

# Create the main application window
app = tk.Tk()
app.title("To-Do App with Chat")

# To-Do List
tasks = []

# Function to add a task
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

# Function to delete a task
def delete_task():
    selected_task = listbox.curselection()
    if selected_task:
        index = selected_task[0]
        listbox.delete(index)
        tasks.pop(index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Function to get task suggestions from GPT-3
def get_task_suggestions():
    input_text = "I need suggestions for my to-do list. My current tasks are: " + ", ".join(tasks)
    suggestion = chat_with_gpt(input_text)
    entry.insert(tk.END, suggestion)

# Create and configure widgets
frame = tk.Frame(app)
frame.pack(pady=10)

label = tk.Label(frame, text="To-Do List:")
label.pack()

listbox = tk.Listbox(frame, selectmode=tk.SINGLE)
listbox.pack()

entry = tk.Entry(frame, width=40)
entry.pack()

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack()

delete_button = tk.Button(frame, text="Delete Task", command=delete_task)
delete_button.pack()

get_suggestions_button = tk.Button(frame, text="Get Task Suggestions", command=get_task_suggestions)
get_suggestions_button.pack()

# Main loop
app.mainloop()

