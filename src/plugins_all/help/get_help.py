from nonebot.plugin import require,plugins
import os,re

def helpmsg(module_name):
    #读取插件名及用法
    plugin_dic = {}
    for plugin_name in plugins.keys():
        try:
            name,usage = get_info_from_plugin(plugin_name)
            plugin_dic[name] = usage
        except:
            name,usage = plugin_name,'未能成功找到该插件的用法'
            plugin_dic[name] = usage
    #匹配查询内容
    if module_name == '':
        msg = '\n'.join(plugin_dic.keys())
        return  f'现已加载的插件列表有:\n{msg}\n使用"/help 插件名"以获取具体信息'
    elif module_name in plugin_dic:
        return plugin_dic[module_name]
    else:
        return "未能成功找到该插件，使用/help以获取插件列表"
    
def get_info_from_plugin(plugin):
    plugin_info = require(plugin)
    name = plugin_info.name
    usage = plugin_info.usage
    return name,usage