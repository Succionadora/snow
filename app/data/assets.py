
from app.objects.asset import Asset
from app.engine import Instance
import config

asset_url = f"http://{config.MEDIA_LOCATION}/game/mpassets/minigames/cjsnow/en_US/deploy/png/large"
sound_url = f"http://{config.MEDIA_LOCATION}/game/mpassets/minigames/cjsnow/en_US/deploy/sound/gameplay"

Instance.assets.update([
    Asset(1, "blank_png", f"{asset_url}/env/pixel.png"),
    Asset(30044, "waterninja_move_ghost", f"{asset_url}/ninja_water_char_anim/waterninja_move_ghost_large.tpk"),
    Asset(30070, "fireninja_move_ghost", f"{asset_url}/ninja_fire_char_anim/fireninja_move_ghost_large.tpk"),
    Asset(100018, "snowninja_move_ghost", f"{asset_url}/ninja_snow_char_anim/snowninja_move_ghost_large.tpk"),
    Asset(100040, "ui_target_red_attack_intro_anim", f"{asset_url}/hud/ui_target_red_attack_intro_anim_large.tpk"),
    Asset(100041, "ui_target_red_attack_idle_anim", f"{asset_url}/hud/ui_target_red_attack_idle_anim_large.tpk"),
    Asset(100042, "ui_target_green_attack_selected_intro_anim", f"{asset_url}/hud/ui_target_green_attack_selected_intro_anim_large.tpk"),
    Asset(100043, "ui_target_green_attack_selected_idle_anim", f"{asset_url}/hud/ui_target_green_attack_selected_idle_anim_large.tpk"),
    Asset(100044, "ui_target_white_heal_intro_anim", f"{asset_url}/hud/ui_target_white_heal_intro_anim_large.tpk"),
    Asset(100045, "ui_target_white_heal_idle_anim", f"{asset_url}/hud/ui_target_white_heal_idle_anim_large.tpk"),
    Asset(100046, "ui_target_green_heal_selected_intro_anim", f"{asset_url}/hud/ui_target_green_heal_selected_intro_anim_large.tpk"),
    Asset(100047, "ui_target_green_heal_selected_idle_anim", f"{asset_url}/hud/ui_target_green_heal_selected_idle_anim_large.tpk"),
    Asset(100048, "ui_healfx_anim", f"{asset_url}/hud/ui_healfx_anim_large.tpk"),
    Asset(100063, "ui_tile_move", f"{asset_url}/hud/ui_tile_move_large.tpk"),
    Asset(100064, "ui_tile_attack", f"{asset_url}/hud/ui_tile_attack_large.tpk"),
    Asset(100065, "ui_tile_heal", f"{asset_url}/hud/ui_tile_heal_large.tpk"),
    Asset(100067, "ui_attack_numbers_anim", f"{asset_url}/hud/ui_attack_numbers_anim_large.tpk"),
    Asset(100120, "ui_card_fire", f"{asset_url}/hud/ui_card_fire_large.tpk"),
    Asset(100121, "ui_card_snow", f"{asset_url}/hud/ui_card_snow_large.tpk"),
    Asset(100122, "ui_card_water", f"{asset_url}/hud/ui_card_water_large.tpk"),
    Asset(100195, "confirm", f"{asset_url}/hud/ui_confirm_checkmark_large.tpk"),
    Asset(100240, "tank_swipe_horiz_anim", f"{asset_url}/snowman_tank_char_anim/tank_swipe_horiz_anim_large.tpk"),
    Asset(100241, "tank_swipe_vert_anim", f"{asset_url}/snowman_tank_char_anim/tank_swipe_vert_anim_large.tpk"),
    Asset(100250, "ui_heal_numbers_anim", f"{asset_url}/hud/ui_heal_numbers_anim_large.tpk"),
    Asset(100266, "ui_card_pattern3x3", f"{asset_url}/hud/ui_card_pattern3x3_large.tpk"),
    Asset(100267, "ui_card_pattern3x2", f"{asset_url}/hud/ui_card_pattern3x2_large.tpk"),
    Asset(100268, "ui_card_pattern2x3", f"{asset_url}/hud/ui_card_pattern2x3_large.tpk"),
    Asset(100269, "ui_card_pattern2x2", f"{asset_url}/hud/ui_card_pattern2x2_large.tpk"),
    Asset(100270, "ui_tile_no_move", f"{asset_url}/hud/ui_tile_no_move_large.tpk"),
    Asset(100271, "tuskhealthbar_animation", f"{asset_url}/hud/tuskhealthbar_animation_large.tpk"),
    Asset(100272, "ui_target_red_attack_tusk_intro", f"{asset_url}/hud/ui_target_red_attack_tusk_intro_large.tpk"),
    Asset(100273, "ui_target_red_attack_idle_tusk_anim", f"{asset_url}/hud/ui_target_red_attack_idle_tusk_anim_large.tpk"),
    Asset(100291, "ui_target_green_attack_selected_intro_tusk_anim", f"{asset_url}/hud/ui_target_green_attack_selected_intro_tusk_anim_large.tpk"),
    Asset(100293, "ui_target_green_idle_tusk", f"{asset_url}/hud/ui_target_green_idle_tusk_large.tpk"),
    Asset(100297, "tank_idle_anim", f"{asset_url}/snowman_tank_char_anim/tank_idle_anim_large.tpk"),
    Asset(100299, "tank_attack_anim", f"{asset_url}/snowman_tank_char_anim/tank_attack_anim_large.tpk"),
    Asset(100300, "ui_tile_frame", f"{asset_url}/hud/ui_tile_frame_large.tpk"),
    Asset(100302, "tank_hit_anim", f"{asset_url}/snowman_tank_char_anim/tank_hit_anim_large.tpk"),
    Asset(100303, "tank_move_anim", f"{asset_url}/snowman_tank_char_anim/tank_move_anim_large.tpk"),
    Asset(100304, "tank_ko_anim", f"{asset_url}/snowman_tank_char_anim/tank_knockout_anim_large.tpk"),
    Asset(100305, "sly_idle_anim", f"{asset_url}/snowman_sly_char_anim/sly_idle_anim_large.tpk"),
    Asset(100306, "sly_attack_anim", f"{asset_url}/snowman_sly_char_anim/sly_attack_anim_large.tpk"),
    Asset(100307, "sly_move_anim", f"{asset_url}/snowman_sly_char_anim/sly_move_anim_large.tpk"),
    Asset(100308, "sly_hit_anim", f"{asset_url}/snowman_sly_char_anim/sly_hit_anim_large.tpk"),
    Asset(100309, "sly_ko_anim", f"{asset_url}/snowman_sly_char_anim/sly_ko_anim_large.tpk"),
    Asset(100310, "sly_projectile_anim", f"{asset_url}/snowman_sly_char_anim/sly_projectile_anim_large.tpk"),
    Asset(100311, "scrap_idle_anim", f"{asset_url}/snowman_scrap_char_anim/scrap_idle_anim_large.tpk"),
    Asset(100312, "scrap_attack_anim", f"{asset_url}/snowman_scrap_char_anim/scrap_attack_anim_large.tpk"),
    Asset(100313, "scrap_attackeffect_anim", f"{asset_url}/snowman_scrap_char_anim/scrap_attackeffect_anim_large.tpk"),
    Asset(100314, "scrap_attacklittleeffect_anim", f"{asset_url}/snowman_scrap_char_anim/scrap_attacklittleeffect_anim_large.tpk"),
    Asset(100315, "scrap_projectileeast_anim", f"{asset_url}/snowman_scrap_char_anim/scrap_projectileeast_anim_large.tpk"),
    Asset(100316, "scrap_projectilenorth_anim", f"{asset_url}/snowman_scrap_char_anim/scrap_projectilenorth_anim_large.tpk"),
    Asset(100317, "scrap_projectilenortheast_anim", f"{asset_url}/snowman_scrap_char_anim/scrap_projectilenortheast_anim_large.tpk"),
    Asset(100318, "scrap_hit_anim", f"{asset_url}/snowman_scrap_char_anim/scrap_hit_anim_large.tpk"),
    Asset(100319, "scrap_move_anim", f"{asset_url}/snowman_scrap_char_anim/scrap_move_anim_large.tpk"),
    Asset(100320, "scrap_ko_anim", f"{asset_url}/snowman_scrap_char_anim/scrap_ko_anim_large.tpk"),
    Asset(100321, "waterninja_attack_anim", f"{asset_url}/ninja_water_char_anim/waterninja_attack_anim_large.tpk"),
    Asset(100322, "waterninja_idle_anim", f"{asset_url}/ninja_water_char_anim/waterninja_idle_anim_large.tpk"),
    Asset(100323, "waterninja_move_anim", f"{asset_url}/ninja_water_char_anim/waterninja_move_anim_large.tpk"),
    Asset(100324, "waterninja_hit_anim", f"{asset_url}/ninja_water_char_anim/waterninja_hit_anim_large.tpk"),
    Asset(100325, "waterninja_knockout_intro_anim", f"{asset_url}/ninja_water_char_anim/waterninja_knockout_intro_anim_large.tpk"),
    Asset(100326, "waterninja_knockout_loop_anim", f"{asset_url}/ninja_water_char_anim/waterninja_knockout_loop_anim_large.tpk"),
    Asset(100327, "waterninja_celebrate_anim", f"{asset_url}/ninja_water_char_anim/waterninja_celebrate_anim_large.tpk"),
    Asset(100328, "waterninja_powercard_fishdrop_anim", f"{asset_url}/ninja_water_char_anim/waterninja_powercard_fishdrop_anim_large.tpk"),
    Asset(100329, "waterninja_powercard_summon_anim", f"{asset_url}/ninja_water_char_anim/waterninja_powercard_summon_anim_large.tpk"),
    Asset(100330, "waterninja_powercard_water_loop_anim", f"{asset_url}/ninja_water_char_anim/waterninja_powercard_water_loop_anim_large.tpk"),
    Asset(100331, "waterninja_revived_anim", f"{asset_url}/ninja_water_char_anim/waterninja_revived_anim_large.tpk"),
    Asset(100332, "waterninja_revive_other_intro_anim", f"{asset_url}/ninja_water_char_anim/waterninja_revive_other_intro_anim_large.tpk"),
    Asset(100333, "waterninja_revive_other_loop_anim", f"{asset_url}/ninja_water_char_anim/waterninja_revive_other_loop_anim_large.tpk"),
    Asset(100334, "effect_rageloop_anim", f"{asset_url}/effects_anim/effect_rageloop_anim_large.tpk"),
    Asset(100335, "effect_explosion_anim", f"{asset_url}/effects_anim/effect_explosion_anim_large.tpk"),
    Asset(100336, "effect_shield_loop", f"{asset_url}/effects_anim/effect_shield_loop_large.tpk"),
    Asset(100337, "effect_shieldpop_anim", f"{asset_url}/effects_anim/effect_shieldpop_anim_large.tpk"),
    Asset(100339, "effect_resisualfiredamage_anim", f"{asset_url}/effects_anim/effect_resisualfiredamage_anim_large.tpk"),
    Asset(100340, "fireninja_idle_anim", f"{asset_url}/ninja_fire_char_anim/fireninja_idle_anim_large.tpk"),
    Asset(100341, "fireninja_move_anim", f"{asset_url}/ninja_fire_char_anim/fireninja_move_anim_large.tpk"),
    Asset(100342, "fireninja_hit_anim", f"{asset_url}/ninja_fire_char_anim/fireninja_hit_anim_large.tpk"),
    Asset(100343, "fireninja_attack_anim", f"{asset_url}/ninja_fire_char_anim/fireninja_attack_anim_large.tpk"),
    Asset(100344, "fireninja_powerbottle_anim", f"{asset_url}/ninja_fire_char_anim/fireninja_powerbottle_anim_large.tpk"),
    Asset(100345, "fireninja_powerskyfire_anim", f"{asset_url}/ninja_fire_char_anim/fireninja_powerskyfire_anim_large.tpk"),
    Asset(100346, "fireninja_projectile_angleup_anim", f"{asset_url}/ninja_fire_char_anim/fireninja_projectile_angleup_anim_large.tpk"),
    Asset(100347, "fireninja_projectile_angledown_anim", f"{asset_url}/ninja_fire_char_anim/fireninja_projectile_angledown_anim_large.tpk"),
    Asset(100348, "fireninja_projectile_down_anim", f"{asset_url}/ninja_fire_char_anim/fireninja_projectile_down_anim_large.tpk"),
    Asset(100349, "fireninja_projectile_downfar_anim", f"{asset_url}/ninja_fire_char_anim/fireninja_projectile_downfar_anim_large.tpk"),
    Asset(100350, "fireninja_projectile_right_anim", f"{asset_url}/ninja_fire_char_anim/fireninja_projectile_right_anim_large.tpk"),
    Asset(100351, "fireninja_projectile_rightfar_anim", f"{asset_url}/ninja_fire_char_anim/fireninja_projectile_rightfar_anim_large.tpk"),
    Asset(100352, "fireninja_projectile_up_anim", f"{asset_url}/ninja_fire_char_anim/fireninja_projectile_up_anim_large.tpk"),
    Asset(100353, "fireninja_projectile_upfar_anim", f"{asset_url}/ninja_fire_char_anim/fireninja_projectile_upfar_anim_large.tpk"),
    Asset(100354, "fireninja_celebratestart_anim", f"{asset_url}/ninja_fire_char_anim/fireninja_celebratestart_anim_large.tpk"),
    Asset(100355, "fireninja_celebrateloop_anim", f"{asset_url}/ninja_fire_char_anim/fireninja_celebrateloop_anim_large.tpk"),
    Asset(100356, "fireninja_kostart_anim", f"{asset_url}/ninja_fire_char_anim/fireninja_kostart_anim_large.tpk"),
    Asset(100357, "fireninja_koloop_anim", f"{asset_url}/ninja_fire_char_anim/fireninja_koloop_anim_large.tpk"),
    Asset(100358, "fireninja_revived_anim", f"{asset_url}/ninja_fire_char_anim/fireninja_revived_anim_large.tpk"),
    Asset(100359, "fireninja_reviveother_anim", f"{asset_url}/ninja_fire_char_anim/fireninja_reviveother_anim_large.tpk"),
    Asset(100360, "fireninja_reviveotherloop_anim", f"{asset_url}/ninja_fire_char_anim/fireninja_reviveotherloop_anim_large.tpk"),
    Asset(100361, "snowninja_idle_anim", f"{asset_url}/ninja_snow_char_anim/snowninja_idle_anim_large.tpk"),
    Asset(100362, "snowninja_attack_anim", f"{asset_url}/ninja_snow_char_anim/snowninja_attack_anim_large.tpk"),
    Asset(100363, "snowninja_heal_anim", f"{asset_url}/ninja_snow_char_anim/snowninja_heal_anim_large.tpk"),
    Asset(100364, "snowninja_hit_anim", f"{asset_url}/ninja_snow_char_anim/snowninja_hit_anim_large.tpk"),
    Asset(100365, "snowninja_kointro_anim", f"{asset_url}/ninja_snow_char_anim/snowninja_kointro_anim_large.tpk"),
    Asset(100366, "snowninja_koloop_anim", f"{asset_url}/ninja_snow_char_anim/snowninja_koloop_anim_large.tpk"),
    Asset(100367, "snowninja_move_anim", f"{asset_url}/ninja_snow_char_anim/snowninja_move_anim_large.tpk"),
    Asset(100368, "snowninja_celebrate_anim", f"{asset_url}/ninja_snow_char_anim/snowninja_celebrate_anim_large.tpk"),
    Asset(100370, "snowninja_beam_anim_", f"{asset_url}/ninja_snow_char_anim/snowninja_beam_anim_large.tpk"),
    Asset(100371, "snowninja_powercard_anim", f"{asset_url}/ninja_snow_char_anim/snowninja_powercard_anim_large.tpk"),
    Asset(100372, "snowninja_projectileangle_anim", f"{asset_url}/ninja_snow_char_anim/snowninja_projectileangle_anim_large.tpk"),
    Asset(100373, "snowninja_projectilehoriz_anim", f"{asset_url}/ninja_snow_char_anim/snowninja_projectilehoriz_anim_large.tpk"),
    Asset(100374, "snowninja_projectilevert_anim", f"{asset_url}/ninja_snow_char_anim/snowninja_projectilevert_anim_large.tpk"),
    Asset(100375, "snowninja_revive_anim_", f"{asset_url}/ninja_snow_char_anim/snowninja_revive_anim_large.tpk"),
    Asset(100376, "snowninja_reviveothersintro_anim", f"{asset_url}/ninja_snow_char_anim/snowninja_reviveothersintro_anim_large.tpk"),
    Asset(100377, "snowninja_reviveothersloop_anim", f"{asset_url}/ninja_snow_char_anim/snowninja_reviveothersloop_anim_large.tpk"),
    Asset(100378, "fireninja_power_anim", f"{asset_url}/ninja_fire_char_anim/fireninja_power_anim_large.tpk"),
    Asset(100379, "snowman_spawn_anim", f"{asset_url}/effects_anim/snowman_spawn_anim_large.tpk"),
    Asset(100380, "env_mountaintop_bg", f"{asset_url}/env/mountaintop_bg_large.tpk"),
    Asset(100381, "sensei_attackstart_anim", f"{asset_url}/sensei_char_anim/sensei_attackstart_anim_large.tpk"),
    Asset(100382, "sensei_attackloop_anim", f"{asset_url}/sensei_char_anim/sensei_attackloop_anim_large.tpk"),
    Asset(100383, "sensei_idle_anim", f"{asset_url}/sensei_char_anim/sensei_idle_anim_large.tpk"),
    Asset(100384, "sensei_lose_anim", f"{asset_url}/sensei_char_anim/sensei_lose_anim_large.tpk"),
    Asset(100385, "sensei_powerupfire_anim", f"{asset_url}/sensei_char_anim/sensei_powerupfire_anim_large.tpk"),
    Asset(100386, "sensei_powerupfireloop_anim", f"{asset_url}/sensei_char_anim/sensei_powerupfireloop_anim_large.tpk"),
    Asset(100387, "sensei_powerupsnow_anim", f"{asset_url}/sensei_char_anim/sensei_powerupsnow_anim_large.tpk"),
    Asset(100388, "sensei_powerupsnowloop_anim", f"{asset_url}/sensei_char_anim/sensei_powerupsnowloop_anim_large.tpk"),
    Asset(100389, "sensei_powerupwater_anim", f"{asset_url}/sensei_char_anim/sensei_powerupwater_anim_large.tpk"),
    Asset(100390, "sensei_powerupwaterloop_anim", f"{asset_url}/sensei_char_anim/sensei_powerupwaterloop_anim_large.tpk"),
    Asset(100391, "sensei_win_anim", f"{asset_url}/sensei_char_anim/sensei_win_anim_large.tpk"),
    Asset(100392, "effect_rageattack_anim", f"{asset_url}/effects_anim/effect_rageattack_anim_large.tpk"),
    Asset(100394, "rock_mountaintop", f"{asset_url}/env/rock_mountaintop_large.tpk"),
    Asset(100395, "reghealthbar_animation", f"{asset_url}/hud/reghealthbar_animation_large.tpk"),
    Asset(100396, "effect_ragehit_anim", f"{asset_url}/effects_anim/effect_ragehit_anim_large.tpk"),
    Asset(1840001, "tusk_background_under", f"{asset_url}/env/tusk_background_under_large.tpk"),
    Asset(1840002, "tusk_idle_anim", f"{asset_url}/tusk_char_anim/tusk_idle_anim_large.tpk"),
    Asset(1840003, "tusk_hit_anim", f"{asset_url}/tusk_char_anim/tusk_hit_anim_large.tpk"),
    Asset(1840005, "tusk_pushattack_anim", f"{asset_url}/tusk_char_anim/tusk_pushattack_anim_large.tpk"),
    Asset(1840006, "tusk_lose_anim", f"{asset_url}/tusk_char_anim/tusk_lose_anim_large.tpk"),
    Asset(1840007, "tusk_win_anim", f"{asset_url}/tusk_char_anim/tusk_win_anim_large.tpk"),
    Asset(1840008, "tusk_icicle_drop_anim", f"{asset_url}/tusk_char_anim/tusk_icicle_drop_anim_large.tpk"),
    Asset(1840010, "tank_daze_anim", f"{asset_url}/snowman_tank_char_anim/tank_daze_anim_large.tpk"),
    Asset(1840011, "sly_daze_anim", f"{asset_url}/snowman_sly_char_anim/sly_daze_anim_large.tpk"),
    Asset(1840012, "scrap_dazed_anim", f"{asset_url}/snowman_scrap_char_anim/scrap_dazed_anim_large.tpk"),
    Asset(6740001, "tusk_stun_anim", f"{asset_url}/tusk_char_anim/tusk_stun_anim_large.tpk"),
    Asset(6740002, "effect_tusk_push", f"{asset_url}/effects_anim/effect_tusk_push_large.tpk"),
    Asset(6740003, "cragvalley_bg", f"{asset_url}/env/cragvalley_bg_large.tpk"),
    Asset(6740004, "cragvalley_fg", f"{asset_url}/env/cragvalley_fg_large.tpk"),
    Asset(6740005, "tusk_background_over", f"{asset_url}/env/tusk_background_over_large.tpk"),
    Asset(6740006, "forest_bg", f"{asset_url}/env/forest_bg_large.tpk"),
    Asset(6740007, "forest_fg", f"{asset_url}/env/forest_fg_large.tpk"),
    Asset(6740008, "crag_rock", f"{asset_url}/env/crag_rock_large.tpk"),
    Asset(6740009, "Empty Tile", f"{asset_url}/env/pixel.png"),
    Asset(6740010, "open", f"{asset_url}/env/pixel.png"),
    Asset(6740011, "enemy", f"{asset_url}/env/pixel.png"),
    Asset(6740012, "penguin", f"{asset_url}/env/pixel.png"),
    Asset(6740013, "penguin_spawn_occupied", f"{asset_url}/env/pixel.png"),
    Asset(6740014, "penguin_spawn_unoccupied", f"{asset_url}/env/pixel.png"),
    Asset(6740015, "enemy_spawn_unoccupied", f"{asset_url}/env/pixel.png"),
    Asset(6740016, "enemy_spawn_occupied", f"{asset_url}/env/pixel.png"),
    Asset(6740017, "obstacle", f"{asset_url}/env/pixel.png"),
    Asset(7940001, "water_spawn", f"{asset_url}/env/pixel.png"),
    Asset(7940002, "enemy_spawn_unoccupied", f"{asset_url}/env/pixel.png"),
    Asset(7940003, "enemy_spawn_occupied", f"{asset_url}/env/pixel.png"),
    Asset(7940004, "obstacle", f"{asset_url}/env/pixel.png"),
    Asset(7940005, "penguin_spawn_occupied", f"{asset_url}/env/pixel.png"),
    Asset(7940006, "Empty Tile", f"{asset_url}/env/pixel.png"),
    Asset(7940007, "blankblue", f"{asset_url}/env/pixel.png"),
    Asset(7940008, "blankgreen", f"{asset_url}/env/pixel.png"),
    Asset(7940009, "blankgrey", f"{asset_url}/env/pixel.png"),
    Asset(7940010, "blankpurpl", f"{asset_url}/env/pixel.png"),
    Asset(7940011, "blankwhite", f"{asset_url}/env/pixel.png"),
    Asset(7940012, "Empty Tile", f"{asset_url}/env/pixel.png"),
    Asset(7940013, "open", f"{asset_url}/env/pixel.png"),
    Asset(7940014, "enemy", f"{asset_url}/env/pixel.png"),
    Asset(7940015, "penguin", f"{asset_url}/env/pixel.png"),
    Asset(7940016, "penguin_spawn_occupied", f"{asset_url}/env/pixel.png"),
    Asset(7940017, "penguin_spawn_unoccupied", f"{asset_url}/env/pixel.png"),
    Asset(7940018, "enemy_spawn_unoccupied", f"{asset_url}/env/pixel.png"),
    Asset(7940019, "enemy_spawn_occupied", f"{asset_url}/env/pixel.png"),
    Asset(7940020, "obstacle", f"{asset_url}/env/pixel.png"),
    Asset(8740001, "tusk_iciclesummon1_anim", f"{asset_url}/tusk_char_anim/tusk_iciclesummon1_anim_large.tpk"),
    Asset(8740002, "tusk_iciclesummon2_anim", f"{asset_url}/tusk_char_anim/tusk_iciclesummon2_anim_large.tpk"),
    Asset(8740003, "snowninja_igloodrop_anim1", f"{asset_url}/ninja_snow_char_anim/snowninja_igloodrop_anim1_large.tpk"),
    Asset(8740004, "snowninja_igloodrop_anim2", f"{asset_url}/ninja_snow_char_anim/snowninja_igloodrop_anim2_large.tpk"),
    Asset(8740005, "ui_card_member_snow", f"{asset_url}/hud/ui_card_member_large.tpk"),
    Asset(8740006, "ui_card_member_water", f"{asset_url}/hud/ui_card_member_large.tpk"),
    Asset(8740007, "ui_card_member_fire", f"{asset_url}/hud/ui_card_member_large.tpk"),
    Asset(8740008, "revivebeam_anim", f"{asset_url}/effects_anim/revivebeam_anim_large.tpk"),
    Asset(8740009, "fireninja_member_revive", f"{asset_url}/ninja_fire_char_anim/fireninja_member_revive_large.tpk"),
    Asset(8740010, "waterninja_member_revive", f"{asset_url}/ninja_water_char_anim/waterninja_member_revive_anim_large.tpk"),
    Asset(8740011, "snowninja_member_revive", f"{asset_url}/ninja_snow_char_anim/snowninja_member_revive_anim_large.tpk"),
])

