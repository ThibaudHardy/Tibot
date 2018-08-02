
import yaml


class GetToken(object):

    @staticmethod
    def get_token():
        with open("static/token.yaml", 'r') as stream:
            token_obj = yaml.load(stream)
            token = token_obj["token"]
        return token