import React from 'react';
import { createRoot } from 'react-dom/client';
import Modal from 'react-modal'

import "./reset.scss"
import { App } from './app';



const root_tag = document.getElementById('root')
if (root_tag) {
    const root = createRoot(root_tag)
    root.render(
        <App></App>
    )
}
else console.log("Can't find html root tag id to start app")