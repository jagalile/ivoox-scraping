import argparse

from src.download_podcast import DownloadPodcast

parser = argparse.ArgumentParser(description='Download podcast from Ivoox.')
parser.add_argument(
    '-p',
    metavar='Podcast name',
    type=str,
    nargs='+',
    help='alias for podcast name',
    required=True,
)
parser.add_argument(
    '-c',
    metavar='Chapter name',
    type=str,
    nargs='+',
    help='full or partial name of podcast chapter, should be in quotation marks',
)
parser.add_argument(
    '-n',
    metavar='Number of chapters',
    type=int,
    nargs='+',
    help='full or partial name of podcast chapter, should be in quotation marks',
)

args = parser.parse_args()


def main(podcast_name, chapter, chapters):
    last = None
    podcast_name = podcast_name[0] if podcast_name else None
    chapter = chapter[0] if chapter else None
    chapters = chapters[0] if chapters else None
    if not chapter and not chapters:
        last = True
    dp = DownloadPodcast(podcast_name, chapter, chapters, last)
    dp.download_podcast()


main(args.p, args.c, args.n)
