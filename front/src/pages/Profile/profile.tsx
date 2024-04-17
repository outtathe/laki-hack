import React from "react";
import "./profile.scss"

import { Header } from "../../components/header/header";
import { Button } from "../../components/button/button";
import "../../components/card/card.scss"

type Props = {}
type State = {}

export class Profile extends React.Component<Props, State> {
    getProfileCard = (name, tag, about, skils, groupe, contacts, wins) => {
        return <>
            <div className="Card">
                <img className="icon" src="assets/profile_icon_2.jpg"></img>
                <h5 className="name">{name}</h5>
                <p className="tag">{tag}</p>
                <p className="sub_title">о себе</p>
                <p className="text">{about}</p>
                <p className="sub_title">скиллы</p>
                <p className="text">{skils}</p>
                <p className="sub_title">группа</p>
                <p className="text">{groupe}</p>
                <p className="sub_title">контакты</p>
                {Array.from(contacts, (contact: Object, idx) => {
                    return <a className="text" key={idx} href={contact["value"]}>
                        {`${contact["name"]}`}
                    </a>
                })}
                <p className="sub_title">победы</p>
                {Array.from(wins, (win: Object, idx) => {
                    return <p className="text" key={idx}>
                        {`${win["place"]} место - ${win["name"]}`}
                    </p>
                })}
                <Button color={"purple"} text={"редактировать"} />
            </div>
        </>
    }
    getXPGraph = () => {
        return <>
            <div className="Card"></div>
        </>
    }
    getTeamCard = () => {
        return <>
            <div className="Card">

            </div>
        </>
    }
    render(): React.ReactNode {
        return (<>
            <Header></Header>
            <div className="Profile">
                <h1 className="title">профиль</h1>
                <div className="profile_card">
                    {this.getProfileCard(
                        "вася пупкин",
                        "@pupochek",
                        "Вася Пупкин является популярным персонажем в российской культуре и часто используется в шутках и анекдотах.",
                        "figma, adobe пакет",
                        "БИСТ 20-1",
                        [
                            { "name": "github", "value": "https://github.com/ArzymKoteyko" },
                        ],
                        [
                            { "name": "мтс хакатон 2022", "place": 2 },
                            { "name": "хакатон хакатонистый", "place": 1 },
                        ]
                    )}
                </div>
                <div className="achivments"></div>
                <div className="xp_gpraph">
                    {this.getXPGraph()}
                </div>
                <div className="statistics"></div>
                <div className="team_card">
                    {this.getTeamCard()}
                </div>
            </div>
        </>)
    }
}