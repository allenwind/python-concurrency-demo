import asyncio
import urllib.parse
import sys

async def print_http_headers(url):
    url = urllib.parse.urlsplit(url)
    if url.scheme == 'https':
        connect = asyncio.open_connection(url.hostname, 443, ssl=True)
    else:
        connect = asyncio.open_connection(url.hostname, 80)

    reader, writer = await connect 
    query = ('GET {path} HTTP/1.1\r\n'
             'Host: {hostname}\r\n'
             '\r\n').format(path=url.path or '/', hostname=url.hostname)

    writer.write(query.encode('utf-8'))
    while True:
        line = await reader.readline()
        if not line:
            break
        if line == b'\r\n':
            break
        line = line.decode('utf-8').rstrip()
        if line:
            print('HTTP header> %s' % line)

    writer.close()

url = sys.argv[1]
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(print_http_headers(url))
loop.run_until_complete(task)
loop.close()