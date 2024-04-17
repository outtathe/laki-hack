import React from "react";

import "../../card/card.scss"
import "./hack_preview.scss"
import { Button } from "../../button/button";
import { Spacer } from "../../spacer/spacer";

type Props = {}
type State = {}

export class HackPreview extends React.Component<Props, State> {
    render(): React.ReactNode {
        return (<>
            <div className="Card">
                <div className="HackPreview">
                    <img src="assets/hack_default.jpg"></img>
                    <h5>название</h5>
                    <p>даты</p>
                    <Spacer></Spacer>
                    <Button text="подробнее" color="purple" href="/hack_info"></Button>
                </div>
            </div>
        </>)
    }
}