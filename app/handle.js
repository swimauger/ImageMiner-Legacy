document.querySelector('button').addEventListener('click', () => {
    pywebview.api.send('open_explorer', null);
});