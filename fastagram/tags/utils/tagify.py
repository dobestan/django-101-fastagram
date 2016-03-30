def get_tag_list(content):
    tag_list = [
        word.replace("#", "")
        for word
        in content.split(" ")
        if word.startswith("#")
    ]

    return tag_list
