from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "25%",
    "background-color": "#ffffff",
}

HOME_CONTENT_STYLE = {
    "marginTop": "10%",
    "marginLeft": "40%",
    "marginRight": "10%",
}

FOOTER_STYLE = {
    "position": "absolute",
    "left": "2%",
    "bottom": 0,
    "width": "100%",
    "text-align": "left",
}


class OutputParser(BaseModel):
    jokes: List[str] = Field(description="Jokes about the content")

    def to_dict(self):
        return {"jokes": self.jokes}


OUTPUT_PARSER = PydanticOutputParser(pydantic_object=OutputParser)
