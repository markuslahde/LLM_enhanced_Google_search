#!/usr/bin/env python3

import ast
import ollama
from googlesearch import search
import ollama # models in this machine: tinyllama / stablelm2 / phi3

query = input('Enter search query: ')

response = ollama.chat(model='phi3', messages=[
  {
    'role': 'user',
    'content': f'Return your answer in a python list format. Your answer should only contain the list. For items in the list, make alternative google search sentences to this query: {query}.',
  },
])

llm_response = response['message']['content']
llm_response_list = ast.literal_eval(llm_response)

print('\nSearch results:')
for item in search(query, advanced=True, num_results=1):
  print(item.title)
  print(item.url)
  print(item.description)
  print('\n')

print('\nAlternative search results:')
for response in llm_response_list:
    for item in search(response, advanced=True, num_results=1):
      print(item.title)
      print(item.url)
      print(item.description)
      print('\n')