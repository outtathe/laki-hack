import React from "react";
import { Link } from 'react-router-dom';
import "./header.scss"

const axios = require('axios');

import { MenuItem } from "../menu_item/menu_item";
import { Spacer } from "../spacer/spacer";
import { API } from "../../env";

type Props = {}
type State = { name: string }

export class Header extends React.Component<Props, State> {
    constructor(props) {
        super(props)
        this.state = {
            name: "Личный кабинет"
        }
        let setName = (name) => { this.setState({ name: name }) }
        axios.get(
            `${API}/user`,
            { headers: { "id_user": localStorage.getItem("id") } }
        ).then((response) => {
            setName(response.data.user.login)
            console.log(response.data.user) // REMOVE IT
        })
    }

    render(): React.ReactNode {
        return (<>
            <div className="Header">
                <MenuItem text="хакатоны" />
                <MenuItem text="команды" href="/teams" />
                <MenuItem text="объявления" />
                <MenuItem text="календарь" href="/calendar" />
                <MenuItem text="справочник" />
                <Spacer></Spacer>
                <MenuItem text={this.state.name} icon="user.svg" href="/profile"></MenuItem>
                <MenuItem text="RU" />
            </div>
        </>)
    }
}