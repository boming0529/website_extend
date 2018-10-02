# -*- coding: utf-8 -*-
import time
import hashlib
from urllib import urlencode
from urlparse import urlparse, urlunparse
import urllib2
import xmltodict
from functools import wraps


def slideshare_api(func):
    service_url = 'https://www.slideshare.net/api/2/' + func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        """API Validation using the SlideShare API
            All requests made using the SlideShare API must have the following parameters:

            api_key: Set this to the API Key that SlideShare has provided for you.
            ts: Set this to the current time in Unix TimeStamp format, to the nearest second(?).
            hash: Set this to the SHA1 hash of the concatenation of the shared secret and the timestamp (ts). 
            i.e. SHA1 (sharedsecret + timestamp). The order of the terms in the concatenation is important.
        """
        result = {'values': dict()}
        try:
            self = args[0]
            fparams, fargs = func(*args, **kwargs)
            ts = int(time.time())
            params = {
                'api_key': self.api_key,
                'ts': ts,
                'hash': hashlib.sha1(self.sharedsecret + str(ts)).hexdigest(),
            }
            for k, v in fargs.iteritems():
                if (k in fparams) and v:
                    params[k] = v

            eparams = urlencode(params)
            data = urllib2.urlopen(service_url, eparams).read()
            json = xmltodict.parse(data)
            result['values'] = json
        except urllib2.HTTPError as e:
            result['error'] = e.read()
            e.close()
        except urllib2.URLError as e:
            result['error'] = e.reason
        return result
    return wrapper


class SlideshareAPI(object):
    api_key = None
    sharedsecret = None

    def __init__(self, api_key, sharedsecret):
        if api_key and sharedsecret:
            self.sharedsecret = sharedsecret
            self.api_key = api_key
        else:
            raise ValueError

    @slideshare_api
    def get_slideshow(self, slideshow_id=None, slideshow_url=None, **kwargs):
        params = ['slideshow_id', 'slideshow_url', 'username', 'password', 'exclude_tags', 'detailed']
        if slideshow_id or slideshow_url:
            if slideshow_id:
                kwargs['slideshow_id'] = slideshow_id
            else:
                urlob = urlparse(slideshow_url)
                if urlob.hostname == 'www.slideshare.net':
                    url = urlunparse([urlob.scheme, urlob.netloc,
                                      urlob.path, '', '', ''])
                    kwargs['slideshow_url'] = url
                else:
                    raise ValueError
        else:
            raise ValueError
        return params, kwargs
