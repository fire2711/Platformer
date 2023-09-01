# Platformer
Description: This describes the thought process behind my CS50 Final Project and the difficulties that I went through. What my project is and the process I went through in order to
My Project
My project is a simple platforming game where you play as a small slime stuck at the bottom of a dungeon or well and the aim is the get to the top and escape. In order to move left and right the arrow keys are used and to jump space is used. There is collision between the blocks ensuring that the character sprite will not clip through the edges. Once the slime reaches the top, it displays, "You Win!" onto the screen.

Files
I have two main files for the program. One file is where all of the code and functions go that run the program/game, while the other file is where the level data is located. They are called platformer1.py and settings.py respectively.

Platformer1.py
For platofrmer1.py inside of the file it includes code that creates the sprites and images that make up the level and the character, the collision detecting, the movement of the character, and the conditions for winning.

There are multiple classes within this program with functions inside. Each one has a specific purpose whether to control the player, display the level, or make the buttons seen usable.

The update function updates the player so that they are able to move around and collide with the blocks that are making up the level. The create function creates the level, and so on.

Settings.py
In settings.py it is an array illustrating the design of the level where the 1s are the blocks and 0s are air.

Troubles
I initially could not decide how I wanted the program to run. I could not decide whether or not I wanted the level to scroll or be static. I eventually decided on having it static due to the fact that I was unable to get the screen to scroll correctly to the right. I also debated whether or not to put the functions and classes into other files therefore abstracting them. I decided not to as I was a little unclear on how I would import those files into the main program and so in order to make it easier on myself I put it all into one program where I could easily see if there was a problem occurring. I also had trouble creating the main menu screen as I could not figure out how to make that the starting screen to begin and how to make the buttons on that screen interactable.

Why I Made This Project
I initially wanted to make a type of program that was like an aim trainer but I felt that doing so was too simple. As a result, I decided to make a type of game and decided on a platformer due to being inspired by the game CELESTE. I had always wanted to make something similar to a game and this allowed me to be able to do so.

Improvement
Adding enemies/dangers
Adding a reset button
Adding animations or other levels
Ability to create your own levels
How to run
1. Ensure that pygame is downloaded
2. Clone the code
3. Run the platformer1.py program
4. All Set!
