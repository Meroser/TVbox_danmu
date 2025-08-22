class Proxy:
    @staticmethod
    def getUrl(local):
        return f'http://127.0.0.1:{Proxy.getPort()}'

    @staticmethod
    def getPort():
        return 9978
