const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function getRequest(character_url) {
    return new Promise((resolve, reject) => {
        request(character_url, (error, response, body) => {
            if (error)
                reject(error);
            resolve(JSON.parse(body));
        });
    });
}

async function characterName() {
    const response = await getRequest(url);
    let i;
    let characters_lenght = Object.keys(response.characters).length;
    for (i = 0 ; i < characters_lenght ; i++) {
        const character = await getRequest(response.characters[i]);
        console.log(character.name);
    }
}

characterName();
