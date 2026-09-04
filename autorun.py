"""Run the page_info scraping from terminal arguments"""

import argparse
from datetime import datetime
from csv import DictWriter
from facebook_page_scraper import FacebookPageScraper

def _main():
    parser = argparse.ArgumentParser(prog="Facebook page information scrapper")
    parser.add_argument(
        "accounts", type=str, nargs="+", help="Facebook usernames to be scrapped"
    )

    parser.add_argument(
        "--directory",
        type=str,
        nargs="?",
        default="",
        help="Output directory (will be created if it doesn't exist)",
    )

    args = parser.parse_args()
    path = f"facebook_pages_{datetime.now().replace(microsecond=0).isoformat()}.csv"

    if args.directory:
        path = f"{args.directory}/{path}"

    fields = [
        "page_name",
        "page_url",
        "profile_pic",
        "cover_photo",
        "page_likes",
        "page_followers",
        "page_id",
        "is_business_page",
        "page_likes_count",
        "page_talking_count",
        "page_were_here_count",
        "page_category",
        "page_address",
        "page_phone",
        "page_email",
        "page_website",
        "page_business_hours",
        "page_business_price",
        "page_rating",
        "page_services",
        "page_social_accounts",
    ]
    with open(path, "w", encoding="utf-8") as f:
        writer = DictWriter(f, fields)
        writer.writeheader()

        for acc in args.accounts:
            page_info = FacebookPageScraper.PageInfo(f"https://www.facebook.com/{acc}")
            writer.writerow(page_info)

if __name__ == "__main__":
    _main()