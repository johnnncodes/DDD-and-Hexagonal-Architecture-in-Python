import uuid as uuid_lib

from my_helpdesk.exceptions import InvalidArgumentException
from my_helpdesk.value_objects import EmailAddress

class Customer(object):

    def __init__(self, uuid=None, email=None):
        if uuid is None:
            self.__uuid = uuid_lib.uuid4()
        else:
            self.__uuid = uuid

        if email is not None:
            if not isinstance(email, EmailAddress):
                raise Exception
            self.__email = email

    def get_uuid(self):
        return self.__uuid

    def get_email(self):
        return self.__email


class Ticket(object):

    def __init__(self, uuid=None, title=None, body=None, customer=None, messages=[]):
        if uuid is None:
            self.__uuid = uuid_lib.uuid4()
        else:
            self.__uuid = uuid

        if title is None:
            raise InvalidArgumentException

        if body is None:
            raise InvalidArgumentException

        self.__title = title
        self.__body = body
        self.__customer = customer
        self.__messages = messages

    def get_uuid(self):
        return self.__uuid

    def get_title(self):
        return self.__title

    def get_body(self):
        return self.__body

    def get_messages(self):
        return self.__messages

    def get_customer(self):
        return self.__customer

    def update(self, title=None, body=None):
        self.__title = title

    def add_message(self, message):
        self.__messages.append(message)

    def update_message(self, message):
        for m in self.__messages:
            if m.get_uuid() == message.get_uuid():
                self.__messages.remove(m)
                self.__messages.append(message)


class Message(object):

    def __init__(self, uuid=None, title=None, body=None):
        if uuid is None:
            self.__uuid = uuid_lib.uuid4()
        else:
            self.__uuid = uuid

        self.__title = title
        self.__body = body

    def get_uuid(self):
        return self.__uuid

    def get_title(self):
        return self.__title

    def get_body(self):
        return self.__body

    def update(self, title=None, body=None):
        if title is not None:
            self.__title = title

        if body is not None:
            self.__body = body
