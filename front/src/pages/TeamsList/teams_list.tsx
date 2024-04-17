import React from "react";

import { MenuItem } from "../../components/menu_item/menu_item";
import { Spacer } from "../../components/spacer/spacer";
import { TeamPreview } from "../../components/team/preview/team_preview";
import { Header } from "../../components/header/header";
import "./teams_list.scss"

type Props = {}
type State = {}

export class TeamsList extends React.Component<Props, State> {
    render(): React.ReactNode {
        return (<>
            <Header></Header>
            <div className="TeamsList">
                <h1 className="title">команды</h1>
                <div className="sub_header">
                    <MenuItem text="по популярности"></MenuItem>
                    <MenuItem text="фильтр"></MenuItem>
                    <Spacer></Spacer>
                    <MenuItem text="создать"></MenuItem>
                </div>
                <div className="card_carousel">
                    <TeamPreview></TeamPreview>
                    <TeamPreview></TeamPreview>
                    <TeamPreview></TeamPreview>
                </div>
            </div>
        </>)
    }
}