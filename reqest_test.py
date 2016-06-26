# -*- coding:cp932 -*-
u'''Request module(sandobox ver.)


UserAgets are reffered in http://utaukitune.ldblog.jp/archives/65696057.html
'''

import random
import socket
import time
import urllib2

from scglib.util import error

USER_AGENTS = [
    # Firefox 32bit / Windows 10 / 64bit 
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    # Firefox 64bit / Windows 8.1 / 64bit
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
    # Google Chrome / Windows 10 /64 bit
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
    # Google Chrome / Windows 8.1 /64bit
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
    ]

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko']

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36']

class Request(object):

    def __init__(self, retry_cnt=3):
        self.retry_cnt = 3
        socket.timeout(10)

    def get(self, url):
        try:
            t = time.time()
            result = Result()
            # リトライ回数分繰り返す
            for i in range(1, self.retry_cnt+1):
                isErr = False
                try:
                    opener = urllib2.build_opener()
                    ua = random.choice(USER_AGENTS)
                    result.user_agent = ua
                    print('ua=%s' % ua)
                    opener.addheaders = [('User-agent', ua)]
                    page = opener.open(url)
                except urllib2.HTTPError, e:
                    print(
                        'HTTPError(%d,%s):%s' % (e.code, e.msg, url))
                    isErr = True
                    if i <= self.retry_cnt:
                        print('retry(%d)' % (i))
                        time.sleep(5)
                        continue
                except urllib2.URLError, e:
                    print('URLError(%s):%s' % (e.reason, url))
                    isErr = True
                    if i <= self.retry_cnt:
                        print('retry(%d)' % (i))
                        time.sleep(5)
                        continue
                except socket.error, e:
                    print('socket.error(%s):%s' % (e, url))
                    isErr = True
                    if i <= self.retry_cnt:
                        print('retry(%d)' % (i))
                        time.sleep(5)
                        continue
                data = page.read()
                page.close()
                break
            t = time.time() - t
            if isErr:
                print('failure:%s' % url)
                return ''
            print('success(%.2f sec):%s' % (t, url))
            result.body = data
            return result
        except:
            error.addErrUnit('リクエスト処理に失敗しました。', {'URL': url})
            raise


class Result(object):

    def __init__(self):
        self.user_agent = ''
        self.body = ''
