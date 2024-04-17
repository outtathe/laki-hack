
import React from "react";
import Modal from "react-modal"
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import "./app.scss"

import { Header } from "./components/header/header"
import { Background } from "./components/background/background";
import { HacksLists } from "./pages/HacksList/hacks_list";
import { TeamsList } from "./pages/TeamsList/teams_list";
import { HackInfo } from "./pages/HackInfo/hack_info";
import { Login } from "./pages/Auth/login";
import { Singin } from "./pages/Auth/singin";
import { TeamInfo } from "./pages/TeamInfo/team_info";
import { AIChat } from "./pages/AIChat/ai_chat";
import { Calendar } from "./pages/Calendar/calendar";
import { Profile } from "./pages/Profile/profile";

Modal.defaultStyles = {
    overlay: {
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        backdropFilter: 'blur(10px)',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center'
    },
    content: {
        WebkitOverflowScrolling: 'touch',
    }
}



type Props = {}
type State = {}

export class App extends React.Component<Props, State> {
    render(): React.ReactNode {
        return (<>
            <div className="App">
                <BrowserRouter>
                    <Routes>
                        <Route path="/" element={<HacksLists />} />
                        <Route path="/teams" element={<TeamsList />} />
                        <Route path="/hack_info" element={<HackInfo />} />
                        <Route path="/login" element={<Login />} />
                        <Route path="/singin" element={<Singin />} />
                        <Route path="/team_info" element={<TeamInfo />} />
                        <Route path="/chat" element={<AIChat />} />
                        <Route path="/calendar" element={<Calendar />} />
                        <Route path="/profile" element={<Profile />} />
                    </Routes>
                </BrowserRouter>
                <Background></Background>
            </div >
        </>)
    }
}