window.onload = function () {
    eel.GetLiveScheduleDict()(function (LiveScheduleDict) {
        var liveScheduleDays = Object.keys(LiveScheduleDict)
        const widgetBody = document.createElement("div");
        widgetBody.className = "widgetBody";
        for (let day of liveScheduleDays) {
            const dateSeprator = document.createElement("div");
            dateSeprator.innerText = day;
            dateSeprator.className = "dateSeprator";
            widgetBody.appendChild(dateSeprator)
            for (let match in LiveScheduleDict[day]) {
                const broadcastMatch = document.createElement("div");
                broadcastMatch.className = "broadcastMatch";
                for (let detail in LiveScheduleDict[day][match]) {
                    const temp = document.createElement("div");
                    switch (detail) {
                        case "broadcastMatchTime":
                            temp.className = "broadcastMatchTime";
                            break;
                        case "broadcastMatchHost":
                            temp.className = "broadcastMatchHost";
                            break;
                        case "broadcastMatchGuest":
                            temp.className = "broadcastMatchGuest";
                            break;
                        case "broadcastInfo":
                            temp.className = "broadcastInfo";
                            break;
                        case "broadcastTvs":
                            temp.className = "broadcastTvs";
                            break;
                        case "broadcastMatchNoTeams":
                            temp.className = "broadcastMatchNoTeams";
                            break;

                    }
                    temp.innerText = LiveScheduleDict[day][match][detail];
                    broadcastMatch.appendChild(temp)
                    widgetBody.appendChild(broadcastMatch)
                    document.getElementById("01").appendChild(widgetBody);
                }
            }
        }

    })

}
