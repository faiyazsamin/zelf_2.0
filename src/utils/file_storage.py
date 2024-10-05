import json

def save_json_data(data, file_path):
    with open(file_path, 'a', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def save_raw_data(data, file_path):
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(data)
        print(f"Data saved to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def clear_file_contents(file_path):
    """Clear the contents of the specified file."""
    with open(file_path, 'w') as file:
        file.truncate()  # Truncating the file, but opening in 'w' already clears it.

