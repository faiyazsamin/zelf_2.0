import json


def get_value(data_dict, *keys):
    """Helper function to safely get a value from a nested dictionary."""
    for key in keys:
        try:
            data_dict = data_dict[key]
        except (KeyError, TypeError):
            return None
    return data_dict


def load_cookies(context, cookies_file):
    with open(cookies_file, 'r') as f:
        cookies = json.load(f)
        context.add_cookies(cookies)


def save_cookies(cookies, cookies_file):
    # Save cookies to a file
    with open(cookies_file, 'w') as f:
        json.dump(cookies, f)