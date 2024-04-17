import React from "react";
import "./join_everyone.scss"

import { Button } from "../../button/button";

type Props = { onClose }
type State = {}

export class ModalJoinEveryone extends React.Component<Props, State> {
    render(): React.ReactNode {
        return (<>
            <div className="ModalJoinEveryone">
                <Button text="Confirm" onClick={() => { this.props.onClose() }} />
            </div>
        </>)
    }
}