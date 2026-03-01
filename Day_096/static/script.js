document.addEventListener('DOMContentLoaded', () => {
    if (window.lucide) {
        lucide.createIcons();
    }

    const updateClock = () => {
        const clockElement = document.getElementById('os-clock');
        if (clockElement) {
            const now = new Date();
            clockElement.innerText = now.toLocaleTimeString([], {
                hour: '2-digit',
                minute: '2-digit'
            });
        }
    };
    setInterval(updateClock, 1000);
    updateClock();

    const closeButtons = document.querySelectorAll('.btn-close');
    closeButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            console.log("System: Closing application window...");
        });
    });

    const progressSegments = document.querySelectorAll('.progress-segment');
    if (progressSegments.length > 0) {
        let currentSegment = 0;
        const progressInterval = setInterval(() => {
            if (currentSegment < progressSegments.length) {
                progressSegments[currentSegment].classList.add('active');
                currentSegment++;
            } else {
                clearInterval(progressInterval);
                console.log("Analysis: 100% Complete.");
            }
        }, 150); // Adjust speed of the "scanning" effect here
    }

    const fileInput = document.getElementById('file-upload');
    const uploadForm = document.getElementById('upload-form');

    if (fileInput && uploadForm) {
        fileInput.addEventListener('change', () => {
            console.log("System: File detected. Initializing upload...");
            const statusLabel = document.querySelector('.status-label');
            if (statusLabel) statusLabel.innerText = "System: Uploading...";

            uploadForm.submit();
        });
    }

    const desktopIcons = document.querySelectorAll('.desktop-icon');
    desktopIcons.forEach(icon => {
        icon.addEventListener('dblclick', () => {
            const label = icon.querySelector('.icon-label').innerText;
            alert(`Opening ${label}... (Feature pending system update)`);
        });
        icon.addEventListener('click', () => {
            desktopIcons.forEach(i => i.style.outline = 'none');
            icon.style.outline = '1px dotted var(--os-border)';
        });
    });
});

function toggleAbout() {
    alert("Palette OS v1.0.4\nKernel: Vanilla JS\nUI: Retro-Modern");
}