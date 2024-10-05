from playwright.sync_api import sync_playwright

def get_browser(headless=True):
    playwright = sync_playwright().start()
    # browser = playwright.chromium.launch(headless=False)
    browser = playwright.firefox.launch(headless=False)
    return browser

