const titleInput = document.getElementById("title");


if (titleInput) {

    titleInput.addEventListener("input", function () {

        if (titleInput.value.trim() === "") {

            titleInput.setCustomValidity(
                "Title cannot contain only spaces."
            );

        } else {

            titleInput.setCustomValidity("");

        }

    });

}


const editForm = document.querySelector("form");


if (editForm) {

    editForm.addEventListener("submit", function (event) {

        const confirmUpdate = confirm(
            "Are you sure you want to update this note?"
        );


        if (!confirmUpdate) {

            event.preventDefault();

        }

    });

}


console.log("Edit Note page loaded successfully.");