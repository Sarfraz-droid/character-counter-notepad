from playwright.sync_api import sync_playwright
import time

def verify(page):
    # Set up state with goals
    page.goto("http://localhost:8000")

    # Inject state
    page.evaluate("""() => {
        localStorage.setItem('notepadTabs', JSON.stringify([{
            id: '1',
            title: 'Note 1',
            content: 'A'.repeat(1670),
            charGoal: 1500,
            wordGoal: 250
        }]));
        localStorage.setItem('activeTabId', '1');
    }""")

    # Reload to apply state
    page.reload()

    # Wait for counters to update
    time.sleep(1) # simple wait

    # Take screenshot
    page.screenshot(path="verification/before_fix.png")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    # Use a small viewport width
    context = browser.new_context(viewport={"width": 375, "height": 667})
    page = context.new_page()
    try:
        verify(page)
    finally:
        browser.close()
