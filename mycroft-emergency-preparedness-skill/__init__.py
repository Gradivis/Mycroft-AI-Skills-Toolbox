# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'gradivis'

LOGGER = getLogger(__name__)


class EmergencySkill(MycroftSkill):
    def __init__(self):
        super(EmergencySkill, self).__init__(name="EmergencySkill")

    def initialize(self):
        nuclear_action_intent = IntentBuilder("NuclearActionIntent"). \
            require("NuclearActionKeyword").build()
        self.register_intent(nuclear_action_intent, 
                            self.handle_nuclear_action_intent)

        tornado_action_intent = IntentBuilder("TornadoActionIntent"). \
            require("TornadoActionKeyword").build()
        self.register_intent(tornado_action_intent,
                             self.handle_tornado_action_intent)

        wildfire_action_intent = IntentBuilder("WildfireActionIntent"). \
            require("WildfireActionKeyword").build()
        self.register_intent(wildfire_action_intent,
                             self.handle_wildfire_action_intent)

    def handle_nuclear_action_intent(self, message):
        self.speak_dialog("nuclear.action")

    def handle_tornado_action_intent(self, message):
        self.speak_dialog("tornado.action")

    def handle_wildfire_action_intent(self, message):
        self.speak_dialog("wildfire.action")

    def stop(self):
        pass


def create_skill():
    return EmergencySkill()