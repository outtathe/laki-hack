import React from 'react';
import { createRoot } from 'react-dom/client';

import "./reset.scss"
import { App } from './app';

const root_tag = document.getElementById('root')
if (root_tag) {
    const root = createRoot(root_tag)
    root.render(<><h1>This is Admin Panel</h1></>)
}
else console.log("Can't find html root tag id to start app")