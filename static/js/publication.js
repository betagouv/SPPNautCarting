
async function generate_publication_from_files(e) {
    e.preventDefault();

    const form = e.target
    const UPLOAD_URL = form.elements['upload_url'].value
    const OUVRAGE = form.elements['ouvrage'].value
    const AUTH_TOKEN = form.elements['auth_token'].value
    const LAUNCH_GENERATION_URL = form.elements['launch_generation_url'].value

    const uploads = [];
    if (form.elements['files'] == undefined) {
        // Ouvrage stored in Cellar
        uploads.push(
            fetch(UPLOAD_URL, {
                headers: new Headers({
                    authorization: `Basic ${AUTH_TOKEN}`,
                }),
                method: "POST",
                body: JSON.stringify({ "ouvrage": OUVRAGE }),
            })
        );
    } else {
        // Ouvrage uploaded from browser
        for (const file of form.elements['files'].files) {

            const data = new FormData();
            data.append("file", file);
            data.append("webkitRelativePath", file.webkitRelativePath);
            uploads.push(
                fetch(UPLOAD_URL, {
                    headers: new Headers({
                        authorization: `Basic ${AUTH_TOKEN}`,
                    }),
                    method: "POST",
                    body: data,
                })
            );
        }
    }

}

document.getElementById("uploadForm").addEventListener("submit", generate_publication_from_files);
