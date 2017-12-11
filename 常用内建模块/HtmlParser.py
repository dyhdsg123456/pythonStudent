from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request
import re

class MyHTMLParser(HTMLParser):

    _is_time = False
    _is_location = False
    _is_title = False

    def handle_starttag(self, tag, attrs):
        if tag == 'time':
            self._is_time = True
        elif tag == 'span' and len(attrs) and attrs[0][1] == 'event-location':
            self._is_location = True
        elif tag == 'a' and len(attrs) and re.match(r'[a-z\/\-]+\/[0-9]+\/', attrs[0][1]):
            self._is_title = True

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        if self._is_time:
            print('Time: %s' % data)
            self._is_time = False
        if self._is_location:
            print('Location: %s' % data)
            self._is_location = False
        if self._is_title:
            print('Event Title: %s' % data)
            self._is_title = False

with request.urlopen('https://www.python.org/events/python-events/') as f:
    my_data = f.read()

parser = MyHTMLParser()
parser.feed(str(my_data))