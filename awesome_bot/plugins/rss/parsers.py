import feedparser as fp

url_dic = {}


async def rssParsers(url):
    if url not in url_dic:
        url_dic[url] = None
    dd = fp.parse(url, etag=url_dic[url])
    msg = ""
    if not dd.status == 304:
        msg = dd.feed
    else:
        msg = "暂时还没有更新哦~"
    url_dic[url] = dd.etag
    return dd.status, msg
