import argparse

import twint

parser = argparse.ArgumentParser()

parser.add_argument('--hashtag', type=str, help='use \",\" to seperate multiple words')
parser.add_argument('--year', type=int, help='use \",\" to seperate multiple words')
parser.add_argument('--save_path', type=str)
parser.add_argument('--limit', type=int)
parser.add_argument('--lang', type=str)

args = parser.parse_args()

if __name__ == '__main__':
    print(args)

    c = twint.Config()

    c.Store_csv = True
    c.Output = args.save_path
    c.Search = args.hashtag.split(',')
    c.Year = args.year
    c.Limit = args.limit
    c.Lang = args.lang

    twint.run.Search(c)
