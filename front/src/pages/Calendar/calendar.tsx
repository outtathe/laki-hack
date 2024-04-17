import React from "react";
import "./calendar.scss"


import { Header } from "../../components/header/header";
import { months } from "../../env";
import { week_days } from "../../env";
import { colors } from "../../env";
import "../../components/card/card.scss"

const arrow_src = "assets/drop_down.svg"

type Props = {

}
type State = {
    year
    month
}

const event_data = [
    { "name": "хакатоним жостка", "reg_start": "2023-09-02", "reg_end": "2023-09-04", "start": "2023-09-05", "end": "2023-09-08" },
    { "name": "хакатоним ещё жостче", "reg_start": "2023-09-08", "reg_end": "2023-09-16", "start": "2023-09-19", "end": "2023-09-22" },
    { "name": "хакатончик", "reg_start": "2023-09-08", "reg_end": "2023-10-05", "start": "2023-10-08", "end": "2023-10-09" },
    { "name": "хакатоним ещё жостче 2", "reg_start": "2023-08-01", "reg_end": "2023-09-06", "start": "2023-09-12", "end": "2023-09-22" },
    { "name": "супер хак", "reg_start": "2023-09-08", "reg_end": "2023-09-24", "start": "2023-09-26", "end": "2023-09-29" }
]

let isLesEq = (date_1, date_2) => {
    let year_1 = date_1.getYear()
    let year_2 = date_2.getYear()
    let month_1 = date_1.getMonth()
    let month_2 = date_2.getMonth()
    let day_1 = date_1.getDate()
    let day_2 = date_2.getDate()
    return (year_1 < year_2) ||
        (year_1 == year_2 && month_1 < month_2) ||
        (year_1 == year_2 && month_1 == month_2 && day_1 <= day_2)
}
let isMoreEq = (date_1, date_2) => {
    let year_1 = date_1.getYear()
    let year_2 = date_2.getYear()
    let month_1 = date_1.getMonth()
    let month_2 = date_2.getMonth()
    let day_1 = date_1.getDate()
    let day_2 = date_2.getDate()
    return (year_1 > year_2) ||
        (year_1 == year_2 && month_1 > month_2) ||
        (year_1 == year_2 && month_1 == month_2 && day_1 >= day_2)
}

export class Calendar extends React.Component<Props, State> {
    constructor(props) {
        super(props)
        this.state = {
            year: 2023,
            month: 9
        }
        console.log()
    }
    addMonth = () => {
        this.setState({
            month: this.state.month % 12 + 1,
            year: this.state.month == 12 ? this.state.year + 1 : this.state.year
        })
    }
    subMonth = () => {
        this.setState({
            month: ((this.state.month - 2) % 12 + 12) % 12 + 1,
            year: this.state.month == 1 ? this.state.year - 1 : this.state.year
        })

    }
    getDateBox = () => {
        let len = new Date(this.state.year, this.state.month, 0).getDate()
        return Array.from({ length: len }, (_, i) => <>
            <div className="date">
                <p className="day">{i + 1}</p>
                <p className="week_day">
                    {week_days[new Date(this.state.year, this.state.month, i + 1).getDay()]}
                </p>
            </div>
        </>)
    }
    getCalendarEventBox = () => {
        return Array.from(event_data, (event, i) => <>
            <div className="event_box"><h5 className="event_name">{event["name"]}</h5></div>
        </>)
    }
    getCalendarDataBox = () => {
        return Array.from(event_data, (event, row) => <>
            <div className="data_row">
                {this.getCalendarDataRow(event, row)}
            </div>
        </>)
    }
    getCalendarDataRow = (event, row) => {
        let len = new Date(this.state.year, this.state.month, 0).getDate()
        return Array.from({ length: len }, (_, i) => {
            let date = new Date(this.state.year, this.state.month - 1, i + 1)
            let height = 0
            if (isLesEq(new Date(event["reg_start"]), date) && isMoreEq(new Date(event["reg_end"]), date)) {
                height = 2
            }
            if (isLesEq(new Date(event["start"]), date) && isMoreEq(new Date(event["end"]), date)) {
                height = 15
            }
            return <>
                <div className="data_item">
                    <div className={`filler ${colors[row % colors.length]}`} style={{ height: height }}></div>
                </div>
            </>
        })
    }
    render(): React.ReactNode {
        return (<>
            <Header />
            <div className="CalendarPage">
                <h1 className="title">календарь</h1>
                <div className="Card">

                    <div className="Calendar">
                        <p className="year">{this.state.year}</p>
                        <div className="month_box">
                            <img className="arrow left" src={arrow_src} onClick={this.subMonth}></img>
                            <p className="month">{months[this.state.month]}</p>
                            <img className="arrow right" src={arrow_src} onClick={this.addMonth}></img>
                        </div>
                        <div className="calendar_body">
                            <div className="date_box">
                                {this.getDateBox()}
                            </div>
                            <div className="calendar_events">
                                {this.getCalendarEventBox()}
                            </div>
                            <div className="calendar_data_box">
                                {this.getCalendarDataBox()}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>)
    }
}