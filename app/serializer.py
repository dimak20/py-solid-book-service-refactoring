import json
import xml.etree.ElementTree as XmlET
from abc import ABC, abstractmethod


class Serializer(ABC):
    def __init__(self, entity: str) -> None:
        self.entity = entity

    @abstractmethod
    def convert_data(self, context: dict) -> str:
        """
        This method converts given context and returns string
        of converted(to required type) data.
        Title or article's name should be named like 'heading'.
        Other information should be named like 'text'.
        Args:
            context: dict{'heading', 'text'}

        Returns: str

        """


class JSONSerializer(Serializer):
    def convert_data(self, context: dict) -> str:
        return json.dumps(
            {
                "title": context["heading"],
                "content": context["text"]
            }
        )


class XMLSerializer(Serializer):
    def convert_data(self, context: dict) -> str:
        root = XmlET.Element(self.entity)
        title = XmlET.SubElement(root, "title")
        title.text = context["heading"]
        content = XmlET.SubElement(root, "content")
        content.text = context["text"]
        return XmlET.tostring(root, encoding="unicode")
