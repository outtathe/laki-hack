import React from "react";
import "./team_info.scss"
import "../../components/card/card.scss"

import { Header } from "../../components/header/header";
import { List } from "../../components/team/list/team_list";
import { Applications } from "../../components/applications/applications";

type Props = {}
type State = {}

export class TeamInfo extends React.Component<Props, State> {
    render(): React.ReactNode {
        return (<>
            <Header />
            <div className="TeamInfo">
                <div id="col_1">
                    <div className="Card"><div className="TeamCard">
                        <h5 className="name">laki team</h5>
                        <p className="about">хакатон мечты и вкусной еды</p>
                        <p className="tag">в поиске</p>
                        <h5 className="description">участники команды</h5>
                        <List is_subdable={true} />
                    </div></div>
                    <div className="Card"><div className="AboutCard">
                        About Card
                    </div></div>
                </div>
                <div id="col_2">
                    <div className="Card">
                        <Applications />
                        <Applications />
                    </div>
                </div>
                <div id="col_3">
                    <div className="card"><div className="StatisticCard">
                        StatisticCard
                    </div></div>
                    <div className="card"><div className="ProfileCard">
                        Profile Card
                    </div></div>
                </div>
            </div>
        </>)
    }
}