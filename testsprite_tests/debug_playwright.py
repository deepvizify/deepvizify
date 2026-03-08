import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        url = "http://127.0.0.1:5173/login"
        print(f"Navigating to {url}...")
        try:
            await page.goto(url, wait_until="networkidle", timeout=30000)
            print(f"Current URL: {page.url}")
            
            # Check for ts-email
            input_exists = await page.locator("#ts-email").count() > 0
            print(f"Does #ts-email exist? {input_exists}")
            
            # Take screenshot
            screenshot_path = r"c:\Users\Vicky\Desktop\data-canvas-x-main me spactual 7868\data-canvas-x-main me spactual 7868\data-canvas-x-main\testsprite_tests\tmp\absolute_debug.png"
            await page.screenshot(path=screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")
            
            # Dump source if missing
            if not input_exists:
                content = await page.content()
                with open(r"c:\Users\Vicky\Desktop\data-canvas-x-main me spactual 7868\data-canvas-x-main me spactual 7868\data-canvas-x-main\testsprite_tests\tmp\page_source.html", "w", encoding="utf-8") as f:
                    f.write(content)
                print("Page source dumped to page_source.html")
                
        except Exception as e:
            print(f"Error: {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
