import React from "react";
import "./create_team.scss"

import { Button } from "../../button/button";

type Props = { onClose }
type State = {}

export class ModalCreateTeam extends React.Component<Props, State> {
    render(): React.ReactNode {
        return (<>
            <div className="ModalCreateTeam">
                <Button text="Confirm" onClick={() => { this.props.onClose() }} />
            </div>
        </>)
    }
}