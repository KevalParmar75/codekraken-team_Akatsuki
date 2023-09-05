Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> pip install tkinter openai
... import tkinter as tk
... import openai
... 
... # Replace with your OpenAI GPT-3 API key
... api_key = "YOUR_API_KEY"
... openai.api_key = api_key
... 
... def generate_task_suggestion(task_description):
...     response = openai.Completion.create(
...         engine="text-davinci-002",
...         prompt=f"Suggest a task related to: {task_description}\n",
...         max_tokens=30,
...         n=1,
...         stop=None,
...         temperature=0.7,
...     )
...     return response.choices[0].text.strip()
... 
... def add_task():
...     task_description = entry.get()
...     if task_description:
...         suggestion = generate_task_suggestion(task_description)
...         task_list.insert(tk.END, suggestion)
...         entry.delete(0, tk.END)
... 
... def remove_task():
...     selected_task_index = task_list.curselection()
...     if selected_task_index:
...         task_list.delete(selected_task_index)
... 
... # Create the main window
... root = tk.Tk()
... root.title("To-Do Application")
... 
... # Create and configure widgets
... entry = tk.Entry(root, width=50)
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
task_list = tk.Listbox(root, selectmode=tk.SINGLE, width=60)

# Place widgets in the window
entry.pack()
add_button.pack()
remove_button.pack()
task_list.pack()

# Start the application
root.mainloop()

