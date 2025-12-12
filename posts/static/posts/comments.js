function toggleReplyBox(id) {
    const box = document.getElementById(`reply-box-${id}`);
    box.classList.toggle("hidden");
}

function toggleReplies(id) {
    const show_button = document.getElementById(`toggle-replies-${id}`);
    show_button.innerText = show_button.innerText === "show replies" ? "hide replies" : "show replies";
    document.querySelectorAll(`.show-reply-${id}`).forEach(reply => {
        reply.classList.toggle("hidden");
    });

    
   
   
    
}


