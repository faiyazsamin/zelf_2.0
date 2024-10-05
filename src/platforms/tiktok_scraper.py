from src.playwright_helpers.tiktok_actions import scrape_tiktok_by_hashtag, login_and_save_cookie, \
    scrape_tiktok_by_keyword
from src.parsers.tiktok_parser import parse_tiktok_api_by_keyword, parse_tiktok_api_by_hashtag
from src.utils.file_storage import save_raw_data, save_json_data, clear_file_contents


def run_tiktok_scraper():
    hashtag_list = ["traveltok", "wanderlust", "backpackingadventures", "luxurytravel", "hiddengems", "solotravel", "roadtripvibes", "travelhacks", "foodietravel", "sustainabletravel"]
    keyword_list = ["beautiful destinations", "places to visit", "places to travel", "places that don't feel real", "travel hacks"]
    # scrape_tiktok_by_hashtag(hashtag_list)
    scrape_tiktok_by_keyword(keyword_list)