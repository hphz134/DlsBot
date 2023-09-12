# copy from https://github.com/HibiKier/zhenxun_bot (utils/browser.py)

import asyncio
from typing import Optional
from playwright.async_api import Browser, async_playwright

_browser: Optional[Browser] = None


async def init(**kwargs) -> Optional[Browser]:
    global _browser
    browser = await async_playwright().start()
    try:
        _browser = await browser.chromium.launch(**kwargs)
        return _browser
    except Exception as e:
        # logger.warning(f"启动chromium发生错误 {type(e)}：{e}")
        await asyncio.get_event_loop().run_in_executor(None, install)
        _browser = await browser.chromium.launch(**kwargs)
    return None


async def get_browser(**kwargs) -> Browser:
    return _browser or await init(**kwargs)


def install():
    """自动安装、更新 Chromium"""
    print("正在检查 Chromium 更新")
    import sys
    from playwright.__main__ import main
    
    sys.argv = ["", "install", "chromium"]
    try:
        main()
    except SystemExit:
        print("安装结束")
