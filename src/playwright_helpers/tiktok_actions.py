import json

from src.parsers.tiktok_parser import parse_tiktok_api_by_hashtag, parse_tiktok_api_by_keyword
from src.playwright_helpers.browser_setup import get_browser
from src.utils.file_storage import save_json_data
from src.utils.helper_functions import load_cookies, save_cookies


# Intercept network requests and capture the desired API response
def handle_response(response, api_responses, listen_url):
    if listen_url in response.url:  # Adjust based on the actual API endpoint
        if response is not None:
            try:
                json_data = response.json()  # Attempt to parse JSON
                # Check if the JSON data is not empty and not just an empty list
                if json_data and json_data != []:
                    api_responses.append(json_data)  # Append the JSON response
            except ValueError:  # Catch JSON decoding errors
                pass

def scroll_page(page, times=3, wait_time=2000):
    for _ in range(times):
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")  # Scroll to the bottom
        page.wait_for_timeout(wait_time)  # Wait for new content to load

def scrape_tiktok_by_hashtag(hastag_list):
    browser = get_browser()
    page = browser.new_page()
    api_responses = []
    all_responses = []

    try:
        load_cookies(page.context, '/data/cookies/tiktok_cookies.json')
    except FileNotFoundError:
        pass

    for item in hastag_list:
        page.on('response', lambda response: handle_response(response, api_responses, '/api/challenge/item_list/'))
        page.goto('https://www.tiktok.com/tag/'+item)
        # Perform login or scraping actions here
        page.wait_for_load_state('networkidle')
        if page.is_visible('#tiktok-verify-ele'):
            page.wait_for_selector('#tiktok-verify-ele', state='hidden')
            page.wait_for_timeout(10000)
        page.wait_for_timeout(5000)  # Adjust to match real scraping actions
        # Scroll the page to trigger more API calls
        scroll_page(page, times=20)  # Adjust the number of scrolls as needed

        # save_json_data(api_responses, '../data/processed/hashtags/'+item+'data.json')
        parsed_video_data, parsed_author_data = parse_tiktok_api_by_hashtag(api_responses)
        save_json_data(parsed_video_data, '../data/processed/hashtags/#'+item+'_video_data.json')
        save_json_data(parsed_author_data, '../data/processed/hashtags/#'+item+'_author_data.json')
        all_responses.append(api_responses)

    cookies = page.context.cookies()
    save_cookies(cookies, '../data/cookies/tiktok_cookies.json')
    browser.close()
    return all_responses


def scrape_tiktok_by_keyword(keyword_list):
    browser = get_browser()
    page = browser.new_page()
    api_responses = []
    all_responses = []

    # try:
    #     load_cookies(page.context, '/data/cookies/tiktok_cookies.json')
    # except FileNotFoundError:
    #     pass

    for item in keyword_list:
        page.on('response', lambda response: handle_response(response, api_responses, '/api/search/general/full/'))
        url_path = '/search?q='+item.replace(' ','%20')+'&t=1728108845846'
        page.goto('https://www.tiktok.com'+url_path)
        # Perform login or scraping actions here
        # page.wait_for_load_state('networkidle')
        if page.is_visible('#tiktok-verify-ele'):
            page.wait_for_selector('#tiktok-verify-ele', state='hidden')
        page.wait_for_timeout(5000)  # Adjust to match real scraping actions
        # Scroll the page to trigger more API calls
        scroll_page(page, times=1)  # Adjust the number of scrolls as needed

        # save_json_data(api_responses, '../data/processed/hashtags/'+item+'data.json')
        parsed_video_data, parsed_author_data = parse_tiktok_api_by_keyword(api_responses)
        save_json_data(parsed_video_data, '../data/processed/keywords/'+item+'_video_data.json')
        save_json_data(parsed_author_data, '../data/processed/keywords/'+item+'_author_data.json')
        all_responses.append(api_responses)

    cookies = page.context.cookies()
    save_cookies(cookies, '../data/cookies/tiktok_cookies.json')
    browser.close()
    return all_responses


def login_and_save_cookie():
    browser = get_browser(headless=False)
    page = browser.new_page()

    # Navigate to the login page
    page.goto('https://www.tiktok.com/login/phone-or-email/email')


    # Fill in the login form
    page.fill('input[name="username"]', 'void_samin')  # Username field
    page.fill('input[placeholder="Password"]', 'Rasengan123!@#')  # Password field

    # Submit the form
    page.click('button[data-e2e="login-button"]')  # Submit button

    # Wait for navigation after login
    page.wait_for_load_state('networkidle')
    page.wait_for_timeout(10000)

    # Get cookies
    cookies = page.context.cookies()

    save_cookies(cookies, '../data/cookies/tiktok_cookies.json')

    # Get page content after login
    page_content = page.content()

    browser.close()

    return page_content

