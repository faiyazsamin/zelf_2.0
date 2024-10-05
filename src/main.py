import argparse
import logging
from src.platforms.tiktok_scraper import run_tiktok_scraper

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main(platform):
    if platform == "tiktok":
        logger.info("Starting TikTok scraper...")
        run_tiktok_scraper()
        logger.info("TikTok scraping completed.")
    else:
        logger.error(f"Platform '{platform}' is not supported.")
        raise ValueError(f"Unsupported platform: {platform}")

if __name__ == '__main__':
    try:
        # main(args.platform)
        main("tiktok")
    except Exception as e:
        # print stack trace
        logger.exception(e)
        logger.error(f"An error occurred: {e}")

