from bs4 import BeautifulSoup
from urllib.request import urlopen
from functools import reduce
from assets.constants import OUTPUT_PARSER
import re

from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain


# Def function to create two jokes with gtp given the url of a wikipedia page
def make_jokes(
        url: str,
        openai_api_key: str = "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",
):
    """
    Starting from the URL of an English Wikipedia page,
    it returns two jokes related to the content of the page
    :param url: url of the Wikipedia page
    :return: List of jokes
    """

    # Get HTML
    html = urlopen(url)

    # Get list of all paragraphs
    soup = BeautifulSoup(html.read().decode('utf-8', 'ignore'), features='html.parser')
    raw_lst_p = soup.find_all("p")

    # Clean paragraphs
    lst_p = list(map(lambda x: x.text, raw_lst_p))
    lst_p = list(map(lambda x: x.replace("\n", " "), lst_p))
    text = reduce(lambda x, y: x+y, lst_p)

    # Remove references
    for s in re.findall("\[[0-9]+\]", text):
        text = text.replace(s, "")

    # Be sure we are below the token limit
    length = len(text.split(" "))
    n = 2000
    if length > n:
        text = reduce(lambda x, y: x+" "+y, text.split(" ")[:n])

    # Let's create a prompt template
    summary_template = """
        given the text {information}, I want you to create two short jokes of at most 
        50 words each related to the content.
        \n{format_instructions}
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={"format_instructions": OUTPUT_PARSER.get_format_instructions()}
    )

    # Create llm model
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)

    # Put everything together
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    # Run
    result = chain.run(information=text)

    # Return
    return OUTPUT_PARSER.parse(result)
