window.onload = function(){
    const chatbox = document.getElementById("chat-box");
    chatbox.scrollTop  = chatbox.scrollHeight
}

const textarea = document.getElementById("chat-input");
const error = document.getElementById("text-error");

textarea.addEventListener('input',function() {

    this.style.height = "auto";
    this.style.height = this.scrollHeight + "px";

});

if (error) {
    textarea.style.height = "auto";
    textarea.style.height = textarea.scrollHeight + "px";
}