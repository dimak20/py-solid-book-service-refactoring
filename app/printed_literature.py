from abc import ABC, abstractmethod


class PrintedLiterature(ABC):
    @abstractmethod
    def get_context(self, *args) -> dict:
        """
        Takes range of arguments and returns dict of
        universalized data with 'heading' and 'text' keys
        Args:
            *args:

        Returns: dict{'heading', 'text'}

        """


class Book(PrintedLiterature):
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def get_context(self, *args) -> dict:
        return {"heading": self.title, "text": self.content}
