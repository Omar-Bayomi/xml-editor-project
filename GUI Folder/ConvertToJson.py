JsonData = ""


def ConvertToJson(Root):
    global JsonData
    JsonData = "{"
    ConvertToJsonRecursive(Root)
    JsonData += "}"
    return JsonData


def ConvertToJsonRecursive(Root):
    global JsonData
    JsonData += '\n'

    if Root.TagData is None:
        for _ in range(Root.Depth):
            JsonData += '\t'
        JsonData += '"' + Root.TagName + '"'
        JsonData += ":\n"
        for _ in range(Root.Depth * 2):
            JsonData += '\t'
        JsonData += "{"
        lenght = len(Root.Children)
        index = 0
        for child in Root.Children:
            ConvertToJsonRecursive(child)
            index += 1
            if index != lenght:
                JsonData += ","
        JsonData += "\n"
        for _ in range(Root.Depth * 2):
            JsonData += '\t'
        JsonData += "}\n"

    else:
        for _ in range(Root.Depth * 2):
            JsonData += '\t'
        JsonData += '"'
        JsonData += Root.TagName + '":'
        JsonData += '"'
        JsonData += Root.TagData
        JsonData += '"'

    return
