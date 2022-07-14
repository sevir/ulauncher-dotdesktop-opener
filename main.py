import json
import requests
import logging
import os
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction

logger = logging.getLogger(__name__)


class DotDesktopOpenerExtension(Extension):

    def __init__(self):
        super(DotDesktopOpenerExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []

        on_enter = {'alt_enter': False}

        dotdesktop_files = extension.preferences['dotdesktop_files']
        dotdesktop_files = dotdesktop_files.replace(':', ' ')

        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name='Run Apps',
                                         description='%s'%(dotdesktop_files),
                                         highlightable=False,
                                         on_enter=ExtensionCustomAction(on_enter)
                                         ))

        return RenderResultListAction(items)


class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension):
        dotdesktop_files = extension.preferences['dotdesktop_files']
        programs = dotdesktop_files.split(':')

        for p in programs:
            os.system("gtk-launch %s"%(p))

        os.system("notify-send 'Programs launched' '%s' -a 'Ulauncher' -u critical -i checkbox-checked-symbolic"%(dotdesktop_files))

        # return RenderResultListAction([ExtensionResultItem(icon='images/icon.png',
        #                                                    name=data['new_name'],
        #                                                    on_enter=HideWindowAction())])


if __name__ == '__main__':
    DotDesktopOpenerExtension().run()
