window.onload = () => {
    let currentUrl = window.location.href;
    let query = getSearchQuery(currentUrl).toLowerCase();
    
    readTextFile("senators.json", function(text){
        data = JSON.parse(text);
        let nameList = Object.values(data['Name']);
        let matchListIndex = [];

        for(let i = 0; i < nameList.length; i++) {
            if(nameList[i].toLowerCase().includes(query)) {
                matchListIndex.push((i).toString());
            }
        }
        for(let elem of matchListIndex) {
            console.log(data['Name'][elem]);
        }       
        document.getElementById('index').innerHTML = matchListIndex[0]
        
    });
}

function getSearchQuery(url) {
    let startIndex = url.indexOf('=');
    let query = url.slice(startIndex+1, (url.length)).replace('+', ' ');
    return query;
}

function readTextFile(file, callback) {
    var rawFile = new XMLHttpRequest();
    rawFile.overrideMimeType("application/json");
    rawFile.open("GET", file, true);
    rawFile.onreadystatechange = function() {
        if (rawFile.readyState === 4 && rawFile.status == "200") {
            callback(rawFile.responseText);
        }
    }
    rawFile.send(null);
}
