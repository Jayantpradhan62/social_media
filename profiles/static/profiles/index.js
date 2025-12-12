


document.addEventListener("DOMContentLoaded", () => {
    // Followers elements
    const followersBtn = document.querySelector(".profile-stats li:nth-child(2)");
    const followersModal = document.getElementById("followersModal");
    const followersOverlay = document.getElementById("followersOverlay");
    const followersCloseBtn = followersModal.querySelector(".close-btn");
  
    // Following elements
    const followingBtn = document.querySelector(".profile-stats li:nth-child(3)");
    const followingModal = document.getElementById("followingModal");
    const followingOverlay = document.getElementById("followingOverlay");
    const followingCloseBtn = followingModal.querySelector(".close-btn");
  
    // Open followers modal
    followersBtn.addEventListener("click", () => {
      followersModal.style.display = "block";
      followersOverlay.style.display = "block";
      document.body.classList.add("modal-open");
    });
  
    // Close followers modal
    followersCloseBtn.addEventListener("click", () => {
      followersModal.style.display = "none";
      followersOverlay.style.display = "none";
      document.body.classList.remove("modal-open");
    });
  
    followersOverlay.addEventListener("click", () => {
      followersModal.style.display = "none";
      followersOverlay.style.display = "none";
      document.body.classList.remove("modal-open");
    });
  
    // Open following modal
    followingBtn.addEventListener("click", () => {
      followingModal.style.display = "block";
      followingOverlay.style.display = "block";
      document.body.classList.add("modal-open");
    });
  
    // Close following modal
    followingCloseBtn.addEventListener("click", () => {
      followingModal.style.display = "none";
      followingOverlay.style.display = "none";
      document.body.classList.remove("modal-open");
    });
  
    followingOverlay.addEventListener("click", () => {
      followingModal.style.display = "none";
      followingOverlay.style.display = "none";
      document.body.classList.remove("modal-open");
    });
  });
  


  // search bar ---------

  document.addEventListener("DOMContentLoaded", function () {
    const input = document.getElementById("liveSearchInput");
    const resultsContainer = document.getElementById("liveSearchResults");
  
    input.addEventListener("input", function () {
      const query = input.value.trim();
      if (query.length === 0) {
        resultsContainer.innerHTML = "";
        resultsContainer.style.display = "none";
        return;
      }
  
      fetch(`/search-users/?q=${encodeURIComponent(query)}`)
        .then((response) => response.json())
        .then((data) => {
          resultsContainer.innerHTML = "";
          if (data.results.length > 0) {
            data.results.forEach((user) => {
              const userItem = document.createElement("a");
              userItem.href = user.profile_url;
              userItem.innerHTML = `
                <img src="${user.profile_pic_url}" alt="${user.username}">
                <span>${user.username}</span>
              `;
              resultsContainer.appendChild(userItem);
            });
            resultsContainer.style.display = "block";
          } else {
            resultsContainer.style.display = "none";
          }
        });
    });
  
    document.addEventListener("click", function (e) {
      if (!e.target.closest(".search-bar-container")) {
        resultsContainer.style.display = "none";
      }
    });
  });
  

  
  
  
  
  // Create Posts ---------

  document.addEventListener("DOMContentLoaded",() => {

    // create-post elements
    const CreatePostBtn = document.querySelectorAll(".profile-edit-btn")[2];
    const CreatePostModal = document.getElementById("createpostModal");
    const PostOverlay = document.getElementById("PostOverlay");
    const CreatePostCloseBtn = CreatePostModal.querySelector(".close-btn");


    // Open create-post modal
    CreatePostBtn.addEventListener("click", () => {
      CreatePostModal.style.display = "block";
      PostOverlay.style.display = "block";
      document.body.classList.add("modal-open");
    });
  
    // Close create-post modal
    CreatePostCloseBtn.addEventListener("click", () => {
      CreatePostModal.style.display = "none";
      PostOverlay.style.display = "none";
      document.body.classList.remove("modal-open");
    });

    PostOverlay.addEventListener("click", () => {
      CreatePostModal.style.display = "none";
      PostOverlay.style.display = "none";
      document.body.classList.remove("modal-open");
    });







  });




// Create Post Image Preview

document.getElementById("id_post_image").addEventListener("change", function (event) {
  const file = event.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = function (e) {
      document.getElementById("imagePreview").src = e.target.result;
    };
    reader.readAsDataURL(file);
  }
});
