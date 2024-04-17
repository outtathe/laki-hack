import React from "react";
import "./applications.scss"

type Props = {}
type State = {}

export class Applications extends React.Component<Props, State> {
    render(): React.ReactNode {
        return (<>
            <div className="Applications">
                <table>
                    <tr>
                        <td>имя</td>
                        <td>опыт</td>
                        <td>скиллы</td>
                        <td>победы</td>
                    </tr>
                    <tr>
                        <td>@usertag</td>
                        <td>1 год</td>
                        <td>ux/ui дизайн</td>
                        <td>хакатончик</td>
                    </tr>
                    <tr>
                        <td>@....</td>
                        <td>2 года</td>
                        <td>ux/ui дизайн</td>
                        <td>МТС хакатон</td>
                    </tr>
                    <tr>
                        <td></td>
                        <td>1 год</td>
                        <td>figma, adobe, python, c#, sql, css</td>
                        <td>хакатончик</td>
                    </tr>
                    <tr>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                </table>
            </div>
        </>)
    }
}