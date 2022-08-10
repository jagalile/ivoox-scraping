import argparse

from src.download_podcast import DownloadPodcast
from src.driver import Driver


parser = argparse.ArgumentParser(description='Download podcast from Ivoox.')
parser.add_argument(
        'podcast_name', 
        metavar='podcast_name', 
        type=str, 
        nargs='+', 
        help='alias for podcast name'
    )
parser.add_argument(
        'chapter_name', 
        metavar='chapter_name', 
        type=str, 
        nargs='+', 
        help='name of podcast chapter'
    )

args = vars(parser.parse_args())

def main(podcast_name, chapter):
    # driver = Driver()
    # driver.get_driver()
    dp = DownloadPodcast(podcast_name, chapter_search_name=chapter)
    dp.download_podcast()
    

main(args['podcast_name'][0], args['chapter_name'][0])
