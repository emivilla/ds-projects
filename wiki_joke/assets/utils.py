from bs4 import BeautifulSoup
from urllib.request import urlopen
from functools import reduce
import re

from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser


# Def function to create two jokes with gtp given the url of a wikipedia page
def make_jokes(
        url: str,
        openai_api_key: str,
):
    """
    Starting from the URL of an English Wikipedia page,
    it returns two jokes related to the content of the page
    :param url: url of the Wikipedia page
    :param openai_api_key: openai api key neeeded to run GPT-3.5-TURBO
    :return: List of jokes
    """

    # Get HTML
    html = urlopen(url)

    # Get list of all paragraphs
    soup = BeautifulSoup(html.read().decode("utf-8", "ignore"), features="html.parser")
    raw_lst_p = soup.find_all("p")

    # Clean paragraphs
    lst_p = list(map(lambda x: x.text, raw_lst_p))
    lst_p = list(map(lambda x: x.replace("\n", " "), lst_p))
    text = reduce(lambda x, y: x + y, lst_p)

    # Remove references
    for s in re.findall("\[[0-9]+\]", text):
        text = text.replace(s, "")

    # Be sure we are below the token limit
    length = len(text.split(" "))
    n = 2000
    if length > n:
        text = reduce(lambda x, y: x + " " + y, text.split(" ")[:n])

    # Let's define the output parser
    response_schemas = [
        ResponseSchema(name="joke1", description="First joke"),
        ResponseSchema(name="joke2", description="Second joke"),
    ]
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    format_instructions = output_parser.get_format_instructions()

    # Let's create a prompt template
    template = """
        given the text {information}, I want you to create two short jokes of at most 
        50 words each related to the content.

        Format the output as a python dictionary with the following keys:
        joke1
        joke2

        {format_instructions}
    """
    prompt_template = ChatPromptTemplate.from_template(template)

    # Create llm model
    llm = ChatOpenAI(
        temperature=1, model_name="gpt-3.5-turbo", openai_api_key=openai_api_key
    )

    # Run llm model
    messages = prompt_template.format_messages(information=text, format_instructions=format_instructions)
    response = llm(messages)

    # Return
    return output_parser.parse(response.content)