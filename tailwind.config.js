/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["templates/**/*html", "carting/**/*xslt"],
    prefix: "sn-",
    corePlugins: {
        preflight: false,
    },
    theme: {
        colors: {
            // https://www.systeme-de-design.gouv.fr/elements-d-interface/fondamentaux-identite-de-l-etat/couleurs-palette/
            info: {
                "975-active": "#c2cfff",
            },
        },
        maxWidth: {
            readable: "80ch",
            "120w": "60rem",
        },
        spacing: {
            // https://www.systeme-de-design.gouv.fr/elements-d-interface/fondamentaux-techniques/espacements
            0: 0,
            "1v": "0.25rem",
            "1w": "0.5rem",
            "3v": "0.75rem",
            "2w": "1rem",
            "3w": "1.5rem",
            "4w": "2rem",
            "5w": "2.5rem",
            "6w": "3rem",
            "7w": "3.5rem",
            "8w": "4rem",
            "9w": "4.5rem",
            "12w": "6rem",
            "15w": "7.5rem",
        },
        extend: {
            minWidth: ({ theme }) => ({ ...theme("spacing") }),
        },
    },
    plugins: [],
}
