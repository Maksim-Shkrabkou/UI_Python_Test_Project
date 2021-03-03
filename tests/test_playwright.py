from playwright.sync_api import sync_playwright


def test_playwright():
    with sync_playwright() as p:
        for browser_type in [p.chromium]:
            browser = browser_type.launch(headless=False)
            page = browser.new_page()
            page.goto('http://whatsmyuseragent.org/')
            page.screenshot(path=f'example-{browser_type.name}.png')
            browser.close()
