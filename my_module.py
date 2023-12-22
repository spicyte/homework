def count_words(file_obj):

    content = file_obj.read()
    words = content.split()
    return len(words)