import React from "react";
import "./button.scss"

type Props = { text?: String, color?: String, href?: string, size?: String, type?: String, onClick?}
type State = {}

export class Button extends React.Component<Props, State> {
    handleClick = () => {
        if (this.props.onClick) this.props.onClick();
        if (this.props.href) {
            window.location.href = this.props.href
        }
    }
    render(): React.ReactNode {
        return (<>
            <button
                type={this.props.type ?? "button"}
                className={`ButtonLarge ${this.props.color ?? "blue"} ${this.props.size ?? "large"}`}
                onClick={this.handleClick}
            >
                {this.props.text ?? "..."}
            </button>
        </>)
    }
}