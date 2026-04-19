from urllib.parse import urlparse, parse_qs, urlencode, urlunparse


class URL:
    def __init__(self, url):
        parsed = urlparse(url)
        self.scheme = parsed.scheme
        self.host = parsed.netloc
        self.path = parsed.path
        self.query_params = {}
        
        if parsed.query:
            params = parse_qs(parsed.query, keep_blank_values=True)
            self.query_params = {k: v[0] for k, v in params.items()}
    
    def get_scheme(self):
        return self.scheme
    
    def set_scheme(self, scheme):
        self.scheme = scheme
        return self
    
    def get_host(self):
        return self.host
    
    def set_host(self, host):
        self.host = host
        return self
    
    def get_path(self):
        return self.path
    
    def set_path(self, path):
        self.path = path
        return self
    
    def get_query_param(self, param_name, default=None):
        return self.query_params.get(param_name, default)
    
    def set_query_param(self, key, value):
        if value is None:
            self.query_params.pop(key, None)
        else:
            self.query_params[key] = str(value)
        return self
    
    def to_string(self):
        query_string = urlencode(self.query_params)
        return urlunparse((self.scheme, self.host, self.path, '', query_string, ''))


def make(url):
    return URL(url)


def get_scheme(data):
    return data.get_scheme()


def set_scheme(data, scheme):
    return data.set_scheme(scheme)


def get_host(data):
    return data.get_host()


def set_host(data, host):
    return data.set_host(host)


def get_path(data):
    return data.get_path()


def set_path(data, path):
    return data.set_path(path)


def get_query_param(data, param_name, default=None):
    return data.get_query_param(param_name, default)


def set_query_param(data, key, value):
    return data.set_query_param(key, value)


def to_string(data):
    return data.to_string()

