import argparse

from src.download_podcast import DownloadPodcast

parser = argparse.ArgumentParser(description='Download podcast from Ivoox.')
parser.add_argument(
    '-p',
    metavar='Podcast name',
    type=str,
    nargs='+',
    help='Alias for podcast name',
    required=True,
)
parser.add_argument(
    '-c',
    metavar='Episode name',
    type=str,
    nargs='+',
    help='Full or partial name of podcast episode, should be in quotation marks',
)
parser.add_argument(
    '-latest',
    action='store_true',
    help='Downloads the latest episode from provided podcast',
)
# parser.add_argument(
#     '-all',
#     action='store_true',
#     help='Downloads all episodes from provided podcast',
# )

args = parser.parse_args()


def main(podcast_name, episode_name, latest_episode):
    podcast_name = podcast_name[0] if podcast_name else None
    episode_name = episode_name[0] if episode_name else None
    dp = DownloadPodcast(podcast_name, episode_name, latest_episode)
    dp.download_episode()


main(args.p, args.c, args.latest)
