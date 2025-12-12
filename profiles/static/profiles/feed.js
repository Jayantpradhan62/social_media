function setFirstPost(postId){

 const prev_form = document.getElementById("new-form");
 if(prev_form){
    document.body.removeChild(prev_form);
 };
    
const form = document.createElement("form");
form.id = "new-form";
form.method = "POST";
form.action = "/fyp";

const csrf = document.createElement("input");
csrf.name = "csrfmiddlewaretoken";
csrf.type = "hidden";
csrf.value = csrfToken;
form.appendChild(csrf);



const input = document.createElement("input");
input.type = "hidden";
input.name = "first_post_id";
input.value = postId;
form.appendChild(input);

document.body.appendChild(form);
form.submit();


   

}
