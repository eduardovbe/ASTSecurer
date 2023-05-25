import solidity_parser
import json


def open_file_and_save(SOLIDITY_FILE_PATH):
    with open(SOLIDITY_FILE_PATH, "r") as file:
        solidity_code = file.read()
    ast = solidity_parser.parse(solidity_code)
    ast_json = json.dumps(ast, indent=4)
    file.close()
    with open('ast.json', 'w') as f:
        f.write(ast_json)
        f.close()
    with open('ast.json', 'r') as f:
        data = f.read()
    return json.loads(data)

