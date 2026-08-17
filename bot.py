import os
import time
from playwright.sync_api import sync_playwright

USERNAME = os.environ.get("PELLA_USERNAME")
PASSWORD = os.environ.get("PELLA_PASSWORD")
PANEL_URL = "https://www.pella.app/server/e6cf31aac4184a6487363aa3fc790e27"  # ئادڕەسی ڕاستەوخۆی پانێڵەکەت لێرە بنووسە


def restart_pella_server():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        print("چوونە سەر ماڵپەڕ...")
        page.goto(PANEL_URL)
        page.wait_for_timeout(3000)

        # ئەگەر لاپەڕەی Login هات، زانیارییەکان دەخاتە ناوەوە
        if page.locator("input[name='username']").is_visible():
            print("تۆمارکردنی چوونەژوورەوە...")
            page.fill("input[name='username']", USERNAME)
            page.fill("input[name='password']", PASSWORD)
            page.click("button[type='submit']")
            page.wait_for_timeout(4000)

        # کلیک کردن لەسەر دوگمەی RESTART
        print("گەڕان بەدوای دوگمەی RESTART...")
        restart_button = page.locator("button:has-text('RESTART')")
        if restart_button.is_visible():
            restart_button.click()
            print("دوگمەی RESTART بە سەرکەوتوویی داگیرا!")
            page.wait_for_timeout(3000)
        else:
            print("دوگمەی RESTART نەدۆزرایەوە!")

        browser.close()


if __name__ == "__main__":
    restart_pella_server()
