import requests
from lxml import etree
from pyquery import PyQuery as pq


class Login(object):
    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.feed_url = 'https://github.com/dashboard-feed'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()

    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = pq(response.text)
        token = selector('input[name="authenticity_token"]').attr('value')
        return token

    def login(self, email, password):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.token(),
            'login': email,
            'password': password
        }
        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        if response.status_code == 200:
            self.dynamics(response.text)

        response = self.session.get(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)

    def dynamics(self, html):
        selector = pq(html)
        # print(selector.text())
        dynamics = selector('div[class="d-flex flex-items-baseline"] div')
        dynamics.find('span').remove()
        # print(dynamics.text())
        for item in dynamics.items():
            dynamic = item.text().strip()
            print(dynamic)

    def profile(self, html):
        selector = pq(html)
        name = selector('input[id="user_profile_name"]').attr('value')
        email = selector('select[id="user_profile_email"] option[selected="selected"]').text()
        print(name, email)


if __name__ == "__main__":
    login = Login()
    login.login(email='cqc@cuiqingcai.com', password='password')
