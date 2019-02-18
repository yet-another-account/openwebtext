import tldextract
import tqdm


# domains that aren't scraper friendly. do not include subdomains!
exclude_domains = set([
    # image & video hosting sites
    'imgur.com',
    'redd.it',
    'gfycat.com',
    'giphy.com',
    'reddituploads.com',
    'redditmedia.com',
    'twimg.com',
    'sli.mg',
    'magaimg.net',
    'flickr.com',
    'imgflip.com',
    'youtube.com',
    'youtu.be',
    'youtubedoubler.com',
    'vimeo.com',
    'twitch.tv',
    'streamable.com',
    'bandcamp.com',
    'soundcloud.com',

    # not scraper friendly

    'reddit.com',
    'gyazo.com',
    'github.com',
    'xkcd.com',
    'twitter.com',
    'spotify.com',
    'itunes.apple.com',
    'facebook.com',
    'gunprime.com',
    'strawpoll.me',
    'voyagefusion.com',
    'rollingstone.com',
    'google.com',
    'timeanddate.com',
    'walmart.com',
    'roanoke.com',
    'spotrac.com'

    # original paper excluded wikipedia
    'wikipedia.org',

    # lots of top posts for this one
    'battleforthenet.com',
])

exclude_extensions = (
    '.png',
    '.jpg',
    '.jpeg',
    '.gif',
    '.gifv',
    '.pdf',
    '.mp4',
    '.mp3',
    '.ogv',
    '.webm',
    '.doc',
    '.docx',
    '.log',
    '.csv',
    '.dat',
    '.iso',
    '.bin',
    '.exe',
    '.apk',
    '.jar',
    '.app',
    '.ppt',
    '.pps',
    '.pptx',
    '.xml',
    '.gz',
    '.xz',
    '.bz2',
    '.tgz',
    '.tar',
    '.zip',
    '.wma',
    '.mov',
    '.wmv',
    '.3gp',
    '.svg',
)


def should_exclude(url):
    ext = tldextract.extract(url)
    domain = '.'.join([x for x in ext if x])
    basedomain = '.'.join(ext[-2:])

    if basedomain in exclude_domains or domain in exclude_domains:
        return True

    if url.split('?')[0].endswith(exclude_extensions):
        return True

    return False


if __name__ == '__main__':
    with open('urls.txt') as urls, open('urls-filtered.txt', 'w') as out:
        for line in tqdm.tqdm(list(urls)):
            line = line.strip()
            if should_exclude(line):
                continue

            out.write(line + '\n')
