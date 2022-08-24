
async function generate_publication_from_files(e) {
    e.preventDefault();

    const form = e.target
    const UPLOAD_URL = form.elements['upload_url'].value
    const AUTH_TOKEN = form.elements['auth_token'].value
    const LAUNCH_GENERATION_URL = form.elements['launch_generation_url'].value

    /*
    FIXME: On ne gère que le cas dossier vide.
    Autres cas que l'on pourrait gérer pour mieux informer les utilisateurices
    - Présence du fichier {PUB}/xml/document.xml
    - Présence des trois sous-dossiers {PUB}/illustrations, {PUB}/tableaux, {PUB}/xml
    */
    if (form.elements['files'].files.length == 0) {
        document.getElementById('div-error').hidden = false;
    }
    else {
        document.getElementById('div-error').hidden = true;
        submit_button = document.getElementsByTagName('button')[0];
        submit_button.getElementsByTagName('img')[0].hidden = false;
        submit_button.disabled = true;

        const uploads = [];
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

        // FIXME: Gestion d'erreur si un upload échoue
        await Promise.all(uploads);

        // FIXME: Gestion d'erreur si le status_code est pas 200
        await fetch(LAUNCH_GENERATION_URL, {
            method: "POST",
            headers: new Headers({
                authorization: `Basic ${AUTH_TOKEN}`,
            }),
        });
        window.location = form.action;
    }

}

document.getElementById("uploadForm").addEventListener("submit", generate_publication_from_files);
