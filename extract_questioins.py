# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 13:48:22 2023

@author: jaswa
"""

import re
import pandas as pd

data = []
for i in range(50,790):
    with open(f"stories/story_{i}.txt","r") as f:
        text = f.read()
        
    # Split the text into sections (story, questions, answers, reasoning)
    sections = re.split("Story.?\n{1,2}|Question.*[0-9]|Answer.?:|Answer.? *\n|Reasoning:|Reasoning",re.sub("\*","",text))
    story = sections[1].strip()
    
    # Extract and clean questions, answers, and reasoning
    questions = []
    id = 1
    print(i)
    for j in range(2, len(sections), 3):
        record = {}
        record["story"] = story
        record["story_id"] = i
        question = sections[j].strip()
        record["question"] = question
        answer = sections[j + 1].strip()
        record["answer"] = answer
        reasoning = sections[j + 2].strip()
        record["reason"] = reasoning
        id+=1
        record["question_id"] = id
        data.append(record)
        

    
    
    
    
    

    



