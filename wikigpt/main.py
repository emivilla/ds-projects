from bs4 import BeautifulSoup
from urllib.request import urlopen
from functools import reduce
from assets.constants import OUTPUT_PARSER
import re

from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain


# Get URL
url = "https://en.wikipedia.org/wiki/Mario_Draghi"

# Get HTML
html = urlopen(url)

# Keep the first 50 paragraphs only
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

# Let's create a prompt template
summary_template = """
    given the text {information}, I want you to create two short jokes of at most 
    50 words each related to the content.
    \n{format_instructions}
"""
summary_prompt_template = PromptTemplate(
    input_variables=["information"],
    template=summary_template,
    partial_variables={"format_instructions": OUTPUT_PARSER.get_format_instructions()},
)

# Create llm model
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

# Put everything together
chain = LLMChain(llm=llm, prompt=summary_prompt_template)

# Run
result = chain.run(information=text)
print(OUTPUT_PARSER.parse(result))
