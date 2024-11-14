import url_finder


async def link_check(link: str) -> bool:
    if 'https://vk.com' not in link:
        return False
    # MOC


def extract_urls(text):
    urls = list(url_finder.get_urls(text))
    return urls
