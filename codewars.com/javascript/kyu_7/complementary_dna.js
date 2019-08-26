// https://www.codewars.com/kata/complementary-dna

const DNAStrand = (dna) => {
    const pairs = {A: 'T', T: 'A', C: 'G', G: 'C'};
    return dna.split('').map(x => pairs[x]).join('');
};
