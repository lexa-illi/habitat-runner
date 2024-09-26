namespace SpriteKind {
    export const info = SpriteKind.create()
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile1`, function (sprite, location) {
    controller.moveSprite(mySprite, 0, 0)
    pause(2000)
    mySprite.setPosition(43, 20)
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mySprite.vy == 0) {
        mySprite.vy = -150
    }
    if (Habitat == 0) {
        animation.runImageAnimation(
        mySprite,
        assets.animation`penguin jumping`,
        100,
        false
        )
    }
    if (Habitat == 1) {
    	
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`egg two`, function (sprite3, location3) {
    scene.setBackgroundImage(assets.image`Snowy Background`)
    tiles.setCurrentTilemap(tilemap`level1`)
    mySprite.setPosition(43, 20)
    level += 1
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`egg 3`, function (sprite2, location2) {
    scene.setBackgroundImage(assets.image`Snowy Background`)
    tiles.setCurrentTilemap(tilemap`level1`)
    mySprite.setPosition(43, 20)
    level += 1
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Habitat == 0) {
        animation.runImageAnimation(
        mySprite,
        assets.animation`penguin sliding left`,
        100,
        false
        )
    }
    if (Habitat == 1) {
        animation.runImageAnimation(
        mySprite,
        assets.animation`penguin sliding left`,
        100,
        false
        )
    }
})
controller.right.onEvent(ControllerButtonEvent.Released, function () {
    if (Habitat == 0) {
        animation.runImageAnimation(
        mySprite,
        assets.animation`penguin standing right`,
        75,
        false
        )
    }
    if (Habitat == 1) {
    	
    }
})
controller.left.onEvent(ControllerButtonEvent.Released, function () {
    if (Habitat == 0) {
        animation.runImageAnimation(
        mySprite,
        assets.animation`penguin standing left`,
        75,
        false
        )
    }
    if (Habitat == 1) {
    	
    }
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Habitat == 0) {
        animation.runImageAnimation(
        mySprite,
        assets.animation`penguin sliding right`,
        100,
        false
        )
    }
    if (level == 1) {
    	
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`Egg one`, function (sprite4, location4) {
    scene.setBackgroundImage(assets.image`Snowy Background`)
    tiles.setCurrentTilemap(tilemap`level1`)
    mySprite.setPosition(116, 20)
    level += 1
})
let level = 0
let Habitat = 0
let mySprite: Sprite = null
game.splash("Habitat Runner")
game.splash("Use the left and right arrow keys to move")
game.splash("Coins can be used to buy items")
game.splash("When in the store, use the A button to choose which item to buy and the B button to buy that item.")
game.splash("Use the up arrow key to jump and the A button to use your item")
scene.setBackgroundImage(assets.image`Snowy Background`)
tiles.setCurrentTilemap(tilemap`level1`)
mySprite = sprites.create(assets.image`Penguin still`, SpriteKind.Player)
controller.moveSprite(mySprite, 100, 0)
scene.cameraFollowSprite(mySprite)
mySprite.setPosition(43, 20)
let stats = sprites.create(assets.image`stats`, SpriteKind.info)
stats.setPosition(80, 10)
mySprite.ay = 300
forever(function () {
	
})
