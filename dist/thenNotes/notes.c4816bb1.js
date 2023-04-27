window.addEventListener("load", ()=>{
    for (let i of document.querySelectorAll(".collapse ol")){
        let tog = document.createElement("div");
        tog.innerHTML = i.previousSibling.textContent;
        tog.className = "toggle";
        tog.onclick = ()=>tog.classList.toggle("show");
        i.parentElement.removeChild(i.previousSibling);
        i.parentElement.insertBefore(tog, i);
    }
});

//# sourceMappingURL=notes.c4816bb1.js.map
