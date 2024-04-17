import React from "react";
import "./background.scss"


type Props = {}
type State = {}

export class Background extends React.Component<Props, State> {
    render(): React.ReactNode {
        return (<>
            <div className="Background">
                <img id="blob_1" src="assets/blob_1.svg"></img>
                <img id="blob_2" src="assets/blob_2.svg"></img>
                <img id="blob_3" src="assets/blob_3.svg"></img>
            </div>
        </>)
    }
}