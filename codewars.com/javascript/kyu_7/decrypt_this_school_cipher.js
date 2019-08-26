// https://www.codewars.com/kata/decrypt-this-school-cipher

const decrypt = (str) => {
    let result = [];
    // ty https://regex101.com/
    const regex = /(?:\d+)|(?:'[0-9]*')|(?:\s)/g;
    let m;

    while ((m = regex.exec(str)) !== null) {
        // This is necessary to avoid infinite loops with zero-width matches
        if (m.index === regex.lastIndex) {
            regex.lastIndex++;
        }

        // The result can be accessed through the `m`-variable.
        m.forEach((match, groupIndex) => {
            // console.log(`Found match, group ${groupIndex}: ${match}`);
            result.push(match)
        });
    }

    return result
        .reverse()
        .map(x => x.startsWith("'") ? String.fromCharCode(x.replace(/'/g, "")) : x.split('').reverse().join(''))
        .join('');
};
