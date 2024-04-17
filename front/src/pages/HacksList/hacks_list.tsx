import React from "react";

import { MenuItem } from "../../components/menu_item/menu_item";
import { Spacer } from "../../components/spacer/spacer";
import { HackPreview } from "../../components/hack/preview/hack_preview";
import { Header } from "../../components/header/header";
import "./hacks_list.scss"

type Props = {}
type State = {}

export class HacksLists extends React.Component<Props, State> {
    render(): React.ReactNode {
        return (<>
            <Header></Header>
            <div className="HacksLists">
                <h1 className="title">хакатоны</h1>
                <div className="sub_header">
                    <MenuItem text="по популярности"></MenuItem>
                    <MenuItem text="фильтр"></MenuItem>
                    <MenuItem text="архив"></MenuItem>
                    <Spacer></Spacer>
                    <MenuItem text="календарь"></MenuItem>
                    <MenuItem text="создать"></MenuItem>
                </div>
                <div className="card_grid">
                    <HackPreview></HackPreview>
                    <HackPreview></HackPreview>
                    <HackPreview></HackPreview>
                    <HackPreview></HackPreview>
                    <HackPreview></HackPreview>
                    <HackPreview></HackPreview>
                </div>
            </div>
        </>)
    }
}