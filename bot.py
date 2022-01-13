#!/usr/bin/env python3
# -*- coding: utf-8 -*-  #pip直接下载会比较慢，用镜像源会快很多

import nonebot
from nonebot.adapters.cqhttp import Bot as CQHTTPBot
import config

# Custom your logger
# 
# from nonebot.log import logger, default_format
# logger.add("error.log",
#            rotation="00:00",
#            diagnose=False,
#            level="ERROR",
#            format=default_format)

# You can pass some keyword args config to init function
nonebot.init()  # 初始化
nonebot.load_plugins("src/plugins")  # 加载插件

driver = nonebot.get_driver()

driver.register_adapter("cqhttp", CQHTTPBot)

nonebot.load_builtin_plugins()

app = nonebot.get_asgi()

# nonebot.load_from_toml("pyproject.toml")

# Modify some config / config depends on loaded configs
# 
# config = driver.config
# do something...


if __name__ == "__main__":
    nonebot.logger.warning("Always use `nb run` to start the bot instead of manually running!")
    nonebot.run(app="__mp_main__:app")
