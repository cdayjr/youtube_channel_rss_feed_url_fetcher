# YouTube Channel RSS Feed URL Fetcher

A simple script to fetch the RSS feed URL from a YouTube channel URL.

## Usage

```sh
pdm run fetch <youtube_channel_url>
```

Which should return the RSS feed URL or an error if there was a problem.

Example:

```sh
pdm run fetch https://www.youtube.com/@AEW
```

Which results in:

```
https://www.youtube.com/feeds/videos.xml?channel_id=UCFN4JkGP_bVhAdBsoV9xftA
```
