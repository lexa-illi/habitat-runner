@namespace
class SpriteKind:
    info = SpriteKind.create()

def on_overlap_tile(sprite, location):
    controller.move_sprite(mySprite, 0, 0)
    pause(2000)
    mySprite.set_position(43, 20)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile1
    """),
    on_overlap_tile)

def on_up_pressed():
    if mySprite.vy == 0:
        mySprite.vy = -150
    if Habitat == 0:
        animation.run_image_animation(mySprite,
            assets.animation("""
                penguin jumping
            """),
            100,
            False)
    if Habitat == 1:
        pass
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile2(sprite3, location3):
    global level
    scene.set_background_image(assets.image("""
        Snowy Background
    """))
    tiles.set_current_tilemap(tilemap("""
        level1
    """))
    mySprite.set_position(43, 20)
    level += 1
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        egg two
    """),
    on_overlap_tile2)

def on_overlap_tile3(sprite2, location2):
    global level
    scene.set_background_image(assets.image("""
        Snowy Background
    """))
    tiles.set_current_tilemap(tilemap("""
        level1
    """))
    mySprite.set_position(43, 20)
    level += 1
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        egg 3
    """),
    on_overlap_tile3)

def on_left_pressed():
    if Habitat == 0:
        animation.run_image_animation(mySprite,
            assets.animation("""
                penguin sliding left
            """),
            100,
            False)
    if Habitat == 1:
        animation.run_image_animation(mySprite,
            assets.animation("""
                penguin sliding left
            """),
            100,
            False)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_released():
    if Habitat == 0:
        animation.run_image_animation(mySprite,
            assets.animation("""
                penguin standing right
            """),
            75,
            False)
    if Habitat == 1:
        pass
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    if Habitat == 0:
        animation.run_image_animation(mySprite,
            assets.animation("""
                penguin standing left
            """),
            75,
            False)
    if Habitat == 1:
        pass
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_right_pressed():
    if Habitat == 0:
        animation.run_image_animation(mySprite,
            assets.animation("""
                penguin sliding right
            """),
            100,
            False)
    if level == 1:
        pass
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_overlap_tile4(sprite4, location4):
    global level
    scene.set_background_image(assets.image("""
        Snowy Background
    """))
    tiles.set_current_tilemap(tilemap("""
        level1
    """))
    mySprite.set_position(116, 20)
    level += 1
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        Egg one
    """),
    on_overlap_tile4)

level = 0
Habitat = 0
mySprite: Sprite = None
game.splash("Habitat Runner")
game.splash("Use the left and right arrow keys to move")
game.splash("Coins can be used to buy items")
game.splash("When in the store, use the A button to choose which item to buy and the B button to buy that item.")
game.splash("Use the up arrow key to jump and the A button to use your item")
scene.set_background_image(assets.image("""
    Snowy Background
"""))
tiles.set_current_tilemap(tilemap("""
    level1
"""))
mySprite = sprites.create(assets.image("""
    Penguin still
"""), SpriteKind.player)
controller.move_sprite(mySprite, 100, 0)
scene.camera_follow_sprite(mySprite)
mySprite.set_position(43, 20)
stats = sprites.create(assets.image("""
    stats
"""), SpriteKind.info)
stats.set_position(80, 10)
mySprite.ay = 300

def on_forever():
    pass
forever(on_forever)
