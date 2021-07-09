from importlib import util
from pathlib import Path
from sys import modules


def load_plugins(plugin_name):
    if plugin_name.startswith("__"):
        pass
    elif plugin_name.endswith("_"):
        path = Path(f"plugins/{plugin_name}.py")
        name = "plugins.{}".format(plugin_name)
        spec = util.spec_from_file_location(name, path)
        mod = util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    else:
        from . import HNDLR, LOGS, petercordpanda_bot, udB
        from .dB.core import HELP, PLUGINS
        from .dB.database import Var
        from .misc import _supporter as xxx
        from .misc._assistant import (
            asst_cmd,
            callback,
            in_pattern,
            inline,
            inline_owner,
            owner,
        )
        from .misc._decorators import ilhammansiz_cmd
        from .misc._wrappers import eod, eor

        path = Path(f"plugins/{plugin_name}.py")
        name = "plugins.{}".format(plugin_name)
        spec = util.spec_from_file_location(name, path)
        mod = util.module_from_spec(spec)
        mod.asst = petercordpanda_bot.asst
        mod.tgbot = petercordpanda_bot.asst
        mod.petercordpanda_bot = petercordpanda_bot
        mod.bot = petercordpanda_bot
        mod.petercordpanda = petercordpanda_bot
        mod.owner = owner()
        mod.in_owner = inline_owner()
        mod.inline = inline()
        mod.in_pattern = in_pattern
        mod.eod = eod
        mod.edit_delete = eod
        mod.LOGS = LOGS
        mod.hndlr = HNDLR
        mod.HNDLR = HNDLR
        mod.Var = Var
        mod.eor = eor
        mod.edit_or_reply = eor
        mod.asst_cmd = asst_cmd
        mod.ilhammansiz_cmd = ilhammansiz_cmd
        mod.on_cmd = ilhammansiz_cmd
        mod.callback = callback
        mod.Redis = udB.get
        modules["support"] = xxx
        modules["userbot"] = xxx
        modules["userbot.utils"] = xxx
        modules["userbot.config"] = xxx
        spec.loader.exec_module(mod)
        modules["plugins." + plugin_name] = mod
        if not plugin_name.startswith("_"):
            try:
                PLUGINS.append(plugin_name)
            except BaseException:
                if plugin_name not in PLUGINS:
                    PLUGINS.append(plugin_name)
                else:
                    pass
            try:
                doc = modules[f"plugins.{plugin_name}"].__doc__
                HELP.update({f"{plugin_name}": doc.format(i=HNDLR)})
            except KeyError:
                pass
            except Exception as e:
                print(e)


# for modules


def load_modules(plugin_name):
    if plugin_name.startswith("__"):
        pass
    elif plugin_name.endswith("_"):
        path = Path(f"modules/{plugin_name}.py")
        name = "modules.{}".format(plugin_name)
        spec = util.spec_from_file_location(name, path)
        mod = util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    else:
        from . import HNDLR, LOGS, petercordpanda_bot, udB
        from .dB.core import HELP, MODULES
        from .dB.database import Var
        from .misc import _supporter as xxx
        from .misc._assistant import (
            asst_cmd,
            callback,
            in_pattern,
            inline,
            inline_owner,
            owner,
        )
        from .misc._decorators import ilhammansiz_cmd
        from .misc._supporter import Config, admin_cmd, sudo_cmd
        from .misc._wrappers import eod, eor

        path = Path(f"addons/{plugin_name}.py")
        name = "modules.{}".format(plugin_name)
        spec = util.spec_from_file_location(name, path)
        mod = util.module_from_spec(spec)
        mod.asst = petercordpanda_bot.asst
        mod.tgbot = petercordpanda_bot.asst
        mod.petercordpanda_bot = petercordpanda_bot
        mod.ub = petercordpanda_bot
        mod.bot = petercordpanda_bot
        mod.petercordpanda = petercordpanda_bot
        mod.borg = petercordpanda_bot
        mod.telebot = petercordpanda_bot
        mod.jarvis = petercordpanda_bot
        mod.friday = petercordpanda_bot
        mod.owner = owner()
        mod.in_owner = inline_owner()
        mod.inline = inline()
        mod.eod = eod
        mod.edit_delete = eod
        mod.LOGS = LOGS
        mod.in_pattern = in_pattern
        mod.hndlr = HNDLR
        mod.handler = HNDLR
        mod.HNDLR = HNDLR
        mod.CMD_HNDLR = HNDLR
        mod.Config = Config
        mod.Var = Var
        mod.eor = eor
        mod.edit_or_reply = eor
        mod.asst_cmd = asst_cmd
        mod.ilhammansiz_cmd = ilhammansiz_cmd
        mod.on_cmd = ilhammansiz_cmd
        mod.callback = callback
        mod.Redis = udB.get
        mod.admin_cmd = admin_cmd
        mod.sudo_cmd = sudo_cmd
        modules["ub"] = xxx
        modules["var"] = xxx
        modules["jarvis"] = xxx
        modules["support"] = xxx
        modules["userbot"] = xxx
        modules["telebot"] = xxx
        modules["fridaybot"] = xxx
        modules["jarvis.utils"] = xxx
        modules["uniborg.util"] = xxx
        modules["telebot.utils"] = xxx
        modules["userbot.utils"] = xxx
        modules["userbot.events"] = xxx
        modules["jarvis.jconfig"] = xxx
        modules["userbot.config"] = xxx
        modules["fridaybot.utils"] = xxx
        modules["fridaybot.Config"] = xxx
        modules["userbot.uniborgConfig"] = xxx
        spec.loader.exec_module(mod)
        modules["addons." + plugin_name] = mod
        if not plugin_name.startswith("_"):
            try:
                MODULES.append(plugin_name)
            except BaseException:
                if plugin_name not in MODULES:
                    MODULES.append(plugin_name)
                else:
                    pass
            try:
                doc = modules[f"modules.{plugin_name}"].__doc__
                HELP.update({f"{plugin_name}": doc.format(i=HNDLR)})
            except KeyError:
                pass
            except Exception as e:
                print(e)


