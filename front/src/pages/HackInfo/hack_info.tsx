import React from "react";
import Modal from 'react-modal';

import { MenuItem } from "../../components/menu_item/menu_item";
import { Spacer } from "../../components/spacer/spacer";
import { HackPreview } from "../../components/hack/preview/hack_preview";
import { Header } from "../../components/header/header";
import { Button } from "../../components/button/button";
import { ModalJoinEveryone } from "../../components/modal/join_evryone/join_everyone";
import { ModalCreateTeam } from "../../components/modal/create_team/create_team";


import "./hack_info.scss"
import "../../components/card/card.scss"

import { List } from "../../components/team/list/team_list";

type TeamProps = {}
type TeamState = { is_open: boolean }

class Team extends React.Component<TeamProps, TeamState> {
    constructor(props) {
        super(props)
        this.state = {
            is_open: false
        }
    }
    render(): React.ReactNode {
        return (<>
            <li className={this.state.is_open ? "back_vis" : "back_invis"}>
                <img className="profile_icon" src="assets/profile_icon_3.jpg"></img>
                <h5 className="name">удивленный котик</h5>
                <p className="status"></p>
                <p className="tag">в поиске</p>
                <img className={`drop_down ${this.state.is_open ? "open" : "close"}`} src="assets/drop_down.svg" onClick={() => { this.setState({ is_open: !this.state.is_open }) }}></img>
                <List is_open={this.state.is_open}></List>
            </li>
        </>)
    }
}

type Props = {}
type State = {
    window: string,
    create_modal_open: boolean,
    join_modal_open: boolean,
}

export class HackInfo extends React.Component<Props, State> {
    constructor(props) {
        super(props)
        this.state = {
            window: "description",
            create_modal_open: false,
            join_modal_open: false,
        }
    }
    componentDidMount(): void {
        Modal.setAppElement("#root");
    }
    handleModalJoinEveryoneClose = () => {
        this.setState({ join_modal_open: false })
    }
    handleModalCreateTeamClose = () => {
        this.setState({ create_modal_open: false })
    }
    getContent = () => {
        if (this.state.window == "description") return (<>
            <img src="assets/hack_default.jpg"></img>
            <h5>Название</h5>
            <p>Формат</p>
            <p>Сложность</p>
            <p>Даты</p>
            <p>Регистрация</p>
            <p>Технический фокус</p>
            <p>Целевая аудитория</p>
            <p>Приз</p>

            <div className="button_holder">
                <Button color="purple" size="large" text="хочу командовать" onClick={() => { this.setState({ create_modal_open: true }) }} />
                <Button color="purple" size="large" text="хочу подчиняться" onClick={() => { this.setState({ join_modal_open: true }) }} />
            </div>
        </>)
        else if (this.state.window == "teams") return (<>
            <div className="team_list">
                <ul>
                    <Team />
                    <Team />
                    <Team />
                </ul>
                <ul>
                    <Team />
                    <Team />
                    <Team />
                    <Team />
                </ul>
            </div>
            <div className="button_holder">
                <Button color="purple" size="large" text="хочу командовать" onClick={() => { this.setState({ create_modal_open: true }) }} />
                <Button color="purple" size="large" text="хочу подчиняться" onClick={() => { this.setState({ join_modal_open: true }) }} />
            </div>
        </>)
        else if (this.state.window == "my_team") return (<>
            <div className="team_info">
                <img className="icon" src="assets/profile_icon_1.jpg"></img>
                <div className="info">
                    <h5>laki team</h5>
                    <p className="tag">в поиске</p>
                    <p>Мы планируем создать приложение для управления финансами, которое поможет людям лучше понимать свои расходы и доходы, а также даст рекомендации по улучшению финансового положения.</p>
                </div>
                <List is_subdable={true} />
            </div>
        </>)
    }

    render(): React.ReactNode {
        return (<>
            <Header></Header>
            <div className="HackInfo">
                <Modal
                    contentLabel="Join everyone"
                    isOpen={this.state.join_modal_open}
                >
                    <ModalCreateTeam onClose={this.handleModalJoinEveryoneClose} />
                </Modal>
                <Modal
                    contentLabel="Create team"
                    isOpen={this.state.create_modal_open}
                >
                    <ModalJoinEveryone onClose={this.handleModalCreateTeamClose} />
                </Modal>
                <h1 className="title">хакатоны</h1>
                <div className="sub_header">
                    <MenuItem text="хакатоны / название хакатона"></MenuItem>
                    <Spacer></Spacer>
                </div>
                <div className="wrap"><div className="Card">
                    <div className="button_holder">
                        <Button color="black" size="small" text="описание" onClick={() => (this.setState({ window: "description" }))} />
                        <Button color="black" size="small" text="команды" onClick={() => (this.setState({ window: "teams" }))} />
                        <Button color="black" size="small" text="моя команда" onClick={() => (this.setState({ window: "my_team" }))} />
                    </div>
                    {this.getContent()}
                </div></div>
            </div>
        </>)
    }
}