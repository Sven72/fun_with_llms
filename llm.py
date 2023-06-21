import openai
import os
import config
import gradio as gr
import json
import sqlite3
import requests

# connection = sqlite3.connect('database.db')

# os.environ['OPENAI_API_KEY'] = 

os.environ['OPENAI_API_KEY'] = config.OPENAI_KEY

class Prompter:
    def __init__(self, gpt_model, temper):
        openai.api_key = os.environ.get("OPENAI_API_KEY")

        self.gpt_model = gpt_model
        self.temper = temper

    def prompt_model_print(self, messages: list):
        response = openai.ChatCompletion.create(
            model=self.gpt_model, messages=messages)
        return response["choices"][0]["message"]["content"]

#System-Prompt JSON Format
new_emotions_prompt = [
    {"role": "system", "content": "Act as an inventor of new emotions. Consider the following: Mankind as a whole experiences many"
     "emotions like happiness, sadness, hate, love, Beauty, and much more. Cultures in particular experience emotions or label emotions other"
     "cultures don't have words for. So for example in Korea exists an emotion labeled as 'Aegyo' which describes a special kind of behavior"
     "to make people love you. Or 'German Angst' even attributes a certain facet of anxiety to a nationality. Search for feelings that are part"
     "of human existence. But these feelings should not have been labeled yet. They exist, but they don't have a label."
     "Define these feelings and invent a label for each of these feelings. Also provide an example sentence and"
     "explain the etymological background for the label of the emotion  you invented. Provide your answer in JSON format with the following keys: label, explanation, etymology, example. It is important that your output is in JSON format. So format your output like {\"key\": \"value\"}"},{"role": "user", "content": "Generate 1 new feeling"},
]

def emo(name, temper):
    prompters = Prompter("gpt-3.5-turbo", temper)
    return prompters.prompt_model_print(new_emotions_prompt)
    
def test(output):
    data = json.loads(output)
    label = data['label']
    explanation = data['explanation']
    etymology = data['etymology']
    example = data['example']
    # created = data['created']
    
    connection = sqlite3.connect('database.db')
    
    
    cur = connection.cursor()

    cur.execute("INSERT INTO emotions (label, explanation, etymology, example) VALUES (?, ?, ?, ?)",(label, explanation, etymology, example))

    connection.commit()
    connection.close()
    requests.get('http://localhost:5000/update')
    print(data)

 
with gr.Blocks() as demo:
  with gr.Row():
    slider = gr.Slider(0,
                       1,
                       label='Temperature',
                       #default=0,
                       info="Chose a float value between 0 and 1 to set the 'creativity'"
                       "of the machine. Keep in mind, that a value of 1 (highest) may create incosistent but also interesting results.")
    emo_out = gr.Textbox(value='text', label="Output", lines=3)
    with gr.Row():
        btn = gr.Button(value="Generate Emotion")
        btn.click(emo, inputs=slider, outputs=emo_out)
    with gr.Row():
        btn_save = gr.Button(value="Save Emotion")
        btn_save.click(test, inputs=[emo_out], outputs=emo_out)
      


if __name__ == "__main__":
  demo.launch(share = True)
