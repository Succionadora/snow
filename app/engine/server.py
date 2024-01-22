
from twisted.internet.address import IPv4Address, IPv6Address
from twisted.internet.protocol import Factory
from twisted.internet import reactor

from ..data import ServerType, BuildType
from ..events import EventHandler
from .penguin import Penguin

import logging
import config

class SnowflakeEngine(Factory):
    def __init__(self):
        self.players: set[Penguin] = set()
        self.protocol = Penguin

        self.server_type = ServerType.LIVE
        self.build_type = BuildType.RELEASE

        self.world_id = 101
        self.world_name = "clubpenguin_town_en_3"

        self.logger = logging.getLogger("snowflake")
        self.events = EventHandler()

    def buildProtocol(self, address: IPv4Address | IPv6Address):
        self.logger.info(f'-> "{address.host}:{address.port}"')
        self.players.add(player := self.protocol(self, address))
        return player

    def stopFactory(self):
        self.logger.warning("Shutting down...")

    def run(self):
        self.logger.info(f"Starting engine: {self} ({config.PORT})")
        reactor.listenTCP(config.PORT, self)
        reactor.run()

Instance = SnowflakeEngine()