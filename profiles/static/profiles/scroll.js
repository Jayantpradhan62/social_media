function setScroll(post){
    sessionStorage.setItem("scrollTo",post);
}

window.addEventListener("DOMContentLoaded",() => {
    const scrollTo = sessionStorage.getItem("scrollTo");
    if(scrollTo){
        const postElement = document.getElementById(scrollTo);
        if (postElement){
            postElement.scrollIntoView()
        }

        sessionStorage.removeItem("scrollTo");
    }

    
})