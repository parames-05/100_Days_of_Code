// --- STATE MANAGEMENT ---
const state = {
    view: 'IDLE', // IDLE, PROCESSING, COMPLETED, ERROR
    file: null,
    progress: 0,
    isPlaying: false
};

// --- DOM ELEMENTS ---
const elements = {
    statusMsg: document.getElementById('status-msg'),
    fileInput: document.getElementById('file-input'),
    fileNameDisplay: document.getElementById('file-name-display'),
    uploadZone: document.getElementById('upload-zone'),
    startZone: document.getElementById('start-zone'),
    progressFill: document.getElementById('progress-fill'),
    progressPercent: document.getElementById('progress-percent'),
    audioEngine: document.getElementById('audio-engine'),
    playIcon: document.getElementById('icon-play'),
    pauseIcon: document.getElementById('icon-pause'),
    downloadLink: document.getElementById('download-link'),
    errorMsg: document.getElementById('error-msg')
};

// --- VIEW UPDATER ---
function updateUI() {
    // Hide all views
    document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));

    // Show current view
    document.getElementById(`state-${state.view.toLowerCase()}`).classList.add('active');

    // Update Status Bar
    if (state.view === 'IDLE') elements.statusMsg.innerText = state.file ? 'CARTRIDGE DETECTED' : 'SYSTEM READY';
    if (state.view === 'PROCESSING') elements.statusMsg.innerText = 'PROCESSING DATA...';
    if (state.view === 'COMPLETED') elements.statusMsg.innerText = 'CONVERSION COMPLETE';
    if (state.view === 'ERROR') elements.statusMsg.innerText = 'SYSTEM FAILURE';
}

// --- HELPER: BASE64 TO BLOB ---
function b64toBlob(b64Data, contentType = '', sliceSize = 512) {
    const byteCharacters = atob(b64Data);
    const byteArrays = [];
    for (let offset = 0; offset < byteCharacters.length; offset += sliceSize) {
        const slice = byteCharacters.slice(offset, offset + sliceSize);
        const byteNumbers = new Array(slice.length);
        for (let i = 0; i < slice.length; i++) {
            byteNumbers[i] = slice.charCodeAt(i);
        }
        const byteArray = new Uint8Array(byteNumbers);
        byteArrays.push(byteArray);
    }
    return new Blob(byteArrays, { type: contentType });
}

// --- EVENT HANDLERS ---
elements.fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (file && file.type === 'application/pdf') {
        state.file = file;
        elements.fileNameDisplay.innerText = file.name.toUpperCase();
        elements.uploadZone.style.display = 'none';
        elements.startZone.style.display = 'block';
        updateUI();
    }
});

document.getElementById('btn-start').addEventListener('click', startConversion);

async function startConversion() {
    if (!state.file) return;

    state.view = 'PROCESSING';
    updateUI();

    // Fake progress animation for retro feel while waiting for server
    let p = 0;
    const progressInterval = setInterval(() => {
        if (p < 90) {
            p += 2;
            elements.progressFill.style.width = `${p}%`;
            elements.progressPercent.innerText = `${p}%`;
        }
    }, 200);

    const formData = new FormData();
    formData.append('file', state.file);

    try {
        const response = await fetch('/convert', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (data.error) throw new Error(data.error);

        clearInterval(progressInterval);
        elements.progressFill.style.width = `100%`;
        elements.progressPercent.innerText = `100%`;

        // Using audio/mpeg for gTTS MP3 compatibility
        const audioBlob = b64toBlob(data.audio_base64, 'audio/mpeg');
        const audioUrl = URL.createObjectURL(audioBlob);

        elements.audioEngine.src = audioUrl;
        elements.downloadLink.href = audioUrl;
        elements.downloadLink.download = data.filename;

        state.view = 'COMPLETED';
        updateUI();
    } catch (err) {
        clearInterval(progressInterval);
        state.view = 'ERROR';
        elements.errorMsg.innerText = err.message || 'SYSTEM FAILURE';
        updateUI();
    }
}

document.getElementById('btn-toggle-play').addEventListener('click', () => {
    state.isPlaying = !state.isPlaying;
    if (state.isPlaying) {
        elements.playIcon.style.display = 'none';
        elements.pauseIcon.style.display = 'block';
        elements.audioEngine.play().catch(() => {
            state.isPlaying = false;
            elements.playIcon.style.display = 'block';
            elements.pauseIcon.style.display = 'none';
        });
    } else {
        elements.playIcon.style.display = 'block';
        elements.pauseIcon.style.display = 'none';
        elements.audioEngine.pause();
    }
});

elements.audioEngine.addEventListener('ended', () => {
    state.isPlaying = false;
    elements.playIcon.style.display = 'block';
    elements.pauseIcon.style.display = 'none';
});

document.getElementById('btn-reset').addEventListener('click', () => {
    location.reload();
});

document.getElementById('btn-reboot').addEventListener('click', () => {
    location.reload();
});

// Initial Render
updateUI();