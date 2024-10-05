from src.playwright_helpers.tiktok_actions import scrape_tiktok_by_hashtag, login_and_save_cookie, \
    scrape_tiktok_by_keyword
from src.parsers.tiktok_parser import parse_tiktok_api_by_keyword, parse_tiktok_api_by_hashtag
from src.utils.file_storage import save_raw_data, save_json_data, clear_file_contents


def run_tiktok_scraper():
    hashtag_list = ["traveltok", "wanderlust", "backpackingadventures", "luxurytravel", "hiddengems", "solotravel", "roadtripvibes", "travelhacks", "foodietravel", "sustainabletravel"]
    keyword_list = ["beautiful destinations", "places to visit", "places to travel", "places that don't feel real", "travel hacks"]
    # keyword_list = ["beautiful destinations"]
    api_response = scrape_tiktok_by_hashtag(hashtag_list)
    # api_response = scrape_tiktok_by_keyword(keyword_list)

    clear_file_contents('../data/raw/tiktok_data.txt')
    clear_file_contents('../data/processed/tiktok_api_response.json')
    clear_file_contents('../data/processed/tiktok_data.json')
    clear_file_contents('../data/processed/tiktok_video_data.json')
    clear_file_contents('../data/processed/tiktok_author_data.json')


    # save_raw_data(raw_data, '../data/raw/tiktok_data.txt')
    save_json_data(api_response, '../data/processed/tiktok_api_response.json')
    # parsed_video_data, parsed_author_data = parse_tiktok_api(api_response)
    # save_json_data(parsed_video_data, '../data/processed/tiktok_video_data.json')
    # save_json_data(parsed_author_data, '../data/processed/tiktok_author_data.json')
    # login_and_save_cookie()
