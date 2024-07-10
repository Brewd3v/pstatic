class TextNode:
    def __init__(self, text, text_type, url = None):
        self.__text = text
        self.__text_type = text_type
        self.__url = url

    def __eq__(self, target):
        if(
            target.__text == self.__text
            and target.__text_type == self.__text_type
            and self.__url == target.__url
        ):
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.__text}, {self.__text_type}, {self.__url})"

