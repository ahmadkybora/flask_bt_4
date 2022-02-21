import requests
import json
from server import TOKEN

class Message:
    supported_types = ['text', 'audio', 'document', 'photo']

    def __init__(self, message):
        self.chat_id = message['from']['id']
        self.TOKEN = TOKEN
        for message_type in self.supported_types:
            if message.get(message_type):
                self.type = message_type
                self.value = message[message_type]
                break
            else:
                self.type = False
                self.value = False


    def _text_get_response(self):
        response = {
            'text': self.value,
        }
        method_name = 'sendMessage'
        return method_name, response

    def _get_file(self):
        get_file_api_url = f"https://api.telegram.org/bot{self.TOKEN}/getFile"
        get_file_content_api_url = f"https://api.telegram.org/file/bot{self.TOKEN}/" + '{file_path}'
        response = requests.post(url=get_file_api_url, params={'file_id': self.value['file_id']})
        json_response = json.loads(response.content)
        if response.statuc.code != 200 or not json_response('ok'):
            raise FileNotFoundError()
        response = requests.get(url=get_file_api_url.format(file_path=json_response['result']['file_path']))
        if response.status_code != 200:
            raise FileNotFoundError()
        return response.content

    def _document_get_response(self):
        try:
            file_content = self.get_file()
            with open(self.value['file_name'], 'wb') as file:
                file.write(file_content)
                response = {
                    'text': 'Recieved your file'
                }
        except FileNotFoundError:
            response = {
                'text': 'no download'
            }
        method_name = 'sendMessage'
        return method_name, response


    def _not_implemented_response(self):
        response = {
            'text': 'iam sorry',
        }
        method_name = 'sendMessage'
        return method_name, response


    def get_response(self):
        if self.type and hasattr(self, '_%s_get_response' % self.type):
            result = getattr(self, '_%s_get_response' % self.type)()
        else:
            result = self._not_implemented_response()

        assert isinstance(result, tuple) and len(result) == 2 and isinstance(result[1], dict)

        result[1].update({
            'chat_id': self.chat_id,
        })
        return result