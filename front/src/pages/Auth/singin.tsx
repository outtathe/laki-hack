import React from "react";
import "./auth.scss"

const axios = require('axios');
import { API } from "../../env";

import "../../components/card/card.scss"
import { Button } from "../../components/button/button";
import { Spacer } from "../../components/spacer/spacer";

type Props = {}
type State = {}

export class Singin extends React.Component<Props, State> {
    name
    true_pass
    check_pass
    error_label
    constructor(props) {
        super(props)
        this.name = React.createRef()
        this.true_pass = React.createRef()
        this.check_pass = React.createRef()
        this.error_label = React.createRef()
    }
    handleFocus = () => {
        this.error_label.current.textContent = ""
    }
    handleSubmit = () => {
        let name = this.name.current.value
        let true_pass = this.true_pass.current.value
        let check_pass = this.check_pass.current.value
        let success = true
        let setError = (text) => {
            this.error_label.current.textContent = text
        }
        if (true_pass == check_pass) {
            axios.post(
                `${API}/registration`,
                {
                    "login": name,
                    "password": true_pass,
                },
                { headers: { "Access-Control-Allow-Origin": "*" } }
            ).then((response) => {
                localStorage.setItem("id", response.data.id_user);
            }).catch(function (error) {
                success = false
                if (error.code == "ERR_BAD_REQUEST") {
                    setError("Имя пользователя занято")
                } else console.log(error.code);
            }).finally(() => {
                this.true_pass.current.value = ""
                this.check_pass.current.value = ""
                if (success) window.location.href = "/"
            });
        } else {
            this.error_label.current.textContent = "Пароли не совпадают"
        }

    }
    render(): React.ReactNode {
        return (<>
            <div className="Auth"><div className="Card">
                <div className="content">
                    <form>
                        <h1 className="title">хакатоны</h1>
                        <Spacer></Spacer>
                        <label>имя</label>
                        <input type="text" ref={this.name} onFocus={this.handleFocus}></input>
                        <label>пароль</label>
                        <input type="password" ref={this.true_pass} onFocus={this.handleFocus}></input>
                        <label>повтори пароль</label>
                        <input type="password" ref={this.check_pass} onFocus={this.handleFocus}></input>
                        <label className="error" ref={this.error_label}></label>
                        <Spacer />
                        <Button color="black" text="войти" type="button" onClick={this.handleSubmit} />
                        <p>Уже зарегестрировался?<a href="/login">Войди</a></p>
                    </form>
                </div>
            </div></div>
        </>)
    }
}