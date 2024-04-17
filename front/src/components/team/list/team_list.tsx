import React from "react"
import Modal from "react-modal"

import { Button } from "../../button/button"
import { ModalJoinTeam } from "../../modal/join_team/join_team"
import { Applications } from "../../applications/applications"
import "./team_list.scss"

type VactionProps = {
    tag?: string
    role: string
    is_subdable?: boolean
    is_parent_open?: boolean
    is_vacant: boolean
}
type VactionState = {
    is_subdable: boolean
    is_parent_open?: boolean
    is_open: boolean
}

class Vaction extends React.Component<VactionProps, VactionState> {
    constructor(props) {
        super(props)
        this.state = {
            is_subdable: this.props.is_subdable ?? false,
            is_open: false,
            is_parent_open: this.props.is_parent_open ?? true,
        }
    }
    componentDidUpdate(prevProps) {
        if (this.props.is_parent_open != prevProps.is_parent_open) this.setState({ is_parent_open: this.props.is_parent_open })
    }
    render(): React.ReactNode {
        if (!this.props.is_vacant) {
            return (<>
                <li className={`Vacation ${this.state.is_parent_open ? "open" : "close"}`}>
                    <p className="role">{this.props.role}</p>
                    <p className="tag">{this.props.tag ?? "@...."}</p>
                </li>
            </>)
        } else if (this.state.is_subdable) {
            return (<>
                <li className={`Vacation ${this.state.is_parent_open ? "open" : "close"}`}>
                    <p className="role">{this.props.role}</p>
                    <p
                        className="tag vacant"
                        onClick={() => { this.setState({ is_open: !this.state.is_open }) }}
                    >
                        заявки<img className={`drop_down ${this.state.is_open ? "open" : "close"}`} src="assets/drop_down.svg"></img>
                    </p>
                    <ul className={`list ${this.state.is_open ? "sub_opne" : "sub_close"}`}>
                        <Applications />
                    </ul>
                </li>
            </>)
        } else {
            return (<>
                <li className={`Vacation ${this.state.is_parent_open ? "open" : "close"}`}>
                    <p className="role">{this.props.role}</p>
                    <p
                        className="tag vacant"
                    >
                        свободно
                    </p>
                </li>
            </>)
        }
    }
}

type ListProps = {
    is_open?: boolean
    is_subdable?: boolean
}
type ListState = {
    is_open?: boolean
    is_subdable: boolean
    modal_open: boolean
}

export class List extends React.Component<ListProps, ListState> {
    constructor(props) {
        super(props);
        this.state = {
            is_open: this.props.is_open ?? true,
            is_subdable: this.props.is_subdable ?? false,
            modal_open: false
        }
    }
    handleModalJoinTeamClose = () => {
        this.setState({ modal_open: false })
    }
    componentDidUpdate(prevProps) {
        if (this.props.is_open != prevProps.is_open) this.setState({ is_open: this.props.is_open })
    }
    componentDidMount(): void {
        Modal.setAppElement("#root");
    }
    render(): React.ReactNode {
        return (<>
            <div className={`List ${this.state.is_open ? "open" : "close"}`} >
                <Modal
                    contentLabel="Minimal Modal Example"
                    isOpen={this.state.modal_open}
                >
                    <ModalJoinTeam onClose={this.handleModalJoinTeamClose} />
                </Modal>
                <ul>
                    <Vaction is_vacant={false} is_subdable={this.state.is_subdable} role="team leader" tag="@bro" />
                    <Vaction is_vacant={false} is_subdable={this.state.is_subdable} role="ml" tag="@talisman" />
                    <Vaction is_vacant={true} is_subdable={this.state.is_subdable} role="frontend" />
                    <Vaction is_vacant={false} is_subdable={this.state.is_subdable} role="backend" />
                    <Vaction is_vacant={true} is_subdable={this.state.is_subdable} role="design" />
                </ul>
                {(() => {
                    if (!this.state.is_subdable) return (<Button
                        color="black"
                        text="откликнуться"
                        onClick={() => { this.setState({ modal_open: true }) }}
                    />)
                })()}
            </div>
        </>)
    }
}
