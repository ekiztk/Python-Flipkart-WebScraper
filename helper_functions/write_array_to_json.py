import json 

def write_array_to_json(object, filePath):
    f = open(filePath, "a")
    f.write(json.dumps(object,ensure_ascii=False, indent=4,separators=(',', ':')))
    f.close()