"""CLI interface for hiddify_support_bot project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""
import asyncio
from . import utils
from . import basebot
def main():  # pragma: no cover
    from dotenv import load_dotenv
    load_dotenv()

    utils.setup_translation()
    # import i18n
    # print(i18n.t("start",locale='fa'))
    import sys
    if 1 or hasattr(sys, 'gettrace') and sys.gettrace() is not None: #is debug mode
        asyncio.run(basebot.bot.polling())      
    else:
        try:
            asyncio.run(basebot.bot.polling(restart_on_change=True))  
        except:
            asyncio.run(basebot.bot.polling())  
    