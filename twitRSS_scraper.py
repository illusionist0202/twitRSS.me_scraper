from bs4 import BeautifulSoup
import requests
import lxml


def main():
    username = str((input("Enter Twitter Username(Example: realDonaldTrump)\n")).strip())
    url_add = "https://twitrss.me/twitter_user_to_rss/?user=" + str(username)
    source_code = requests.get(url_add)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    # print(soup)

    tweets = soup.findAll('title')
    tweets_links = soup.findAll('guid')

    # tweet_ids = soup.find('dc:creator')
    # tweet_link = tweets_links.text

    # print(tweet_ids)
    # print(type(tweets))
    # print(tweets)
    # print(tweets_links)

    for i in range(1, 25):
        try:
            tweets[i]
            print('tweet #' + str(i))
            print((tweets[i]).text)

            tweeted_by = str(((tweets_links[i-1]).text)[20:-26])
            # print(username)
            # print(tweeted_by)
            if username != tweeted_by:
                print("Retweet")
                print("Originally tweeted by:"+ tweeted_by)
            # print('twitter_username:' + '@' + str(((tweets_links[i-1]).text)[20:-26]))
            print((tweets_links[i-1]).text)
        except IndexError:
            print('')
            print("End of tweets!")
            break


if __name__ == '__main__':
    main()
