#!/usr/bin/env python3
"""
Dungeon Crawler (single-file)
Features:
- Procedural dungeon map (rooms + corridors)
- Player with HP, attack, defense, XP, level
- Monsters with simple AI (move randomly; attack when adjacent)
- Items: healing potions, weapons, armor, XP scroll
- Inventory, equipping weapon/armor, using consumables
- Fog of war (limited sight)
- Turn-based loop
- Simple, readable code with comments
"""

import random
import os
import sys
import math
from dataclasses import dataclass, field
from typing import List, Tuple, Optional

# === Config ===
MAP_WIDTH = 40
MAP_HEIGHT = 20
ROOM_MIN_SIZE = 4
ROOM_MAX_SIZE = 8
MAX_ROOMS = 8
SIGHT_RADIUS = 6

MAX_MONSTERS = 10
MAX_ITEMS = 10
STARTING_POTIONS = 2

# === Data classes ===
@dataclass
class Actor:
    x: int
    y: int
    char: str
    name: str
    max_hp: int
    hp: int
    attack: int
    defense: int
    xp_reward: int = 0

    def is_alive(self):
        return self.hp > 0

@dataclass
class Item:
    x: int
    y: int
    char: str
    name: str
    kind: str  # 'potion', 'weapon', 'armor', 'scroll'
    power: int

@dataclass
class Player:
    x: int
    y: int
    char: str = '@'
    name: str = 'Hero'
    max_hp: int = 30
    hp: int = 30
    base_attack: int = 5
    base_defense: int = 2
    level: int = 1
    xp: int = 0
    xp_to_next: int = 20
    inventory: List[Item] = field(default_factory=list)
    weapon: Optional[Item] = None
    armor: Optional[Item] = None

    def attack_value(self):
        return self.base_attack + (self.weapon.power if self.weapon else 0)

    def defense_value(self):
        return self.base_defense + (self.armor.power if self.armor else 0)

    def is_alive(self):
        return self.hp > 0

    def add_xp(self, amount):
        self.xp += amount
        leveled = False
        while self.xp >= self.xp_to_next:
            self.xp -= self.xp_to_next
            self.level_up()
            leveled = True
        return leveled

    def level_up(self):
        self.level += 1
        self.max_hp += 6
        self.hp = self.max_hp
        self.base_attack += 1
        self.base_defense += 1
        self.xp_to_next = int(self.xp_to_next * 1.5)
        print(f"\n>>> You leveled up! Now level {self.level}. HP restored.")

# === Utility / Map generation ===

class Rect:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

    def center(self):
        return ( (self.x1 + self.x2)//2, (self.y1 + self.y2)//2 )

    def intersect(self, other:'Rect'):
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)

