# 2D Shooting Game
Right now this is a simple demo. We can refine it after finishing the basics.

## Overview
The prototype of this game:
* player controls a ship that appears at the bottom center of the screen.
* ship can move horizontally, controled by left and right arrow key (may add vertical movement in the future)
* ship can launch projectiles by pressing spacebar
* enemies appear at the top of the screen, they will:
  * shoot projectiles toward player's ship 
  * move downward at various speed
* player will lose one ship if following condition is true. Player has 3 ships.
  * player's ship was hit by enemy's projectile
  * enemy reached bottom
* if player shoots all enemies, a new wave of enemy will respawn. They should move faster toward the bottom and harder to kill.

Current Progress:
