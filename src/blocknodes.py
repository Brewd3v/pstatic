def markdown_to_blocks(markdown):
    split =  markdown.split("\n\n")
    strip_spaces = map(lambda item: item.strip().replace("  ", "") , split)
    filter_empty = filter(lambda item: item != '', strip_spaces)
    return list(filter_empty)