def make_map():
    # Start with all walls
    dungeon = [['#' for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
    rooms: List[Rect] = []
    for _ in range(MAX_ROOMS):
        w = random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        h = random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        x = random.randint(1, MAP_WIDTH - w - 2)
        y = random.randint(1, MAP_HEIGHT - h - 2)
        new_room = Rect(x,y,w,h)
        if any(new_room.intersect(other) for other in rooms):
            continue
        create_room(dungeon, new_room)
        if rooms:
            # connect to previous room center
            (prev_x, prev_y) = rooms[-1].center()
            (new_x, new_y) = new_room.center()
            if random.choice([True, False]):
                create_h_tunnel(dungeon, prev_x, new_x, prev_y)
                create_v_tunnel(dungeon, prev_y, new_y, new_x)
            else:
                create_v_tunnel(dungeon, prev_y, new_y, prev_x)
                create_h_tunnel(dungeon, prev_x, new_x, new_y)
        rooms.append(new_room)
    return dungeon, rooms

def create_room(dungeon, room:Rect):
    for y in range(room.y1, room.y2):
        for x in range(room.x1, room.x2):
            dungeon[y][x] = '.'

def create_h_tunnel(dungeon, x1, x2, y):
    for x in range(min(x1,x2), max(x1,x2)+1):
        dungeon[y][x] = '.'

def create_v_tunnel(dungeon, y1, y2, x):
    for y in range(min(y1,y2), max(y1,y2)+1):
        dungeon[y][x] = '.'

# === Game logic ===

def place_player(rooms) -> Tuple[int,int]:
    center = rooms[0].center()
    return center

def random_empty_in_room(room:Rect, dungeon, actors, items):
    for _ in range(50):
        x = random.randint(room.x1+1, room.x2-1)
        y = random.randint(room.y1+1, room.y2-1)
        if dungeon[y][x] == '.' and not any(a.x==x and a.y==y for a in actors) and not any(i.x==x and i.y==y for i in items):
            return x, y
    return None

def spawn_monsters_and_items(rooms, dungeon, player) -> Tuple[List[Actor], List[Item]]:
    monsters: List[Actor] = []
    items: List[Item] = []
    for room in rooms[1:]:
        # spawn a random number of monsters in the room
        num_mon = random.randint(0, 2)
        for _ in range(num_mon):
            pos = random_empty_in_room(room, dungeon, monsters + [player], items)
            if not pos: continue
            x, y = pos
            if random.random() < 0.6:
                m = Actor(x,y,'g','Goblin', max_hp:=8, hp:=8, attack:=3, defense:=0, xp_reward:=8)
            else:
                m = Actor(x,y,'o','Orc', max_hp:=100, hp:=100, attack:=5, defense:=1, xp_reward:=15)
            monsters.append(m)

        # spawn items
        if random.random() < 0.7 and len(items) < MAX_ITEMS:
            pos = random_empty_in_room(room, dungeon, monsters + [player], items)
            if not pos: continue
            x,y = pos
            roll = random.random()
            if roll < 0.4:
                items.append(Item(x,y,'!','Healing Potion','potion', power:=10))
            elif roll < 0.7:
                items.append(Item(x,y,')','Short Sword','weapon', power:=2))
            else:
                items.append(Item(x,y,'[','Leather Armor','armor', power:=1))
    # add some starter potions near entrance
    for _ in range(STARTING_POTIONS):
        items.append(Item(player.x + random.randint(-1,1), player.y + random.randint(-1,1), '!', 'Healing Potion', 'potion', 10))
    return monsters, items

def distance(a_x, a_y, b_x, b_y):
    return math.hypot(a_x-b_x, a_y-b_y)

def is_blocked(x,y, dungeon, monsters, player):
    if x < 0 or y < 0 or x >= MAP_WIDTH or y >= MAP_HEIGHT: return True
    if dungeon[y][x] == '#': return True
    if any(m.x==x and m.y==y and m.is_alive() for m in monsters): return True
    if player.x == x and player.y == y: return True
    return False

def draw(dungeon, player:Player, monsters:List[Actor], items:List[Item], message_log:List[str]):
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    # Draw map with fog of war
    top_lines = []
    for y in range(MAP_HEIGHT):
        line = ''
        for x in range(MAP_WIDTH):
            if distance(x,y,player.x,player.y) <= SIGHT_RADIUS:
                ch = dungeon[y][x]
                # check for item
                it = next((it for it in items if it.x==x and it.y==y), None)
                if player.x==x and player.y==y:
                    line += player.char
                elif any(m.x==x and m.y==y and m.is_alive() for m in monsters):
                    m = next(m for m in monsters if m.x==x and m.y==y and m.is_alive())
                    line += m.char
                elif it:
                    line += it.char
                else:
                    line += ch
            else:
                line += ' '
        top_lines.append(line)
    # Show top area
    for l in top_lines:
        print(l)
    # Stats & Inventory summary
    print("-" * MAP_WIDTH)
    wname = player.weapon.name if player.weapon else "None"
    aname = player.armor.name if player.armor else "None"
    print(f"{player.name}  HP: {player.hp}/{player.max_hp}  Level: {player.level}  XP: {player.xp}/{player.xp_to_next}")
    print(f"Attack: {player.attack_value()}  Defense: {player.defense_value()}  Weapon: {wname}  Armor: {aname}")
    # Nearby items/monsters quick info
    nearby = [m for m in monsters if distance(m.x,m.y,player.x,player.y) <= SIGHT_RADIUS and m.is_alive()]
    if nearby:
        print("Nearby monsters: " + ", ".join(f"{m.name}({m.hp})@({m.x},{m.y})" for m in nearby))
    else:
        print("No monsters in sight.")
    if items:
        visible_items = [i for i in items if distance(i.x,i.y,player.x,player.y) <= SIGHT_RADIUS]
        if visible_items:
            print("Visible items: " + ", ".join(f"{it.name}@({it.x},{it.y})" for it in visible_items))
    print("-" * MAP_WIDTH)
    # Message log (last 5)
    for msg in message_log[-5:]:
        print(msg)
    print("-" * MAP_WIDTH)
    print("Controls: WASD to move, i Inventory, h Help, q Quit")
    print("-" * MAP_WIDTH)

def move_player(dx, dy, dungeon, player:Player, monsters:List[Actor], items:List[Item], message_log:List[str]):
    new_x = player.x + dx
    new_y = player.y + dy
    # bounds & wall
    if new_x < 0 or new_y < 0 or new_x >= MAP_WIDTH or new_y >= MAP_HEIGHT:
        message_log.append("You cannot move there.")
        return
    if dungeon[new_y][new_x] == '#':
        message_log.append("A wall blocks your way.")
        return
    # is there a monster -> attack
    target = next((m for m in monsters if m.x==new_x and m.y==new_y and m.is_alive()), None)
    if target:
        combat(player, target, message_log)
        return
    # otherwise move
    player.x = new_x
    player.y = new_y
    # check for items to pick up
    item = next((it for it in items if it.x==player.x and it.y==player.y), None)
    if item:
        player.inventory.append(item)
        items.remove(item)
        message_log.append(f"You picked up: {item.name} ({item.kind}).")

def combat(attacker:Player, defender:Actor or Player, message_log:List[str]):
    # attacker might be Player or Actor; handle both
    if isinstance(attacker, Player):
        atk_value = attacker.attack_value()
    else:
        atk_value = attacker.attack

    if isinstance(defender, Player):
        def_value = defender.defense_value()
    else:
        def_value = defender.defense

    damage = max(0, atk_value - def_value + random.randint(-1,2))
    # small variance
    if damage <= 0:
        message = f"{attacker.name} attacks {defender.name} but does no damage."
    else:
        defender.hp -= damage
        message = f"{attacker.name} hits {defender.name} for {damage} damage."
    message_log.append(message)
    # death handling for monsters
    if isinstance(defender, Actor) and defender.hp <= 0:
        message_log.append(f"{defender.name} dies! You gain {defender.xp_reward} XP.")
        attacker.add_xp(defender.xp_reward)
    # death handling for player
    if isinstance(defender, Player) and defender.hp <= 0:
        message_log.append("You have been slain...")

def monsters_take_turn(monsters:List[Actor], dungeon, player:Player, message_log:List[str]):
    for m in monsters:
        if not m.is_alive(): continue
        # if adjacent to player -> attack
        if abs(m.x - player.x) + abs(m.y - player.y) == 1:
            combat(m, player, message_log)
            if not player.is_alive():
                return
            continue
        # if player in sight radius, move toward player occasionally
        if distance(m.x,m.y,player.x,player.y) <= SIGHT_RADIUS and random.random() < 0.6:
            dx = 1 if player.x > m.x else -1 if player.x < m.x else 0
            dy = 1 if player.y > m.y else -1 if player.y < m.y else 0
            # try horizontal first then vertical
            if not is_blocked(m.x+dx, m.y, dungeon, monsters, player):
                m.x += dx
            elif not is_blocked(m.x, m.y+dy, dungeon, monsters, player):
                m.y += dy
            else:
                # stuck, random step
                rx, ry = random.choice([(1,0),(-1,0),(0,1),(0,-1)])
                if not is_blocked(m.x+rx, m.y+ry, dungeon, monsters, player):
                    m.x += rx
                    m.y += ry
        else:
            # random wander
            if random.random() < 0.3:
                rx, ry = random.choice([(1,0),(-1,0),(0,1),(0,-1)])
                if not is_blocked(m.x+rx, m.y+ry, dungeon, monsters, player):
                    m.x += rx
                    m.y += ry

def open_inventory(player:Player, message_log:List[str]):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Inventory:")
        if not player.inventory:
            print("(empty)")
        else:
            for idx, it in enumerate(player.inventory):
                print(f"{idx+1}. {it.name} - {it.kind} (power {it.power})")
        print("-" * 40)
        print("Equipped -> Weapon:", player.weapon.name if player.weapon else "None",
              "  Armor:", player.armor.name if player.armor else "None")
        print("Choices: u<number> use, e<number> equip, d<number> drop, b back")
        choice = input("Inventory> ").strip().lower()
        if choice == 'b' or choice == '':
            return
        if len(choice) < 2:
            continue
        cmd, rest = choice[0], choice[1:]
        if not rest.isdigit():
            continue
        idx = int(rest)-1
        if idx < 0 or idx >= len(player.inventory):
            print("Invalid index.")
            input("Press Enter...")
            continue
        item = player.inventory[idx]
        if cmd == 'u':
            if item.kind == 'potion':
                heal = item.power
                player.hp = min(player.max_hp, player.hp + heal)
                message_log.append(f"You use {item.name} and heal {heal} HP.")
                player.inventory.pop(idx)
            elif item.kind == 'scroll':
                xpgain = item.power
                player.add_xp(xpgain)
                message_log.append(f"You read {item.name} and gain {xpgain} XP.")
                player.inventory.pop(idx)
            else:
                message_log.append("You cannot 'use' that item. Try equip (e).")
        elif cmd == 'e':
            if item.kind == 'weapon':
                player.weapon = item
                message_log.append(f"You equip {item.name} as weapon.")
                player.inventory.pop(idx)
            elif item.kind == 'armor':
                player.armor = item
                message_log.append(f"You equip {item.name} as armor.")
                player.inventory.pop(idx)
            else:
                message_log.append("You cannot equip that.")
        elif cmd == 'd':
            # drop item on current tile
            item.x = player.x
            item.y = player.y
            player.inventory.pop(idx)
            message_log.append(f"You dropped {item.name}.")
        input("Press Enter...")

def try_pick_item(player:Player, items:List[Item], message_log:List[str]):
    item = next((it for it in items if it.x==player.x and it.y==player.y), None)
    if item:
        player.inventory.append(item)
        items.remove(item)
        message_log.append(f"You pick up: {item.name}.")

def show_help():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Help / Controls ===")
    print("w/a/s/d : Move (up/left/down/right)")
    print("i : Open inventory (use/equip/drop items)")
    print("h : Show help")
    print("q : Quit the game")
    print()
    print("Pick up items by walking on them.")
    print("Fight monsters by moving into them.")
    print("Gain XP to level up and improve stats.")
    input("\nPress Enter to continue...")

# === Main game loop ===

def main():
    random.seed()  # could be seeded for reproducibility
    dungeon, rooms = make_map()
    px, py = place_player(rooms)
    player = Player(px, py)
    monsters, items = spawn_monsters_and_items(rooms, dungeon, player)
    message_log = ["Welcome to the Dungeon! Find treasure, defeat monsters, and level up."]
    turn_count = 0

    # place some random scrolls/weapons scattered
    for _ in range(2):
        r = random.choice(rooms[1:])
        pos = random_empty_in_room(r, dungeon, monsters + [player], items)
        if pos:
            x,y = pos
            items.append(Item(x,y,'?','Scroll of Knowledge','scroll', power:=15))
    for _ in range(2):
        r = random.choice(rooms[1:])
        pos = random_empty_in_room(r, dungeon, monsters + [player], items)
        if pos:
            x,y = pos
            items.append(Item(x,y,')','Rusty Dagger','weapon', power:=1))

    # game loop
    while True:
        draw(dungeon, player, monsters, items, message_log)
        if not player.is_alive():
            print("\n*** YOU DIED. GAME OVER ***")
            return
        # Victory condition? For this simple game, survive many turns or kill all monsters
        alive_monsters = [m for m in monsters if m.is_alive()]
        if not alive_monsters:
            print("\n*** All monsters defeated! You win! ***")
            return

        cmd = input("Action> ").strip().lower()
        turn_count += 1
        if cmd == '':
            # skip
            pass
        elif cmd in ('w','a','s','d'):
            mapping = {'w':(0,-1),'s':(0,1),'a':(-1,0),'d':(1,0)}
            dx,dy = mapping[cmd]
            move_player(dx,dy,dungeon,player,monsters,items,message_log)
            # After player's move, try pick up automatically
            try_pick_item(player, items, message_log)
            # monsters move/attack
            monsters_take_turn(monsters, dungeon, player, message_log)
        elif cmd == 'i':
            open_inventory(player, message_log)
        elif cmd == 'h':
            show_help()
        elif cmd == 'q':
            print("Quitting. Goodbye.")
            return
        else:
            message_log.append("Unknown command. Press h for help.")
        # small world events: sometimes spawn a wandering monster
        if random.random() < 0.01 and len(monsters) < MAX_MONSTERS+5:
            # find a floor tile to spawn
            tries = 0
            while tries < 50:
                rx = random.randint(0, MAP_WIDTH-1)
                ry = random.randint(0, MAP_HEIGHT-1)
                if dungeon[ry][rx]=='.' and distance(rx,ry,player.x,player.y) > 3 and not any(m.x==rx and m.y==ry for m in monsters):
                    monsters.append(Actor(rx,ry,'w','Wanderer', 12,12,4,0,10))
                    message_log.append("You hear distant footsteps...")
                    break
                tries += 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye!")
