document.addEventListener('DOMContentLoaded', function() {
    const videoInput = document.querySelector('input[name="video_file"]');
    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        if (videoInput.files.length > 0) {
            event.preventDefault();
            const formData = new FormData();
            formData.append('video', videoInput.files[0]);

            fetch('/upload_video/', {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            }).then(response => response.json())
              .then(data => {
                  if (data.success) {
                      // Set the video field to the uploaded file path
                      document.querySelector('input[name="video"]').value = data.file_path;
                      form.submit();
                  } else {
                      alert('Video upload failed');
                  }
              });
        }
    });
});
