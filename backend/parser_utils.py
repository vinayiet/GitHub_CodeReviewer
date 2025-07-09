import ast

def extract_functions(code: str) -> dict:
    """
    Extract all function definitions from the code.
    Returns a dictionary of {function_name: function_code}.
    """
    try:
        tree = ast.parse(code)
        functions = {}

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                name = node.name
                start_line = node.lineno - 1  # zero-indexed
                end_line = node.body[-1].lineno  # approximate end

                lines = code.splitlines()[start_line:end_line]
                functions[name] = "\n".join(lines)

        return functions
    except Exception as e:
        return {"error": str(e)}
