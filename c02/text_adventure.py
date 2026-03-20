# 文件: text_adventure_framework.py
# 说明：一个基于模式匹配的文字冒险游戏核心逻辑框架

# 导入必要的库
from dataclasses import dataclass
from typing import List, Optional
import sys

# ========== 数据模型定义 (Data Models) ==========
@dataclass
class Room:
    """房间类"""
    name: str
    description: str
    exits: dict  # 键为方向，值为目标房间对象
    items: List[str]

@dataclass
class Character:
    """角色类"""
    name: str
    inventory: List[str]
    location: Room

@dataclass
class GameEvent:
    """游戏事件基类 (用于图形界面扩展)"""
    pass

@dataclass
class KeyPress(GameEvent):
    key_name: str

@dataclass
class Click(GameEvent):
    position: tuple
    button: str  # 例如 "LEFT", "RIGHT"

@dataclass
class QuitEvent(GameEvent):
    pass

# ========== 核心游戏状态 (Core Game State) ==========
current_room: Room = None
player: Character = None
game_running: bool = True

# ========== 游戏命令处理函数 (Command Handlers) ==========
def handle_look() -> None:
    """处理‘look’命令"""
    print(f"[{current_room.name}]: {current_room.description}")
    if current_room.items:
        print(f"你看到这里有: {', '.join(current_room.items)}")
    if current_room.exits:
        print(f"出口: {', '.join(current_room.exits.keys())}")

def handle_get(item: str) -> None:
    """处理‘get <物品>’命令"""
    if item in current_room.items:
        current_room.items.remove(item)
        player.inventory.append(item)
        print(f"你捡起了{item}。")
    else:
        print(f"这里没有{item}。")

def handle_drop(*items: str) -> None:
    """处理‘drop <物品1> <物品2>...’命令"""
    for item in items:
        if item in player.inventory:
            player.inventory.remove(item)
            current_room.items.append(item)
            print(f"你丢下了{item}。")
        else:
            print(f"你的背包里没有{item}。")

def handle_go(direction: str) -> None:
    """处理‘go <方向>’ 或 ‘<方向>’命令"""
    global current_room
    if direction in current_room.exits:
        current_room = current_room.exits[direction]
        print(f"你向{direction}走去。")
        handle_look()  # 进入新房间后自动查看
    else:
        print(f"抱歉，你不能往{direction}走。")

def handle_inventory() -> None:
    """处理‘inventory’或‘i’命令"""
    if player.inventory:
        print(f"你的背包里有: {', '.join(player.inventory)}")
    else:
        print("你的背包空空如也。")

def handle_quit() -> None:
    """处理‘quit’命令"""
    global game_running
    print("再见！")
    game_running = False

def handle_help() -> None:
    """处理‘help’命令"""
    help_text = """
    可用命令:
        look / l          - 查看当前房间
        go <方向>         - 向指定方向移动 (如: go north, east)
        <方向>            - 移动的快捷方式 (如: north, south)
        get <物品>        - 捡起物品
        drop <物品>...    - 丢弃一个或多个物品
        inventory / i     - 查看背包
        help             - 显示此帮助信息
        quit             - 退出游戏
    """
    print(help_text)

# ========== 主命令解析与匹配循环 (Main Parser & Match Loop) ==========
def process_command(command_input: str) -> None:
    """
    使用模式匹配解析和处理用户输入的命令。
    这是整个游戏逻辑的核心。
    """
    tokens = command_input.strip().lower().split()

    match tokens:
        # 1. 无参数命令 (单元素序列匹配)
        case ["look"] | ["l"]:
            handle_look()
        case ["inventory"] | ["i"]:
            handle_inventory()
        case ["quit"] | ["exit"]:
            handle_quit()
        case ["help"]:
            handle_help()

        # 2. 方向移动命令 (使用或模式和as模式)
        case ["go", ("north" | "south" | "east" | "west") as direction]:
            handle_go(direction)
        case [("north" | "south" | "east" | "west" | "up" | "down") as direction]:
            # 允许直接输入方向词
            handle_go(direction)

        # 3. 带一个参数的命令
        case ["get", obj]:
            handle_get(obj)
        case ["examine", obj] | ["x", obj]:
            # 示例：可以扩展“检查物品”的功能
            print(f"你仔细检查了{obj}，没发现什么特别的。")

        # 4. 带可变数量参数的命令 (使用*rest)
        case ["drop", *items] if len(items) > 0:
            handle_drop(*items)

        # 5. 使用守卫 (Guard) 进行条件判断
        case ["use", item, "on", target] if item in player.inventory:
            # 示例：使用物品，需在背包中
            print(f"你对{target}使用了{item}。")
        case ["use", item, "on", _]:
            print(f"你没有{item}。")

        # 6. 处理来自客户端/UI的JSON消息 (映射模式示例)
        # 假设 `action` 是一个从JSON解析出来的字典
        # 此部分展示如何集成到网络版游戏中
        # case {"type": "command", "text": str(cmd_text)}:
        #     process_command(cmd_text)  # 递归处理命令文本
        # case {"type": "notification", "message": str(msg), "color": str(color)}:
        #     print(f"[{color}消息] {msg}")

        # 7. 处理图形界面事件 (类模式示例)
        # 假设 `event` 是一个事件对象
        # case KeyPress(key_name="Q") | QuitEvent():
        #     handle_quit()
        # case Click(position=(x, y), button="LEFT"):
        #     handle_click_at(x, y)
        # case KeyPress(key_name="up arrow"):
        #     handle_go("north")

        # 8. 默认/未识别命令
        case []:
            # 用户输入了空行
            pass
        case _:
            # 通配符模式，匹配所有其他情况
            print(f"我不理解‘{command_input}’。输入‘help’查看帮助。")

# ========== 游戏初始化和主循环 (Initialization & Main Loop) ==========
def init_game() -> None:
    """初始化游戏世界和角色状态"""
    global current_room, player

    # 创建房间
    hall = Room("大厅", "你站在一个古老城堡的入口大厅。", {}, ["火把"])
    library = Room("图书馆", "四周是直达天花板的书架，布满了灰尘。", {}, ["古书", "羽毛笔"])
    garden = Room("花园", "一个荒废的花园，中央有一口枯井。", {}, ["玫瑰"])

    # 设置房间连接
    hall.exits = {"north": library, "east": garden}
    library.exits = {"south": hall}
    garden.exits = {"west": hall}

    # 初始化玩家
    current_room = hall
    player = Character("冒险者", ["小刀", "绳子"], hall)

    print("=== 文字冒险游戏 ===")
    print("输入 'help' 获取命令列表。")
    handle_look()

def main_game_loop() -> None:
    """游戏主循环"""
    init_game()
    while game_running:
        try:
            user_input = input("\n> ")
            process_command(user_input)
        except (EOFError, KeyboardInterrupt):
            # 处理 Ctrl+C 或 Ctrl+D
            print("\n游戏被中断。")
            handle_quit()
            break

# ========== 程序入口 ==========
if __name__ == "__main__":
    main_game_loop()

# 文件结束