Instance.sound_assets.update([
    Asset(1840002, "mus_mg_201303_cjsnow_gamewindamb", f"{sound_url}/mus_mg_201303_cjsnow_gamewindamb.mp3"),
    Asset(1840003, "sfx_mg_2013_cjsnow_snowmantankhit", f"{sound_url}/sfx_mg_2013_cjsnow_snowmantankhit.mp3"),
    Asset(1840004, "sfx_mg_2013_cjsnow_snowmanslyhit", f"{sound_url}/sfx_mg_2013_cjsnow_snowmanslyhit.mp3"),
    Asset(1840005, "sfx_mg_2013_cjsnow_snowmanscraphit", f"{sound_url}/sfx_mg_2013_cjsnow_snowmanscraphit.mp3"),
    Asset(1840006, "sfx_mg_2013_cjsnow_snowmandeathexplode", f"{sound_url}/sfx_mg_2013_cjsnow_snowmandeathexplode.mp3"),
    Asset(1840007, "sfx_mg_2013_cjsnow_penguinground", f"{sound_url}/sfx_mg_2013_cjsnow_penguininground.mp3"),
    Asset(1840008, "sfx_mg_2013_cjsnow_penguinhitsuccess", f"{sound_url}/sfx_mg_2013_cjsnow_penguinhitsuccess.mp3"),
    Asset(1840009, "sfx_mg_2013_cjsnow_snowmenappear", f"{sound_url}/sfx_mg_2013_cjsnow_snowmenappear.mp3"),
    Asset(1840010, "sfx_mg_2013_cjsnow_impactsly", f"{sound_url}/sfx_mg_2013_cjsnow_impactsly.mp3"),
    Asset(1840011, "sfx_mg_2013_cjsnow_impactscrap", f"{sound_url}/sfx_mg_2013_cjsnow_impactscrap.mp3"),
    Asset(1840012, "sfx_mg_2013_cjsnow_impactpowercardsnow", f"{sound_url}/sfx_mg_2013_cjsnow_impactpowercardsnow.mp3"),
    Asset(1840013, "sfx_mg_2013_cjsnow_footsteptank", f"{sound_url}/sfx_mg_2013_cjsnow_footsteptank.mp3"),
    Asset(1840014, "sfx_mg_2013_cjsnow_footstepsly_loop", f"{sound_url}/sfx_mg_2013_cjsnow_footstepsly_loop.mp3"),
    Asset(1840015, "sfx_mg_2013_cjsnow_footstepscrap_loop", f"{sound_url}/sfx_mg_2013_cjsnow_footstepscrap_loop.mp3"),
    Asset(1840016, "sfx_mg_2013_cjsnow_footsteppenguinfire", f"{sound_url}/sfx_mg_2013_cjsnow_footsteppenguinfire.mp3"),
    Asset(1840017, "sfx_mg_2013_cjsnow_footsteppenguin", f"{sound_url}/sfx_mg_2013_cjsnow_footsteppenguin.mp3"),
    Asset(1840018, "sfx_mg_2013_cjsnow_attackwater", f"{sound_url}/sfx_mg_2013_cjsnow_attackwater.mp3"),
    Asset(1840019, "sfx_mg_2013_cjsnow_attacktank", f"{sound_url}/sfx_mg_2013_cjsnow_attacktank.mp3"),
    Asset(1840020, "sfx_mg_2013_cjsnow_attacksnow", f"{sound_url}/sfx_mg_2013_cjsnow_attacksnow.mp3"),
    Asset(1840021, "sfx_mg_2013_cjsnow_attacksly", f"{sound_url}/sfx_mg_2013_cjsnow_attacksly.mp3"),
    Asset(1840022, "sfx_mg_2013_cjsnow_attackscrap", f"{sound_url}/sfx_mg_2013_cjsnow_attackscrap.mp3"),
    Asset(1840023, "sfx_mg_2013_cjsnow_attackpowercardwater", f"{sound_url}/sfx_mg_2013_cjsnow_attackpowercardwater.mp3"),
    Asset(1840024, "sfx_mg_2013_cjsnow_attackpowercardsnow", f"{sound_url}/sfx_mg_2013_cjsnow_attackpowercardsnow.mp3"),
    Asset(1840025, "sfx_mg_2013_cjsnow_attackpowercardfire", f"{sound_url}/sfx_mg_2013_cjsnow_attackpowercardfire.mp3"),
    Asset(1840026, "sfx_mg_2013_cjsnow_attackfire", f"{sound_url}/sfx_mg_2013_cjsnow_attackfire.mp3"),
    Asset(1840028, "sfx_mg_2013_cjsnow_tusklaugh", f"{sound_url}/sfx_mg_2013_cjsnow_tusklaugh.mp3"),
    Asset(1840029, "sfx_mg_2013_cjsnow_impactsenseisnow", f"{sound_url}/sfx_mg_2013_cjsnow_impactsenseisnow.mp3"),
    Asset(1840030, "sfx_mg_2013_cjsnow_hittusk", f"{sound_url}/sfx_mg_2013_cjsnow_hittusk.mp3"),
    Asset(1840031, "sfx_mg_2013_cjsnow_hitsensei", f"{sound_url}/sfx_mg_2013_cjsnow_hitsensei.mp3"),
    Asset(1840032, "sfx_mg_2013_cjsnow_attacktuskicicle02", f"{sound_url}/sfx_mg_2013_cjsnow_attacktuskicicle02.mp3"),
    Asset(1840033, "sfx_mg_2013_cjsnow_attacktuskicicle01", f"{sound_url}/sfx_mg_2013_cjsnow_attacktuskicicle01.mp3"),
    Asset(1840034, "sfx_mg_2013_cjsnow_attacktuskearthquake", f"{sound_url}/sfx_mg_2013_cjsnow_attacktuskearthquake.mp3"),
    Asset(1840035, "sfx_mg_2013_cjsnow_attacksenseiwater", f"{sound_url}/sfx_mg_2013_cjsnow_attacksenseiwater.mp3"),
    Asset(1840036, "sfx_mg_2013_cjsnow_attacksenseisnow", f"{sound_url}/sfx_mg_2013_cjsnow_attacksenseisnow.mp3"),
    Asset(1840037, "sfx_mg_2013_cjsnow_attacksenseifire", f"{sound_url}/sfx_mg_2013_cjsnow_attacksenseifire.mp3"),
    Asset(1840038, "sfx_mg_2013_cjsnow_uitargetselect", f"{sound_url}/sfx_mg_2013_cjsnow_uitargetselect.mp3"),
    Asset(1840039, "sfx_mg_2013_cjsnow_uitargetred", f"{sound_url}/sfx_mg_2013_cjsnow_uitargetred.mp3"),
    Asset(1840040, "sfx_mg_2013_cjsnow_uiselecttile", f"{sound_url}/sfx_mg_2013_cjsnow_uiselecttile.mp3"),
    Asset(1840041, "mus_mg_201303_cjsnow_tuskthemecaveamb", f"{sound_url}/mus_mg_201303_cjsnow_tuskthemecaveamb.mp3"),
    Asset(1840042, "SFX_MG_2013_CJSnow_UIPlayerReady_VBR8", f"{sound_url}/sfx_mg_2013_cjsnow_uiplayerready_vbr8.mp3"),
    Asset(1840043, "SFX_MG_CJSnow_PowercardReviveStart", f"{sound_url}/SFX_MG_CJSnow_PowercardReviveStart.mp3"),
    Asset(1840044, "SFX_MG_CJSnow_PowercardReviveEnd", f"{sound_url}/SFX_MG_CJSnow_PowercardReviveEnd.mp3"),
])
