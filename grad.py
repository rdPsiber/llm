import gradio as gr
# import modules.shared as shared
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re

SEARCH_ACCESS = True

def ui():
    global SEARCH_ACCESS
    SEARCH_ACCESS = gr.components.Checkbox(label="Enable Google Search", default=False)
    return [SEARCH_ACCESS]

def input_modifier(user_input):
    global SEARCH_ACCESS
    if SEARCH_ACCESS:
        if user_input.lower().startswith("search:"):
            query = user_input[len("search:"):].strip()
            search_results = search(query, num_results=3)
            search_data = []

            for result in search_results:
                try:
                    response = requests.get(result)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    text = soup.get_text(strip=True)
                    text = re.sub(r'\s+', ' ', text)
                    search_data.append(text)
                except Exception as e:
                    pass

            compiled_data = "\n".join(search_data)
            return f"{user_input}\n\n{compiled_data}"
    return user_input


demo = gr.Interface(
    fn = input_modifier,
    inputs = ['text'],
    outputs = gr.components.Textbox(),
    title = 'Google Search Extension'
)

demo.launch(share=True)
def output_modifier(output):
    return output

def bot_prefix_modifier(prefix):
    return prefix