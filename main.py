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
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction

logger = logging.getLogger(__name__)


class DotDesktopOpenerExtension(Extension):

    def __init__(self):
        super(DotDesktopOpenerExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        element_selected = event.get_argument()
        dotdesktopapps = extension.preferences['dotdesktop_files']

        if event.get_argument() is None:
            return        

        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name='resulttext',
                                         description='Description',
                                         highlightable=False
                                         ))

        return RenderResultListAction(items)


class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension):
        data = event.get_data()
        os.system("notify-send 'Automato deploy' 'Subida a Vercel. Actualizado y subido!!' -a 'Automato' -u critical -i checkbox-checked-symbolic")

        # return RenderResultListAction([ExtensionResultItem(icon='images/icon.png',
        #                                                    name=data['new_name'],
        #                                                    on_enter=HideWindowAction())])


if __name__ == '__main__':
    DotDesktopOpenerExtension().run()
