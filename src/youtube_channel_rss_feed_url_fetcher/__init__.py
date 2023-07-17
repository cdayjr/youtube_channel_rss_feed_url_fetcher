from re import search
from requests import get
from sys import argv, stderr

if __name__ == "__main__":
    channel_url = argv[1]
    response = get(channel_url)
    response.raise_for_status()
    matches = search(
        "{\"key\":\"browse_id\",\"value\":\"(?P<channel_id>[^\"]+)\"}",
        response.text
    )
    channel_id = matches.group("channel_id")
    if not channel_id:
        print(f"Could not find channel ID for {channel_url}", stderr)
        exit(1)

    print(f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}")
