def read_json_file(file_path: str) -> list[dict]:
    import json
    with open(file_path, 'r') as file:
        return json.load(file)

def write_json_file(file_path: str, data: list[dict]) -> None:
    import json
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
