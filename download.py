import multiprocessing as mp
import newspaper
import os
import hashlib
import traceback
import tldextract
import tqdm

hash = hashlib.sha256

try:
    os.mkdir('data')
except FileExistsError:
    pass


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
    'nfl.com',

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
)


def dl(url):
    url = url.strip()

    ext = tldextract.extract(url)
    domain = '.'.join([x for x in ext if x])
    if '.'.join(ext[-2:]) in exclude_domains or domain in exclude_domains:
        return

    if url.split('?')[0].endswith(exclude_extensions):
        return

#    print('Downloading', url)
    try:
        article = newspaper.Article(url)
        article.download()
        article.parse()
    except newspaper.article.ArticleException:
#        print('Dead link:', url)
        return
#        traceback.print_exc()

    text = article.text

    fname = 'data/{}-{}.txt'.format(domain, hash(url.encode()).hexdigest())

    if text.strip() == '':
#        print('Empty')
        return

    with open(fname, 'w') as out:
        out.write(text)

if __name__ == '__main__':
    p = mp.Pool(100) # num of download threads
    with open('urls.txt') as fh:
        urls = list(fh)

        list(tqdm.tqdm(p.imap(dl, urls), total=len(urls)))
        print('Done!')
