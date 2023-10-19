"""Functions to manipulate text in specifically stupid ways."""


def get_sarcastic_text(text: str) -> str:
    """Returns the sarcastic version of a string."""

    if not isinstance(text, str):
        raise TypeError("Argument must be a string.")

    return "".join([c.lower()
                    if i % 2 == 0
                    else c.upper()
                    for i, c in enumerate(text)])


if __name__ == "__main__":
    print(get_sarcastic_text("Look at me; I'm reading the example code!"))
