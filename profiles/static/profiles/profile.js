
document.getElementById('id_profile_pic').addEventListener('change', function (e) {
    const [file] = e.target.files;
    if (file) {
        document.getElementById('profile-pic-preview').src = URL.createObjectURL(file);
    }
});




