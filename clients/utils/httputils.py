import requests,bs4

def get_csrf_token(html):
    """
    返回页面的csrf_token
    """
    soup = bs4.BeautifulSoup(html,'html.parser')
    csrf_token=soup.find(attrs={'name':'csrfmiddlewaretoken'})
    return {'csrfmiddlewaretoken':csrf_token['value']}

def init_session(main_page_url):
    """
    初始化一个到目标网站的session对象
    """
    session = requests.Session()
    session.get(main_page_url)
    return session




    