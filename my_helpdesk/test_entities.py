import uuid as uuid_lib
import pytest

from my_helpdesk.entities import Ticket, Message, Customer
from my_helpdesk.exceptions import InvalidArgumentException
from my_helpdesk.value_objects import EmailAddress


class TestTicket:
    def test_uuid_is_being_set(self):
        uuid = uuid_lib.uuid4()
        title = "title"
        body = "body"
        ticket = Ticket(uuid=uuid, title=title, body=body)
        assert ticket.get_uuid() == uuid

    def test_title_is_being_set(self):
        uuid = uuid_lib.uuid4()
        title = "title"
        body = "body"
        ticket = Ticket(uuid=uuid, title=title, body=body)
        assert ticket.get_title() == title

    def test_body_is_being_set(self):
        uuid = uuid_lib.uuid4()
        title = "title"
        body = "body"
        ticket = Ticket(uuid=uuid, title=title, body=body)
        assert ticket.get_body() == body

    def test_add_message(self):
        uuid = uuid_lib.uuid4()
        title = "title"
        body = "body"
        ticket = Ticket(uuid=uuid, title=title, body=body)

        uuid2 = uuid_lib.uuid4()
        message = Message(
            uuid=uuid2,
            title="message title",
            body="message body"
        )

        ticket.add_message(message)

        assert len(ticket.get_messages()) == 1

    def test_get_customer(self):
        customer_uuid = uuid_lib.uuid4()
        email = EmailAddress("john@gmail.com")
        customer = Customer(uuid=customer_uuid, email=email)

        uuid = uuid_lib.uuid4()
        title = "title"
        body = "body"
        ticket = Ticket(uuid=uuid, title=title, body=body, customer=customer)

        assert ticket.get_customer() == customer

    def test_update_message(self):
        message_uuid = uuid_lib.uuid4()
        message = Message(
            uuid=message_uuid,
            title="message title",
            body="message body"
        )

        uuid = uuid_lib.uuid4()
        title = "title"
        body = "body"
        ticket = Ticket(uuid=uuid, title=title, body=body, messages=[message])

        new_title = "new title"
        message.update(title=new_title)

        ticket.update_message(message)

        assert ticket.get_messages()[0].get_title() == new_title

    def test_update(self):
        uuid = uuid_lib.uuid4()
        title = "title"
        body = "body"
        ticket = Ticket(uuid=uuid, title=title, body=body)

        new_title = "new title"
        ticket.update(title=new_title)

        assert ticket.get_title() == new_title

    def test_should_not_be_able_to_create_a_ticket_without_a_title(self):
        with pytest.raises(InvalidArgumentException):
                Ticket(body="body")

        def test_should_not_be_able_to_create_a_ticket_without_a_body(self):
            with pytest.raises(InvalidArgumentException):
                Ticket(title="title")
