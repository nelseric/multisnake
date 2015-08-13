# Multisnake
A muliplayer Snake game

Snakes will move around in Rooms.  
Rooms will randomly have one to four Doors on its the edges.  
Door widths can be random

When a Snake enters a Door completely, it will be transported to a different room.  
The room the Snake enters will have at least one other Snake in it  
A Snake is considered in the room until every segment has left through the Door  
A Snake spawns in a new room from a Door, one segment at a time, initially moving directly away from the Door  
A Snake can leave a room while it is still entering

A Snake will always move in one of four directions north, east, south, west  
A Snake will always once one space per ticka

A new Snake will spawn in a new room.
Food will not be generated unless there are two Snakes in a Cell

If a Snake bites another Snake, it dies
If a Snake bites itself it dies

When a Snake eats a food, it grows one new segment
Segments will have different colors to show movement

The longest snake is winning
The longest ever snake has the highest score

## Server Tick Steps
1. Send Game State
2. Listen player commands
3. Wait tick length
4. Calculate Movement
5. Calculate Collisions
6. Repeat

## Client
1. Listen for game State
    * Update game state
    * Redraw room
2. Listen for input
    * Send new directions for next tick

## Installation
This is a standalone application so you should execute:

    $ pip install multisnake
### From Git
    $ git clone git@github.com:nelseric/multisnake.git
    $ cd multisnake && ./setup.py install

## Usage
### Server
    $ multisnake server [-t 200] [-l 0.0.0.0] [-p 42000]
      Options:
        --tick   [-t] : Sets the tick length in seconds, or how fast players move
        --listen [-l] : Sets the servers listening address
        --port   [-p] : Sets the server's port
### Client
    $ multisnake client <host> <port>
