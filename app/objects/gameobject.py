
from __future__ import annotations

from typing import TYPE_CHECKING, Callable

from app.data.constants import OriginMode, MirrorMode
from .collections import SoundCollection, AssetCollection
from .asset import Asset
from .sound import Sound

if TYPE_CHECKING:
    from app.engine.penguin import Penguin
    from app.engine.game import Game

class GameObject:
    def __init__(
        self,
        game: "Game",
        name: str,
        x: int = 0,
        y: int = 0,
        assets=AssetCollection(),
        sounds=SoundCollection(),
        on_click: Callable | None = None,
        grid: bool = False
    ) -> None:
        self.game = game
        self.name = name
        self.id = -1
        self.x = x
        self.y = y
        self.assets = assets
        self.sounds = sounds
        self.game.objects.add(self)
        self.on_click = on_click
        self.grid = grid

        # Place object in grid
        if grid: self.game.grid[x, y] = self

    def __eq__(self, other: object) -> bool:
        if not getattr(other, 'id', None):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

    @classmethod
    def from_asset(
        cls,
        name: str | list,
        game: "Game",
        x: int = 0,
        y: int = 0,
        grid: bool = False,
        on_click: Callable | None = None
    ) -> "GameObject":
        if isinstance(name, list):
            assets = AssetCollection([Asset.from_name(n) for n in name])
        else:
            assets = AssetCollection([Asset.from_name(name)])

        return GameObject(
            game,
            name,
            x,
            y,
            assets,
            grid=grid,
            on_click=on_click
        )

    def place_object(self) -> None:
        x = self.x
        y = self.y

        if self.grid:
            x = self.x + self.game.grid.x_offset
            y = self.y + self.game.grid.y_offset

        self.game.send_tag(
            'O_HERE',
            self.id,
            '0:1',  # TODO
            x,
            y,
            0,      # TODO
            1,      # TODO
            0,      # TODO
            0,      # TODO
            0,      # TODO
            self.name,
            '0:1',  # TODO
            0,      # TODO
            1,      # TODO
            0       # TODO
        )

    def move_object(self, x: int, y: int, duration: int = 600) -> None:
        self.x = x
        self.y = y

        if self.grid:
            self.game.grid.move(self, x, y)
            x = x + self.game.grid.x_offset
            y = y + self.game.grid.y_offset

        self.game.send_tag(
            'O_SLIDE',
            self.id,
            x,
            y,
            128, # Z Coordinate
            duration
        )

    def remove_object(self) -> None:
        self.game.send_tag('O_GONE', self.id)
        self.game.objects.remove(self)
        self.game.grid.remove(self)

        try:
            self.game.callbacks.pending_animations.pop(self.id)
        except KeyError:
            pass

    def animate_object(
        self,
        name: str,
        play_style: str = 'play_once',
        duration: int | None = None,
        time_scale: int = 1,
        reset: bool = False,
        callback: Callable | None = None
    ) -> None:
        asset = self.assets.by_name(name)
        handle_id = self.game.callbacks.register_animation(self.id, callback)

        self.game.send_tag(
            'O_ANIM',
            self.id,
            f'0:{asset.index}',
            play_style,
            duration or '',
            time_scale,
            int(not reset),
            self.id,
            handle_id
        )

    def place_sprite(self, name: str, target: "Penguin" | None = None) -> None:
        asset = self.assets.by_name(name)

        if target is None:
            target = self.game

        target.send_tag(
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

    def animate_sprite(
        self,
        start_frame: int = 0,
        end_frame: int = 0,
        backwards: bool = False,
        play_style = 'play_once',
        duration: int = 50,
    ) -> None:
        self.game.send_tag(
            'O_SPRITEANIM',
            self.id,
            start_frame + 1,
            end_frame + 1,
            int(backwards),
            play_style,
            duration
        )

    def sprite_settings(
        self,
        scale_x: int = 1,
        scale_y: int = 1,
        origin_mode: OriginMode = OriginMode.NONE,
        mirror_mode: MirrorMode = MirrorMode.NONE
    ) -> None:
        """This will update the sprite settings"""
        self.game.send_tag(
            'O_SPRITESETTINGS',
            self.id,
            'none', # Sprite layers
            scale_x,
            scale_y,
            '',
            '',
            '',
            origin_mode.value,
            mirror_mode.value
        )

    def hide(self) -> None:
        if not self.assets.by_name('blank_png'):
            self.assets.add(Asset.from_name('blank_png'))

        self.place_sprite('blank_png')

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

    def play_sound(self, sound_name: str, target: "Penguin" | None = None) -> None:
        sound = self.sounds.by_name(sound_name)
        sound.play(target or self.game)

class LocalGameObject(GameObject):
    def __init__(
        self,
        game: "Game",
        client: "Penguin",
        name: str,
        x: int = 0,
        y: int = 0,
        assets=AssetCollection(),
        sounds=SoundCollection(),
        on_click: Callable | None = None
    ) -> None:
        self.game = game
        self.client = client
        self.name = name
        self.id = -1
        self.x = x
        self.y = y
        self.assets = assets
        self.sounds = sounds
        self.game.objects.add(self)
        self.on_click = on_click

    @classmethod
    def from_asset(
        cls,
        name: str | list,
        game: "Game",
        client: "Penguin",
        x: int = 0,
        y: int = 0,
        on_click: Callable | None = None
    ) -> "GameObject":
        if isinstance(name, list):
            assets = AssetCollection([Asset.from_name(n) for n in name])
        else:
            assets = AssetCollection([Asset.from_name(name)])

        return LocalGameObject(
            game,
            client,
            name,
            x,
            y,
            assets,
            on_click=on_click
        )

    def place_object(self) -> None:
        self.client.send_tag(
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
            self.name,
            '0:1',  # TODO
            0,      # TODO
            1,      # TODO
            0       # TODO
        )

    def move_object(self, x: int, y: int, duration: int = 600) -> None:
        self.x = x
        self.y = y

        self.client.send_tag(
            'O_SLIDE',
            self.id,
            x,
            y,
            128, # Z Coordinate
            duration
        )

    def remove_object(self) -> None:
        self.client.send_tag('O_GONE', self.id)
        self.game.objects.remove(self)

        try:
            self.game.callbacks.pending_animations.pop(self.id)
        except KeyError:
            pass

    def animate_object(
        self,
        name: str,
        play_style: str = 'play_once',
        duration: int | None = None,
        time_scale: int = 1,
        reset: bool = False,
        callback: Callable | None = None
    ) -> None:
        asset = self.assets.by_name(name)
        handle_id = self.game.callbacks.register_animation(self.id, callback)

        self.client.send_tag(
            'O_ANIM',
            self.id,
            f'0:{asset.index}',
            play_style,
            duration or '',
            time_scale,
            int(not reset),
            self.id,
            handle_id
        )

    def place_sprite(self, name: str) -> None:
        asset = self.assets.by_name(name)

        self.client.send_tag(
            'O_SPRITE',
            self.id,
            f'0:{asset.index}',
            0, # TODO
            '' # TODO
        )

    def load_sprite(self, name: str) -> None:
        asset = self.assets.by_name(name)
        self.client.send_tag(
            'S_LOADSPRITE',
            f'0:{asset.index}'
        )

    def load_sprites(self) -> None:
        for asset in self.assets:
            self.client.send_tag(
                'S_LOADSPRITE',
                f'0:{asset.index}'
            )

    def animate_sprite(
        self,
        start_frame: int = 0,
        end_frame: int = 0,
        backwards: bool = False,
        play_style = 'play_once',
        duration: int = 50,
    ) -> None:
        self.client.send_tag(
            'O_SPRITEANIM',
            self.id,
            start_frame + 1,
            end_frame + 1,
            int(backwards),
            play_style,
            duration
        )

    def sprite_settings(
        self,
        scale_x: int = 1,
        scale_y: int = 1,
        origin_mode: OriginMode = OriginMode.NONE,
        mirror_mode: MirrorMode = MirrorMode.NONE
    ) -> None:
        """This will update the sprite settings"""
        self.client.send_tag(
            'O_SPRITESETTINGS',
            self.id,
            'none', # Sprite layers
            scale_x,
            scale_y,
            '',
            '',
            '',
            origin_mode.value,
            mirror_mode.value
        )

    def hide(self) -> None:
        if not self.assets.by_name('blank_png'):
            self.assets.add(Asset.from_name('blank_png'))

        self.place_sprite('blank_png')

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
        sound.play(self.client)
