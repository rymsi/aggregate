// Elements initialized from markup

window.onload = () => {
    let searchBox = document.getElementById("searchBox");
    let submitButton = document.getElementById("submitButton");
    searchBox.focus();

    //add mouse click event listener
    submitButton.addEventListener("click", mouseClickListener,false);

    //enter to search
    searchBox.addEventListener("keyup", function(event) {
        //prevent default
        event.preventDefault();
        //trigger submit if enter is pressed
        if(event.keyCode === 13) {
            submitButton.click();
        }
    });
};

function mouseClickListener() {
    let submittedInput = searchBox.value;
    submittedInput = submittedInput.replace(/ /g,'+');
    let currenturl = window.location.href;
    if(submittedInput != '')
        window.open("/results/" + submittedInput, '_self', false);
}
