import React from 'react';
import { createRoot } from 'react-dom/client';
import { WebAppProvider, MainButton, BackButton } from '@vkruglikov/react-telegram-web-app';

import "./reset.scss"
import { App } from './app';

const root_tag = document.getElementById('root')
let tg = window.Telegram.WebApp;

if (root_tag) {
    const root = createRoot(root_tag)
    root.render(
        <WebAppProvider
            options={{
                smoothButtonsTransition: true,
            }}
        >
            <p>Hello</p>
            <p>{tg.initData}</p> //
            <p>{JSON.stringify(tg.initDataUnsafe)}</p>
        </WebAppProvider>
    )
}
else console.log("Can't find html root tag id to start app")