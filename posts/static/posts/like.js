document.addEventListener("DOMContentLoaded", () => {
    const likeCount = document.querySelector(".like-count");
    const likesModal = document.getElementById("likesModal");
    const likeOverlay = document.getElementById("likeOverlay");
    const likeCloseBtn = likesModal.querySelector(".close-btn");
  
    likeCount.addEventListener("click", () => {
      likesModal.style.display = "block";
      likeOverlay.style.display = "block";
    });
  
    likeCloseBtn.addEventListener("click", () => {
      likesModal.style.display = "none";
      likeOverlay.style.display = "none";
    });
  
    likeOverlay.addEventListener("click", () => {
      likesModal.style.display = "none";
      likeOverlay.style.display = "none";
    });
  });
  