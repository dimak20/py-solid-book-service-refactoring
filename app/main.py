from app.command_factories import (
    DisplayCommands,
    PrintCommands,
    SerializerCommands
)
from app.printed_literature import Book, PrintedLiterature

PRINTED_LITERATURE = {
    "book": Book
}


def main(
        printed_literature: PrintedLiterature,
        commands: list[tuple[str, str]]
) -> None | str:
    if isinstance(printed_literature, PrintedLiterature):
        if isinstance(printed_literature, Book):
            return process_book_commands(printed_literature, commands)
    print(f"There is no matched printed literature {printed_literature}")


def process_book_commands(
        book: Book,
        commands: list[tuple[str, str]],
) -> None | str:
    entity = "book"
    context = book.get_context()
    for cmd, method_type in commands:
        if cmd == "display":
            DisplayCommands().create_command_class(
                method_type,
                entity
            ).display(
                context["text"]
            )
        elif cmd == "print":
            PrintCommands().create_command_class(
                method_type,
                entity
            ).print_entity(
                context
            )
        elif cmd == "serialize":
            return SerializerCommands().create_command_class(
                method_type,
                entity
            ).convert_data(
                context
            )


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
