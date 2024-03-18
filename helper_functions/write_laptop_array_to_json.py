import json 

def write_laptop_array_to_json(object, filePath):
    f = open(filePath, "a",encoding="utf-8")
    f.write(json.dumps(object,ensure_ascii=False, indent=4,separators=(',', ':')))
    f.close()