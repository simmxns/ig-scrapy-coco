from Soup import Soup
from Helpers import Helpers
from Helpers.enums import CONSTANTS

class User():
    @staticmethod
    def find_by_username(user_name):
        soup = Soup(user_name)

        if (soup.not_found):
            return { 'message': CONSTANTS.NotFound }

        username = soup.find_many('h2', '_aacl _aacs _aact _aacx _aada')[0].text
        name = soup.find_many('span', '_aacl _aacp _aacw _aacx _aad7 _aade')[0].text
        photo = soup.find_many('img', 'x6umtig x1b1mbwd xaqea5y xav7gou xk390pu x5yr21d xpdipgo xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x11njtxf xh8yej3')[1].attrs['src']
        rating = soup.find_many('span', '_ac2a')
        total_posts = int(Helpers.replace(',', '', rating[0].span.text))
        followers = int(Helpers.replace(',', '', rating[1].attrs['title']))
        followed = int(Helpers.replace(',', '', rating[2].span.text))
        unformat_posts = soup.find_many('div', '_aabd _aa8k _aanf')[:6]
        verified = soup.find('span', '_act0 _a9_u _9ys7') is not None

        posts = map(
            lambda post: post.a.div.select(f'div._aagv')[0].img.attrs['src'],
            unformat_posts
        )

        return {
            'username': username,
            'verified': verified, 
            'name': name,
            'photo': photo,
            'rating': {
                'posts': total_posts,
                'followers': followers,
                'followed': followed
            },
            'posts': list(posts)
        }