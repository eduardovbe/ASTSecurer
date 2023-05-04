import re

def find_old_version(node):
    text_version = node["children"][0]["value"]
    version = re.findall(r"\d+\.\d+\.\d+", text_version)
    outdate = False
    if int(version[-1][2]) < 8:
        outdate = True

    return outdate, version[-1]