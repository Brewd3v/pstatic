

def markdown_to_blocks(markdown):
    split =  markdown.split("\n\n")
    strip_spaces = map(lambda item: item.strip().replace("  ", "") , split)
    return list(strip_spaces)

