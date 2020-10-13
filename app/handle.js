const $nofiles = document.querySelector('div.nofiles');
const $files = document.querySelector('div.files');
const $export = document.querySelector('button.export');

async function uploadFiles() {
    const response = await pywebview.api.send('open_explorer', null);
    const images = JSON.parse(response)[0];
    if (images.length) {
        $nofiles.style.display = 'none';
        $files.style.display = 'block';
        $export.style.display = 'block';
    }
    for (const image of images) {
        $files.innerHTML += `
            <div class="file-item">
                <div>
                    <i class="fa fa-file"></i>
                    <p>${image}</p>
                </div>
                <i class="fa fa-times"></i>
            </div>
        `;
    }
}

document.querySelector('button.file-explorer').addEventListener('click', uploadFiles);

document.querySelector('div.nofiles a').addEventListener('click', uploadFiles);