import React from "react";
import { Link } from "react-router-dom";
import "./menu_item.scss"

type Props = { text?, icon?, href?}
type State = {}

export class MenuItem extends React.Component<Props, State> {
    render(): React.ReactNode {
        return (<><a href={this.props.href ?? "/"}>
            <div className="MenuItem">
                {this.props.icon ? (<img src={`assets/${this.props.icon}`}></img>) : <></>}
                {this.props.text ? (<p>{this.props.text}</p>) : <></>}
            </div></a>
        </>)
    }
}