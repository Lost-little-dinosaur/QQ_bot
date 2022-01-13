import nonebot
from nonebot import export, require
from nonebot.adapters.cqhttp import Bot, Event
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.adapters.cqhttp.permission import GROUP_ADMIN, GROUP_OWNER, PRIVATE
from nonebot.permission import SUPERUSER
from nonebot.plugin import on_command

from .check import weather_report, change_schedule, check_report

export = export()
export.name = '天气预报'
export.usage = '''暂无教程'''

scheduler = require('nonebot_plugin_apscheduler').scheduler


@scheduler.scheduled_job('cron', hour='19', id='weather_report')
async def scheduled_job_handle():
    bot = list(nonebot.get_bots().values())[0]
    info = weather_report()
    for i in info:
        id_key = i[0]
        id_value = i[1]
        message = i[2]
        await bot.call_api('send_msg', **{
            id_key: id_value,
            'message': message
        })


weather_change_schedule = on_command('tqyb', permission=GROUP_ADMIN | GROUP_OWNER | PRIVATE | SUPERUSER, priority=50)


@weather_change_schedule.handle()
async def weather_change_schedule_handle(bot: Bot, event: Event):
    await weather_change_schedule.finish(
        change_schedule(
            str(event.get_session_id()),
            str(event.get_message())
        )
    )


weather_now = on_command('tq', priority=50)


@weather_now.handle()
async def weather_now_handle(bot: Bot, event: Event):
    await weather_now.finish(
        check_report(
            str(event.get_message())
        )
    )
