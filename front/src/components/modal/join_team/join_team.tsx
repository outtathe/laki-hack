import React from "react";
import "./join_team.scss"

import { Button } from "../../button/button";

type Props = { onClose }
type State = {}

export class ModalJoinTeam extends React.Component<Props, State> {
    render(): React.ReactNode {
        return (<>
            <div className="ModalJoinTeam">
                <Button text="Confirm" onClick={() => { this.props.onClose() }} />
            </div>
        </>)
    }
}