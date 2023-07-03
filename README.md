# *CuisineWizard*

## LangChain
LangChain is a library that simplifies the interaction with OpenAI's language model, enabling the generation of text using prompts and templates.

requirement:  `Python`

### Dependencies
*The code snippet requires the following dependencies:*

- Open terminal
` pip install langchain openapi streamlit `

## How to run:
`streamlit run main.py`

### API Key
The OpenAI API key is set using the os.environ method and is stored in a separate file called secret_key.py using the openapi_key variable.
- `Visit https://openai.com/`
- Signup and create your secret_key
- copy and input it in the secret_key.py

### Used Classes
- langchain.llms.OpenAI: This is the OpenAI language model class used for text generation.
- langchain.prompts.PromptTemplate: This class helps in creating prompt templates with input variables.
- langchain.chains.LLMChain: This class represents a single language model chain in the sequential chain.
- langchain.chains.SequentialChain: This class represents a sequential chain of multiple language model chains.

### Functions
` get_restaurant_name_and_items(spice) `
- This function retrieves the restaurant name and menu items for a given cuisine (spice). It uses the PromptTemplate and LLMChain classes to generate the desired text using the OpenAI language model.

### Input:
- spice (string): The cuisine or spice for which restaurant details are requested.
### Output:
- response (dictionary): A dictionary containing the restaurant name and menu items.
` how_to(dish) `
- This function generates instructions on how to prepare a given dish. It also uses the PromptTemplate and LLMChain classes to generate the text.

### Input:
- dish (string): The dish for which preparation instructions are requested.
### Output:
- response (dictionary): A dictionary containing the generated text for the preparation instructions.

## Streamlit Application
Streamlit is an open-source Python library that allows you to create interactive web applications and dashboards with ease. It is designed to make it simple for data scientists and developers to build and share data-driven applications.

With Streamlit, you can create interactive web interfaces directly from Python scripts. It provides an intuitive and straightforward API for quickly building and customizing web apps. Streamlit takes care of the underlying web server and frontend components, allowing you to focus on the application's logic and visualizations.

The code includes a Streamlit application that allows users to select a cuisine and retrieve the restaurant name, menu items, and preparation instructions for a selected dish.

- A sidebar selectbox allows the user to pick a cuisine. The selected cuisine is stored in the cuisine variable.
- If a cuisine is selected (if cuisine is not None:), the get_restaurant_name_and_items function is called to retrieve the restaurant name and menu items for the selected cuisine.
- The restaurant name is displayed as a header using st.header.
- The menu items are split, cleaned, and displayed using a for loop and st.write.
- A selectbox is provided to select a dish for which the preparation instructions are requested. The selected dish is stored in the selected variable.
- If a dish is selected (` if prepare: `), the how_to function is called to retrieve the preparation instructions.
- The preparation instructions are displayed using st.write. 
The code includes a Streamlit application that allows users to select a cuisine and retrieve the restaurant name, menu items, and preparation instructions for a selected dish.

# Hope you have fun with this!!
