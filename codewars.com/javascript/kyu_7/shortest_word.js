// https://www.codewars.com/kata/shortest-word

const findShort = (s) => Math.min(...s.split(' ').map(x => x.length));
