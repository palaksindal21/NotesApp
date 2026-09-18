const deleteForms = document.querySelectorAll(".note-actions form");

deleteForms.forEach(function(form) {

    form.addEventListener("submit", function(event) {

        const confirmDelete = confirm(
            "Are you sure you want to delete this note?"
        );

        if (!confirmDelete) {
            event.preventDefault();
        }

    });

});


const titleInput = document.getElementById("title");

if (titleInput) {

    titleInput.addEventListener("input", function() {

        if (titleInput.value.trim() === "") {
            titleInput.setCustomValidity(
                "Title cannot contain only spaces."
            );
        } else {
            titleInput.setCustomValidity("");
        }

    });

}


console.log("Notes App loaded successfully.");