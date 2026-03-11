from drawmenu import draw_menu
import asyncio
from terminal import myTool


async def main():
    draw_menu()
    tool = myTool()
    tool.cmdloop()

    

    

if __name__ == "__main__":
    asyncio.run(main())