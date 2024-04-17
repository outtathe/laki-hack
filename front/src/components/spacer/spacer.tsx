import React from "react";
import "./spacer.scss"

type Props = {}
type State = {}

export class Spacer extends React.Component<Props, State> {
    render(): React.ReactNode {
        return (<>
            <div className="Spacer">
            </div>
        </>)
    }
}