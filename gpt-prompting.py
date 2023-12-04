# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 11:11:45 2023

@author: jaswa
"""

import openai
import random


apikey = "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"

events_list = [
    "Historical Events Timeline Creation",
    "Geographical and Geopolitical Data Generation",
    "Scientific Discoveries and Breakthroughs",
    "Historical Texts Synthesis",
    "Weather and Climate Data Generation",
    "Political Speech and Diplomacy Synthesis",
    "Economic and Financial Market Data",
    "Space Exploration and Astronomy Events",
    "Environmental and Natural Disaster Records",
    "Cultural and Artistic Movements Synthesis",
    "Medical Case Histories",
    "Technological Advancements and Inventions",
    "Literary and Artistic Movements Synthesis",
    "Legal Case Summaries",
    "Archaeological Discoveries and Excavations",
    "Astronomical Events and Celestial Phenomena",
    "Environmental Conservation Efforts",
    "Sports Statistics and Records",
    "Educational Milestones and Reforms",
    "Psychological Case Studies",
    "Great Inventions and Their Impact",
    "Humanitarian and Aid Efforts",
    "Civil Engineering Milestones",
    "Epidemic and Pandemic Outbreaks",
    "Historical Fashion Trends",
    "Space-Time Anomalies",
    "Architectural Styles and Landmarks",
    "Historical Economic Crises",
    "Historical Innovations in Transportation",
    "Environmental Restoration Projects"
]


openai.api_key = apikey

prompt = """
Generate a 5-sentence long story following the given event type and conditions. 

Event type: {event}

Conditions 1: The story involves many events and actions related to {event}. 
Condition 2: These events and actions will have temporal and spatial changes. 
Condition 3: The temporal and spatial changes need to be logical and consistent, such that it is possible to ask reasoning questions based on these changes. 

Then, generate 5 questions with 4 possible answer choices. The conditions mentioned below must be followed while generating questions and answer choices.  

Condition 1: The questions should be composed of temporal, spatial, or both temporal and spatial information from the context. Anything explicitly mentioned in the context should not be considered for question generation. 
Condition 2: The question needs to be phrased in such a way that reasoning is required to find the correct answer, but no additional information is needed to answer the question.

Generate the answers and the reason for the answer after the question.  Please follow this template for text generation. 

**Story**

**Question: 1**
Answer choices
Answer
Reasoning

**Question: 2**
Answer choices
Answer
Reasoning

**Question: 3**
Answer choices
Answer
Reasoning

**Question: 4**
Answer choices
Answer
Reasoning

**Question: 5**
Answer choices
Answer
Reasoning

### End of text generation ###

"""

for i in range(790,1000):
    event_choice = random.choice(events_list)
    event_prompt = prompt.format(event = event_choice)
    res = openai.ChatCompletion.create(
        model = "gpt-4",
        messages=[{
            "role":"user",
            "content":event_prompt}])
    story = res["choices"][0]["message"]["content"]
    with open("stories/story_"+str(i)+".txt","w") as f:
        f.write(story)
    print(i)
    
    

#res = openai.ChatCompletion.create(
 #   model = "gpt-4",
  #  messages=[{
   #     "role":"user",
    #    "content":prompt}])