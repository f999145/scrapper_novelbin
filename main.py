from scrapper import get_urls, run_async
from decor import spent_time
import os





@spent_time
def main():
    # urls_list = get_urls()
    # run_async(urls_list)
    print(os.getcwd())

if __name__ == '__main__':
    main()