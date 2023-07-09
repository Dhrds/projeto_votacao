function openPopup() {
    var popup = document.getElementById("popup");
    popup.style.opacity = 1;
    popup.style.visibility = "visible";
}

function closePopup() {
    var popup = document.getElementById("popup");
    popup.style.opacity = 0;
    popup.style.visibility = "hidden";
}


function aguarde() {
    const div = document.createElement("div");
    div.classList.add("loading");
    const label = document.createElement("label");
    label.innerText="Aguarde...";
    div.appendChild(label);
       
    document.body.appendChild(div);
    setTimeout(() => hideAguarde(), 5000);
}

function hideAguarde() {
    const loadings = document.getElementsByClassName("loading");
    if (loadings.length) {
        loadings[0].remove();
    }
}