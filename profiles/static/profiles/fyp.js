
function showLikes(id){
    const likeCount = document.getElementById(`like-count-${id}`);
    const likesModal = document.getElementById(`likesModal-${id}`);
    const likeOverlay = document.getElementById(`likeOverlay-${id}`);
    const likeCloseBtn = document.getElementById(`close-btn-${id}`);

    likesModal.style.display = "block";
    likeOverlay.style.display = "block";

    likeCloseBtn.addEventListener("click", () => {
        likesModal.style.display = "none";
        likeOverlay.style.display = "none";
      });

    likeOverlay.addEventListener("click", () => {
        likesModal.style.display = "none";
        likeOverlay.style.display = "none";
      });




}




























// const firstPost = sessionStorage.getItem("firstPost");

// if (firstPost){
//     sessionStorage.removeItem("firstPost");
    
//     const form = document.createElement("form");
//     form.method = "POST";
//     form.action = "{% url 'fyp' %}";

//     const csrf = document.createElement("input");
//     csrf.name = "csrfmiddlewaretoken";
//     csrf.value = csrfToken;
//     form.appendChild(csrf);

//     const input = document.createElement("input");
//     input.type = "hidden";
//     input.name = "first_post_id";
//     input.value = firstPost;
//     form.appendChild(input);

//     document.body.appendChild(form);
//     form.submit();

// }