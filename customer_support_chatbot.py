import spacy
import tkinter as tk
from tkinter import Scrollbar, Text

# Load the English language model
nlp = spacy.load("en_core_web_sm")

responses = {
    "hello": "Hello! How can I assist you today?",
    "problem": "I'm sorry to hear that you're experiencing a problem. Please provide more details so I can help you better.",
    "order_status": "To check your order status, please provide your order number.",
    "thank_you": "You're welcome! If you have any more questions, feel free to ask.",
    "default": "Thank you for contacting us. A support agent will assist you shortly.",
}


def chatbot_response(user_input):
    doc = nlp(user_input.lower())
    
    for token in doc:
        if "hello" in token.text:
            return responses["hello"]
        elif "problem" in token.text:
            return responses["problem"]
        elif "order" in token.text and "status" in doc.text:
            return responses["order_status"]
        elif "thank" in token.text:
            return responses["thank_you"]
    
    return responses["default"]

def send_message(event=None):
    user_input = user_input_text.get("1.0", "end-1c")
    user_input_text.delete("1.0", "end")
    
    response = chatbot_response(user_input)
    chat_display_text.config(state="normal")
    chat_display_text.insert("end", "You: " + user_input + "\n", "user_message")
    chat_display_text.insert("end", "Chatbot: " + response + "\n", "bot_message")
    chat_display_text.config(state="disabled")
    chat_display_text.see("end")

# Create a tkinter window
root = tk.Tk()
root.title("Customer Support Chatbot")

user_input_text = Text(root, height=3, width=40)
user_input_text.bind("<Return>", send_message)
user_input_text.pack(pady=10)

chat_display_text = Text(root, height=15, width=40, state="disabled")
chat_display_text.tag_configure("user_message", foreground="blue", background="yellow")
chat_display_text.tag_configure("bot_message", foreground="green", background="black")
chat_display_text.pack()

scrollbar = Scrollbar(root, command=chat_display_text.yview)
scrollbar.pack(side="right", fill="y")
chat_display_text.config(yscrollcommand=scrollbar.set)

send_button = tk.Button(root, text="Send", command=send_message, bg="green", fg="white")
send_button.pack()

root.mainloop()
