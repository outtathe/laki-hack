import React from "react";

import "../../card/card.scss"
import "./team_preview.scss"
import { Spacer } from "../../spacer/spacer";
import { Button } from "../../button/button";

type Props = {}
type State = {}

export class TeamPreview extends React.Component<Props, State> {
    render(): React.ReactNode {
        return (<>
            <div className="Card">
                <div className="TeamPreview">
                    <img className="team_icon" src="assets/team_icon.jpg"></img>
                    <h5>laki team</h5>
                    <p>хакатон мечты и вкусной еды</p>
                    <ul>
                        <li>
                            <img className="profile_icon" src="assets/profile_icon_1.jpg"></img>
                            <h5 className="name">голодный котик</h5>
                            <p className="role" style={{ "color": "#3692E7" }}>team leader</p>
                            <p className="tag">@....</p>
                        </li>
                        <li>
                            <img className="profile_icon" src="assets/profile_icon_2.jpg"></img>
                            <h5 className="name">озорной котик</h5>
                            <p className="role">ml</p>
                            <p className="tag">@....</p>
                        </li>
                        <li>
                            <img className="profile_icon" src="assets/profile_icon_3.jpg"></img>
                            <h5 className="name">удивленный котик</h5>
                            <p className="role">frontend</p>
                            <p className="tag">@....</p>
                        </li>
                        <li>
                            <img className="profile_icon" src="assets/profile_icon_4.jpg"></img>
                            <h5 className="name">смелый котик</h5>
                            <p className="role">backend</p>
                            <p className="tag">@....</p>
                        </li>
                        <li>
                            <img className="profile_icon" src="assets/profile_icon_5.jpg"></img>
                            <h5 className="name">недоступен...</h5>
                            <p className="role">designer</p>
                            <p className="tag">@....</p>
                        </li>
                    </ul>
                    <Spacer></Spacer>
                    <Button text="посмотреть" color="blue"></Button>
                </div>
            </div>
        </>)
    }
}