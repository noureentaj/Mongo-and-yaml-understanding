import json

# def codingthis(code_fname, document):
#     pass

def coding_this(code_fname, document):
    with open(code_fname) as file:
        codes = json.load(file)
    for each_specimen in document:
        contact = str(document.get(each_specimen).get("number"))
        country = document.get(each_specimen).get("country")
        code = str(codes[country])
        document[each_specimen]["number"] = code + contact
    return document

