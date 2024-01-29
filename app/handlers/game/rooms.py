
from app.engine import Penguin, Instance
from app.data import Phase

@Instance.triggers.register('roomToRoomMinTime')
def on_room_to_room_min_time(client: Penguin, data: dict):
    client.is_ready = True

@Instance.triggers.register('roomToRoomComplete')
def on_room_to_room_complete(client: Penguin, data: dict):
    client.loaded = True

@Instance.triggers.register('roomToRoomScreenClosed')
def on_room_to_room_screen_closed(client: Penguin, data: dict):
    if client.last_tip in (Phase.MEMBER_CARD, Phase.CARD):
        infotip = client.window_manager.get_window('cardjitsu_snowinfotip.swf')
        infotip.send_payload('disable')

@Instance.triggers.register('roomToRoomMemberReviveTip')
def on_room_to_room_member_revive_tip(client: Penguin, data: dict):
    client.game.send_tip(Phase.MEMBER_CARD, client)

@Instance.triggers.register('roomToRoomMemberBuyCardsTip')
def on_room_to_room_member_buy_cards_tip(client: Penguin, data: dict):
    client.game.send_tip(Phase.CARD, client)
