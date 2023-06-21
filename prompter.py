import openai
import config
import os

# os.environ['OPENAI_API_KEY'] = 
os.environ['OPENAI_API_KEY'] = config.OPENAI_KEY

class Prompter:
    def __init__(self, gpt_model, temper):
        openai.api_key = os.environ.get  ('OPENAI_API_KEY')
        openai.api_key = config.OPENAI_KEY

        self.gpt_model = gpt_model
        self.temper = temper

    def prompt_model_print(self, messages: list):
        response = openai.ChatCompletion.create(model=self.gpt_model, messages=messages)
        return response["choices"][0]["message"]["content"]
    
    
new_emotions_prompt = [
    {"role" : "system", "content" : "Act as an inventor of new emotions. Consider the following: Mankind as a whole experiences many"  
     "emotions like happiness, sadness, hate, love, Beauty, and much more. Cultures in particular experience emotions or label emotions other"  
     "cultures don't have words for. So for example in Korea exists an emotion labeled as 'Aegyo' which describes a special kind of behavior"  
     "to make people love you. Or 'German Angst' even attributes a certain facet of anxiety to a nationality. Search for feelings that are part"  
     "of human existence. But these feelings should not have been labeled yet. They exist, but they don't have a label."  
     "Define these feelings and invent a label for each of these feeling. Print the label in a bold typo. Also provide me with an example sentence someone could say and"  
     "explain your reasoning for the word (label) you invented and why you think that this could be a human emotion."
     "when experiences these feelings. Also provide an antonym. Focus only on the English Language. Display your output in this HTML format: [<li><strong>{Name of the new emotion}</strong>"  
     "<p>{Description of the new emotion}</p><p>Example sentence: {Example sentence}</p><p>Explanation: {Explanation why this could be an interestingly emotion}</p>]"},
    {"role" : "user", "content" : "Generate 1 new feeling"},
]