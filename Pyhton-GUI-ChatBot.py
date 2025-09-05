#install all Dependencies and Extensions
import tkinter as tk  # pip install tkinter
import google.generativeai as genai # pip install google.generativeai
genai.configure(api_key="Your_api_Key") # Just copy and paste your Api Key
model = genai.GenerativeModel("gemini-2.0-flash")

def send():
    user_text = entry.get()
    if not user_text: return
    chat.insert(tk.END, "You: " + user_text + "\n")
    entry.delete(0, tk.END)
    reply = model.generate_content(user_text).text
    chat.insert(tk.END, "Gemini: " + reply + "\n\n")

root = tk.Tk()
root.title("Gemini Chatbot")
chat = tk.Text(root, wrap="word")
chat.pack(padx=10, pady=10, fill="both", expand=True)
entry = tk.Entry(root)
entry.pack(side="left", fill="x", expand=True, padx=5, pady=5)
entry.bind("<Return>", lambda e: send())
send_btn = tk.Button(root, text="Send", command=send)
send_btn.pack(side="right", padx=5, pady=5)
root.mainloop()
#Syntax By Umran666
