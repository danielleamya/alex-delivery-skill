from mycroft import MycroftSkill, intent_file_handler


class AlexDelivery(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('delivery.alex.intent')
    def handle_delivery_alex(self, message):
        self.speak_dialog('delivery.alex')


def create_skill():
    return AlexDelivery()

