    // Get the drop area element
    const dropArea = document.getElementById('drop-area');

    // Add the dragover event listener
    dropArea.addEventListener('dragover', function (event) {
        // Prevent the default behavior (Prevent file from being opened)
        event.preventDefault();
    });

    // Add the drop event listener
    // Add the drop event listener
    dropArea.addEventListener('drop', function (event) {
        // Prevent the default behavior (Prevent file from being opened)
        event.preventDefault();

        // Get the dropped files
        const files = event.dataTransfer.files;

        // Create a new JSZip instance
        const zip = new JSZip();

        // Add each dropped file to the zip
        for (let i = 0; i < files.length; i++) {
            zip.file(files[i].name, files[i]);
        }

        // Generate the zip file
        zip.generateAsync({type: "blob"}).then(function (content) {
            // Create a new FormData instance
            const formData = new FormData();

            // Append the zip file to the form data
            formData.append('file', content, 'files.zip');

            // Append the is_password field to the form data
            formData.append('is_password', 'false');

            // Make a POST request to the endpoint
            fetch('http://127.0.0.1:8000/upload', {
                method: 'POST',
                headers: {
                    'accept': 'application/json',
                },
                body: formData
            })
                .then(response => response.json())
                .then(data => console.log(data))
                .catch(error => console.error(error));
        });
    });


    // Add the click event listener
    dropArea.addEventListener('click', function () {
        // Open the file explorer
        document.getElementById('file-input').click();
    });