# for assistant


def load_assistant(plugin_name):
    if plugin_name.startswith("__"):
        pass
    elif plugin_name.endswith("_"):
        path = Path(f"assistant/{plugin_name}.py")
        name = "assistant.{}".format(plugin_name)
        spec = util.spec_from_file_location(name, path)
        mod = util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    else:
        from . import HNDLR, petercordpanda_bot, udB
        from .misc._assistant import asst_cmd, callback, in_pattern, inline_owner, owner
        from .misc._wrappers import eod, eor

        path = Path(f"assistant/{plugin_name}.py")
        name = "assistant.{}".format(plugin_name)
        spec = util.spec_from_file_location(name, path)
        mod = util.module_from_spec(spec)
        mod.petercordpanda_bot = petercordpanda_bot
        mod.petercordpanda = petercordpanda_bot
        mod.Redis = udB.get
        mod.udB = udB
        mod.bot = petercordpanda_bot
        mod.asst = petercordpanda_bot.asst
        mod.owner = owner()
        mod.in_pattern = in_pattern
        mod.in_owner = inline_owner()
        mod.eod = eod
        mod.eor = eor
        mod.callback = callback
        mod.hndlr = HNDLR
        mod.HNDLR = HNDLR
        mod.asst_cmd = asst_cmd
        spec.loader.exec_module(mod)
        modules["assistant." + plugin_name] = mod


# msg forwarder


def load_pmbot(plugin_name):
    if plugin_name.startswith("__"):
        pass
    elif plugin_name.endswith("_"):
        path = Path(f"assistant/pmbot/{plugin_name}.py")
        name = "assistant.pmbot.{}".format(plugin_name)
        spec = util.spec_from_file_location(name, path)
        mod = util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    else:
        from . import HNDLR, petercordpanda_bot, udB
        from .misc._assistant import asst_cmd, callback, owner
        from .misc._wrappers import eod, eor

        path = Path(f"assistant/pmbot/{plugin_name}.py")
        name = "assistant.pmbot.{}".format(plugin_name)
        spec = util.spec_from_file_location(name, path)
        mod = util.module_from_spec(spec)
        mod.petercordpanda_bot = petercordpanda_bot
        mod.petercordpanda_bot = petercordpanda_bot
        mod.bot = petercordpanda_bot
        mod.Redis = udB.get
        mod.udB = udB
        mod.asst = petercordpanda_bot.asst
        mod.owner = owner()
        mod.eod = eod
        mod.eor = eor
        mod.callback = callback
        mod.hndlr = HNDLR
        mod.HNDLR = HNDLR
        mod.asst_cmd = asst_cmd
        spec.loader.exec_module(mod)
        modules["assistant.pmbot" + plugin_name] = mod
