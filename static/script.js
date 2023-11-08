// Get the drop area element
const dropArea = document.getElementById('drop-area');
const fileInput = document.getElementById('file-input');

// Prevent the default behavior (Prevent file from being opened)
const preventDefaults = (event) => {
    event.preventDefault();
    event.stopPropagation();
};

// Handle the dropped files
const handleDrop = (event) => {
    const files = event.dataTransfer.files;
    const zip = new JSZip();

    // Add each dropped file to the zip
    Array.from(files).forEach(file => {
        zip.file(file.name, file);
    });

    // Generate the zip file
    zip.generateAsync({type: "blob"}).then(content => {
        const formData = new FormData();

        // Append the zip file to the form data
        formData.append('file', content, 'files.zip');
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
};

// Open the file explorer
const handleClick = () => {
    fileInput.click();
};

// Add the event listeners
['dragover', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, preventDefaults, false);
});

dropArea.addEventListener('drop', handleDrop, false);
dropArea.addEventListener('click', handleClick, false);

const img2 = document.querySelector('.img-2');
const imgArrow = document.querySelector('.img-arrow');

// Define the animation
const animation = imgArrow.animate([
  { transform: 'translateX(0)', width: '233px'   },
  { transform: 'translateX(15px)', width: '350px'  }
], {
  duration: 400,
  fill: 'forwards'
});

// Pause the animation initially
animation.pause();

// Listen for the mouseenter event
img2.addEventListener('mouseenter', () => {
  // Only play the animation if it hasn't been played yet
  if (animation.currentTime === 0) {
    animation.play();
  }
});