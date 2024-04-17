import React from "react"
import "./ai_chat.scss"

import { Header } from "../../components/header/header"
const axios = require('axios');

type Props = {}
type State = {}

export class AIChat extends React.Component<Props, State> {
    descriptionRef
    textRef
    constructor(props) {
        super(props)
        this.descriptionRef = React.createRef();
        this.textRef = React.createRef();
    }
    componentDidMount(): void {

    }
    handleRequest = () => {
        let description = this.descriptionRef.current.value
        let text = this.textRef.current.valu
        let tmp = {
            "model": "general",
            "generationOptions": {
                "partialResults": true,
                "temperature": 0.5,
                "maxTokens": 400
            },
            "messages": [
                {
                    "role": "Programmer",
                    "text": "How to write hellow world"
                }
            ],
            "instructionText": "Please help with problem"
        }
        axios.post(
            "https://llm.api.cloud.yandex.net/llm/v1alpha/chat",
            tmp,
            {
                headers: { "Access-Control-Allow-Origin": "*", "Content-Type": "application/x-www-form-urlencoded" },
                proxy: { host: 'proxy.koteykko.space' },
            },
        ).then(function (response) {
            console.log(response);
        }).catch(function (error) {
            console.log(error);
        });
        console.log(description)
        console.log(text)


        this.descriptionRef.current.value = ""
        this.textRef.current.value = ""
    }
    render(): React.ReactNode {
        return (<>
            <Header />

            <div className="AIChat">
                <input ref={this.descriptionRef}></input>
                <input ref={this.textRef}></input>
                <button onClick={this.handleRequest}></button>
            </div>
        </>)
    }
}