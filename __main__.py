import os

from bot import Pangu

if __name__ == "__main__":
    if os.name != "nt":
        import uvloop
        uvloop.install()


    bot = Pangu()

    bot.run()



