import urllib
import urllib2
import json

class HttpClient():
    """docstring for HttpClient"""
    def http_get(self, url, payload = None, headers = None):
        if payload is None:
            payload = {}
        if headers is None:
            headers = {}
        data = urllib.urlencode(payload)
        url = url + '?' + data
        request = urllib2.Request(url, None, headers)
        response = urllib2.urlopen(request)
        return response

    def http_post(self, url, payload = None, headers = None):
        if payload is None:
            payload = {}
        if headers is None:
            headers = {}
        data = json.dumps(payload)
        request = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(request)
        return response

    def http_put(self):
        pass

    def http_delete(self):
        pass

    def http_head(self):
        pass

    def https_get(self):
        pass

    def https_post(self):
        pass

    def https_put(self):
        pass

    def https_delete(self):
        pass

    def https_head(self):
        pass


