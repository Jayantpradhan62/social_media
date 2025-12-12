document.addEventListener("DOMContentLoaded", function () {
    const input = document.getElementById("liveSearchInput");
    const resultsContainer = document.getElementById("chatSidebar");
  
    input.addEventListener("input", function () {
      const query = input.value.trim();
      if (query.length === 0) {
        document.querySelectorAll(".default").forEach(message => {
            message.style.display = "flex";
        });
        document.querySelectorAll(".not-default").forEach(message => message.remove());
        return;
      }
  
      fetch(`/search-user-messages/?q=${encodeURIComponent(query)}`)
        .then((response) => response.json())
        .then((data) => {
          if (data.results.length > 0) {

            document.querySelectorAll(".default").forEach(message => {
              message.style.display = "none";
          });

          document.querySelectorAll(".not-default").forEach(message => message.remove());
            
           
            
            data.results.forEach((user) => {
              const userItem = document.createElement("a");
              userItem.href = user.message_url;
              userItem.classList.add("chat-preview","not-default")
              userItem.innerHTML = `
                <img src="${user.profile_pic_url}" alt="${user.username}" class="avatar" />
                 <div class="chat-info">
                    <p class="username">${user.username}</p>
                    <p class="latest">${user.latest_message}</p>
                </div>

              `;
              resultsContainer.appendChild(userItem);
            });
          } 

        else {

            document.querySelectorAll(".not-default").forEach(message => message.remove());

            const noItem = document.createElement("p");
              noItem.classList.add("chat-preview","not-default")
              noItem.innerHTML = `
               No results found

              `;
              resultsContainer.appendChild(noItem);


          }
          
        });
    });
  
    
  });
  
