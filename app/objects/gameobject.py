
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Set

import app.engine as Engine

from .collections import SoundCollection, AssetCollection
from .asset import Asset
from .sound import Sound

if TYPE_CHECKING:
    from app.engine.game import Game

@dataclass
class GameObject:
    name: str
    game: "Game"
    x: int = 0
    y: int = 0
    id: int = 0
    assets: AssetCollection = field(default_factory=AssetCollection)
    sounds: SoundCollection = field(default_factory=SoundCollection)

    def __eq__(self, obj: "GameObject") -> bool:
        return self.id == obj.id

    def __hash__(self) -> int:
        return hash(self.id)

    def place_object(self) -> None:
        self.game.send_tag(
            'O_HERE',
            self.id,
            '0:1',  # TODO
            self.x,
            self.y,
            0,      # TODO
            1,      # TODO
            0,      # TODO
            0,      # TODO
            0,      # TODO
            '',     # TODO
            '0:1',  # TODO
            0,      # TODO
            1,      # TODO
            0       # TODO
        )

    def move_object(self) -> None:
        ...

    def animate_object(self) -> None:
        ...

    def place_sprite(self, name: str) -> None:
        asset = self.assets.by_name(name)
        self.game.send_tag(
            'O_SPRITE',
            self.id,
            f'0:{asset.index}',
            0, # TODO
            '' # TODO
        )

    def load_sprite(self, name: str) -> None:
        asset = self.assets.by_name(name)
        self.game.send_tag(
            'S_LOADSPRITE',
            f'0:{asset.index}'
        )

    def load_sprites(self) -> None:
        for asset in self.assets:
            self.game.send_tag(
                'S_LOADSPRITE',
                f'0:{asset.index}'
            )

    def animate_sprite(self) -> None:
        ...

    def add_sound(
        self,
        name: str,
        looping: bool = False,
        volume: int = 100,
        radius: int = 0
    ) -> None:
        self.sounds.add(
            Sound.from_name(
                name,
                looping,
                volume,
                radius,
                self.id,
                self.id # TODO: Different id for response object?
            )
        )

    def play_sound(self, sound_name: str) -> None:
        sound = self.sounds.by_name(sound_name)
        sound.play(self.game)
