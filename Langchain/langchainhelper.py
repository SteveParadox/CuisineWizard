from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

import os
from secret_key import openapi_key

os.environ["OPENAI_API_KEY"] = openapi_key

llm = OpenAI(temperature = 0.7)

def get_restaurant_name_and_items(spice):

    prompt_template = PromptTemplate(
    input_variables = ['spice'],
    template = "suggest a tasty {spice} name"
    )
    name_chain = LLMChain(llm = llm, prompt= prompt_template, output_key = "restaurant_name")

    prompt_template = PromptTemplate(
        input_variables = ['restaurant_name'],
        template = "suggest some menu items for {restaurant_name}"
    )
    food_chain = LLMChain(llm = llm, prompt= prompt_template, output_key = "menu_items")

    chain = SequentialChain(
    chains= [name_chain, food_chain],
    input_variables = ['spice'],
    output_variables = ["restaurant_name", "menu_items"]    
    )
    response = chain({'spice': spice})
    return response

def how_to(dish):
    prompt_template = PromptTemplate(
        input_variables = ['dish'],
        template = "How to prepare {dish}"
    )
    how_to_chain = LLMChain(llm = llm, prompt= prompt_template)

    chain = SequentialChain(
    chains= [how_to_chain],
    input_variables = ['dish'],
    )
    response = chain({'dish': dish})

    return response

